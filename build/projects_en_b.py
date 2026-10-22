"""English content for projects 7-12 and strengths (translated from projects.py)."""
from projects import GH, M_NONE

PART_B = [
    # ------------------------------------------------------------------ CARRIER
    dict(
        slug="carrier-reporting",
        short="Carrier — HVAC Europe Reporting",
        kicker="Professional experience · Measurable impact",
        title="Master Data Reporting & Analysis — Carrier",
        title_html='Carrier: <span class="highlight">−40% processing time</span>, €100K/month of errors detected',
        lead="Power BI dashboards for Master Data & HVAC Europe Business: a unified flow from 5 SAP sources, detection of critical "
             "anomalies, Power Query automation and Europe-wide performance management, in an international FR/EN setting.",
        kpis=[("−40%", "processing time"), ("€100K/month", "errors detected"), ("5", "SAP sources unified"), ("10 months", "internship + fixed-term contract")],
        links=[],
        context=[
            "In an international industrial group, the quality of reference data (items, prices, customers) drives "
            "invoicing, margin and the customer relationship. Errors are costly and often invisible.",
            "Mission: unify SAP extracts, make reference data reliable and give European teams "
            "management dashboards.",
        ],
        rh=[
            "<strong>Quantified impact</strong>: −40% processing time and roughly €100K of errors detected every month.",
            "<strong>International</strong> setting (FR/EN), European Customer Care and Master Data teams.",
            "Dual skill set put into practice: HVAC business knowledge + data tooling.",
        ],
        tech=[
            "Multi-source SAP Power BI semantic model, DAX quality-control measures.",
            "Automation of recurring processing with Power Query and VBA.",
            "Anomaly detection rules on reference data.",
        ],
        stages=[
            ("Sources", "source", ["5 SAP extracts"]),
            ("Preparation", "ingest", ["Power Query (M)"]),
            ("Model", "storage", ["Power BI semantic model"]),
            ("Controls", "process", ["DAX measures", "Anomaly rules"]),
            ("Management", "ui", ["Master Data dashboards", "HVAC Business dashboards"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s2n0", "", False), ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False),
               ("s3n0", "s4n1", "", False), ("s3n1", "s4n0", "", False)],
        band=None,
        steps=[
            "Consolidation of 5 SAP sources into a single flow with Power Query.",
            "Semantic modeling and DAX measures for management and control.",
            "Detection of reference data anomalies and escalation to the relevant teams.",
            "Rollout of Master Data and HVAC Business dashboards across Europe.",
        ],
        extra_diagrams=[],
        langs=None,
        langs_note="Company project: code not public.",
        tags=["Power BI", "DAX", "Power Query", "SAP", "Excel VBA", "Master Data", "Data Quality"],
        stack=[
            ("Power BI", "Semantic model and dashboards", "Reporting for decision-makers"),
            ("DAX", "Management and control measures", "Analytical logic"),
            ("Power Query", "Consolidation of 5 SAP sources", "Automated data preparation"),
            ("SAP", "Reference and transactional data", "ERP proficiency"),
            ("Excel VBA", "Automation of recurring tasks", "Productivity gains"),
        ],
        matrix=None,
        limits=[
            "Confidential data and code: this page describes the approach without disclosing internal information.",
        ],
    ),
    # ------------------------------------------------------------------ CSV
    dict(
        slug="csvtraitement",
        short="Csvtraitement",
        kicker="Python tool · ERP data quality",
        title="Csvtraitement — fixing ERP exports",
        title_html='<span class="highlight">Clean</span> ERP exports, even at 500,000 rows',
        lead="Python application (GUI + CLI) that detects and fixes defects in ERP exports: shifted columns, "
             "mixed FR/US decimal formats, invalid dates, duplicates, personal data — with human validation before export.",
        kpis=[("500K+", "rows processed"), ("59", "tests"), ("6", "formats read / written"), ("A→F", "quality score")],
        links=[("Source code", GH + "Csvtraitement", True)],
        context=[
            "Every analyst who works with SAP knows the problem: a CSV export with a shifted column, amounts "
            "“1.234,56” and “1,234.56” mixed together, dates like <code>00.00.0000</code> or <code>#REF!</code> errors. "
            "Manual cleanup takes hours and remains error-prone.",
            "Csvtraitement automates detection, suggests corrections, and lets the user validate before exporting.",
        ],
        rh=[
            "Born from a day-to-day pain point with SAP extracts.",
            "Direct time savings for Procurement, sales administration and management control / finance teams.",
            "Human in the loop: no correction is applied without validation.",
        ],
        tech=[
            "<strong>Streaming reads in 10,000-row chunks</strong>; Parquet read with <code>iter_batches</code>: no memory saturation.",
            "Automatic encoding and separator detection (score mean / (1 + standard deviation)), column typing on a sample.",
            "Exact and fuzzy duplicates (<code>SequenceMatcher</code> &gt; 85% with prefix blocking), file reconciliation, personal data masking (email, phone, IBAN, French social security number).",
            "8-tab Tkinter interface, batch CLI, undo / redo, 27 modules with logging, type hints and docstrings.",
        ],
        stages=[
            ("Input", "source", ["CSV · XLSX · ODS", "JSON · Parquet"]),
            ("Detection", "ingest", ["Encoding + separator", "9-type profiling"]),
            ("Analysis", "process", ["Column shifts", "A→F quality score", "Exact / fuzzy duplicates"]),
            ("Correction", "ml", ["Dates, FR/US decimals", "PII masking"]),
            ("Validation", "ui", ["Human review (GUI / CLI)"]),
            ("Export", "serve", ["Annotated XLSX + report", "CSV · Parquet"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s1n0", "s1n1", "", False),
               ("s1n1", "s2n0", "", False), ("s1n1", "s2n1", "", False), ("s1n1", "s2n2", "", False),
               ("s2n0", "s3n0", "", False), ("s2n2", "s3n1", "", False), ("s3n0", "s4n0", "", False),
               ("s3n1", "s4n0", "", False), ("s4n0", "s5n0", "", False), ("s4n0", "s5n1", "", False)],
        band=("Streaming processing (10,000-row chunks) · pytest · logging", "infra"),
        steps=[
            "Reads any tabular format, converted into a CSV stream processed in chunks.",
            "Detects the encoding, separator and type of each column on a representative sample.",
            "Cell-by-cell detection of column shifts, weighted quality score, duplicate search.",
            "Suggested corrections (dates, decimals, accounting parentheses, realignment) and optional masking of personal data.",
            "User validation, then XLSX export with corrected cells highlighted and a report sheet.",
        ],
        extra_diagrams=[],
        langs=[("Python", 100)],
        tags=["Python", "Tkinter", "CLI", "Streaming", "Data Quality", "chardet", "xlsxwriter", "pyarrow", "pytest"],
        stack=[
            ("Python standard library", "csv, difflib, statistics, argparse, logging", "Robust without heavy dependencies"),
            ("chardet", "Encoding detection", "Resilience to heterogeneous exports"),
            ("xlsxwriter (constant_memory)", "Annotated Excel export", "Large volumes without memory saturation"),
            ("pyarrow", "Parquet read / write", "Data interoperability"),
            ("Tkinter", "8-tab graphical interface", "A tool non-developers can use"),
            ("pytest", "59 tests on detection, analysis, correction", "Reliable core logic"),
        ],
        matrix=dict(ci="n", tests="y", docker="n", orch="n", tracking="n", monitoring="n", serving="n", deploy="p", iac="n"),
        matrix_notes=dict(tests="59 tests (detector, analyzer, corrector)", deploy="Installable package + Windows launcher"),
        snippets=[
            ("core/detector.py — the most consistent separator wins",
             '''for sep in CANDIDATE_SEPARATORS:
    counts = [line.count(sep) for line in lines]

    # Skip if never present
    if max(counts) == 0:
        continue

    avg_count = mean(counts)
    std_count = stdev(counts) if len(counts) > 1 else 0.0'''),
        ],
        limits=[
            "No GitHub Actions CI or Docker image yet.",
            "Test coverage focused on the core (detection, analysis, correction); secondary modules still to be covered.",
        ],
    ),
    # ------------------------------------------------------------------ MCP
    dict(
        slug="mcp-open-data",
        short="Open data MCP servers",
        kicker="Agentic AI · Model Context Protocol",
        title="MCP servers for French open data",
        title_html='Connecting an LLM to <span class="highlight">public open data</span>',
        lead="Two Model Context Protocol servers that let an AI assistant (Claude Desktop, for example) query "
             "data.gouv.fr and data.grandlyon.com, including WFS geographic layers.",
        kpis=[("11", "tools exposed"), ("2", "open data portals"), ("stdio", "MCP transport")],
        links=[],
        context=[
            "LLMs are powerful but have no knowledge of up-to-date public data. The Model Context Protocol "
            "standardizes how tools are provided to them.",
            "These servers turn the data.gouv.fr and Grand Lyon APIs into tools usable in natural language: "
            "“find datasets on air quality in Lyon and show me the first 10 stations”.",
        ],
        rh=[
            "Active monitoring of <strong>agentic AI</strong>: MCP is the emerging standard for connecting assistants to enterprise data.",
            "The same approach can be applied to an ERP or an internal data warehouse.",
        ],
        tech=[
            "Low-level <code>mcp</code> SDK: <code>list_tools</code> / <code>call_tool</code> handlers, stdio transport.",
            "data.gouv.fr: 6 tools (dataset search and details, resources, organizations, latest additions).",
            "Grand Lyon: 5 tools including <strong>WFS 2.0 GetFeature</strong> with CQL filter, layer listing, layer schema.",
            "httpx client with timeout, HTTP errors returned cleanly to the LLM; one Dockerfile per server.",
        ],
        stages=[
            ("Client", "ui", ["AI assistant (MCP client)"]),
            ("Transport", "ingest", ["stdio"]),
            ("Servers", "serve", ["mcp-data-gouv (6 tools)", "mcp-data-lyon (5 tools)"]),
            ("API", "source", ["data.gouv.fr API v1", "Grand Lyon datapusher + WFS"]),
        ],
        edges=[("s0n0", "s1n0", "tool call", False), ("s1n0", "s2n0", "", False), ("s1n0", "s2n1", "", False),
               ("s2n0", "s3n0", "httpx", False), ("s2n1", "s3n1", "httpx", False)],
        band=("Docker (one container per server, stdin open)", "infra"),
        steps=[
            "The assistant discovers the tools exposed by each server (name, description, JSON schema of arguments).",
            "When the question calls for it, it invokes a tool; the server queries the corresponding public API.",
            "The response is formatted as Markdown and returned to the model, which summarizes it for the user.",
        ],
        extra_diagrams=[],
        langs=[("Python", 100)],
        langs_note="MCP servers only.",
        tags=["MCP", "LLM", "Agents", "httpx", "WFS", "Open data", "Docker"],
        stack=[
            ("mcp (Python SDK)", "Tool declaration and execution", "Standardized agentic AI"),
            ("httpx", "HTTP calls with timeout", "API integration"),
            ("OGC WFS 2.0", "Filtered geographic queries (CQL)", "GIS data"),
            ("Docker", "Isolation of each server", "Distribution"),
        ],
        matrix=dict(ci="n", tests="n", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(docker="Dockerfile + compose per server", serving="MCP protocol (stdio)", deploy="Local / Claude Desktop"),
        snippets=[
            ("mcp-data-lyon/server.py — WFS request with optional CQL filter",
             '''params = {
    "SERVICE": "WFS",
    "VERSION": "2.0.0",
    "REQUEST": "GetFeature",
    "TYPENAME": arguments["type_name"],
    "OUTPUTFORMAT": arguments.get("output_format", "application/json"),
    "COUNT": arguments.get("max_features", 10),
}
if arguments.get("cql_filter"):
    params["CQL_FILTER"] = arguments["cql_filter"]'''),
        ],
        limits=[
            "No automated tests or logging yet.",
            "stdio transport only; an HTTP (streamable) transport would allow a shared server deployment.",
        ],
    ),
    # ------------------------------------------------------------------ SPOTIFY
    dict(
        slug="gouvernance-spotify",
        short="Data Governance — Spotify",
        kicker="Data Governance · Consulting · RNCP 38777 Block 1",
        title="Data governance strategy — Spotify case study",
        title_html='Data governance: <span class="highlight">from assessment to action plan</span>',
        lead="Consulting engagement for an executive committee (Spotify case study, 450M users): maturity assessment "
             "across 9 dimensions, governance org chart, rollout plan, budget and executive presentation.",
        kpis=[("9", "dimensions assessed"), ("~2.4/5", "initial maturity"), ("4", "deliverables"), ("×3", "target ROI")],
        links=[("Deliverables", GH + "BLOC1-SPOTIFY", True)],
        context=[
            "Siloed data (marketing, product, content, engineering) and GDPR / CCPA / PDPA exposure with fines of up to "
            "4% of global revenue: the company needs to structure its governance.",
            "Educational case study based on a provided business case: the figures come from the case, not from a real engagement.",
        ],
        rh=[
            "<strong>Advisory role with senior leadership</strong>: assessment, recommendation, budget, decision requested.",
            "Targeted 6-month pilot on one domain (marketing engagement data) before scaling: a pragmatic approach.",
            "Clear roles: DPO, CDO, data stewards, governance committee.",
        ],
        tech=[
            "Target architecture: Databricks lakehouse + Unity Catalog as a common foundation.",
            "Tooling recommended per need: catalog (Collibra), quality (dbt, Talend), compliance (OneTrust), security (SIEM), ML lifecycle (MLflow + Evidently).",
            "Measurable governance KPIs: −10% missing data, 100% of consents tracked, incidents detected within 24 h.",
        ],
        stages=[
            ("Sources", "source", ["Marketing", "Product", "Content", "Engineering"]),
            ("Foundation", "storage", ["Databricks lakehouse", "Unity Catalog"]),
            ("Governance", "process", ["Catalog", "Quality (dbt)", "GDPR compliance", "Security"]),
            ("ML", "ops", ["MLflow + Evidently"]),
            ("Organization", "ui", ["Committee · CDO · DPO", "Data stewards"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False), ("s0n3", "s1n0", "", False),
               ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False), ("s1n1", "s2n1", "", False), ("s1n1", "s2n2", "", False),
               ("s1n1", "s2n3", "", False), ("s1n1", "s3n0", "", False), ("s2n2", "s4n0", "", True), ("s2n1", "s4n1", "", True)],
        band=("Rollout: 6-month pilot (marketing) → centralized model → Center of Excellence", "infra"),
        steps=[
            "Maturity assessment across 9 dimensions: governance, compliance and integration at the “defined” level, the others to be strengthened.",
            "Organization design: centralized start, then transition to a Center of Excellence.",
            "Phased implementation plan, compliance priorities first, pilot on engagement data.",
            "Executive presentation with budget, expected ROI and the decision requested from the committee.",
        ],
        extra_diagrams=[],
        langs=[("Deliverables (Word, PDF, PowerPoint)", 100)],
        langs_note="Consulting project, no code.",
        tags=["Data Governance", "GDPR", "Databricks", "Unity Catalog", "Collibra", "dbt", "MLflow", "Change management"],
        stack=[
            ("Databricks + Unity Catalog", "Lakehouse foundation and access control", "Target architecture"),
            ("Collibra", "Catalog and lineage", "Metadata governance"),
            ("dbt / Talend", "Data quality", "Automated controls"),
            ("OneTrust", "Consent and compliance", "GDPR / CCPA"),
            ("MLflow + Evidently", "Model lifecycle and drift", "ML governance"),
        ],
        matrix=None,
        limits=[
            "Certification case study: recommendations not implemented.",
        ],
    ),
    # ------------------------------------------------------------------ PREDICTIRA
    dict(
        slug="predictira",
        short="PredictIRA",
        kicker="Public health ML · Team project",
        title="PredictIRA — forecasting emergency department visits",
        title_html='Anticipating <span class="highlight">respiratory emergencies</span> before the wave',
        lead="Weekly forecast of emergency department visits for acute respiratory infections by French department, based on "
             "weather, pollution, the flu index and Google Trends searches. LightGBM model served with Flask, "
             "then productionized as a containerized FastAPI API.",
        kpis=[("28", "features"), ("LightGBM", "model"), ("2", "applications (Flask, FastAPI)"), ("4", "team members")],
        links=[("Flask application", GH + "PredictIRA", True), ("FastAPI API + Docker", GH + "industrialisation", False)],
        context=[
            "Respiratory epidemics overwhelm emergency departments every winter. Anticipating the load one to two weeks ahead "
            "makes it possible to adjust staffing and beds.",
            "Training team project (M2i / Jedha): model design, then productionization as an API.",
        ],
        rh=[
            "Teamwork in a group of 4 on a public-interest topic.",
            "First move from notebook to a usable application, then to a containerized service.",
        ],
        tech=[
            "Environmental features (O3, PM2.5, PM10, NO2…), flu index and search signals; cyclical encoding of the week.",
            "Serialized LightGBM + <code>StandardScaler</code>, Flask form prefilled by department / week.",
            "Productionization: FastAPI endpoint <code>POST /predict/</code>, Docker image, HTML client.",
        ],
        stages=[
            ("Sources", "source", ["Weather · pollution", "Flu index", "Google Trends"]),
            ("Preparation", "process", ["Features + scaler"]),
            ("Model", "ml", ["LightGBM"]),
            ("Service", "serve", ["Flask (form)", "FastAPI + Docker"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
               ("s1n0", "s2n0", "", False), ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False)],
        band=None,
        steps=[
            "Weekly assembly of environmental, epidemiological and search features by department.",
            "Normalization and training of a LightGBM regression model.",
            "Flask application: the user picks a department and week, adjusts the features and gets the prediction.",
            "Productionization: the same model exposed through a FastAPI API in a Docker container.",
        ],
        extra_diagrams=[],
        langs=[("HTML / CSS", 70), ("Python", 30)],
        tags=["LightGBM", "scikit-learn", "Flask", "FastAPI", "Docker", "Public health"],
        stack=[
            ("LightGBM", "Regression of visit counts", "Gradient boosting"),
            ("scikit-learn", "Normalization", "Data preparation"),
            ("Flask + Jinja", "Web application", "First usable product"),
            ("FastAPI + Docker", "Containerized prediction API", "Productionization"),
        ],
        matrix=dict(ci="n", tests="n", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="n", iac="n"),
        matrix_notes=dict(docker="python:3.9 image + uvicorn", serving="Flask, then FastAPI"),
        snippets=[
            ("industrialisation/api.py — the minimal prediction API",
             '''@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction_ira": int(prediction[0])}'''),
        ],
        limits=[
            "Early-training project: no tests, schema validation or published metrics in the repository.",
            "What I took away and applied afterwards: Pydantic schemas, tests, CI and model monitoring (see LyonFlow and Stripe).",
        ],
    ),
]

# Key strengths of each solution, shown at the top of the "Key strengths" section of project pages.
STRENGTHS_EN = {
    "lyonflow": [
        "<strong>In production, not in a notebook</strong>: deployed on a server, monitored (Prometheus / Grafana), backed up nightly, one-command deployment and rollback.",
        "<strong>Closed MLOps loop</strong>: MLflow registry, daily PSI drift, automatic XGBoost retraining.",
        "<strong>Measured architecture choice</strong>: 3 specialized models instead of one, MAE 5.8 → 3.2 (−45%).",
        "<strong>Built for decision-making</strong>: 3 personas (rider, operator, elected official), bus delay × congestion cross-analysis to prioritize investment.",
    ],
    "stripe-fraude-temps-reel": [
        "<strong>Real time end to end</strong>: Debezium CDC → Kafka → scoring (sub-second target), score written back idempotently.",
        "<strong>Zero training / serving skew</strong>: Redis feature store and the same feature vector for training and inference.",
        "<strong>A self-monitoring model</strong>: automatic retraining on drift or a drop in recall / precision, with a cooldown period.",
        "<strong>Costed, compliant architecture</strong>: 9 AWS Terraform modules, FinOps ~$3,100 → ~$2,400/month, no card numbers stored.",
    ],
    "detection-fraude": [
        "<strong>Business need → automated service</strong>: ingestion every minute, Telegram / email alerts, daily report at 07:00, API.",
        "<strong>Deliberate business trade-off</strong>: recall prioritized (0.83), threshold adjustable by the team without redeployment.",
        "<strong>Reproducible features in production</strong>: the more accurate but non-servable V1 was dropped.",
        "<strong>Operable</strong>: 6 Docker services with health checks, visible fallback to a backup scorer.",
    ],
    "copilot-maintenance": [
        "<strong>Privacy by design</strong>: local LLM (Qwen2.5 via MLX), no data sent to the cloud.",
        "<strong>Robust retrieval</strong>: hybrid dense + BM25 merged with RRF, optional reranker, 5,105 pages indexed.",
        "<strong>Sourced, verifiable answers</strong>: technician trust comes before demo effect.",
        "<strong>Production-grade</strong>: versioned FastAPI API, Prometheus metrics, 141 tests, Ubuntu + macOS CI.",
    ],
    "maintenance-predictive": [
        "<strong>Physics before ML</strong>: BPFO / BPFI / BSF / FTF fault features computed from bearing geometry.",
        "<strong>Leak-free validation</strong>: asset-grouped CV and an <code>assert_no_asset_leakage</code> safeguard.",
        "<strong>Full traceability</strong>: TimescaleDB, MLflow, dataset hash, Evidently drift.",
        "<strong>Rigor</strong>: “zero mock” CI on real data, negative results published as is.",
    ],
    "marche-hvac": [
        "<strong>Field knowledge</strong>: features chosen by domain expertise (MaPrimeRénov', CEE energy-saving certificates, housing type).",
        "<strong>Honest forecasting</strong>: temporal split, TimeSeriesSplit, 5 model families compared, SHAP explainability.",
        "<strong>Extensible</strong>: plugin-based collectors, portable star schema (SQLite, PostgreSQL, SQL Server).",
        "<strong>Ready to deploy</strong>: 562 tests, non-root Docker, monthly Airflow DAG and equivalent Kubernetes CronJob.",
    ],
    "carrier-reporting": [
        "<strong>Measured impact</strong>: −40% processing time, roughly €100K of errors detected every month.",
        "<strong>Unified view</strong>: Power BI semantic model over 5 SAP sources.",
        "<strong>Automated quality control</strong>: DAX measures and anomaly rules on reference data.",
        "<strong>International setting</strong>: European Customer Care and Master Data teams, FR / EN.",
    ],
    "achats-negociation": [
        "<strong>Project led end to end</strong>: scoping, 3-scenario business case, architecture, acceptance testing, deployment, go-to-market.",
        "<strong>Never guessed</strong>: what the engine cannot read stays empty with its reason, never zero.",
        "<strong>Extensible through configuration</strong>: adding a supplier is a YAML change, not code; L0 → L3 matching cascade with human arbitration.",
        "<strong>Industrial-grade quality</strong>: ≈ 4,650 tests, 91 interface views under a versioned contract, 8 access profiles.",
    ],
    "csvtraitement": [
        "<strong>Large volumes without memory saturation</strong>: streaming reads in 10,000-row chunks, 500K+ rows processed.",
        "<strong>Automatic detection</strong> of encoding, separator and column types.",
        "<strong>Compliance</strong>: personal data masking (email, phone, IBAN, French social security number).",
        "<strong>Human in the loop</strong>: no correction applied without validation, undo / redo.",
    ],
    "mcp-open-data": [
        "<strong>Agentic AI</strong>: 11 MCP tools that give an assistant direct access to open data.",
        "<strong>Geographic queries</strong>: WFS 2.0 with CQL filter on Grand Lyon data.",
        "<strong>Robust</strong>: timeouts, HTTP errors returned cleanly to the LLM, one Dockerfile per server.",
        "<strong>Transferable</strong> to an ERP or an internal data warehouse.",
    ],
    "gouvernance-spotify": [
        "<strong>Advisory approach</strong>: assessment across 9 dimensions, recommendation, budget, decision requested.",
        "<strong>Pragmatic</strong>: 6-month pilot on one domain before scaling, ×3 target ROI.",
        "<strong>Clear roles</strong>: DPO, CDO, data stewards, governance committee.",
        "<strong>Measurable</strong>: governance KPIs (−10% missing data, 100% of consents tracked, incidents within 24 h).",
    ],
    "predictira": [
        "<strong>Public interest</strong>: weekly forecast of emergency department visits for acute respiratory infections, by department.",
        "<strong>From notebook to service</strong>: Flask application, then containerized FastAPI API.",
        "<strong>Teamwork</strong> in a group of 4, from data to deployment.",
    ],
}
