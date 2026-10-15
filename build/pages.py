"""Render project pages from the PROJECTS data (French or English)."""
from functools import partial
from render import head, nav, footer, badges, arrow, e
from pipeline import interactive, repo_cards, strengths
from i18n import T, MATRIX_COLS as MATRIX_COLS_I18N, MARK_LABEL, home, project_path

MATRIX_COLS = MATRIX_COLS_I18N["fr"]


def marks(lang="fr"):
    lab = MARK_LABEL[lang]
    return {"y": (f'<span class="m-yes" title="{lab["y"]}">●</span>', lab["y"]),
            "p": (f'<span class="m-part" title="{lab["p"]}">◐</span>', lab["p"]),
            "n": (f'<span class="m-no" title="{lab["n"]}">—</span>', lab["n"])}


MARK = marks("fr")


def figure(svg, drawio, alt, lang="fr"):
    """Schéma affiché en SVG ; les sources .drawio ne sont pas publiées (travail protégé)."""
    return f"""<div class="pipeline-figure"><img src="{svg}" alt="{e(alt)}" loading="lazy" draggable="false"></div>
            <div class="figure-actions"><a href="{svg}" target="_blank">{T[lang]["fig_full"]}</a></div>"""


def lang_bars(langs):
    rows = []
    for name, pct in langs:
        rows.append(f"""<div class="skill-item"><span class="skill-name">{e(name)}</span>
                <span style="flex:1;margin:0 1rem;height:6px;background:var(--border);border-radius:3px;overflow:hidden">
                <span style="display:block;height:100%;width:{pct}%;background:var(--gradient-1)"></span></span>
                <span class="code-caption">{pct}%</span></div>""")
    return '<div class="skill-items">' + "".join(rows) + "</div>"


def project_page(p, projects, lang="fr"):
    t = T[lang]
    mark = marks(lang)
    slug = p["slug"]
    path = project_path(slug, lang)
    proj_root = "/en/projects/" if lang == "en" else "/projets/"
    idx = projects.index(p)
    prev_p, next_p = projects[idx - 1], projects[(idx + 1) % len(projects)]

    kpis = "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in p["kpis"])
    buttons = []
    for label, href, primary in p.get("links", []):
        cls = "contact-btn contact-btn-primary" if primary else "contact-btn contact-btn-secondary"
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") or href.startswith("/live") else ""
        buttons.append(f'<a href="{href}"{ext} class="{cls}">{e(label)} {arrow()}</a>')

    badge = (f'<div class="live-badge" style="position:static;display:inline-flex;margin-bottom:1.2rem">'
             f'<span class="live-dot"></span> {e(p["badge"])}</div>') if p.get("badge") else ""
    out = [head(f"{p['title']} — Patrice Duclos", p["lead"], path, lang), nav(projects, path, lang)]
    custom = "".join(f"""
    <section class="page-section{' alt' if i % 2 == 0 else ''}" id="{sid}">
        <div class="section-container">
            <span class="section-label">// {label}</span>
            <h2>{title}</h2>
            {body}
        </div>
    </section>
""" for i, (sid, label, title, body) in enumerate(p.get("custom_sections", [])))
    diagrams = [(slug, t["p_drawio"])] + list(p.get("extra_diagrams", []))
    out.append(f"""
    <header class="page-hero">
        <div class="hero-bg-grid"></div>
        <div class="hero-glow hero-glow-1"></div>
        <div class="hero-content">
            {badge}
            <div class="breadcrumb"><a href="{home(lang)}">{t['home']}</a> / <a href="{proj_root}">{t['projects']}</a> / {e(p['short'])}</div>
            <span class="project-tag" style="color:var(--accent)">{e(p['kicker'])}</span>
            <h1>{p['title_html']}</h1>
            <p class="lead">{p['lead']}</p>
            <div class="kpi-row">{kpis}</div>
            <div class="btn-row">{''.join(buttons)}</div>
        </div>
    </header>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// {t['p_30s']}</span>
            <h2>{t['p_30s_title']}</h2>
            <div style="margin-bottom:2rem">{''.join(f'<p>{x}</p>' for x in p['context'])}</div>
            <div class="two-col">
                <div class="arg-card arg-card--rh reveal">
                    <span class="arg-label">{t['p_rh']}</span>
                    <ul>{''.join(f'<li>{x}</li>' for x in p['rh'])}</ul>
                </div>
                <div class="arg-card arg-card--tech reveal">
                    <span class="arg-label">{t['p_tech']}</span>
                    <ul>{''.join(f'<li>{x}</li>' for x in p['tech'])}</ul>
                </div>
            </div>
        </div>
    </section>

{custom}
    <section class="page-section alt" id="pipeline">
        <div class="section-container">
            <span class="section-label">// {t['p_pipe_label']}</span>
            <h2>{t['p_pipe_title']}</h2>
            <p>{t['p_pipe_intro']}</p>
            {repo_cards(p, lang)}
            {interactive(p, diagrams, partial(figure, lang=lang), lang)}
            <h3 class="pl-steps-title">{t['p_steps']}</h3>
            <ol class="pipeline-steps">{''.join(f'<li>{x}</li>' for x in p['steps'])}</ol>
        </div>
    </section>

    <section class="page-section" id="points-forts">
        <div class="section-container">
            <span class="section-label">// {t['p_pf_label']}</span>
            <h2>{t['p_pf_title']}</h2>
            <ol class="pf-grid">{strengths(p)}</ol>
        </div>
    </section>
""")

    stack_rows = "".join(f"<tr><td>{e(tool)}</td><td>{r}</td><td>{w}</td></tr>" for tool, r, w in p["stack"])
    mlops = "" if not p.get("matrix") else "".join(
        f'<tr><td>{label}</td><td>{mark[p["matrix"][k]][0]} {mark[p["matrix"][k]][1]}</td>'
        f'<td>{e(p.get("matrix_notes", {}).get(k, ""))}</td></tr>'
        for k, label in MATRIX_COLS_I18N[lang])
    out.append(f"""
    <section class="page-section alt" id="stack">
        <div class="section-container">
            <span class="section-label">// {t['p_stack_label']}</span>
            <h2>{t['p_stack_title']}</h2>
            <div class="two-col" style="margin-bottom:2rem;align-items:start">
                <div class="skill-group"><h3 class="skill-group-title">{t['p_langs']}</h3>{lang_bars(p['langs']) if p.get('langs') else ''}
                    <p class="code-caption" style="margin-top:1rem">{e(p.get('langs_note', t['p_langs_note']))}</p></div>
                <div class="skill-group"><h3 class="skill-group-title">{t['p_keywords']}</h3>
                    <div class="project-tech">{badges(p['tags'])}</div></div>
            </div>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>{t['p_tool']}</th><th>{t['p_role']}</th><th>{t['p_shows']}</th></tr></thead>
                <tbody>{stack_rows}</tbody></table></div>
        </div>
    </section>

""")
    if mlops:
        out.append(f"""
    <section class="page-section" id="mlops">
        <div class="section-container">
            <span class="section-label">// {t['p_mlops_label']}</span>
            <h2>{t['p_mlops_title']}</h2>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>{t['p_practice']}</th><th>{t['p_status']}</th><th>{t['p_detail']}</th></tr></thead>
                <tbody>{mlops}</tbody></table></div>
        </div>
    </section>
""")
    if p.get("metrics"):
        head_row = "".join(f"<th>{e(h)}</th>" for h in p["metrics"]["head"])
        body = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in row) + "</tr>" for row in p["metrics"]["rows"])
        out.append(f"""
    <section class="page-section alt" id="resultats">
        <div class="section-container">
            <span class="section-label">// {t['p_res_label']}</span>
            <h2>{t['p_res_title']}</h2>
            <div class="table-wrap"><table class="stack-table"><thead><tr>{head_row}</tr></thead><tbody>{body}</tbody></table></div>
            <p style="margin-top:1.2rem">{p['metrics']['note']}</p>
        </div>
    </section>
""")
    snippets = "".join(
        f'<p class="code-caption">{e(cap)}</p><pre class="code"><code>{e(code)}</code></pre>' for cap, code in p.get("snippets", []))
    if snippets:
        out.append(f"""
    <section class="page-section" id="code">
        <div class="section-container">
            <span class="section-label">// {t['p_code_label']}</span>
            <h2>{t['p_code_title']}</h2>
            {snippets}
        </div>
    </section>
""")
    out.append(f"""
    <section class="page-section alt" id="suite">
        <div class="section-container">
            <span class="section-label">// {t['p_lim_label']}</span>
            <h2>{t['p_lim_title']}</h2>
            <p style="margin-bottom:1.5rem">{t['p_lim_intro']}</p>
            <div class="arg-card arg-card--ok"><ul>{''.join(f'<li>{x}</li>' for x in p['limits'])}</ul></div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container pager">
            <a href="{proj_root}{prev_p['slug']}.html"><small>{t['p_prev']}</small>{e(prev_p['short'])}</a>
            <a class="next" href="{proj_root}{next_p['slug']}.html"><small>{t['p_next']}</small>{e(next_p['short'])}</a>
        </div>
    </section>
""")
    out.append(footer(lang))
    return "".join(out)
