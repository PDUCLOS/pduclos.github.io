"""Generate draw.io diagrams (left-to-right pipeline, one column per stage) and export them to SVG."""
import html
import re
import subprocess
from pathlib import Path

DRAWIO_BIN = "/Applications/draw.io.app/Contents/MacOS/draw.io"

# stage kind -> (fill, stroke)
PALETTE = {
    "source":  ("#FEF3C7", "#D97706"),
    "ingest":  ("#E0F2FE", "#0284C7"),
    "storage": ("#EDE9FE", "#7C3AED"),
    "process": ("#DBEAFE", "#2563EB"),
    "ml":      ("#DCFCE7", "#16A34A"),
    "ops":     ("#FCE7F3", "#DB2777"),
    "serve":   ("#CCFBF1", "#0D9488"),
    "ui":      ("#FFE4E6", "#E11D48"),
    "infra":   ("#F1F5F9", "#475569"),
}

COL_W, NODE_W, NODE_H, GAP_Y, HEAD_H, MARGIN, LANE = 220, 164, 54, 18, 40, 20, 14


def _cell(cid, value, style, x, y, w, h, parent="1"):
    return (f'<mxCell id="{cid}" value="{html.escape(value, quote=True)}" style="{style}" vertex="1" parent="{parent}">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')


def build_xml(title, stages, edges, band=None):
    """stages: list of (stage_title, kind, [node labels]) ; node ids are 's{col}n{row}'.
    edges: list of (src_id, dst_id, label or '', dashed bool).
    band: optional (label, kind) drawn as a full-width strip under the columns (e.g. CI/CD, Docker).

    Edge routing keeps lines out of the boxes: adjacent columns connect through the corridor between them,
    skips of several columns use lanes under the columns, backward edges use lanes above them."""
    cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
    max_rows = max(len(s[2]) for s in stages)
    col_h = HEAD_H + max_rows * (NODE_H + GAP_Y) + GAP_Y
    n_back = sum(1 for a, b, *_ in edges if _col(b) < _col(a) - 1)
    top = MARGIN + 44 + n_back * LANE
    cells.append(_cell("title", title,
                       "text;html=1;fontSize=18;fontStyle=1;fontColor=#0F172A;align=left;verticalAlign=middle;fontFamily=Helvetica;",
                       MARGIN, MARGIN, len(stages) * COL_W - 20, 30))
    pos = {}
    for c, (stitle, kind, nodes) in enumerate(stages):
        fill, stroke = PALETTE[kind]
        x = MARGIN + c * COL_W
        cells.append(_cell(f"col{c}", "", f"rounded=1;arcSize=6;fillColor={fill};strokeColor={stroke};opacity=35;strokeWidth=1;",
                           x, top, COL_W - 20, col_h))
        cells.append(_cell(f"h{c}", f"{c + 1:02d} · {stitle.upper()}",
                           f"text;html=1;fontSize=11;fontStyle=1;fontColor={stroke};align=center;verticalAlign=middle;fontFamily=Helvetica;",
                           x, top + 6, COL_W - 20, 26))
        n_off = (max_rows - len(nodes)) * (NODE_H + GAP_Y) / 2
        for r, label in enumerate(nodes):
            y = top + HEAD_H + n_off + r * (NODE_H + GAP_Y)
            nx = x + (COL_W - 20 - NODE_W) / 2
            pos[f"s{c}n{r}"] = (nx, y)
            cells.append(_cell(f"s{c}n{r}", label,
                               f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={stroke};strokeWidth=1.6;"
                               f"fontSize=12;fontColor=#0F172A;fontFamily=Helvetica;shadow=0;",
                               nx, y, NODE_W, NODE_H))
    bottom = top + col_h
    n_skip = sum(1 for a, b, *_ in edges if _col(b) - _col(a) > 1)
    height = bottom + 12 + n_skip * LANE + MARGIN
    if band:
        blabel, bkind = band
        fill, stroke = PALETTE[bkind]
        cells.append(_cell("band", blabel,
                           f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};dashed=1;fontSize=12;"
                           f"fontColor=#0F172A;fontStyle=1;fontFamily=Helvetica;",
                           MARGIN, height - MARGIN + 8, len(stages) * COL_W - 20, 40))
        height += 60
    base = ("edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#334155;strokeWidth=1.5;endArrow=block;endFill=1;"
            "fontSize=10;fontColor=#334155;labelBackgroundColor=#FFFFFF;fontFamily=Helvetica;")
    corridor = (COL_W - NODE_W) / 2  # distance from a node edge to the middle of the gap
    skip_i = back_i = 0
    for i, (src, dst, label, dashed) in enumerate(edges):
        (sx, sy), (dx, dy) = pos[src], pos[dst]
        sc, dc = _col(src), _col(dst)
        scy, dcy = sy + NODE_H / 2, dy + NODE_H / 2
        style, pts = base + ("dashed=1;" if dashed else ""), []
        if sc == dc:  # vertical, same column
            if dy > sy:
                style += "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"
            else:
                style += "exitX=0.5;exitY=0;entryX=0.5;entryY=1;"
        elif dc == sc + 1:  # adjacent: through the corridor
            style += "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
            cx = sx + NODE_W + corridor
            pts = [(cx, scy), (cx, dcy)]
        elif dc == sc - 1:  # adjacent backward: through the corridor too
            style += "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
            cx = dx + NODE_W + corridor
            pts = [(cx, scy), (cx, dcy)]
        elif dc > sc:  # forward skip: down the corridor, along a bottom lane, up the corridor
            lane = bottom + 12 + skip_i * LANE
            skip_i += 1
            style += "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
            x1, x2 = sx + NODE_W + corridor - 6 + skip_i * 3, dx - corridor + 6 - skip_i * 3
            pts = [(x1, scy), (x1, lane), (x2, lane), (x2, dcy)]
        else:  # backward: via a lane above the columns
            lane = top - 10 - back_i * LANE
            back_i += 1
            style += "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
            x1, x2 = sx - corridor + 6 - back_i * 3, dx + NODE_W + corridor - 6 + back_i * 3
            pts = [(x1, scy), (x1, lane), (x2, lane), (x2, dcy)]
        arr = ""
        if pts:
            arr = '<Array as="points">' + "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in pts) + "</Array>"
        cells.append(f'<mxCell id="e{i}" value="{html.escape(label, quote=True)}" style="{style}" edge="1" parent="1" '
                     f'source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry">{arr}</mxGeometry></mxCell>')
    width = MARGIN * 2 + len(stages) * COL_W - 20
    model = (f'<mxGraphModel dx="{width}" dy="{height}" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
             f'fold="1" page="0" pageScale="1" pageWidth="{width}" pageHeight="{height}" math="0" shadow="0">'
             f'<root>{"".join(cells)}</root></mxGraphModel>')
    return f'<mxfile host="drawio"><diagram name="{html.escape(title, quote=True)}" id="d">{model}</diagram></mxfile>'


def _col(node_id):
    return int(node_id[1:node_id.index("n")])


_FALLBACK_IMG = re.compile(r"(</foreignObject>)\s*<image\b[^>]*?/>(\s*</switch>)")


def slim_svg(svg_path: Path):
    """Drop draw.io's per-label base64 PNG fallbacks (browsers render the foreignObject text)."""
    s = svg_path.read_text(encoding="utf-8")
    svg_path.write_text(_FALLBACK_IMG.sub(r"\1\2", s), encoding="utf-8")


def write_and_export(slug, xml, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    src = out_dir / f"{slug}.drawio"
    svg = out_dir / f"{slug}.svg"
    src.write_text(xml, encoding="utf-8")
    subprocess.run([DRAWIO_BIN, "-x", "-f", "svg", "-b", "10", "-o", str(svg), str(src)],
                   check=True, capture_output=True, timeout=120)
    slim_svg(svg)
    return src, svg
