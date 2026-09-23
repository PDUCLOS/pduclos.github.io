"""Build the multi-page portfolio: diagrams (draw.io -> SVG), project pages, audience pages, index nav.

Usage: python3 build/build.py   (from the site root or anywhere)
"""
import re
from pathlib import Path

from drawio import build_xml, write_and_export, slim_svg, DRAWIO_BIN
from pages import project_page, MATRIX_COLS, MARK
from projects import PROJECTS, GH
from render import head, nav, FOOTER, badges, arrow, e
import subprocess

SITE = Path(__file__).resolve().parent.parent
REPOS = SITE.parent / "repos"
DIAG = SITE / "diagrams"

# Existing diagrams from the project repositories, with sensitive strings masked before publication.
EXISTING = {
    "lyonflow-medallion": "lyonflowfull/présentation/drawio/01_flux_donnees_medallion.drawio",
    "lyonflow-infra": "lyonflowfull/présentation/drawio/02_infra_vps.drawio",
    "lyonflow-ml": "lyonflowfull/présentation/drawio/03_piliers_ml.drawio",
    "lyonflow-airflow": "lyonflowfull/présentation/drawio/04_pipeline_airflow.drawio",
    "stripe-architecture": "BLOC2-STRIPE/presentation/stripe_architecture_globale.drawio",
    "stripe-aws": "BLOC2-STRIPE/presentation/stripe_aws_cible.drawio",
    "fraude-pipeline": "BLOC3-FRAUD-DETECTION/docs/diagrams/02_pipeline.drawio",
}
# Masking rules live in build/redact.local (gitignored, tab-separated "regex<TAB>replacement")
# so the sensitive values themselves never get published with the build script.
REDACT = [(re.compile(rx), repl) for rx, repl in (
    line.split("\t", 1) for line in (Path(__file__).with_name("redact.local").read_text(encoding="utf-8").splitlines())
    if line.strip() and not line.startswith("#"))]


def export_existing():
    for slug, rel in EXISTING.items():
        src = REPOS / rel
        xml = src.read_text(encoding="utf-8")
        for rx, repl in REDACT:
            xml = rx.sub(repl, xml)
        for rx, _ in REDACT:
            assert not rx.search(xml), (slug, rx.pattern)
        out = DIAG / f"{slug}.drawio"
        out.write_text(xml, encoding="utf-8")
        subprocess.run([DRAWIO_BIN, "-x", "-f", "svg", "-b", "10", "-o", str(DIAG / f"{slug}.svg"), str(out)],
                       check=True, capture_output=True, timeout=180)
        slim_svg(DIAG / f"{slug}.svg")
        print("  existing", slug)


def export_generated():
    for p in PROJECTS:
        xml = build_xml(f"{p['short']} — pipeline", p["stages"], p["edges"], p.get("band"))
        write_and_export(p["slug"], xml, DIAG)
        print("  generated", p["slug"])


def write(path, html):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("  page", path.relative_to(SITE))


def hero(path_label, kicker, title_html, lead, extra=""):
    return f"""
    <header class="page-hero">
        <div class="hero-bg-grid"></div>
        <div class="hero-glow hero-glow-1"></div>
        <div class="hero-content">
            <div class="breadcrumb"><a href="/">Accueil</a> / {path_label}</div>
            <span class="project-tag" style="color:var(--accent)">{kicker}</span>
            <h1>{title_html}</h1>
            <p class="lead">{lead}</p>
            {extra}
        </div>
    </header>
"""


def matrix_table():
    head_cells = "".join(f"<th>{label}</th>" for _, label in MATRIX_COLS)
    rows = []
    for p in PROJECTS:
        if not p.get("matrix"):
            continue
        cells = "".join(f"<td>{MARK[p['matrix'][k]][0]}</td>" for k, _ in MATRIX_COLS)
        rows.append(f'<tr><td><a href="/projets/{p["slug"]}.html">{e(p["short"])}</a></td>{cells}</tr>')
    return f"""<div class="table-wrap" style="overflow-x:auto"><table class="matrix">
        <thead><tr><th>Projet</th>{head_cells}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
        <p class="code-caption" style="margin-top:0.8rem">● implémenté · ◐ partiel · — absent — établi à partir du code de chaque dépôt.</p>"""


def tile(p):
    return f"""<a class="proj-tile reveal" href="/projets/{p['slug']}.html">
        <span class="project-tag">{e(p['kicker'])}</span>
        <h3>{e(p['short'])}</h3>
        <p>{p['lead']}</p>
        <div class="project-tech">{badges(p['tags'][:6])}</div>
    </a>"""


# ---------------------------------------------------------------- pages
def page_projects_index():
    path = "/projets/"
    body = hero("Projets", "// Portfolio", 'Projets — <span class="highlight">du besoin métier à la production</span>',
                f"{len(PROJECTS)} projets documentés : pour chacun, le problème métier, le pipeline en draw.io, "
                "les outils et langages, le niveau d'industrialisation, les métriques et les limites assumées.")
    body += f"""
    <section class="page-section">
        <div class="section-container"><div class="proj-grid">{''.join(tile(p) for p in PROJECTS)}</div></div>
    </section>
    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Maturité MLOps</span>
            <h2>Matrice d'industrialisation</h2>
            <p style="margin-bottom:1.5rem">Ce qui est réellement en place dans chaque dépôt — de l'intégration continue au déploiement.</p>
            {matrix_table()}
        </div>
    </section>
"""
    write(SITE / "projets" / "index.html",
          head("Projets — Patrice Duclos", "Tous les projets data, ML et MLOps de Patrice Duclos : pipelines, outils, métriques.", path)
          + nav(PROJECTS, path) + body + FOOTER)


STACK = [
    ("Orchestration & pipelines", [("Apache Airflow", 4, "LyonFlow (27 DAGs), Stripe, Fraude, HVAC"),
                                   ("Kafka + Debezium (CDC)", 3, "Stripe"),
                                   ("Kubernetes CronJob", 2, "HVAC"),
                                   ("Databricks DLT / Asset Bundles", 2, "LyonFlow Databricks")]),
    ("Stockage & modélisation", [("PostgreSQL / PostGIS / pgRouting", 4, "LyonFlow, Stripe, Fraude"),
                                 ("SQL (analytique, spatial, OLAP)", 4, "tous les projets"),
                                 ("Redis (feature store)", 3, "Stripe"),
                                 ("MongoDB", 3, "Stripe"),
                                 ("TimescaleDB", 3, "Maintenance prédictive"),
                                 ("Snowflake / Delta Lake", 2, "Stripe, LyonFlow Databricks"),
                                 ("ChromaDB (vectoriel)", 3, "Copilote maintenance")]),
    ("Machine Learning", [("XGBoost / LightGBM", 4, "LyonFlow, Stripe, Fraude, HVAC, IRA"),
                          ("scikit-learn", 4, "tous les projets ML"),
                          ("Séries temporelles (Prophet, LSTM)", 3, "HVAC"),
                          ("Traitement du signal (SciPy)", 3, "Maintenance prédictive"),
                          ("SHAP / explicabilité", 3, "HVAC")]),
    ("IA générative & agents", [("RAG hybride (dense + BM25 + RRF)", 3, "Copilote maintenance"),
                                ("LLM local (MLX, Qwen2.5)", 3, "Copilote maintenance"),
                                ("LangChain LCEL / RAGAS", 3, "Copilote maintenance"),
                                ("Model Context Protocol", 3, "Serveurs MCP")]),
    ("MLOps & qualité", [("MLflow (tracking + registry)", 4, "LyonFlow, Stripe, Maintenance prédictive"),
                         ("Drift : Evidently / PSI", 4, "LyonFlow, Stripe, Maintenance prédictive"),
                         ("pytest (≈ 1 600 tests cumulés)", 4, "LyonFlow 620, HVAC 562, MLindustrial 189…"),
                         ("GitHub Actions (ruff, mypy, bandit, CodeQL)", 4, "LyonFlow, Stripe, HVAC, RAG, MLindustrial"),
                         ("Prometheus / Grafana", 3, "LyonFlow, Copilote maintenance")]),
    ("Déploiement & infrastructure", [("Docker / Docker Compose", 4, "tous les projets industrialisés"),
                                      ("FastAPI", 4, "LyonFlow, Fraude, HVAC, RAG, IRA"),
                                      ("Nginx, systemd, TLS, VPS Linux", 3, "LyonFlow"),
                                      ("Terraform (AWS)", 3, "Stripe"),
                                      ("Kubernetes (manifests)", 2, "HVAC")]),
    ("Restitution & métier", [("Power BI / DAX / Power Query", 5, "Carrier"),
                              ("Streamlit", 4, "LyonFlow, Stripe, Fraude, HVAC, RAG"),
                              ("SAP / ERP", 4, "Carrier, 20 ans de distribution"),
                              ("Excel avancé / VBA", 5, "Carrier"),
                              ("Gouvernance / RGPD", 3, "Spotify, LyonFlow, Stripe")]),
]


def dots(n):
    return '<div class="skill-level">' + "".join(
        f'<span class="skill-dot{" active" if i < n else ""}"></span>' for i in range(5)) + "</div>"


def page_stack():
    path = "/stack.html"
    groups = []
    for title, items in STACK:
        rows = "".join(f"""<div class="skill-item" style="align-items:flex-start;gap:1rem">
                <span class="skill-name">{e(name)}<br><small class="code-caption">{e(where)}</small></span>{dots(lvl)}</div>"""
                       for name, lvl, where in items)
        groups.append(f'<div class="skill-group reveal"><h3 class="skill-group-title">{e(title)}</h3><div class="skill-items">{rows}</div></div>')
    langs = [("Python", "Langage principal : pipelines, ML, API, tests"), ("SQL", "PostgreSQL, spatial, OLAP, Snowflake"),
             ("HCL", "Terraform AWS"), ("DAX / M", "Power BI, Power Query"), ("Bash", "Déploiement, health checks"),
             ("YAML", "CI, Kubernetes, configs"), ("VBA", "Automatisation Excel")]
    lang_html = "".join(f'<div class="kpi"><b style="font-size:1.2rem">{e(n)}</b><span>{e(d)}</span></div>' for n, d in langs)
    body = hero("Stack MLOps", "// Compétences prouvées par le code",
                'Stack <span class="highlight">MLOps & Data</span> — chaque outil relié à un projet',
                "Niveaux auto-évalués (1 à 5), chacun adossé à au moins un dépôt public ou une expérience professionnelle. "
                "Cliquez sur les projets pour voir l'outil en situation.")
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Langages</span>
            <h2>Langages utilisés</h2>
            <div class="kpi-row">{lang_html}</div>
        </div>
    </section>
    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Outils</span>
            <h2>Outils par étape du cycle de vie</h2>
            <div class="skills-grid">{''.join(groups)}</div>
        </div>
    </section>
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Preuves</span>
            <h2>Où voir chaque pratique MLOps</h2>
            {matrix_table()}
        </div>
    </section>
"""
    write(SITE / "stack.html",
          head("Stack MLOps — Patrice Duclos", "Outils, langages et pratiques MLOps de Patrice Duclos, reliés aux projets.", path)
          + nav(PROJECTS, path) + body + FOOTER)


def page_rh():
    path = "/profil-rh.html"
    objections = [
        ("« C'est une reconversion : a-t-il vraiment le niveau ? »",
         "Deux certifications RNCP (niveau 6 obtenu, niveau 7 Lead Data Science / AI Architect en cours), une certification Databricks, "
         "10 mois chez Carrier avec des résultats chiffrés, et une plateforme MLOps <strong>en production</strong> accessible en ligne. "
         "La reconversion est terminée ; ce qui reste, c'est 20 ans de terrain que les profils juniors n'ont pas."),
        ("« Senior métier, mais junior technique ? »",
         "Le code est public et vérifiable : environ 1 600 tests automatisés cumulés, intégration continue, Docker, Airflow, MLflow, "
         "Terraform. La <a href=\"/profil-tech.html\" style=\"color:var(--accent)\">page technique</a> détaille chaque preuve."),
        ("« Pourquoi pas un profil plus jeune et moins cher ? »",
         "Parce que le coût d'un projet data raté ne vient presque jamais du code : il vient d'un problème mal posé. "
         "Je sais parler à un directeur commercial, un acheteur, un technicien de maintenance — et traduire leur besoin en indicateurs."),
        ("« Saura-t-il s'intégrer dans une équipe tech ? »",
         "Mes projets suivent les standards d'équipe : conventions documentées, tests bloquants en CI, "
         "documentation d'architecture, diagrammes draw.io. Expérience de projets d'équipe en formation et en contexte international chez Carrier."),
        ("« Quel type de poste ? »",
         "Data Analyst senior, Data Scientist, ML Engineer / MLOps, ou Lead Data dans l'industrie, l'énergie, la distribution B2B "
         "ou la supply chain — là où la double compétence métier + data a le plus de valeur. Région lyonnaise, hybride."),
    ]
    obj_html = "".join(f'<details class="objection"><summary>{q}</summary><p>{a}</p></details>' for q, a in objections)
    body = hero("Recruteurs", "// Pour les RH et managers",
                'Pourquoi me recruter — <span class="highlight">en 2 minutes</span>',
                "20 ans de distribution industrielle, une reconversion data certifiée et des projets en production : "
                "un profil qui comprend le métier <strong>et</strong> livre la solution technique.",
                '<div class="btn-row"><a class="contact-btn contact-btn-primary" href="/#contact">Me contacter ' + arrow() + '</a>'
                '<a class="contact-btn contact-btn-secondary" href="/projets/">Voir les projets ' + arrow() + '</a></div>')
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Proposition de valeur</span>
            <h2>Ce que j'apporte dès le premier mois</h2>
            <p class="pitch pitch--warm" style="margin-bottom:2rem">Je ne commence pas par les données : je commence par la question
               que se pose le décideur. Puis je construis l'outil qui y répond — et je le mets en production.</p>
            <div class="three-col">
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Impact business mesuré</span><ul>
                    <li><strong>−40 %</strong> de temps de traitement chez Carrier</li>
                    <li><strong>~100 K€/mois</strong> d'erreurs de données détectées</li>
                    <li><strong>5 sources SAP</strong> unifiées dans un pilotage européen</li></ul></div>
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Expertise métier rare</span><ul>
                    <li><strong>20 ans</strong> en distribution industrielle B2B (Michaud Chailly, Descours &amp; Cabaud)</li>
                    <li>HVAC, énergie, supply chain, grands comptes</li>
                    <li>Crédibilité immédiate face aux équipes terrain</li></ul></div>
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Livraison de bout en bout</span><ul>
                    <li>Plateforme <strong>en production</strong> (LyonFlow), consultable en ligne</li>
                    <li>{len(PROJECTS)} projets documentés, du besoin à l'API</li>
                    <li>IA générative appliquée à l'industrie (copilote maintenance)</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Savoir-être</span>
            <h2>Comment je travaille</h2>
            <div class="two-col">
                <div class="arg-card arg-card--ok reveal"><span class="arg-label">Ce que disent mes projets</span><ul>
                    <li><strong>Rigueur</strong> : chaque projet documente ses limites et ses erreurs corrigées.</li>
                    <li><strong>Autonomie</strong> : LyonFlow conçu, développé, déployé et exploité seul.</li>
                    <li><strong>Pédagogie</strong> : dashboards pensés par persona (usager, opérateur, élu).</li>
                    <li><strong>Sens du résultat</strong> : je mesure l'impact, pas l'activité.</li></ul></div>
                <div class="arg-card arg-card--ok reveal"><span class="arg-label">Ce que j'apporte à une équipe</span><ul>
                    <li>Un pont entre métiers et équipe data : je parle les deux langues.</li>
                    <li>La maturité d'un senior : priorisation, gestion des parties prenantes, négociation.</li>
                    <li>Une veille active : IA générative, agents (MCP), MLOps, Databricks.</li>
                    <li>Une communication claire en français et en anglais.</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Objections fréquentes</span>
            <h2>Les questions que vous vous posez peut-être</h2>
            {obj_html}
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Projets phares</span>
            <h2>Trois projets à regarder en priorité</h2>
            <div class="proj-grid">{''.join(tile(p) for p in PROJECTS if p['slug'] in ('lyonflow', 'carrier-reporting', 'copilot-maintenance'))}</div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Formation</span>
            <h2>Diplômes et certifications</h2>
            <div class="certifications-grid">
                <div class="certification-card"><div class="certification-icon">🚀</div><div><h3 class="certification-title">Lead Data Science / AI Architect</h3><p class="certification-org">Jedha — RNCP 38777, niveau 7 (Bac+5)</p><span class="certification-year">2026 – en cours</span></div></div>
                <div class="certification-card"><div class="certification-icon">🎓</div><div><h3 class="certification-title">Concepteur Développeur en Sciences des Données</h3><p class="certification-org">Jedha / M2i — RNCP niveau 6 (Bac+4)</p><span class="certification-year">2024 – 2025</span></div></div>
                <div class="certification-card"><div class="certification-icon">📜</div><div><h3 class="certification-title">Databricks Lakehouse Fundamentals</h3><p class="certification-org">Databricks Academy</p><span class="certification-year">2025</span></div></div>
                <div class="certification-card"><div class="certification-icon">⚙️</div><div><h3 class="certification-title">DUT Génie Mécanique et Productique</h3><p class="certification-org">IUT B Villeurbanne</p><span class="certification-year">2000 – 2002</span></div></div>
            </div>
        </div>
    </section>
"""
    write(SITE / "profil-rh.html",
          head("Pourquoi me recruter — Patrice Duclos", "Argumentaire recruteur : impact mesuré, expertise industrielle, projets data en production.", path)
          + nav(PROJECTS, path) + body + FOOTER)


def page_tech():
    path = "/profil-tech.html"
    proofs = [
        ("Architecture de données", "Medallion Bronze/Silver/Gold sur PostgreSQL/PostGIS ; OLTP → CDC Debezium → Kafka → Redis / MongoDB → Snowflake ; schémas en étoile.",
         "lyonflow"),
        ("Orchestration", "27 DAGs Airflow en production (collecte */5 min, transforms, ML, maintenance) ; CronJob Kubernetes équivalent à un DAG.",
         "lyonflow"),
        ("Cycle de vie ML", "MLflow registry, split temporel anti-fuite, features partagées train/serve, garde-fous de fuite par actif.",
         "stripe-fraude-temps-reel"),
        ("Monitoring & boucle fermée", "Dérive Evidently / PSI, précision et rappel réellement servis, réentraînement automatique avec délai de carence.",
         "stripe-fraude-temps-reel"),
        ("Serving & exploitation", "FastAPI avec clé API et seuil métier, Nginx + TLS, systemd, deploy / rollback scriptés, 20 health checks, Prometheus / Grafana.",
         "lyonflow"),
        ("IA générative", "RAG hybride dense + BM25 + RRF, reranker, LLM local MLX, évaluation RAGAS ; serveurs MCP pour agents.",
         "copilot-maintenance"),
        ("Qualité logicielle", "≈ 1 600 tests pytest cumulés, CI GitHub Actions (ruff, mypy, bandit, CodeQL, e2e sur stack complète), Docker multi-stage non-root.",
         "marche-hvac"),
        ("Infrastructure as Code", "Terraform AWS : VPC 3 AZ, RDS Multi-AZ, MSK, ElastiCache, ECS Fargate, MWAA, KMS ; Databricks Asset Bundles ; FinOps chiffré.",
         "stripe-fraude-temps-reel"),
    ]
    by_slug = {p["slug"]: p for p in PROJECTS}
    proof_rows = "".join(f'<tr><td>{e(t)}</td><td>{d}</td><td><a href="/projets/{s}.html" style="color:var(--accent);text-decoration:none">{e(by_slug[s]["short"])} →</a></td></tr>'
                         for t, d, s in proofs)
    body = hero("Profil technique", "// Pour les équipes data / tech",
                'Profil technique — <span class="highlight">les preuves dans le code</span>',
                "Data Scientist / ML Engineer orienté production. Voici ce que je sais faire, où le vérifier, "
                "et comment je raisonne sur les compromis.",
                '<div class="btn-row"><a class="contact-btn contact-btn-primary" href="https://github.com/PDUCLOS" target="_blank" rel="noopener">GitHub ' + arrow() + '</a>'
                '<a class="contact-btn contact-btn-secondary" href="/stack.html">Stack détaillée ' + arrow() + '</a></div>')
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <div class="kpi-row">
                <div class="kpi"><b>≈ 1 600</b><span>tests automatisés</span></div>
                <div class="kpi"><b>27</b><span>DAGs Airflow en prod</span></div>
                <div class="kpi"><b>6</b><span>dépôts avec CI</span></div>
                <div class="kpi"><b>{len(PROJECTS)}</b><span>pipelines en draw.io</span></div>
            </div>
            <span class="section-label">// Compétences → preuves</span>
            <h2>Ce que je sais faire, et où le vérifier</h2>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>Domaine</th><th>Preuve concrète</th><th>Projet</th></tr></thead>
                <tbody>{proof_rows}</tbody></table></div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Matrice</span>
            <h2>Maturité MLOps par projet</h2>
            {matrix_table()}
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Façon de raisonner</span>
            <h2>Décisions d'ingénierie dont je peux parler en entretien</h2>
            <div class="two-col">
                <div class="arg-card arg-card--tech reveal"><span class="arg-label">Choix d'architecture</span><ul>
                    <li><strong>3 modèles spécialisés plutôt qu'un</strong> (LyonFlow) : MAE 5,8 → 3,2, car les features routières sont du bruit pour les vélos.</li>
                    <li><strong>PSI maison plutôt qu'Evidently partout</strong> : léger, sans dépendance lourde dans Airflow ; Evidently gardé pour les rapports.</li>
                    <li><strong>Consommateur Python plutôt que Flink</strong> quand PyFlink ne compile pas sur ARM64 — documenté, avec le job Flink en option.</li>
                    <li><strong>Serveur unique durci</strong> avant Kubernetes : la complexité doit être justifiée par le besoin.</li></ul></div>
                <div class="arg-card arg-card--tech reveal"><span class="arg-label">Rigueur ML</span><ul>
                    <li><strong>Split temporel</strong> pour ne jamais « voir le futur » (Stripe, HVAC).</li>
                    <li><strong>Mêmes features à l'entraînement et à l'inférence</strong>, ordre figé, pour éviter le training/serving skew.</li>
                    <li><strong>Abandon d'un modèle plus précis mais non servable</strong> (fraude V1 sur features PCA).</li>
                    <li><strong>Juger un retrain sur la performance servie</strong>, pas seulement offline.</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Tous les projets</span>
            <h2>Pipelines et code</h2>
            <div class="proj-grid">{''.join(tile(p) for p in PROJECTS)}</div>
        </div>
    </section>
"""
    write(SITE / "profil-tech.html",
          head("Profil technique — Patrice Duclos", "Profil technique Data Science / MLOps : compétences reliées aux preuves dans le code.", path)
          + nav(PROJECTS, path) + body + FOOTER)


def patch_index():
    """Replace nav in index.html between markers, keep the rest hand-edited."""
    idx = SITE / "index.html"
    html = idx.read_text(encoding="utf-8")
    new_nav = "<!-- NAV:START -->\n" + nav(PROJECTS, "/") + "    <!-- NAV:END -->"
    html, n = re.subn(r"<!-- NAV:START -->.*?<!-- NAV:END -->", lambda _: new_nav, html, flags=re.S)
    assert n == 1, "NAV markers missing in index.html"
    tiles = "<!-- TILES:START -->\n" + "".join(tile(p) for p in PROJECTS if p["slug"] not in ("lyonflow", "carrier-reporting")) + "\n<!-- TILES:END -->"
    html, n = re.subn(r"<!-- TILES:START -->.*?<!-- TILES:END -->", lambda _: tiles, html, flags=re.S)
    assert n == 1, "TILES markers missing in index.html"
    idx.write_text(html, encoding="utf-8")
    print("  patched index.html")


if __name__ == "__main__":
    import sys
    DIAG.mkdir(exist_ok=True)
    if "--no-diagrams" not in sys.argv:
        print("diagrams"); export_generated(); export_existing()
    print("pages")
    for p in PROJECTS:
        write(SITE / "projets" / f"{p['slug']}.html", project_page(p, PROJECTS))
    page_projects_index(); page_stack(); page_rh(); page_tech(); patch_index()
