"""English content and English page functions for the /en/ version of the portfolio.

Each page function takes a helper namespace `h` (SITE, write, head, nav, FOOTER, hero,
matrix_table, tile, dots, e, arrow, badges, PROJECTS, competences_section) so this module
stays independent from build.py.
"""

# ---------------------------------------------------------------- data
STACK_EN = [
    ("Orchestration & pipelines", [("Apache Airflow", 4, "LyonFlow (27 DAGs), Stripe, Fraud, HVAC"),
                                   ("Kafka + Debezium (CDC)", 3, "Stripe"),
                                   ("Kubernetes CronJob", 2, "HVAC"),
                                   ("Databricks DLT / Asset Bundles", 2, "LyonFlow Databricks")]),
    ("Storage & modeling", [("PostgreSQL / PostGIS / pgRouting", 4, "LyonFlow, Stripe, Fraud"),
                            ("SQL (analytics, spatial, OLAP)", 4, "all projects"),
                            ("Redis (feature store)", 3, "Stripe"),
                            ("MongoDB", 3, "Stripe"),
                            ("TimescaleDB", 3, "Predictive maintenance"),
                            ("Snowflake / Delta Lake", 2, "Stripe, LyonFlow Databricks"),
                            ("ChromaDB (vector)", 3, "Maintenance copilot")]),
    ("Machine Learning", [("XGBoost / LightGBM", 4, "LyonFlow, Stripe, Fraud, HVAC, IRA"),
                          ("scikit-learn", 4, "all ML projects"),
                          ("Time series (Prophet, LSTM)", 3, "HVAC"),
                          ("Signal processing (SciPy)", 3, "Predictive maintenance"),
                          ("SHAP / explainability", 3, "HVAC")]),
    ("Generative AI & agents", [("Hybrid RAG (dense + BM25 + RRF)", 3, "Maintenance copilot"),
                                ("Local LLM (MLX, Qwen2.5)", 3, "Maintenance copilot"),
                                ("LangChain LCEL / RAGAS", 3, "Maintenance copilot"),
                                ("Model Context Protocol", 3, "MCP servers")]),
    ("MLOps & quality", [("MLflow (tracking + registry)", 4, "LyonFlow, Stripe, Predictive maintenance"),
                         ("Drift: Evidently / PSI", 4, "LyonFlow, Stripe, Predictive maintenance"),
                         ("pytest (≈ 1,600 tests in total)", 4, "LyonFlow 620, HVAC 562, MLindustrial 189…"),
                         ("GitHub Actions (ruff, mypy, bandit, CodeQL)", 4, "LyonFlow, Stripe, HVAC, RAG, MLindustrial"),
                         ("Prometheus / Grafana", 3, "LyonFlow, Maintenance copilot")]),
    ("Deployment & infrastructure", [("Docker / Docker Compose", 4, "all production-grade projects"),
                                     ("FastAPI", 4, "LyonFlow, Fraud, HVAC, RAG, IRA"),
                                     ("Nginx, systemd, TLS, Linux VPS", 3, "LyonFlow"),
                                     ("Terraform (AWS)", 3, "Stripe"),
                                     ("Kubernetes (manifests)", 2, "HVAC")]),
    ("Reporting & business", [("Power BI / DAX / Power Query", 5, "Carrier"),
                              ("Streamlit", 4, "LyonFlow, Stripe, Fraud, HVAC, RAG"),
                              ("SAP / ERP", 4, "Carrier, 20 years in distribution"),
                              ("Advanced Excel / VBA", 5, "Carrier"),
                              ("Governance / GDPR", 3, "Spotify, LyonFlow, Stripe")]),
]

CERTIF_EN = {
    "title": "Architecte en intelligence artificielle (AI Architect)",
    "org": "Jedha",
    "rncp": "RNCP 38777",
    "level": "Level 7 (Master's level)",
    "year": "2026",
    "url": "https://www.francecompetences.fr/recherche/rncp/38777/",
}

# code, official title, short label, color, skills, tools (exact names from STACK_EN), projects (slugs)
BLOCS_EN = [
    ("BC01", "Design and lead data governance", "Governance", "#F59E0B",
     ["Design a data governance policy with stakeholders: regulatory compliance, quality, availability, security and privacy",
      "Promote the governance policy and ensure it is applied by the company's teams",
      "Train and raise awareness of data governance among all employees, including people with disabilities",
      "Regularly audit data management practices against local and international regulations (GDPR)",
      "Assess data-related risks, especially quality and security risks"],
     ["Governance / GDPR", "SQL (analytics, spatial, OLAP)", "pytest (≈ 1,600 tests in total)"],
     ["gouvernance-spotify", "stripe-fraude-temps-reel", "csvtraitement", "lyonflow"]),
    ("BC02", "Design and deploy data architectures for AI", "Architecture", "#38BDF8",
     ["Identify architecture needs by analyzing technical and operational constraints and applicable standards",
      "Write the data architecture specifications",
      "Build logical and physical data models",
      "Design databases that meet performance, security, scalability and volume requirements",
      "Deploy virtual servers, in the cloud or on-premise, for AI model training",
      "Design server clusters to increase computing capacity",
      "Set up infrastructure monitoring and optimization",
      "Document the architecture in an accessible way"],
     ["PostgreSQL / PostGIS / pgRouting", "Snowflake / Delta Lake", "Redis (feature store)", "MongoDB",
      "TimescaleDB", "Terraform (AWS)", "Nginx, systemd, TLS, Linux VPS", "Kubernetes (manifests)", "Prometheus / Grafana"],
     ["stripe-fraude-temps-reel", "lyonflow", "maintenance-predictive", "marche-hvac"]),
    ("BC03", "Design and implement data pipelines for AI", "Pipelines", "#34D399",
     ["Design a real-time data management system suited to operational constraints",
      "Build ETL / ELT pipelines to move and transform data between systems",
      "Automate data flows",
      "Monitor data flows: quality and compliance with the governance policy",
      "Develop quality control and error correction procedures"],
     ["Apache Airflow", "Kafka + Debezium (CDC)", "Databricks DLT / Asset Bundles", "Kubernetes CronJob",
      "SQL (analytics, spatial, OLAP)"],
     ["detection-fraude", "lyonflow", "stripe-fraude-temps-reel", "marche-hvac", "csvtraitement"]),
    ("BC04", "Build, deploy and manage AI solutions", "AI solutions", "#818CF8",
     ["Write the specifications of an AI solution: technical, economic and accessibility requirements",
      "Develop the AI algorithm suited to the training data and the specifications",
      "Build the APIs that put the AI solution into production",
      "Design the continuous integration and deployment (CI/CD) pipelines of the solution",
      "Develop automatic model retraining scripts",
      "Manage model performance in production through monitoring (Evidently, PSI)"],
     ["XGBoost / LightGBM", "scikit-learn", "Time series (Prophet, LSTM)", "Signal processing (SciPy)",
      "SHAP / explainability", "Hybrid RAG (dense + BM25 + RRF)", "Local LLM (MLX, Qwen2.5)", "LangChain LCEL / RAGAS",
      "Model Context Protocol", "MLflow (tracking + registry)", "Drift: Evidently / PSI", "FastAPI",
      "Docker / Docker Compose", "GitHub Actions (ruff, mypy, bandit, CodeQL)", "Streamlit"],
     ["lyonflow", "stripe-fraude-temps-reel", "detection-fraude", "copilot-maintenance",
      "maintenance-predictive", "marche-hvac", "mcp-open-data", "predictira"]),
    ("BUSINESS", "Lead a data project, from business need to decision", "Business & leadership", "#F472B6",
     ["Run a project end to end: scoping, business case, specifications, acceptance testing, deployment",
      "Translate a business need into KPIs and quantified decisions (Business Analyst)",
      "20 years in B2B industrial distribution: HVAC, energy, supply chain, key accounts",
      "Report to decision-makers: dashboards, presentations, business arguments"],
     ["Power BI / DAX / Power Query", "Advanced Excel / VBA", "SAP / ERP", "Streamlit"],
     ["achats-negociation", "carrier-reporting", "marche-hvac"]),
]

# Assessment passed for each block (RNCP 38777 assessment framework)
EPREUVES_EN = {
    "BC01": "Governance plan for an organization, presented and defended before the jury.",
    "BC02": "Professional case study: infrastructure plan, deployment code on GitHub, live production demo, oral defense.",
    "BC03": "Professional case study: pipeline plan, code on GitHub, live demo of the pipeline in production, oral defense.",
    "BC04": "Professional case study: AI solution, code and CI/CD pipeline on GitHub, live production demo, oral defense.",
}


# ---------------------------------------------------------------- pages
def page_projects_index(h):
    e, PROJECTS = h.e, h.PROJECTS
    path = "/en/projects/"
    body = h.hero("Projects", "// Portfolio", 'Projects — <span class="highlight">from business need to production</span>',
                  f"{len(PROJECTS)} documented projects: for each one, the business problem, the draw.io pipeline, "
                  "the tools and languages, the level of industrialization, the metrics and the acknowledged limitations.")
    body += f"""
    <section class="page-section">
        <div class="section-container"><div class="proj-grid">{''.join(h.tile(p) for p in PROJECTS)}</div></div>
    </section>
    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// MLOps maturity</span>
            <h2>Industrialization matrix</h2>
            <p style="margin-bottom:1.5rem">What is actually in place in each repository — from continuous integration to deployment.</p>
            {h.matrix_table()}
        </div>
    </section>
"""
    h.write(h.SITE / "en" / "projects" / "index.html",
            h.head("Projects — Patrice Duclos", "All of Patrice Duclos's data, ML and MLOps projects: pipelines, tools, metrics.", path)
            + h.nav(PROJECTS, path) + body + h.FOOTER)


def page_stack(h):
    e, PROJECTS = h.e, h.PROJECTS
    path = "/en/stack.html"
    groups = []
    for title, items in STACK_EN:
        rows = "".join(f"""<div class="skill-item" style="align-items:flex-start;gap:1rem">
                <span class="skill-name">{e(name)}<br><small class="code-caption">{e(where)}</small></span>{h.dots(lvl)}</div>"""
                       for name, lvl, where in items)
        groups.append(f'<div class="skill-group reveal"><h3 class="skill-group-title">{e(title)}</h3><div class="skill-items">{rows}</div></div>')
    langs = [("Python", "Main language: pipelines, ML, APIs, tests"), ("SQL", "PostgreSQL, spatial, OLAP, Snowflake"),
             ("HCL", "Terraform AWS"), ("DAX / M", "Power BI, Power Query"), ("Bash", "Deployment, health checks"),
             ("YAML", "CI, Kubernetes, configs"), ("VBA", "Excel automation")]
    lang_html = "".join(f'<div class="kpi"><b style="font-size:1.2rem">{e(n)}</b><span>{e(d)}</span></div>' for n, d in langs)
    body = h.hero("MLOps stack", "// Skills proven by code",
                  '<span class="highlight">MLOps & Data</span> stack — every tool linked to a project',
                  "Self-assessed levels (1 to 5), each backed by at least one public repository or professional experience. "
                  "Click on the projects to see the tool in action.")
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Languages</span>
            <h2>Languages used</h2>
            <div class="kpi-row">{lang_html}</div>
        </div>
    </section>
    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Tools</span>
            <h2>Tools by lifecycle stage</h2>
            <div class="skills-grid">{''.join(groups)}</div>
        </div>
    </section>
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Proof</span>
            <h2>Where to see each MLOps practice</h2>
            {h.matrix_table()}
        </div>
    </section>
"""
    h.write(h.SITE / "en" / "stack.html",
            h.head("MLOps Stack — Patrice Duclos", "Patrice Duclos's MLOps tools, languages and practices, linked to projects.", path)
            + h.nav(PROJECTS, path) + body + h.FOOTER)


def page_rh(h):
    PROJECTS, arrow = h.PROJECTS, h.arrow
    path = "/en/recruiters.html"
    objections = [
        ("“It's a career change: is he really at the level?”",
         "Two RNCP certifications earned (RNCP is the French national qualification register): level 6, then level 7 (Master's level) "
         "Architecte en intelligence artificielle (AI Architect) in 2026, plus a Databricks certification, "
         "10 months at Carrier with quantified results, and an MLOps platform <strong>in production</strong> available online. "
         "The career change is complete; what remains is 20 years of field experience that junior profiles don't have."),
        ("“Senior on the business side, but junior on the tech side?”",
         "The code is public and verifiable: around 1,600 automated tests in total, continuous integration, Docker, Airflow, MLflow, "
         "Terraform. The <a href=\"/en/tech-profile.html\" style=\"color:var(--accent)\">tech profile page</a> details each proof."),
        ("“Why not a younger, less expensive profile?”",
         "Because the cost of a failed data project almost never comes from the code: it comes from a badly framed problem. "
         "I know how to talk to a sales director, a buyer, a maintenance technician — and translate their need into KPIs."),
        ("“Will he fit into a tech team?”",
         "My projects follow team standards: documented conventions, blocking tests in CI, "
         "architecture documentation, draw.io diagrams. Experience with team projects during training and in an international setting at Carrier."),
        ("“What kind of role?”",
         "Data Project Manager, Senior Data Analyst, Data Scientist, ML Engineer / MLOps or AI Architect in industry, energy, B2B distribution "
         "or supply chain — where combined business and data expertise brings the most value. Lyon area, hybrid."),
    ]
    obj_html = "".join(f'<details class="objection"><summary>{q}</summary><p>{a}</p></details>' for q, a in objections)
    body = h.hero("Recruiters", "// For HR and hiring managers",
                  'Why hire me — <span class="highlight">in 2 minutes</span>',
                  "20 years in industrial distribution, a certified career change into data and projects in production: "
                  "a profile that understands the business <strong>and</strong> delivers the technical solution.",
                  '<div class="btn-row"><a class="contact-btn contact-btn-primary" href="/en/#contact">Contact me ' + arrow() + '</a>'
                  '<a class="contact-btn contact-btn-secondary" href="/en/projects/">See the projects ' + arrow() + '</a></div>')
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Value proposition</span>
            <h2>What I bring from the first month</h2>
            <p class="pitch pitch--warm" style="margin-bottom:2rem">I don't start with the data: I start with the question
               the decision-maker is asking. Then I build the tool that answers it — and I put it into production.</p>
            <div class="two-col">
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Current role</span><ul>
                    <li><strong>End-to-end Project Manager</strong> on a real, ongoing procurement project</li>
                    <li>Scoping, architecture, development, acceptance testing, deployment</li>
                    <li>Go-to-market: presentations and <a href="https://buyvera.fr/en/" style="color:var(--accent)">sales website</a></li>
                    <li><a href="/en/projects/achats-negociation.html" style="color:var(--accent)">See the project →</a></li></ul></div>
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Measured business impact</span><ul>
                    <li><strong>−40%</strong> processing time at Carrier</li>
                    <li><strong>~€100K/month</strong> of data errors detected</li>
                    <li><strong>5 SAP sources</strong> unified into European-level reporting</li></ul></div>
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">Rare business expertise</span><ul>
                    <li><strong>20 years</strong> in B2B industrial distribution (Michaud Chailly, Descours &amp; Cabaud)</li>
                    <li>HVAC, energy, supply chain, key accounts</li>
                    <li>Immediate credibility with field teams</li></ul></div>
                <div class="arg-card arg-card--rh reveal"><span class="arg-label">End-to-end delivery</span><ul>
                    <li>Platform <strong>in production</strong> (LyonFlow), available online</li>
                    <li>{len(PROJECTS)} documented projects, from need to API</li>
                    <li>Procurement business case: quantified levers, 8-phase plan, failure conditions</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Soft skills</span>
            <h2>How I work</h2>
            <div class="two-col">
                <div class="arg-card arg-card--ok reveal"><span class="arg-label">What my projects show</span><ul>
                    <li><strong>Rigor</strong>: every project documents its limitations and the errors it fixed.</li>
                    <li><strong>Autonomy</strong>: LyonFlow designed, developed, deployed and operated on my own.</li>
                    <li><strong>Clear communication</strong>: dashboards designed per persona (user, operator, elected official).</li>
                    <li><strong>Results-driven</strong>: I measure impact, not activity.</li></ul></div>
                <div class="arg-card arg-card--ok reveal"><span class="arg-label">What I bring to a team</span><ul>
                    <li>A bridge between business teams and the data team: I speak both languages.</li>
                    <li>The maturity of a senior: prioritization, stakeholder management, negotiation.</li>
                    <li>Active technology watch: generative AI, agents (MCP), MLOps, Databricks.</li>
                    <li>Clear communication in French and English.</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Frequent objections</span>
            <h2>The questions you may be asking yourself</h2>
            {obj_html}
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Flagship projects</span>
            <h2>Three projects to look at first</h2>
            <div class="proj-grid">{''.join(h.tile(p) for p in PROJECTS if p['slug'] in ('lyonflow', 'carrier-reporting', 'achats-negociation'))}</div>
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// Education</span>
            <h2>Degrees and certifications</h2>
            <div class="certifications-grid">
                <div class="certification-card"><div class="certification-icon">🚀</div><div><h3 class="certification-title">Architecte en intelligence artificielle (AI Architect)</h3><p class="certification-org">Jedha — RNCP 38777, level 7 (Master's level) · <a href="/en/skills.html" style="color:var(--accent);text-decoration:none">4 blocks in detail →</a></p><span class="certification-year">2026 · earned ✓</span></div></div>
                <div class="certification-card"><div class="certification-icon">🎓</div><div><h3 class="certification-title">Data Science Developer-Designer</h3><p class="certification-org">Jedha / M2i — RNCP level 6 (Bachelor's level)</p><span class="certification-year">2024 – 2025</span></div></div>
                <div class="certification-card"><div class="certification-icon">📜</div><div><h3 class="certification-title">Databricks Lakehouse Fundamentals</h3><p class="certification-org">Databricks Academy</p><span class="certification-year">2025</span></div></div>
                <div class="certification-card"><div class="certification-icon">⚙️</div><div><h3 class="certification-title">DUT (2-year technical degree) in Mechanical and Production Engineering</h3><p class="certification-org">IUT B Villeurbanne</p><span class="certification-year">2000 – 2002</span></div></div>
            </div>
        </div>
    </section>
"""
    h.write(h.SITE / "en" / "recruiters.html",
            h.head("Why hire me — Patrice Duclos", "Recruiter brief: measured impact, industrial expertise, data projects in production.", path)
            + h.nav(PROJECTS, path) + body + h.FOOTER)


def page_tech(h):
    e, PROJECTS, arrow = h.e, h.PROJECTS, h.arrow
    path = "/en/tech-profile.html"
    proofs = [
        ("Data architecture", "Bronze/Silver/Gold medallion on PostgreSQL/PostGIS; OLTP → Debezium CDC → Kafka → Redis / MongoDB → Snowflake; star schemas.",
         "lyonflow"),
        ("Orchestration", "27 Airflow DAGs in production (collection every 5 min, transforms, ML, maintenance); Kubernetes CronJob equivalent to a DAG.",
         "lyonflow"),
        ("ML lifecycle", "MLflow registry, leak-proof temporal split, features shared between training and serving, per-asset leakage guardrails.",
         "stripe-fraude-temps-reel"),
        ("Monitoring & closed loop", "Evidently / PSI drift, precision and recall measured on served predictions, automatic retraining with a cooldown period.",
         "stripe-fraude-temps-reel"),
        ("Serving & operations", "FastAPI with API key and business threshold, Nginx + TLS, systemd, scripted deploy / rollback, 20 health checks, Prometheus / Grafana.",
         "lyonflow"),
        ("Generative AI", "Hybrid RAG dense + BM25 + RRF, reranker, local LLM on MLX, RAGAS evaluation; MCP servers for agents.",
         "copilot-maintenance"),
        ("Software quality", "≈ 1,600 pytest tests in total, GitHub Actions CI (ruff, mypy, bandit, CodeQL, e2e on the full stack), non-root multi-stage Docker.",
         "marche-hvac"),
        ("Infrastructure as Code", "Terraform AWS: 3-AZ VPC, Multi-AZ RDS, MSK, ElastiCache, ECS Fargate, MWAA, KMS; Databricks Asset Bundles; costed FinOps.",
         "stripe-fraude-temps-reel"),
    ]
    by_slug = {p["slug"]: p for p in PROJECTS}
    proof_rows = "".join(f'<tr><td>{e(t)}</td><td>{d}</td><td><a href="/en/projects/{s}.html" style="color:var(--accent);text-decoration:none">{e(by_slug[s]["short"])} →</a></td></tr>'
                         for t, d, s in proofs)
    body = h.hero("Tech profile", "// For data / tech teams",
                  'Tech profile — <span class="highlight">the proof is in the code</span>',
                  "Production-oriented Data Scientist / ML Engineer. Here is what I can do, where to verify it, "
                  "and how I reason about trade-offs.",
                  '<div class="btn-row"><a class="contact-btn contact-btn-primary" href="https://github.com/PDUCLOS" target="_blank" rel="noopener">GitHub ' + arrow() + '</a>'
                  '<a class="contact-btn contact-btn-secondary" href="/en/stack.html">Detailed stack ' + arrow() + '</a></div>')
    body += f"""
    <section class="page-section">
        <div class="section-container">
            <div class="kpi-row">
                <div class="kpi"><b>≈ 1,600</b><span>automated tests</span></div>
                <div class="kpi"><b>27</b><span>Airflow DAGs in production</span></div>
                <div class="kpi"><b>6</b><span>repositories with CI</span></div>
                <div class="kpi"><b>{len(PROJECTS)}</b><span>pipelines in draw.io</span></div>
            </div>
            <span class="section-label">// Skills → proof</span>
            <h2>What I can do, and where to verify it</h2>
            <div class="table-wrap"><table class="stack-table">
                <thead><tr><th>Area</th><th>Concrete proof</th><th>Project</th></tr></thead>
                <tbody>{proof_rows}</tbody></table></div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// Matrix</span>
            <h2>MLOps maturity by project</h2>
            {h.matrix_table()}
        </div>
    </section>

    <section class="page-section">
        <div class="section-container">
            <span class="section-label">// How I reason</span>
            <h2>Engineering decisions I can discuss in an interview</h2>
            <div class="two-col">
                <div class="arg-card arg-card--tech reveal"><span class="arg-label">Architecture choices</span><ul>
                    <li><strong>3 specialized models rather than one</strong> (LyonFlow): MAE 5.8 → 3.2, because road features are noise for bikes.</li>
                    <li><strong>Custom PSI rather than Evidently everywhere</strong>: lightweight, no heavy dependency in Airflow; Evidently kept for reports.</li>
                    <li><strong>Python consumer rather than Flink</strong> when PyFlink doesn't compile on ARM64 — documented, with the Flink job as an option.</li>
                    <li><strong>A single hardened server</strong> before Kubernetes: complexity must be justified by the need.</li></ul></div>
                <div class="arg-card arg-card--tech reveal"><span class="arg-label">ML rigor</span><ul>
                    <li><strong>Temporal split</strong> so the model never “sees the future” (Stripe, HVAC).</li>
                    <li><strong>Same features at training and inference</strong>, in a fixed order, to avoid training/serving skew.</li>
                    <li><strong>Dropped a more accurate but unservable model</strong> (fraud V1 on PCA features).</li>
                    <li><strong>Judge a retrain on served performance</strong>, not just offline.</li></ul></div>
            </div>
        </div>
    </section>

    <section class="page-section alt">
        <div class="section-container">
            <span class="section-label">// All projects</span>
            <h2>Pipelines and code</h2>
            <div class="proj-grid">{''.join(h.tile(p) for p in PROJECTS)}</div>
        </div>
    </section>
"""
    h.write(h.SITE / "en" / "tech-profile.html",
            h.head("Tech profile — Patrice Duclos", "Data Science / MLOps tech profile: skills linked to proof in the code.", path)
            + h.nav(PROJECTS, path) + body + h.FOOTER)


def page_competences(h):
    path = "/en/skills.html"
    body = h.hero("Skills", "// AI Architect · RNCP 38777 · level 7",
                  'Skills — <span class="highlight">certified and proven</span> by code',
                  "My skills organized according to the four blocks of the Architecte en intelligence artificielle (AI Architect) certification "
                  "(Jedha, level 7, earned in 2026), complemented by twenty years of business leadership. "
                  "Filter by block, search for a tool, then open the project that puts it to work.")
    h.write(h.SITE / "en" / "skills.html",
            h.head("Skills — Patrice Duclos",
                   "Patrice Duclos's skills according to the RNCP 38777 AI Architect blocks: governance, architecture, pipelines, AI solutions.", path)
            + h.nav(h.PROJECTS, path) + body + h.competences_section() + h.FOOTER)
