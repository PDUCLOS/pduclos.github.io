"""Pipeline interactif (HTML + JS) généré à partir des mêmes données que les schémas draw.io.

Les briques sont des boutons ; assets/site.js trace les flux, anime le parcours et met en évidence
l'amont / l'aval d'une brique. Sans JS, la page garde les colonnes et tous les schémas, empilés.
"""
import json
import re

from drawio import PALETTE
from render import e
from i18n import T

GH_RE = re.compile(r"https://github\.com/(PDUCLOS/[\w.-]+)")
KIND_LABEL = {"source": "Sources", "ingest": "Ingestion", "storage": "Stockage", "process": "Traitement",
              "ml": "Machine learning", "ops": "MLOps", "serve": "Service", "ui": "Interface", "infra": "Socle"}


def repos(p):
    out = []
    for label, href, _ in p.get("links", []):
        m = GH_RE.match(href)
        if m and m.group(1) not in out:
            out.append(m.group(1))
    return out


def repo_cards(p, lang="fr"):
    cards = "".join(f"""<a class="gh-card" href="https://github.com/{r}" target="_blank" rel="noopener" data-repo="{r}">
            <span class="gh-name"><svg viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.06-.49.06-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.34.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>{e(r.split('/')[1])}</span>
            <span class="gh-desc">{T[lang]["gh_desc"]}</span>
            <span class="gh-meta"><span data-k="lang"></span><span data-k="push"></span><span data-k="stars"></span></span>
        </a>""" for r in repos(p))
    return f'<div class="gh-cards">{cards}</div>' if cards else ""


def strengths(p):
    """Points forts : champ dédié s'il existe, sinon les preuves techniques déjà documentées."""
    items = p.get("strengths") or p["tech"][:4]
    return "".join(f'<li class="pf-item reveal"><span class="pf-num">{i + 1:02d}</span><p>{x}</p></li>'
                   for i, x in enumerate(items))


def interactive(p, diagrams, figure, lang="fr"):
    t = T[lang]
    """diagrams: [(slug, caption)] — le schéma principal puis les schémas d'architecture."""
    pid = p["slug"]
    stages = p["stages"]
    cols = []
    for c, (title, kind, nodes) in enumerate(stages):
        color = PALETTE[kind][1]
        btns = "".join(f'<button type="button" class="pl-node" data-id="s{c}n{r}">{e(label)}</button>'
                       for r, label in enumerate(nodes))
        cols.append(f'<div class="pl-col" data-col="{c}" style="--k:{color}"><h4><span>{c + 1:02d}</span>{e(title)}</h4>{btns}</div>')
    band = ""
    if p.get("band"):
        band = f'<div class="pl-band" style="--k:{PALETTE[p["band"][1]][1]}">{e(p["band"][0])}</div>'
    edges = [dict(a=a, b=b, l=l, d=bool(d)) for a, b, l, d in p["edges"]]
    tabs = [f'<button type="button" class="pl-tab" aria-selected="true" data-tab="live">{t["pl_live"]}</button>']
    panels = []
    for i, (d_slug, caption) in enumerate(diagrams):
        tabs.append(f'<button type="button" class="pl-tab" aria-selected="false" data-tab="d{i}">{e(caption)}</button>')
        panels.append(f"""<div class="pl-panel" data-panel="d{i}">
                <h3 class="pl-panel-title">{e(caption)}</h3>
                <div class="pl-zoom-tools" aria-hidden="true"><button type="button" data-z="in">+</button><button type="button" data-z="out">−</button><button type="button" data-z="reset">⟲</button><span>{t["pl_zoom"]}</span></div>
                {figure(f'/diagrams/{d_slug}.svg', f'/diagrams/{d_slug}.drawio', caption)}</div>""")
    return f"""
            <div class="pl" data-pl id="pl-{pid}">
                <div class="pl-tabs" role="tablist">{''.join(tabs)}</div>
                <div class="pl-panel" data-panel="live">
                    <div class="pl-toolbar">
                        <button type="button" class="pl-play">{t["pl_play"]}</button>
                        <button type="button" class="pl-reset" hidden>{t["pl_reset"]}</button>
                        <span class="pl-hint">{t["pl_hint"]}</span>
                    </div>
                    <div class="pl-scroll"><div class="pl-canvas" style="--n:{len(stages)}">
                        <svg class="pl-edges" aria-hidden="true"></svg>
                        <div class="pl-cols">{''.join(cols)}</div>
                    </div></div>
                    {band}
                    <div class="pl-info" aria-live="polite"></div>
                    <div class="pl-legend"><span><i class="solid"></i>{t["pl_flow"]}</span><span><i class="dash"></i>{t["pl_loop"]}</span></div>
                    <script type="application/json" class="pl-data">{json.dumps(edges, ensure_ascii=False).replace("</", "<\\/")}</script>
                </div>
                {''.join(panels)}
            </div>"""
