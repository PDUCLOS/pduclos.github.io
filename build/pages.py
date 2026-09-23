"""Render project pages from the PROJECTS data."""
from urllib.parse import quote
from render import head, nav, FOOTER, badges, arrow, e, REPO_RAW

MATRIX_COLS = [("ci", "CI/CD"), ("tests", "Tests"), ("docker", "Docker"), ("orch", "Orchestration"),
               ("tracking", "Tracking / registry"), ("monitoring", "Monitoring / drift"),
               ("serving", "API"), ("deploy", "Déploiement"), ("iac", "IaC / K8s")]
MARK = {"y": ('<span class="m-yes" title="Implémenté">●</span>', "Implémenté"),
        "p": ('<span class="m-part" title="Partiel">◐</span>', "Partiel"),
        "n": ('<span class="m-no" title="Absent">—</span>', "Absent")}


def drawio_links(path):
    raw = f"{REPO_RAW}{path}"
    return (f'<a href="{path}" download>⬇ Fichier .drawio</a>'
            f'<a href="https://app.diagrams.net/#U{quote(raw, safe="")}" target="_blank" rel="noopener">✎ Ouvrir dans draw.io</a>')


def figure(svg, drawio, alt):
    return f"""<div class="pipeline-figure"><img src="{svg}" alt="{e(alt)}" loading="lazy"></div>
            <div class="figure-actions"><a href="{svg}" target="_blank">⤢ Plein écran (SVG)</a>{drawio_links(drawio)}</div>"""


def lang_bars(langs):
    rows = []
    for name, pct in langs:
        rows.append(f"""<div class="skill-item"><span class="skill-name">{e(name)}</span>
                <span style="flex:1;margin:0 1rem;height:6px;background:var(--border);border-radius:3px;overflow:hidden">
                <span style="display:block;height:100%;width:{pct}%;background:var(--gradient-1)"></span></span>
                <span class="code-caption">{pct}%</span></div>""")
    return '<div class="skill-items">' + "".join(rows) + "</div>"


def project_page(p, projects):
    slug = p["slug"]
    path = f"/projets/{slug}.html"
    idx = projects.index(p)
    prev_p, next_p = projects[idx - 1], projects[(idx + 1) % len(projects)]

    kpis = "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in p["kpis"])
    buttons = []
    for label, href, primary in p.get("links", []):
        cls = "contact-btn contact-btn-primary" if primary else "contact-btn contact-btn-secondary"
        buttons.append(f'<a href="{href}" target="_blank" rel="noopener" class="{cls}">{e(label)} {arrow()}</a>')

    out = [head(f"{p['title']} — Patrice Duclos", p["lead"], path), nav(projects, path)]
    out.append(f"""
    <header class="page-hero">
        <div class="hero-bg-grid"></div>
        <div class="hero-glow hero-glow-1"></div>
        <div class="hero-content">
            <div class="breadcrumb"><a href="/">Accueil</a> / <a href="/projets/">Projets</a> / {e(p['short'])}</div>
            <span class="project-tag" style="color:var(--accent)">{e(p['kicker'])}</span>
            <h1>{p['title_html']}</h1>
            <p class="lead">{p['lead']}</p>
            <div class="kpi-row">{kpis}</div>
            <div class="btn-row">{''.join(buttons)}</div>
        </div>
    </header>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// En 30 secondes</span>
            <h2>Le problème, la réponse, la preuve</h2>
            <div style="margin-bottom:2rem">{''.join(f'<p>{x}</p>' for x in p['context'])}</div>
            <div class="two-col">
                <div class="arg-card arg-card--rh reveal">
                    <span class="arg-label">Pour le recruteur · valeur business</span>
                    <ul>{''.join(f'<li>{x}</li>' for x in p['rh'])}</ul>
                </div>
                <div class="arg-card arg-card--tech reveal">
                    <span class="arg-label">Pour l'équipe technique · ce que le code prouve</span>
                    <ul>{''.join(f'<li>{x}</li>' for x in p['tech'])}</ul>
                </div>
            </div>
        </div>
    </section>

    <section class="page-section alt" id="pipeline">
        <div class="section-container">
            <span class="section-label">// Pipeline</span>
            <h2>Architecture de bout en bout</h2>
            <p>Schéma draw.io généré à partir de l'analyse du dépôt : chaque brique correspond à du code réel.
               Le fichier source est téléchargeable et modifiable.</p>
            {figure(f'/diagrams/{slug}.svg', f'/diagrams/{slug}.drawio', 'Pipeline ' + p['short'])}
            <ol class="pipeline-steps">{''.join(f'<li>{x}</li>' for x in p['steps'])}</ol>
        </div>
    </section>
""")
    if p.get("extra_diagrams"):
        figs = []
        for d_slug, caption in p["extra_diagrams"]:
            figs.append(f"""<div class="reveal" style="margin-bottom:2.5rem"><h3>{e(caption)}</h3>
                {figure(f'/diagrams/{d_slug}.svg', f'/diagrams/{d_slug}.drawio', caption)}</div>""")
        out.append(f"""
    <section class="page-section" id="schemas">
        <div class="section-container">
            <span class="section-label">// Schémas détaillés</span>
            <h2>Les diagrammes d'architecture du projet</h2>
            <p style="margin-bottom:2rem">Diagrammes draw.io réalisés pendant le projet et versionnés dans le dépôt
               (données d'infrastructure sensibles masquées).</p>
            {''.join(figs)}
        </div>
    </section>
""")

    stack_rows = "".join(f"<tr><td>{e(t)}</td><td>{r}</td><td>{w}</td></tr>" for t, r, w in p["stack"])
    mlops = "" if not p.get("matrix") else "".join(
        f'<tr><td>{label}</td><td>{MARK[p["matrix"][k]][0]} {MARK[p["matrix"][k]][1]}</td>'
        f'<td>{e(p.get("matrix_notes", {}).get(k, ""))}</td></tr>'
        for k, label in MATRIX_COLS)
    out.append(f"""
    <section class="page-section alt" id="stack">
        <div class="section-container">
            <span class="section-label">// Outils & langages</span>
            <h2>Stack technique et pourquoi ces choix</h2>
            <div class="two-col" style="margin-bottom:2rem;align-items:start">
                <div class="skill-group"><h3 class="skill-group-title">Langages (part du code)</h3>{lang_bars(p['langs'])}
                    <p class="code-caption" style="margin-top:1rem">{e(p.get('langs_note', 'Lignes de code hors notebooks, calculées sur le dépôt.'))}</p></div>
                <div class="skill-group"><h3 class="skill-group-title">Mots-clés</h3>
                    <div class="project-tech">{badges(p['tags'])}</div></div>
            </div>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>Outil</th><th>Rôle dans le projet</th><th>Ce que ça démontre</th></tr></thead>
                <tbody>{stack_rows}</tbody></table></div>
        </div>
    </section>

""")
    if mlops:
        out.append(f"""
    <section class="page-section" id="mlops">
        <div class="section-container">
            <span class="section-label">// Maturité MLOps</span>
            <h2>Industrialisation : ce qui est en place</h2>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>Pratique</th><th>Statut</th><th>Détail</th></tr></thead>
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
            <span class="section-label">// Résultats</span>
            <h2>Métriques mesurées</h2>
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
            <span class="section-label">// Extraits de code</span>
            <h2>Le code qui fait la différence</h2>
            {snippets}
        </div>
    </section>
""")
    out.append(f"""
    <section class="page-section alt" id="suite">
        <div class="section-container">
            <span class="section-label">// Regard critique</span>
            <h2>Limites connues et prochaines étapes</h2>
            <p style="margin-bottom:1.5rem">Documenter honnêtement les limites fait partie du travail : c'est ce qui permet
               à une équipe de décider en connaissance de cause.</p>
            <div class="arg-card arg-card--ok"><ul>{''.join(f'<li>{x}</li>' for x in p['limits'])}</ul></div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container pager">
            <a href="/projets/{prev_p['slug']}.html"><small>← Projet précédent</small>{e(prev_p['short'])}</a>
            <a class="next" href="/projets/{next_p['slug']}.html"><small>Projet suivant →</small>{e(next_p['short'])}</a>
        </div>
    </section>
""")
    out.append(FOOTER)
    return "".join(out)
