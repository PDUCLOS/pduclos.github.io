"""Compétences organisées selon les blocs de la certification Architecte en IA (RNCP 38777, niveau 7).

Intitulés des blocs et compétences : fiche France Compétences RNCP 38777 (reformulées).
Les niveaux des outils viennent de STACK (build.py) : une seule source de vérité.
"""
from render import e, arrow

CERTIF = {
    "title": "Architecte en intelligence artificielle",
    "org": "Jedha",
    "rncp": "RNCP 38777",
    "level": "Niveau 7 (Bac+5)",
    "year": "2026",
    "url": "https://www.francecompetences.fr/recherche/rncp/38777/",
}

# code, titre officiel, accroche, couleur, compétences, outils (noms exacts de STACK), projets (slugs)
BLOCS = [
    ("BC01", "Concevoir et piloter la gouvernance des données", "Gouvernance", "#F59E0B",
     ["Concevoir une politique de gouvernance des données avec les parties prenantes : conformité réglementaire, qualité, disponibilité, sécurité et confidentialité",
      "Promouvoir la politique de gouvernance et la faire appliquer par les équipes de l'entreprise",
      "Former et sensibiliser l'ensemble des collaborateurs à la gouvernance des données, y compris les personnes en situation de handicap",
      "Auditer régulièrement les pratiques de gestion des données au regard des réglementations locales et internationales (RGPD)",
      "Évaluer les risques liés aux données, en particulier de qualité et de sécurité"],
     ["Gouvernance / RGPD", "SQL (analytique, spatial, OLAP)", "pytest (≈ 1 600 tests cumulés)"],
     ["gouvernance-spotify", "stripe-fraude-temps-reel", "csvtraitement", "lyonflow"]),
    ("BC02", "Concevoir et déployer des architectures de données pour l'IA", "Architecture", "#38BDF8",
     ["Identifier les besoins d'architecture en analysant les contraintes techniques, opérationnelles et les normes applicables",
      "Rédiger le cahier des charges de l'architecture de données",
      "Élaborer les modèles de données logiques et physiques",
      "Concevoir des bases de données adaptées aux exigences de performance, de sécurité, de passage à l'échelle et de volume",
      "Déployer des serveurs virtuels, dans le cloud ou on-premise, pour l'entraînement des modèles d'IA",
      "Concevoir des clusters de serveurs pour augmenter la capacité de calcul",
      "Mettre en place la supervision et l'optimisation de l'infrastructure",
      "Documenter l'architecture de manière accessible"],
     ["PostgreSQL / PostGIS / pgRouting", "Snowflake / Delta Lake", "Redis (feature store)", "MongoDB",
      "TimescaleDB", "Terraform (AWS)", "Nginx, systemd, TLS, VPS Linux", "Kubernetes (manifests)", "Prometheus / Grafana"],
     ["stripe-fraude-temps-reel", "lyonflow", "maintenance-predictive", "marche-hvac"]),
    ("BC03", "Concevoir et mettre en œuvre des pipelines de données pour l'IA", "Pipelines", "#34D399",
     ["Concevoir un système de gestion de données en temps réel adapté aux contraintes opérationnelles",
      "Construire des pipelines ETL / ELT pour déplacer et transformer les données entre systèmes",
      "Automatiser les flux de données",
      "Surveiller les flux de données : qualité et conformité à la politique de gouvernance",
      "Développer des procédures de contrôle qualité et de correction des erreurs"],
     ["Apache Airflow", "Kafka + Debezium (CDC)", "Databricks DLT / Asset Bundles", "Kubernetes CronJob",
      "SQL (analytique, spatial, OLAP)"],
     ["detection-fraude", "lyonflow", "stripe-fraude-temps-reel", "marche-hvac", "csvtraitement"]),
    ("BC04", "Construire, déployer et piloter des solutions d'IA", "Solutions IA", "#818CF8",
     ["Rédiger le cahier des charges d'une solution d'IA : besoins techniques, économiques et d'accessibilité",
      "Développer l'algorithme d'IA adapté aux données d'entraînement et au cahier des charges",
      "Construire les API de mise en production de la solution d'IA",
      "Concevoir les pipelines d'intégration et de déploiement continus (CI/CD) de la solution",
      "Développer les scripts de réentraînement automatique des modèles",
      "Piloter la performance des modèles en production par le monitoring (Evidently, PSI)"],
     ["XGBoost / LightGBM", "scikit-learn", "Séries temporelles (Prophet, LSTM)", "Traitement du signal (SciPy)",
      "SHAP / explicabilité", "RAG hybride (dense + BM25 + RRF)", "LLM local (MLX, Qwen2.5)", "LangChain LCEL / RAGAS",
      "Model Context Protocol", "MLflow (tracking + registry)", "Drift : Evidently / PSI", "FastAPI",
      "Docker / Docker Compose", "GitHub Actions (ruff, mypy, bandit, CodeQL)", "Streamlit"],
     ["lyonflow", "stripe-fraude-temps-reel", "detection-fraude", "copilot-maintenance",
      "maintenance-predictive", "marche-hvac", "mcp-open-data", "predictira"]),
    ("MÉTIER", "Piloter un projet data, du besoin métier à la décision", "Métier & pilotage", "#F472B6",
     ["Conduire un projet de bout en bout : cadrage, business case, cahier des charges, recette, déploiement",
      "Traduire un besoin métier en indicateurs et en décisions chiffrées (Business Analyst)",
      "20 ans de distribution industrielle B2B : HVAC, énergie, supply chain, grands comptes",
      "Restituer aux décideurs : tableaux de bord, présentations, argumentaires"],
     ["Power BI / DAX / Power Query", "Excel avancé / VBA", "SAP / ERP", "Streamlit"],
     ["achats-negociation", "carrier-reporting", "marche-hvac"]),
]


# Épreuve validée pour chaque bloc (référentiel d'évaluation RNCP 38777)
EPREUVES = {
    "BC01": "Plan de gouvernance pour une organisation, présenté et défendu devant le jury.",
    "BC02": "Mise en situation professionnelle : plan d'infrastructure, code de déploiement sur GitHub, démonstration en production, soutenance.",
    "BC03": "Mise en situation professionnelle : plan des pipelines, code sur GitHub, démonstration du pipeline en production, soutenance.",
    "BC04": "Mise en situation professionnelle : solution d'IA, code et pipeline CI/CD sur GitHub, démonstration en production, soutenance.",
}


UI = {
    "fr": dict(lvl="niveau {lvl} sur 5", radar_aria="Niveau moyen des outils par bloc de compétences", all="Tout voir",
               official="Compétences certifiées (référentiel RNCP 38777)", base="Socle professionnel", exam="Épreuve validée",
               meta="{c} compétences · {t} outils · {p} projets · niveau moyen {a} / 5", tools="Outils maîtrisés", used="Mis en œuvre dans",
               badge="✓ Délivrée le 7 octobre 2026 par décision du jury", k_blocs="blocs validés", k_comps="compétences certifiées",
               k_proj="projets de preuve",
               intro="Quatre blocs validés devant jury, du cadrage de la gouvernance à l'exploitation de modèles en production. "
                     "Chaque bloc ci-dessous est relié aux outils employés et aux projets où les vérifier.",
               n_comps="{n} compétences", official_link="Fiche officielle France Compétences",
               caption="Niveau moyen auto-évalué des outils de chaque bloc (1 à 5). Cliquez un bloc pour l'explorer.",
               explore="Explorer", by_bloc="Compétences par bloc", filter="Filtrer par bloc", search="Rechercher un outil",
               placeholder="Rechercher un outil : Airflow, RAG, Terraform…", empty="Aucun outil ne correspond à cette recherche.",
               proofs="Preuves", matrix_title="Projets × blocs de compétences",
               matrix_intro="Quels projets mobilisent quel bloc. Survolez une colonne pour la mettre en évidence.", project="Projet",
               home_cert="compétences certifiées", home_biz="compétences métier", page="/competences.html"),
    "en": dict(lvl="level {lvl} out of 5", radar_aria="Average tool level per skill block", all="Show all",
               official="Certified skills (RNCP 38777 framework)", base="Professional foundation", exam="Assessment passed",
               meta="{c} skills · {t} tools · {p} projects · average level {a} / 5", tools="Tools mastered", used="Applied in",
               badge="✓ Awarded on October 7, 2026 by decision of the jury", k_blocs="blocks passed", k_comps="certified skills",
               k_proj="supporting projects",
               intro="Four blocks passed before a jury, from framing data governance to running models in production. "
                     "Each block below is linked to the tools used and to the projects where you can check them.",
               n_comps="{n} skills", official_link="Official France Compétences listing",
               caption="Self-assessed average tool level per block (1 to 5). Click a block to explore it.",
               explore="Explore", by_bloc="Skills by block", filter="Filter by block", search="Search for a tool",
               placeholder="Search for a tool: Airflow, RAG, Terraform…", empty="No tool matches this search.",
               proofs="Evidence", matrix_title="Projects × skill blocks",
               matrix_intro="Which projects draw on which block. Hover over a column to highlight it.", project="Project",
               home_cert="certified skills", home_biz="business skills", page="/en/skills.html"),
}


def _content(lang):
    if lang == "en":
        import site_en
        return site_en.BLOCS_EN, site_en.CERTIF_EN, site_en.EPREUVES_EN
    return BLOCS, CERTIF, EPREUVES


def _ppath(slug, lang):
    return f"/en/projects/{slug}.html" if lang == "en" else f"/projets/{slug}.html"


def _levels(stack):
    return {name: (lvl, where) for _, items in stack for name, lvl, where in items}


def _bar(lvl, color, lang="fr"):
    segs = "".join(f'<i class="{"on" if i < lvl else ""}"></i>' for i in range(5))
    return f'<span class="cp-bar" style="--c:{color}" role="img" aria-label="{UI[lang]["lvl"].format(lvl=lvl)}">{segs}</span>'


def _avg(tools, levels):
    vals = [levels[t][0] for t in tools]
    return sum(vals) / len(vals)


def radar(stack, lang="fr"):
    """SVG radar : niveau moyen des outils de chaque bloc (dérivé de STACK)."""
    import math
    blocs = _content(lang)[0]
    levels = _levels(stack)
    n, cx, cy, r = len(blocs), 160, 150, 110
    def pt(i, v):
        a = -math.pi / 2 + 2 * math.pi * i / n
        return cx + r * v / 5 * math.cos(a), cy + r * v / 5 * math.sin(a)
    rings = "".join(
        f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, k) for i in range(n)))}" class="cp-ring"/>'
        for k in range(1, 6))
    spokes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{pt(i, 5)[0]:.1f}" y2="{pt(i, 5)[1]:.1f}" class="cp-ring"/>' for i in range(n))
    avgs = [_avg(b[5], levels) for b in blocs]
    shape = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, v) for i, v in enumerate(avgs)))
    dots, labels = [], []
    for i, (b, v) in enumerate(zip(blocs, avgs)):
        x, y = pt(i, v)
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{b[3]}" class="cp-radar-dot" data-bloc="{b[0]}">'
                    f'<title>{e(b[2])} : {v:.1f} / 5</title></circle>')
        lx, ly = pt(i, 6.15)
        anchor = "middle" if abs(lx - cx) < 20 else ("start" if lx > cx else "end")
        labels.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" class="cp-radar-label" data-bloc="{b[0]}">'
                      f'<tspan fill="{b[3]}">{e(b[0])}</tspan><tspan x="{lx:.1f}" dy="1.15em">{e(b[2])}</tspan></text>')
    return f"""<svg class="cp-radar" viewBox="-20 -5 360 320" role="img" aria-label="{UI[lang]['radar_aria']}">
        {rings}{spokes}<polygon points="{shape}" class="cp-shape"/>{''.join(dots)}{''.join(labels)}</svg>"""


def section(stack, projects, lang="fr"):
    """Contenu interactif de la page compétences (FR ou EN)."""
    u = UI[lang]
    blocs, certif, epreuves = _content(lang)
    levels = _levels(stack)
    by_slug = {p["slug"]: p for p in projects}
    tabs = [f'<button class="cp-tab" aria-pressed="true" data-filter="all">{u["all"]}</button>'] + [
        f'<button class="cp-tab" aria-pressed="false" data-filter="{b[0]}" style="--c:{b[3]}">'
        f'<b>{e(b[0])}</b> {e(b[2])}</button>' for b in blocs]
    cards = []
    for code, title, short, color, comps, tools, slugs in blocs:
        comp_li = "".join(f"<li>{e(c)}</li>" for c in comps)
        tool_rows = "".join(
            f'<li class="cp-tool" data-name="{e(t.lower())}"><span>{e(t)}<small>{e(levels[t][1])}</small></span>{_bar(levels[t][0], color, lang)}</li>'
            for t in sorted(tools, key=lambda t: -levels[t][0]))
        proj = "".join(f'<a class="cp-proj" href="{_ppath(s, lang)}">{e(by_slug[s]["short"])}</a>' for s in slugs)
        official = u["official"] if code.startswith("BC") else u["base"]
        epreuve = (f'<p class="cp-epreuve"><b>{u["exam"]}</b>{e(epreuves[code])}</p>' if code in epreuves else "")
        meta = u["meta"].format(c=len(comps), t=len(tools), p=len(slugs), a=f"{_avg(tools, levels):.1f}")
        cards.append(f"""
        <article class="cp-card" id="{code.lower()}" data-bloc="{code}" style="--c:{color}">
            <header class="cp-card-head">
                <span class="cp-code">{e(code)}</span>
                <div><h3>{e(title)}</h3><span class="cp-meta">{meta}</span></div>
            </header>
            <div class="cp-card-body">
                <div><h4>{official} · {len(comps)}</h4><ul class="cp-comps">{comp_li}</ul>{epreuve}</div>
                <div><h4>{u['tools']}</h4><ul class="cp-tools">{tool_rows}</ul></div>
            </div>
            <footer class="cp-projs"><h4>{u['used']}</h4>{proj}</footer>
        </article>""")
    # matrice projets × blocs
    used = []
    for b in blocs:
        for s in b[6]:
            if s not in used:
                used.append(s)
    used.sort(key=lambda s: [p["slug"] for p in projects].index(s))
    head_cells = "".join(f'<th data-bloc="{b[0]}" style="--c:{b[3]}">{e(b[0])}</th>' for b in blocs)
    rows = "".join(
        f'<tr><td><a href="{_ppath(s, lang)}">{e(by_slug[s]["short"])}</a></td>'
        + "".join(f'<td data-bloc="{b[0]}" style="--c:{b[3]}">{"<span class=cp-dot></span>" if s in b[6] else ""}</td>' for b in blocs)
        + "</tr>" for s in used)
    n_cert = sum(len(b[4]) for b in blocs if b[0].startswith('BC'))
    n_proj = len({s for b in blocs for s in b[6]})
    blocs_li = ''.join(f'<li style="--c:{b[3]}"><b>{e(b[0])}</b><span>{e(b[1])}</span><em>{u["n_comps"].format(n=len(b[4]))}</em></li>'
                       for b in blocs if b[0].startswith('BC'))
    return f"""
    <section class="page-section">
        <div class="section-container cp-overview">
            <div class="cp-certif reveal">
                <span class="cp-certif-badge">{u['badge']}</span>
                <h2>{e(certif['title'])}</h2>
                <p class="cp-certif-sub">{e(certif['org'])} · {e(certif['rncp'])} · {e(certif['level'])} · NSF 114b / 326 / 326t</p>
                <div class="cp-kpis"><span><b>4</b>{u['k_blocs']}</span><span><b>{n_cert}</b>{u['k_comps']}</span><span><b>{n_proj}</b>{u['k_proj']}</span></div>
                <p>{u['intro']}</p>
                <ol class="cp-certif-blocs">{blocs_li}</ol>
                <a class="cp-link" href="{certif['url']}" target="_blank" rel="noopener">{u['official_link']} {arrow()}</a>
            </div>
            <figure class="cp-radar-wrap reveal">
                {radar(stack, lang)}
                <figcaption>{u['caption']}</figcaption>
            </figure>
        </div>
    </section>

    <section class="page-section alt" id="explorer">
        <div class="section-container">
            <span class="section-label">// {u['explore']}</span>
            <h2>{u['by_bloc']}</h2>
            <div class="cp-controls">
                <div class="cp-tabs" role="group" aria-label="{u['filter']}">{''.join(tabs)}</div>
                <label class="cp-search"><span class="sr-only">{u['search']}</span>
                    <input type="search" placeholder="{u['placeholder']}" autocomplete="off"></label>
            </div>
            <p class="cp-empty" hidden>{u['empty']}</p>
            <div class="cp-cards">{''.join(cards)}</div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// {u['proofs']}</span>
            <h2>{u['matrix_title']}</h2>
            <p style="margin-bottom:1.5rem">{u['matrix_intro']}</p>
            <div class="table-wrap" style="overflow-x:auto"><table class="matrix cp-matrix">
                <thead><tr><th>{u['project']}</th>{head_cells}</tr></thead><tbody>{rows}</tbody></table></div>
        </div>
    </section>
"""


def home_skills(stack, lang="fr"):
    """Bloc compact pour la section #skills de l'accueil."""
    u = UI[lang]
    blocs = _content(lang)[0]
    levels = _levels(stack)
    cards = "".join(f"""
                <a class="skill-group cp-home reveal" href="{u['page']}#{b[0].lower()}" style="--c:{b[3]}">
                    <span class="cp-code">{e(b[0])}</span>
                    <h3 class="skill-group-title">{e(b[1])}</h3>
                    <span class="cp-meta">{len(b[4])} {u['home_cert'] if b[0].startswith('BC') else u['home_biz']}</span>
                    <div class="project-tech">{''.join(f'<span class="tech-badge">{e(t.split(" (")[0])}</span>' for t in sorted(b[5], key=lambda t: -levels[t][0])[:5])}</div>
                </a>""" for b in blocs)
    return f"""<!-- SKILLS:START -->
            <div class="skills-grid cp-home-grid">{cards}
            </div>
            <!-- SKILLS:END -->"""
