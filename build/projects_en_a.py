"""English content for projects 1-6 (translated from projects.py)."""
from projects import GH, M_NONE

PART_A = [
    # ------------------------------------------------------------------ LYONFLOW
    dict(
        slug="lyonflow",
        short="LyonFlow",
        kicker="MLOps · Production · Urban mobility",
        title="LyonFlow — Multimodal traffic MLOps platform",
        title_html='LyonFlow — Lyon mobility <span class="highlight">predicted in real time</span>',
        lead="End-to-end MLOps platform running in production on a VPS: 9 open data sources, Medallion architecture "
             "on PostgreSQL/PostGIS, 27 Airflow DAGs, automatically retrained XGBoost models, multimodal "
             "pgRouting routing and a dashboard for 3 personas.",
        kpis=[("9", "open data sources"), ("27", "Airflow DAGs"), ("620", "pytest tests"), ("59", "widgets / 18 pages"),
              ("−45%", "MAE (3 models vs 1)")],
        links=[("Source code", GH + "lyonflowfull", True),
               ("Databricks variant", GH + "databrickslyonflow", False)],
        context=[
            "The Lyon Metropolitan Area publishes dozens of open data feeds (traffic counting loops, TCL bus positions, "
            "Vélo'v bike stations, weather, roadworks), but <strong>no tool cross-references them</strong> to help a commuter "
            "choose a transport mode, an operator run its network, or an elected official decide on an investment.",
            "LyonFlow collects these feeds every 5 minutes, refines them through Bronze → Silver → Gold layers, predicts "
            "traffic and Vélo'v availability one hour ahead, recommends the best multimodal route and delivers it all "
            "in an application designed for three audiences.",
        ],
        rh=[
            "<strong>A product in production</strong>, not a notebook: deployed on a server, monitored, backed up every night.",
            "Designed for <strong>3 business users</strong> (commuter, TCL operator, elected official) — same logic as sales management: each decision-maker gets their own view.",
            "Cross-referencing <strong>bus delays × congestion</strong> separates an operational problem from an infrastructure need (dedicated lane): a quantified argument for a budget decision.",
            "Project carried out solo end to end: scoping, data, models, deployment, GDPR documentation.",
        ],
        tech=[
            "Medallion Bronze/Silver/Gold on <strong>PostgreSQL 16 + PostGIS + pgRouting</strong>, parameterized SQL throughout, zero hard-coded credentials.",
            "<strong>27 Airflow DAGs</strong> (collection every 5 min → 6 h, transforms, ML, maintenance), MinIO S3 archiving.",
            "<strong>MLflow</strong> registry (6 models, Production stage), XGBoost retraining every 30 min, custom <strong>PSI</strong> drift + Evidently reports.",
            "GitHub Actions CI: ruff, mypy, bandit, pytest + coverage. Deployment via <code>make deploy-vps</code> / <code>rollback-vps</code>, 20 health checks.",
            "Prometheus + Grafana + Alertmanager observability, Nginx as the only exposed entry point, Let's Encrypt TLS.",
        ],
        stages=[
            ("Sources", "source", ["Grand Lyon traffic loops", "TCL SIRI Lite", "Vélo'v GBFS", "Open-Meteo + air quality", "TomTom · roadworks"]),
            ("Ingestion", "ingest", ["Airflow collect_bronze (*/5 min)", "DataCollector collectors"]),
            ("Medallion", "storage", ["Immutable Bronze JSONB", "Cleaned Silver", "Gold features + views"]),
            ("ML", "ml", ["XGBoost speed H+1h", "XGBoost Vélo'v H+1h", "pgRouting Dijkstra"]),
            ("MLOps", "ops", ["MLflow registry", "PSI drift + Evidently", "Prometheus · Grafana"]),
            ("Serving", "serve", ["FastAPI (X-API-Key)", "Nginx + TLS", "Streamlit 3 personas"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
               ("s0n3", "s1n1", "", False), ("s0n4", "s1n1", "", False), ("s1n0", "s2n0", "", False),
               ("s1n1", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s2n2", "", False),
               ("s2n2", "s3n0", "features", False), ("s2n2", "s3n1", "", False), ("s2n2", "s3n2", "", False),
               ("s3n0", "s4n0", "log", True), ("s3n1", "s4n0", "", True), ("s4n1", "s3n0", "retrain", True),
               ("s3n0", "s5n0", "", False), ("s3n2", "s5n2", "", False), ("s5n0", "s5n1", "", False), ("s5n2", "s5n1", "", False)],
        band=("Docker Compose · GitHub Actions (ruff · mypy · bandit · pytest) · make deploy-vps / rollback-vps · nightly backup", "infra"),
        steps=[
            "<strong>Collection</strong> — 9 open sources with no API key, Airflow DAGs scheduled from every 5 min (traffic, buses, Vélo'v) to every 6 h (weather alerts).",
            "<strong>Bronze</strong> — immutable raw JSONB storage: history can always be replayed.",
            "<strong>Silver</strong> — deduplication (<code>DISTINCT ON</code>), SIRI parsing, geographic reprojection (4326 / 2154), filtering of faulty sensors.",
            "<strong>Gold</strong> — ML features (lags, rolling averages, school calendar, weather) and business materialized views (bottlenecks, delays by road segment).",
            "<strong>Modeling</strong> — XGBoost speed H+1h (inference every 15 min), XGBoost Vélo'v H+1h, car routing with <code>pgr_dijkstra</code> on the OSM network with injected speeds.",
            "<strong>MLOps</strong> — MLflow tracking, continuous comparison with TomTom data, daily drift report, automatic retraining.",
            "<strong>Delivery</strong> — FastAPI API (prediction, recommendation, bottlenecks) and an 18-page / 59-widget Streamlit dashboard, with no simulated data at all.",
        ],
        extra_diagrams=[("lyonflow-medallion", "Medallion data flow"), ("lyonflow-ml", "The 4 ML pillars"),
                        ("lyonflow-infra", "Production infrastructure (VPS, containers)"),
                        ("lyonflow-airflow", "Airflow orchestration")],
        langs=[("Python", 78), ("SQL", 13), ("Shell", 4), ("YAML", 3), ("Makefile", 1)],
        tags=["Airflow", "PostgreSQL", "PostGIS", "pgRouting", "XGBoost", "MLflow", "PSI / Evidently", "FastAPI",
              "Streamlit", "Docker", "Nginx", "Prometheus", "Grafana", "MinIO", "GitHub Actions", "GDPR"],
        stack=[
            ("Apache Airflow 2.9", "27 DAGs: collection, Medallion transforms, training, inference, maintenance", "Production orchestration, dependencies and retries"),
            ("PostgreSQL 16 + PostGIS", "bronze / silver / gold / osm / rgpd schemas", "Medallion modeling, spatial SQL, materialized views"),
            ("pgRouting 3.7", "Car routing over ~101k OSM edges", "Graph algorithms inside the database"),
            ("XGBoost", "Traffic speed and Vélo'v availability at H+1h", "Time series, domain features"),
            ("MLflow 2.12", "Tracking and registry for 6 models", "Model lifecycle"),
            ("PSI + Evidently", "Daily drift detection", "Production model monitoring"),
            ("FastAPI", "Prediction / recommendation API, API key", "Model serving"),
            ("Streamlit", "18 pages, 3 personas, PDF report for elected officials", "Decision-oriented delivery"),
            ("Docker · Nginx · systemd", "Containerized stack, single reverse proxy, TLS", "Deployment and server hardening"),
            ("Prometheus · Grafana · Alertmanager", "Metrics, dashboards, 7 alert groups", "Observability"),
            ("MinIO", "S3 archiving of Silver data", "Data lifecycle management"),
            ("Databricks (variant)", "Delta Lake, DLT <code>expect_or_drop</code>, Unity Catalog, Asset Bundles", "Portability to a managed lakehouse"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="y", monitoring="y", serving="y", deploy="y", iac="p"),
        matrix_notes=dict(ci="ruff, mypy, bandit, pytest + coverage", tests="620 tests (unit, personas, integration, e2e)",
                          docker="Application Compose + monitoring Compose", orch="Airflow, 27 DAGs (25 active)",
                          tracking="MLflow registry, Production stage", monitoring="Daily PSI, Evidently, Prometheus/Grafana",
                          serving="FastAPI + API key", deploy="VPS, scripted deploy/rollback, health checks",
                          iac="Databricks Asset Bundle; dormant Kubernetes branch"),
        metrics=dict(head=["Decision / measurement", "Result", "Source"], rows=[
            ["1 single model (38 features) vs 3 specialized models", "MAE 5.8 → 3.2 (−45%)", "internal validation (private working repository)"],
            ["Exploratory benchmark: vehicle counts, 80/20 temporal split, 5 models",
             "Tuned XGBoost: MAE 6.97 · R² 0.71 (linear regression: MAE 15.5)", "notebook 05, private working repository"],
            ["Network coverage", "~458 Vélo'v stations · ~101k OSM edges", "README / diagrams in the public repository"],
        ], note="Key architecture decision: separate traffic, buses and Vélo'v. Road capacity features are 0 for bikes: "
                "in a single model, they add noise and degrade accuracy."),
        snippets=[
            ("src/monitoring/psi.py — robust PSI drift, no heavy dependency",
             '''def _safe_psi_term(pct_ref: float, pct_curr: float, eps: float = 1e-6) -> float:
    """One term of the PSI sum, protected against log(0) and division by 0."""
    if pct_ref < eps and pct_curr < eps:
        return 0.0
    if pct_curr < eps:
        pct_curr = eps
    if pct_ref < eps:
        pct_ref = eps
    return (pct_curr - pct_ref) * np.log(pct_curr / pct_ref)'''),
            ("Operations — one-command deployment and rollback",
             '''make check-deploy-env        # .deploy.env chmod 600 + critical variables
make deploy-vps              # rsync + systemd restart
./scripts/healthcheck-vps.sh  # 20+ checks: containers, disk, DB, endpoints
make rollback-vps            # back to the previous release'''),
        ],
        limits=[
            "Single server: no high availability. The Kubernetes target (EKS/GKE) exists on a dormant branch.",
            "Bus delay prediction still in the analysis phase: SIRI data needs to accumulate before going to production.",
            "Off-site backup: rclone configuration still to be finalized.",
            "Databricks variant in progress: week 1 delivered (Unity Catalog, Bronze ingestion, DLT), MLflow / Model Serving / Genie to come.",
        ],
    ),
    # ------------------------------------------------------------------ STRIPE
    dict(
        slug="stripe-fraude-temps-reel",
        short="Stripe — real-time fraud",
        kicker="Data Architecture · Streaming · RNCP 38777 Block 2",
        title="Polyglot real-time fraud detection platform",
        title_html='Payments: scoring fraud <span class="highlight">in under a second</span>',
        lead="Stripe-style unified data architecture: transactional PostgreSQL, Debezium CDC to Kafka, "
             "Redis feature store, MongoDB, Snowflake warehouse — with XGBoost, MLflow, Evidently drift, "
             "automatic retraining and an AWS target fully described in Terraform.",
        kpis=[("< 1 s", "scoring target"), ("5", "data components"), ("0.995", "offline ROC-AUC"),
              ("3 jobs", "end-to-end CI"), ("9", "Terraform modules")],
        links=[("Source code", GH + "BLOC2-STRIPE", True)],
        context=[
            "<em>Certification case study inspired by Stripe, on synthetic data — not affiliated with the company.</em>",
            "A payment platform must block a fraudulent transaction <strong>before</strong> approving it, "
            "without slowing down the transactional database and without analytics blocking production. "
            "It must also comply with GDPR and PCI-DSS.",
            "The answer: separate the workloads. PostgreSQL for transactions, Debezium + Kafka to stream changes, "
            "Redis for real-time features, MongoDB for logs, Snowflake for analytics — and a monitored model "
            "that retrains itself when reality changes.",
        ],
        rh=[
            "A high-stakes financial topic: every missed fraud costs money, every false positive <strong>blocks a customer</strong>.",
            "Architecture choices justified and quantified, including <strong>cloud cost (FinOps)</strong>: ~$3,100/month in production, brought down to ~$2,400 with the identified levers.",
            "Compliance built in by design: no card numbers stored, SHA-256 fingerprints, limited log retention.",
            "Real incidents documented and resolved — evidence of an operations mindset, not just development.",
        ],
        tech=[
            "<strong>Debezium CDC</strong> on the PostgreSQL WAL → Kafka (KRaft), idempotent score write-back.",
            "<strong>Redis feature store</strong> (1 h / 24 h velocity in sorted sets) and the same feature vector at training and inference: zero <em>training/serving skew</em>.",
            "Leak-proof <strong>temporal</strong> split, XGBoost with <code>scale_pos_weight</code>, MLflow registry <code>fraud-detector</code>.",
            "Evidently monitor: automatic retraining if drift &gt; 0.3, recall &lt; 0.7 or precision &lt; 0.5, with a cooldown period.",
            "CI that spins up <strong>the entire stack</strong> without mocks + audit notebook executed as a quality gate; Terraform AWS (3-AZ VPC, RDS, MSK, ElastiCache, ECS Fargate, MWAA).",
        ],
        stages=[
            ("Source", "source", ["Transaction producer (5 tx/s)"]),
            ("OLTP", "storage", ["PostgreSQL 16 (3NF, ACID)"]),
            ("Streaming", "ingest", ["Debezium CDC (WAL)", "Kafka KRaft"]),
            ("Scoring", "ml", ["Redis feature store", "Real-time scorer", "XGBoost / rules"]),
            ("MLOps", "ops", ["MLflow registry", "Evidently + retrain"]),
            ("Storage", "storage", ["MongoDB (logs, alerts)", "Snowflake OLAP"]),
            ("Delivery", "ui", ["Streamlit (auth)", "Airflow ETL 02:00"]),
        ],
        edges=[("s0n0", "s1n0", "INSERT", False), ("s1n0", "s2n0", "WAL", False), ("s2n0", "s2n1", "", False),
               ("s2n1", "s3n1", "", False), ("s3n0", "s3n1", "", False), ("s3n1", "s3n2", "", False),
               ("s3n1", "s1n0", "write-back", True), ("s3n2", "s4n0", "", True), ("s4n1", "s4n0", "retrain", True),
               ("s2n1", "s5n0", "", False), ("s1n0", "s6n1", "", True), ("s6n1", "s5n1", "", True), ("s5n0", "s6n0", "", False)],
        band=("GitHub Actions: lint · terraform validate · e2e on full stack · Terraform AWS (VPC, RDS, MSK, ElastiCache, ECS, MWAA)", "infra"),
        steps=[
            "A producer inserts synthetic transactions (5% injected fraud) into PostgreSQL 16, configured for logical replication.",
            "Debezium reads the WAL and publishes every change to Kafka (<code>stripe.public.transactions</code>).",
            "The scorer enriches each transaction with customer velocities stored in Redis, then scores it (rules or XGBoost): allow, review (≥ 0.60) or block (≥ 0.85).",
            "The score is written back idempotently to PostgreSQL; events and alerts go to Kafka, then MongoDB.",
            "Every 2 minutes, the monitor compares recent data to the reference (Evidently) and to the performance actually served; it retriggers training when needed.",
            "Every night, Airflow exports to the Snowflake star schema and refreshes the materialized views.",
            "The Streamlit dashboard (authenticated) shows KPIs, alerts, drift and a rules vs. model comparison.",
        ],
        extra_diagrams=[("stripe-architecture", "Unified data architecture (actual implementation)"),
                        ("stripe-aws", "AWS target (Terraform)")],
        langs=[("Python", 48), ("HCL (Terraform)", 27), ("SQL", 7), ("YAML", 7), ("Shell", 4), ("JavaScript", 3)],
        tags=["PostgreSQL", "Debezium", "Kafka", "Redis", "MongoDB", "Snowflake", "XGBoost", "MLflow", "Evidently",
              "Airflow", "Streamlit", "Terraform", "AWS", "Docker", "GitHub Actions", "PCI-DSS", "FinOps"],
        stack=[
            ("PostgreSQL 16", "3NF OLTP, separate roles, GDPR anonymization function", "Transactional modeling"),
            ("Debezium 2.6 + Kafka 7.6", "Change Data Capture, scores / alerts / dead-letter topics", "Event-driven architecture"),
            ("Redis 7", "Online feature store (velocities)", "Low-latency real-time features"),
            ("MongoDB 7", "Logs with TTL, alerts, features, monitoring", "NoSQL modeling"),
            ("Snowflake", "Star schema, CLUSTER BY", "OLAP modeling (run in dry-run mode)"),
            ("XGBoost + scikit-learn", "Fraud classifier, 7 shared features", "ML on imbalanced data"),
            ("MLflow 2.14", "Tracking + registry", "Model lifecycle"),
            ("Evidently 0.4", "Drift + retraining trigger", "Monitoring and closed loop"),
            ("Airflow 2.9", "Daily ETL to OLAP", "Batch orchestration"),
            ("Terraform 1.10", "VPC, RDS Multi-AZ, MSK, ElastiCache, Atlas, ECS, MWAA, KMS", "Infrastructure as Code"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="y", monitoring="y", serving="p", deploy="p", iac="y"),
        matrix_notes=dict(ci="lint, terraform validate, full-stack e2e", tests="16 e2e checks + 13 ML tests + audit notebook",
                          docker="8 services + Flink / Airflow profiles", orch="Airflow (batch) + Kafka (streaming)",
                          tracking="MLflow, registered model fraud-detector", monitoring="Evidently + served precision/recall, auto retrain",
                          serving="Scoring via Kafka consumer (no REST API)", deploy="Local Docker; AWS target validated, not applied",
                          iac="Terraform AWS, dev / prod environments"),
        metrics=dict(head=["Run (09/15/2026)", "Trigger", "Precision", "Recall", "F1", "ROC-AUC"], rows=[
            ["15:53", "make ml-train", "0.95", "0.97", "0.96", "0.995"],
            ["17:10", "automatic (drift 0.43)", "0.77", "0.97", "0.86", "0.990"],
        ], note="Offline measurements on a temporal hold-out. Precision actually served around the retraining: 0.93 to 0.99 per minute. "
                "Documented lesson: judge a retrained model on its <strong>served</strong> performance, not just on an offline metric."),
        snippets=[
            ("ml/monitor.py — closed loop: drift or degradation ⇒ retraining",
             '''if drift["drift_share"] > DRIFT_THRESHOLD:
    reasons.append(f"drift_share={drift['drift_share']:.2f} > seuil {DRIFT_THRESHOLD}")
if performance is not None and performance["recall"] < MIN_RECALL:
    reasons.append(f"recall={performance['recall']:.2f} < seuil {MIN_RECALL}")
if performance is not None and performance["precision"] < MIN_PRECISION:
    reasons.append(f"precision={performance['precision']:.2f} < seuil {MIN_PRECISION}")

cooldown_ok = (last_retrain_at is None) or (now_ts - last_retrain_at > RETRAIN_COOLDOWN_SECONDS)
if reasons and cooldown_ok:
    doc["retrain_triggered"] = True
    retrain_model()'''),
            ("ml/train_fraud_model.py — temporal split to prevent information leakage",
             '''def temporal_train_test_split(df, X, y, test_frac=0.2):
    """Train/test split in chronological order (not random).
    A random split would mix past/future velocity windows:
    the model would indirectly "see" future transactions."""
    n = len(df)
    cut = int(n * (1 - test_frac))
    return X[:cut], X[cut:], y[:cut], y[cut:]'''),
        ],
        limits=[
            "Flink replaced by an equivalent Python consumer (PyFlink does not compile on ARM64); the PyFlink job exists as an optional profile.",
            "Snowflake run in dry-run mode for lack of an account; Terraform validated but never applied.",
            "No promotion gate or automatic rollback in the MLflow registry yet.",
            "Offline / online gap observed over one window (served precision 0.52): flagged by the audit notebook itself, a lead for calibration.",
        ],
    ),
    # ------------------------------------------------------------------ BLOC3
    dict(
        slug="detection-fraude",
        short="Automated fraud detection",
        kicker="ML in production · Alerting · RNCP 38777 Block 3",
        title="Automated bank fraud detection",
        title_html='Card fraud: <span class="highlight">alert in real time</span>, report every morning',
        lead="Containerized pipeline that polls a payment stream every minute, scores each transaction with XGBoost "
             "through a FastAPI API, sends a Telegram alert above a business threshold and produces an automatic daily report.",
        kpis=[("0.83", "recall (frauds detected)"), ("0.989", "ROC-AUC"), ("1 min", "ingestion frequency"),
              ("6", "Docker services"), ("22", "pytest tests")],
        links=[("Source code", GH + "BLOC3-FRAUD-DETECTION", True), ("Version 1 (RandomForest + MLflow)", GH + "anonymisation", False)],
        context=[
            "Card fraud exceeds one billion euros per year in Europe (ECB, 2019). Fraud teams need "
            "three things: to be <strong>notified instantly</strong>, to get a summary of the previous day <strong>every morning</strong>, "
            "and a prediction served continuously by an API.",
            "The project addresses all three needs with infrastructure reproducible in two commands.",
        ],
        rh=[
            "Direct translation of a business need into an automated service: <strong>alert, report, API</strong>.",
            "A deliberate trade-off: favor <strong>recall</strong> (don't let fraud through), with a threshold the business team can adjust without redeployment.",
            "Willingness to challenge my own work: V1 was abandoned after a critical review (features not reproducible in production).",
        ],
        tech=[
            "Airflow: real-time DAG (<code>*/1 * * * *</code>) with XCom and retries, daily report DAG at 07:00.",
            "FastAPI: <code>/predict</code>, <code>/health</code>, optional API key, <strong>business threshold</strong> via environment variable, visible fallback to a backup scorer.",
            "10 business features reproducible at inference (amount, hour, weekend, merchant geolocation…), weighted XGBoost (<code>scale_pos_weight</code> ≈ 27).",
            "Docker Compose with 6 services and health checks; PostgreSQL 15 via SQLAlchemy 2; Telegram / SMTP alerts.",
        ],
        stages=[
            ("Sources", "source", ["Real-time payments API", "Kaggle fraudTest (fallback)"]),
            ("Orchestration", "ingest", ["DAG fraud_realtime_ingest", "DAG daily_report 07:00"]),
            ("Scoring", "serve", ["FastAPI /predict", "XGBoost + 0.7 threshold"]),
            ("Storage", "storage", ["PostgreSQL 15"]),
            ("Action", "ui", ["Telegram / email alert", "Daily HTML report", "Streamlit dashboard"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", True), ("s1n0", "s2n0", "POST", False),
               ("s2n0", "s2n1", "", False), ("s2n0", "s3n0", "insert", False), ("s2n1", "s4n0", "≥ threshold", False),
               ("s1n1", "s3n0", "D-1", True), ("s1n1", "s4n1", "", False), ("s3n0", "s4n2", "", False)],
        band=("Docker Compose (postgres · fraud-api · airflow init/scheduler/webserver · dashboard) · pytest", "infra"),
        steps=[
            "Every minute, Airflow fetches current transactions (public API, falling back to a Kaggle file with a persistent cursor).",
            "Each transaction is sent to the FastAPI API, which builds the 10 business features and computes the fraud probability.",
            "Above the business threshold (0.7), an alert is sent on Telegram (and optionally by email); all results are stored in PostgreSQL.",
            "At 07:00, a second DAG generates the HTML report of the previous day's frauds.",
            "A Streamlit dashboard shows KPIs, probability distribution, a map and the top 20 riskiest transactions.",
        ],
        extra_diagrams=[("fraude-pipeline", "Detailed pipeline (training, real time, reporting)")],
        langs=[("Python", 85), ("Shell", 8), ("HTML", 4), ("YAML", 3)],
        tags=["XGBoost", "FastAPI", "Airflow", "PostgreSQL", "SQLAlchemy", "Pydantic", "Streamlit", "Docker", "Telegram API", "pytest"],
        stack=[
            ("XGBoost", "Classifier on 10 business features", "Handling class imbalance"),
            ("FastAPI + Pydantic", "Scoring API, input validation", "Robust model serving"),
            ("Airflow 2.9", "Per-minute ingestion + daily report", "Scheduled orchestration"),
            ("PostgreSQL 15 + SQLAlchemy 2", "Prediction history", "Persistence and querying"),
            ("Telegram Bot API / SMTP", "Fraud notifications", "Closing the loop with the business user"),
            ("Streamlit + Plotly", "Real-time monitoring", "Delivery"),
            ("MLflow (V1)", "Tracking of the RandomForest version", "Experiment tracking"),
        ],
        matrix=dict(ci="n", tests="y", docker="y", orch="y", tracking="p", monitoring="n", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(tests="22 tests (API, report); 47 in V1", docker="Compose with 6 services + health checks",
                          orch="2 Airflow DAGs", tracking="MLflow in V1, metrics file in V2",
                          monitoring="Grafana + drift planned", serving="FastAPI", deploy="Reproducible locally in 2 commands"),
        metrics=dict(head=["Model", "Recall", "Precision", "F1", "ROC-AUC"], rows=[
            ["XGBoost business features (V2, threshold 0.5)", "0.831", "0.373", "0.515", "0.989"],
            ["RandomForest PCA features (V1, abandoned)", "0.78", "0.88", "—", "—"],
        ], note="V1 showed better precision but relied on PCA features that cannot be rebuilt in production: "
                "its probabilities capped at ~0.37 and it detected no real fraud. V2 favors a model that can actually be served."),
        snippets=[
            ("api/main.py — business threshold on top of the probability, explicit fallback",
             '''try:
    from src.predict_business import get_predictor as get_business_predictor
    predictor = get_business_predictor()
    result = predictor.predict(dict(transaction))
    probability = float(result["fraud_probability"])
    is_fraud = bool(probability >= FRAUD_THRESHOLD)
    return is_fraud, probability, "xgboost_business"
except FileNotFoundError:
    logger.warning("Modèle business absent (models/fraud_model.pkl) — fallback vers mock")
except Exception as exc:
    logger.error("Erreur prédiction business: %s — fallback vers mock", exc)
return _mock_predict(transaction)'''),
        ],
        limits=[
            "Moderate precision (0.37 at threshold 0.5): probability calibration (<code>CalibratedClassifierCV</code>) and training on the full 555k rows are planned.",
            "No CI or drift monitoring yet (Grafana + monthly retraining DAG planned).",
            "The model is not versioned in the repository: a fresh clone serves the backup scorer until training has been run.",
        ],
    ),
    # ------------------------------------------------------------------ RAG
    dict(
        slug="copilot-maintenance",
        short="Maintenance copilot (local RAG)",
        kicker="Generative AI · RAG · Local LLM",
        title="Industrial Knowledge Copilot — 100% local RAG",
        title_html='An AI copilot for maintenance, <span class="highlight">with no data ever leaving the machine</span>',
        lead="Question-answering assistant over 5,105 pages of technical bearing catalogs (Schaeffler, SKF, NTN-SNR, GGB): "
             "hybrid dense + BM25 search, Qwen2.5-7B LLM running locally via MLX, RAGAS evaluation and an instrumented API.",
        kpis=[("5,105", "indexed pages"), ("13", "PDF catalogs"), ("141", "tests"), ("0", "data sent to the cloud")],
        links=[("Source code", GH + "maintenance", True)],
        context=[
            "A maintenance technician wastes time looking up a tolerance, a tightening torque or a part reference "
            "in catalogs hundreds of pages long. Online AI assistants raise an "
            "<strong>industrial confidentiality</strong> issue.",
            "This copilot answers in French or English, <strong>cites its sources</strong> (catalog and page) and runs entirely "
            "on an Apple Silicon machine, with no API key.",
        ],
        rh=[
            "Generative AI applied to a real pain point in the field, drawn from 20 years in industrial distribution.",
            "<strong>Confidentiality by design</strong>: no data leaves the machine, transparency documented in line with the AI Act.",
            "Sourced, verifiable answers: business user trust comes before demo appeal.",
        ],
        tech=[
            "PyMuPDF ingestion → 500-token chunks (50 overlap) → multilingual <strong>bge-m3</strong> embeddings (1024 dim) → ChromaDB.",
            "<strong>Hybrid search</strong>: dense + BM25 merged with Reciprocal Rank Fusion, optional cross-encoder reranker.",
            "Generation with 4-bit Qwen2.5-7B-Instruct via <strong>MLX</strong> (Metal), LangChain LCEL chain, FR/EN prompts, controlled 504 timeout.",
            "Versioned FastAPI <code>/v1</code>, Prometheus metrics, JSON logs; Ubuntu + macOS CI, ChromaDB integration tests, CodeQL.",
        ],
        stages=[
            ("Sources", "source", ["13 PDF catalogs"]),
            ("Ingestion", "ingest", ["PyMuPDF", "Chunker 500/50"]),
            ("Indexing", "storage", ["bge-m3 embeddings", "ChromaDB", "BM25 index"]),
            ("Retrieval", "process", ["Hybrid RRF", "Cross-encoder reranker"]),
            ("Generation", "ml", ["Qwen2.5-7B (MLX)", "LCEL chain"]),
            ("Serving", "serve", ["FastAPI /v1/query", "Streamlit (chat + sources)", "/metrics Prometheus"]),
            ("Evaluation", "ops", ["RAGAS"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
               ("s2n0", "s2n1", "", False), ("s1n1", "s2n2", "", True), ("s2n1", "s3n0", "dense", False),
               ("s2n2", "s3n0", "sparse", False), ("s3n0", "s3n1", "", False), ("s3n1", "s4n1", "context", False),
               ("s4n0", "s4n1", "", False), ("s4n1", "s5n0", "", False), ("s5n1", "s5n0", "", False),
               ("s5n0", "s5n2", "", True), ("s6n0", "s4n1", "evaluates", True)],
        band=("GitHub Actions (Ubuntu + macOS) · ChromaDB integration tests · CodeQL · multi-stage non-root Docker", "infra"),
        steps=[
            "PDFs are read page by page (page numbers kept for citation) and split into overlapping chunks.",
            "Each chunk is embedded with bge-m3 (multilingual) and stored in ChromaDB; a lexical BM25 index is built in parallel.",
            "For each question, both searches are merged with RRF (robust to different score scales), then reranked.",
            "The local LLM generates an answer grounded in the context, citing the catalog and page.",
            "RAGAS measures faithfulness, answer relevancy, context precision and context recall; each evaluation is frozen as a timestamped snapshot.",
        ],
        extra_diagrams=[],
        langs=[("Python", 74), ("HTML", 10), ("CSS", 7), ("Shell", 3), ("YAML", 2), ("Makefile", 2)],
        tags=["RAG", "LLM", "MLX", "Qwen2.5", "bge-m3", "ChromaDB", "BM25", "LangChain", "RAGAS", "FastAPI",
              "Streamlit", "Prometheus", "CodeQL", "Docker"],
        stack=[
            ("MLX + Qwen2.5-7B-Instruct 4-bit", "Local generation on Apple GPU", "On-device LLM, no API"),
            ("bge-m3 (sentence-transformers)", "FR/EN embeddings, 1024 dim", "Multilingual semantic search"),
            ("ChromaDB", "Vector database", "Vector storage"),
            ("rank-bm25 + RRF", "Lexical search and fusion", "Hybrid retrieval"),
            ("ms-marco-MiniLM", "Cross-encoder reranking", "Top-k precision"),
            ("LangChain LCEL", "Retriever → prompt → LLM chain", "LLM orchestration"),
            ("RAGAS", "RAG quality evaluation", "Measuring instead of assuming"),
            ("FastAPI + Prometheus", "Versioned API, latency counters and histograms", "Instrumented service"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="n", tracking="p", monitoring="y", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(ci="lint + tests on 2 OSes, integration, CodeQL", tests="141 tests", docker="Multi-stage non-root API, ChromaDB in Compose",
                          tracking="Timestamped RAGAS evaluation snapshots", monitoring="/metrics Prometheus, JSON logs",
                          serving="FastAPI /query /ingest /eval", deploy="Local workstation (MLX requires Metal)"),
        snippets=[
            ("src/rag/retriever.py — Reciprocal Rank Fusion of dense + BM25",
             '''rrf_contrib = 1.0 / (_RRF_K0 + rank + 1)
if cid in chunk_map:
    chunk_map[cid]["rrf"] += rrf_contrib
    if chunk_map[cid]["chunk"].retrieval_method == "dense":
        chunk_map[cid]["chunk"].retrieval_method = "rrf"'''),
        ],
        limits=[
            "Baseline RAGAS scores not yet published: the question / answer set is ready, the measured runs still need to be frozen.",
            "Tool-calling agent removed (Qwen / Mistral comparison inconclusive) in favor of a more reliable RAG chain.",
            "Deployment limited to Apple Silicon (MLX); a vLLM / llama.cpp variant would allow a Linux server.",
        ],
    ),
    # ------------------------------------------------------------------ MLINDUSTRIAL
    dict(
        slug="maintenance-predictive",
        short="Vibration-based predictive maintenance",
        kicker="Industrial ML · Signal · Digital twin",
        title="Predictive maintenance — bearing diagnostics",
        title_html='From lab to shop floor: <span class="highlight">detecting a failing bearing</span>',
        lead="Bearing fault detection on the Paderborn dataset (32 bearings, 4 operating conditions) using "
             "explainable physical features, with one key question: does a model trained on artificial faults "
             "hold up on real faults?",
        kpis=[("189", "tests"), ("0.738", "XGBoost macro F1"), ("5.4 GB", "raw signals"), ("5 folds", "CV grouped by asset")],
        links=[("Source code", GH + "MLindustrial", True)],
        context=[
            "Most predictive maintenance demos test a model on the same bearings it saw during "
            "training: the scores look great and don't hold up on the shop floor.",
            "This project honestly measures the lab / field gap, compares a vibration sensor with the <strong>motor current "
            "already available on every drive</strong> (no extra sensor needed) and favors indicators a maintenance manager "
            "can understand.",
        ],
        rh=[
            "Real domain expertise (field deployments with IFM, Schaeffler, SKF) put to work for data.",
            "<strong>Sensor cost / value</strong> reasoning: can we avoid instrumenting a machine?",
            "Negative results published as they are: rigor comes before showcasing.",
        ],
        tech=[
            "Physical features: RMS, kurtosis, crest factor and <strong>BPFO / BPFI / BSF / FTF fault frequencies</strong> computed from the geometry.",
            "Splits by asset / condition / artificial→real, <code>StratifiedGroupKFold</code> and an <code>assert_no_asset_leakage</code> safeguard.",
            "TimescaleDB (features hypertable), MLflow backed by PostgreSQL, dataset hash for traceability, Evidently drift.",
            "CI: Python 3.11 / 3.12 matrix, “zero mock” audit, full ML pipeline on real data with MLflow artifacts.",
            "Physical simulators, SimPy factory simulation and Asset Administration Shell export (Industry 4.0).",
        ],
        stages=[
            ("Source", "source", ["Paderborn .mat (5.4 GB)"]),
            ("Ingestion", "ingest", ["Loaders + physical checks", "Parquet"]),
            ("Storage", "storage", ["TimescaleDB (hypertable)"]),
            ("Features", "process", ["Time domain: RMS, kurtosis", "BPFO/BPFI frequencies"]),
            ("Models", "ml", ["Thresholds (baseline)", "XGBoost", "CV grouped by asset"]),
            ("Tracking", "ops", ["MLflow (Postgres)", "Evidently drift"]),
            ("Delivery", "ui", ["Streamlit digital twin", "AAS export"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
               ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False), ("s3n0", "s4n0", "", False),
               ("s3n1", "s4n1", "", False), ("s4n2", "s4n1", "", True), ("s4n1", "s5n0", "log", False),
               ("s4n0", "s5n0", "", False), ("s5n1", "s6n0", "", True), ("s4n1", "s6n0", "", False), ("s6n0", "s6n1", "", True)],
        band=("uv · GitHub Actions (ruff, pytest, zero-mock audit, ML pipeline on real data) · Docker Compose", "infra"),
        steps=[
            "Download of the Paderborn signals, parsing of file names (bearing, operating condition, fault) and physical plausibility checks.",
            "Hierarchical storage site → area → machine → asset → bearing in TimescaleDB.",
            "Computation of time-domain indicators and characteristic fault frequencies from the bearing geometry.",
            "Comparison of a threshold baseline and XGBoost, with cross-validation grouped by asset (no bearing in both train and test).",
            "MLflow tracking (dataset hash, macro F1, balanced accuracy) and Evidently train / test drift report.",
            "Streamlit delivery: alerts, spectra, factory digital twin, glossary.",
        ],
        extra_diagrams=[],
        langs=[("Python", 84), ("YAML", 15), ("TOML", 1)],
        tags=["Signal processing", "SciPy", "XGBoost", "scikit-learn", "TimescaleDB", "MLflow", "Evidently", "Polars",
              "Streamlit", "SimPy", "uv", "Docker", "GitHub Actions", "Industry 4.0"],
        stack=[
            ("NumPy / SciPy", "Signal processing, spectra, envelope", "Explainable physical features"),
            ("XGBoost / scikit-learn", "Fault classification", "ML on industrial data"),
            ("TimescaleDB", "Time series, features hypertable", "Storage suited to sensor data"),
            ("MLflow", "Baseline vs GBM experiments, dataset hash", "Traceability and reproducibility"),
            ("Evidently", "Train / test drift (KS)", "Detecting distribution shift"),
            ("SimPy", "Discrete-event factory simulation", "Digital twin"),
            ("uv + ruff + pytest", "Dependency management, code quality", "Engineering hygiene"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="n", tracking="y", monitoring="y", serving="n", deploy="p", iac="n"),
        matrix_notes=dict(ci="CI + ML pipeline + tagged releases", tests="189 tests including anti-leakage", docker="db, mlflow, app, dashboard",
                          tracking="MLflow backed by PostgreSQL", monitoring="Evidently + temporal drift", deploy="GitHub Releases"),
        metrics=dict(head=["Model (5-fold CV grouped by asset)", "Macro F1"], rows=[
            ["Kurtosis threshold", "0.682 ± 0.158"],
            ["Crest factor threshold", "0.576 ± 0.174"],
            ["XGBoost vibration (5 features)", "0.738 ± 0.208"],
            ["XGBoost vibration + current (15 features)", "0.726 ± 0.222"],
            ["XGBoost current only (10 features)", "0.542 ± 0.121"],
        ], note="Honest conclusion: at this stage, XGBoost does not clearly beat a simple kurtosis rule (overlapping intervals). "
                "Phase 3 (training on artificial faults, testing on real faults) is the next measurement."),
        snippets=[
            ("src/features/fault_frequencies.py — bearing physics",
             '''def bpfo(n_balls, fr_hz, d_mm, big_d_mm, phi_deg=0.0):
    """Ball Pass Frequency Outer race - outer race fault."""
    return (n_balls / 2) * fr_hz * (1 - _geometry_factor(d_mm, big_d_mm, phi_deg))'''),
            ("src/data/splits.py — safeguard against train/test leakage",
             '''def assert_no_asset_leakage(train_df, test_df, asset_col="asset_id"):
    leaked = set(train_df[asset_col]) & set(test_df[asset_col])
    if leaked:
        raise ValueError(f"Fuite de donnees : assets presents dans train ET test : {leaked}")'''),
        ],
        limits=[
            "Phase 3 (artificial → real) not yet run: this is the measurement that will validate real-world value.",
            "Envelope analysis / kurtogram disabled until it is stable.",
            "No inference API: the current deliverable is the study and the dashboard.",
        ],
    ),
    # ------------------------------------------------------------------ HVAC
    dict(
        slug="marche-hvac",
        short="French HVAC market",
        kicker="Data Engineering · Forecasting · Energy",
        title="HVAC market — forecasting heat pump installations",
        title_html='Anticipating the <span class="highlight">heat pump</span> market, department by department',
        lead="Complete pipeline from open data to prediction: 5 collectors (ADEME DPE, Open-Meteo, INSEE, Eurostat, SITADEL), "
             "star-schema warehouse, Ridge / LightGBM / Prophet / LSTM benchmark, FastAPI API, dashboard, Airflow and Kubernetes.",
        kpis=[("96", "departments"), ("5", "open data sources"), ("562", "tests"), ("5", "model families")],
        links=[("Source code", GH + "Projet-HVAC", True)],
        context=[
            "For an HVAC distributor, knowing where and when the heat pump market will accelerate drives inventory, "
            "sales force and installer partnerships. The signals exist (energy performance diagnostics, building permits, "
            "weather, economic conditions) but are scattered.",
            "The project brings them together every month in a reproducible pipeline and delivers a forecast per department.",
        ],
        rh=[
            "A topic chosen from <strong>my own industry</strong>: the variables (MaPrimeRénov', CEE, housing type) come from field knowledge.",
            "A deliverable a sales leadership team can use: map of France, forecasts, model comparison.",
            "Documented governance (GDPR, AI Act).",
        ],
        tech=[
            "Collectors built on a <strong>plugin architecture</strong> (<code>BaseCollector</code> + registry), no API key required.",
            "SQLAlchemy star schema (SQLite, PostgreSQL 16 or SQL Server), outlier detection with IQR / Z-score / Isolation Forest.",
            "Temporal train / validation / test split + <code>TimeSeriesSplit</code>; SHAP explainability.",
            "FastAPI with 6 endpoints, 6-page Streamlit app, multi-stage non-root Docker, monthly Airflow DAG <strong>and</strong> an equivalent Kubernetes CronJob.",
            "CI: pytest 3.11 / 3.12 with coverage, ruff, Docker build + smoke test.",
        ],
        stages=[
            ("Sources", "source", ["ADEME DPE", "Open-Meteo", "INSEE · Eurostat", "SITADEL permits"]),
            ("Collection", "ingest", ["Plugin collectors"]),
            ("Storage", "storage", ["CSV data lake", "SQL star schema"]),
            ("Preparation", "process", ["Cleaning + outliers", "Feature engineering"]),
            ("Models", "ml", ["Ridge · LightGBM", "Prophet · LSTM", "SHAP"]),
            ("Serving", "serve", ["FastAPI", "Streamlit 6 pages"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False), ("s0n3", "s1n0", "", False),
               ("s1n0", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s3n0", "", False), ("s3n0", "s3n1", "", False),
               ("s3n1", "s4n0", "", False), ("s3n1", "s4n1", "", False), ("s4n1", "s4n2", "", True), ("s4n0", "s5n0", "pkl", False),
               ("s5n0", "s5n1", "", False)],
        band=("Monthly Airflow DAG (0 6 1 * *) ⇄ Kubernetes CronJob · Docker · GitHub Actions (pytest, ruff, Docker smoke) · Render", "infra"),
        steps=[
            "On the 1st of each month, Airflow (or the Kubernetes CronJob) runs the collectors across the 96 departments.",
            "Raw data is cleaned, merged and loaded into a star schema; outliers are detected with three methods.",
            "Feature engineering produces lags, rolling means and rolling standard deviations over 3 and 6 months.",
            "Five model families are trained on a temporal split, then explained with SHAP.",
            "Models are served by FastAPI and visualized in a Streamlit dashboard (map of France, forecasts, comparison).",
        ],
        extra_diagrams=[],
        langs=[("Python", 94), ("SQL", 2), ("YAML", 2), ("Shell", 1), ("Makefile", 1)],
        tags=["Open data", "ETL", "SQLAlchemy", "LightGBM", "Prophet", "PyTorch LSTM", "SHAP", "FastAPI", "Streamlit",
              "Airflow", "Kubernetes", "Docker", "GitHub Actions"],
        stack=[
            ("requests / eurostat", "Collection from 5 public APIs", "Multi-source ingestion"),
            ("SQLAlchemy", "Multi-DBMS star schema", "Analytical modeling"),
            ("scikit-learn · LightGBM · Prophet · PyTorch", "Benchmark of 5 approaches", "Reasoned model selection"),
            ("SHAP", "Feature importance", "Explainability for business users"),
            ("FastAPI + Streamlit", "API and dashboard", "Making results available"),
            ("Airflow + Kubernetes CronJob", "Monthly refresh", "Two orchestration modes"),
            ("Docker multi-stage", "Non-root images, health checks", "Clean containerization"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="n", monitoring="n", serving="y", deploy="p", iac="y"),
        matrix_notes=dict(ci="pytest on 2 versions + coverage, ruff, Docker smoke test", tests="562 tests",
                          docker="Multi-stage, non-root", orch="Airflow + K8s CronJob", tracking="Metrics in CSV/JSON (no MLflow)",
                          serving="FastAPI, 6 endpoints", deploy="Render Blueprint", iac="Kubernetes manifests (Deployment, Ingress, PVC, CronJob)"),
        snippets=[
            ("kubernetes/cronjob-pipeline.yaml — the Airflow DAG, Kubernetes-native version",
             '''apiVersion: batch/v1
kind: CronJob
metadata:
  name: hvac-pipeline-monthly
spec:
  schedule: "0 6 1 * *"    # 1st of the month at 6:00 UTC
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 2
      activeDeadlineSeconds: 7200'''),
        ],
        limits=[
            "Post-project audit: some rolling means include the target's current month, which inflates the scores. "
            "Fix identified (one-month shift); metrics will be republished after re-benchmarking.",
            "No MLflow tracking or drift monitoring: the next component to add.",
        ],
    ),
]
