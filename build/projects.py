"""Portfolio content: one dict per project page. Facts come from the repositories (analysed 2026-09-23)."""

GH = "https://github.com/PDUCLOS/"

M_NONE = dict(ci="n", tests="n", docker="n", orch="n", tracking="n", monitoring="n", serving="n", deploy="n", iac="n")

PROJECTS = [
    # ------------------------------------------------------------------ LYONFLOW
    dict(
        slug="lyonflow",
        short="LyonFlow",
        kicker="MLOps · Production · Mobilité urbaine",
        title="LyonFlow — Plateforme MLOps trafic multimodal",
        title_html='LyonFlow — la mobilité lyonnaise <span class="highlight">prédite en temps réel</span>',
        lead="Plateforme MLOps de bout en bout, en production sur VPS : 9 sources open data, architecture Medallion "
             "sur PostgreSQL/PostGIS, 27 DAGs Airflow, modèles XGBoost réentraînés automatiquement, routage "
             "multimodal pgRouting et un dashboard à 3 personas.",
        kpis=[("9", "sources open data"), ("27", "DAGs Airflow"), ("620", "tests pytest"), ("59", "widgets / 18 pages"),
              ("−45 %", "MAE (3 modèles vs 1)")],
        links=[("Démo live", "/live/", True), ("Code source", GH + "lyonflowfull", False),
               ("Variante Databricks", GH + "databrickslyonflow", False)],
        context=[
            "La Métropole de Lyon publie des dizaines de flux ouverts (boucles de comptage, positions des bus TCL, "
            "stations Vélo'v, météo, chantiers), mais <strong>aucun outil ne les croise</strong> pour aider un usager "
            "à choisir son mode de transport, un opérateur à piloter son réseau ou un élu à arbitrer un investissement.",
            "LyonFlow collecte ces flux toutes les 5 minutes, les raffine en couches Bronze → Silver → Gold, prédit "
            "trafic et disponibilité Vélo'v à H+1h, recommande le meilleur itinéraire multimodal et restitue le tout "
            "dans une application pensée pour trois publics.",
        ],
        rh=[
            "<strong>Un produit en production</strong>, pas un notebook : accessible en ligne, supervisé, sauvegardé chaque nuit.",
            "Pensé pour <strong>3 utilisateurs métier</strong> (usager, opérateur TCL, élu) — même logique que le pilotage commercial : chaque décideur a sa vue.",
            "Le croisement <strong>retard bus × congestion</strong> distingue un problème opérationnel d'un besoin d'infrastructure (voie dédiée) : un argument chiffré pour un arbitrage budgétaire.",
            "Projet porté seul de bout en bout : cadrage, données, modèles, déploiement, documentation RGPD.",
        ],
        tech=[
            "Medallion Bronze/Silver/Gold sur <strong>PostgreSQL 16 + PostGIS + pgRouting</strong>, SQL paramétré partout, zéro credential en dur.",
            "<strong>27 DAGs Airflow</strong> (collecte 5 min → 6 h, transforms, ML, maintenance), archivage MinIO S3.",
            "<strong>MLflow</strong> registry (6 modèles, stage Production), retrain XGBoost toutes les 30 min, drift <strong>PSI</strong> maison + rapports Evidently.",
            "CI GitHub Actions : ruff, mypy, bandit, pytest + couverture. Déploiement <code>make deploy-vps</code> / <code>rollback-vps</code>, 20 health checks.",
            "Observabilité Prometheus + Grafana + Alertmanager, Nginx seul point exposé, TLS Let's Encrypt.",
        ],
        stages=[
            ("Sources", "source", ["Boucles trafic Grand Lyon", "TCL SIRI Lite", "Vélo'v GBFS", "Open-Meteo + air", "TomTom · chantiers"]),
            ("Ingestion", "ingest", ["Airflow collect_bronze (*/5 min)", "Collecteurs DataCollector"]),
            ("Medallion", "storage", ["Bronze JSONB immuable", "Silver nettoyé", "Gold features + vues"]),
            ("ML", "ml", ["XGBoost vitesse H+1h", "XGBoost Vélo'v H+1h", "pgRouting Dijkstra"]),
            ("MLOps", "ops", ["MLflow registry", "Drift PSI + Evidently", "Prometheus · Grafana"]),
            ("Service", "serve", ["FastAPI (X-API-Key)", "Nginx + TLS", "Streamlit 3 personas"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
               ("s0n3", "s1n1", "", False), ("s0n4", "s1n1", "", False), ("s1n0", "s2n0", "", False),
               ("s1n1", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s2n2", "", False),
               ("s2n2", "s3n0", "features", False), ("s2n2", "s3n1", "", False), ("s2n2", "s3n2", "", False),
               ("s3n0", "s4n0", "log", True), ("s3n1", "s4n0", "", True), ("s4n1", "s3n0", "retrain", True),
               ("s3n0", "s5n0", "", False), ("s3n2", "s5n2", "", False), ("s5n0", "s5n1", "", False), ("s5n2", "s5n1", "", False)],
        band=("Docker Compose · GitHub Actions (ruff · mypy · bandit · pytest) · make deploy-vps / rollback-vps · backup nocturne", "infra"),
        steps=[
            "<strong>Collecte</strong> — 9 sources ouvertes sans clé, DAGs Airflow cadencés de 5 min (trafic, bus, Vélo'v) à 6 h (vigilance météo).",
            "<strong>Bronze</strong> — stockage brut JSONB immuable : on peut toujours rejouer l'historique.",
            "<strong>Silver</strong> — déduplication (<code>DISTINCT ON</code>), parsing SIRI, reprojection géographique (4326 / 2154), filtrage des capteurs défaillants.",
            "<strong>Gold</strong> — features ML (lags, moyennes glissantes, calendrier scolaire, météo) et vues matérialisées métier (goulots, retards par tronçon).",
            "<strong>Modélisation</strong> — XGBoost vitesse H+1h (inférence toutes les 15 min), XGBoost Vélo'v H+1h, routage voiture <code>pgr_dijkstra</code> sur le réseau OSM avec vitesses injectées.",
            "<strong>MLOps</strong> — suivi MLflow, comparaison continue aux données TomTom, rapport de dérive quotidien, réentraînement automatique.",
            "<strong>Restitution</strong> — API FastAPI (prédiction, recommandation, goulots) et dashboard Streamlit 18 pages / 59 widgets, sans aucune donnée simulée.",
        ],
        extra_diagrams=[("lyonflow-medallion", "Flux de données Medallion"), ("lyonflow-ml", "Les 4 piliers ML"),
                        ("lyonflow-infra", "Infrastructure de production (VPS, conteneurs)"),
                        ("lyonflow-airflow", "Orchestration Airflow")],
        langs=[("Python", 78), ("SQL", 13), ("Shell", 4), ("YAML", 3), ("Makefile", 1)],
        tags=["Airflow", "PostgreSQL", "PostGIS", "pgRouting", "XGBoost", "MLflow", "PSI / Evidently", "FastAPI",
              "Streamlit", "Docker", "Nginx", "Prometheus", "Grafana", "MinIO", "GitHub Actions", "RGPD"],
        stack=[
            ("Apache Airflow 2.9", "27 DAGs : collecte, transforms Medallion, entraînement, inférence, maintenance", "Orchestration de production, dépendances et reprises"),
            ("PostgreSQL 16 + PostGIS", "Schémas bronze / silver / gold / osm / rgpd", "Modélisation Medallion, SQL spatial, vues matérialisées"),
            ("pgRouting 3.7", "Itinéraire voiture sur ~101 k arêtes OSM", "Algorithmes de graphe dans la base"),
            ("XGBoost", "Vitesse trafic et disponibilité Vélo'v à H+1h", "Séries temporelles, features métier"),
            ("MLflow 2.12", "Tracking et registry de 6 modèles", "Cycle de vie des modèles"),
            ("PSI + Evidently", "Détection de dérive quotidienne", "Monitoring de modèles en production"),
            ("FastAPI", "API prédiction / recommandation, clé API", "Service de modèles"),
            ("Streamlit", "18 pages, 3 personas, rapport PDF élus", "Restitution orientée décision"),
            ("Docker · Nginx · systemd", "Stack conteneurisée, reverse proxy unique, TLS", "Déploiement et durcissement serveur"),
            ("Prometheus · Grafana · Alertmanager", "Métriques, tableaux de bord, 7 groupes d'alertes", "Observabilité"),
            ("MinIO", "Archivage S3 des données Silver", "Gestion du cycle de vie des données"),
            ("Databricks (variante)", "Delta Lake, DLT <code>expect_or_drop</code>, Unity Catalog, Asset Bundles", "Portabilité vers un lakehouse managé"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="y", monitoring="y", serving="y", deploy="y", iac="p"),
        matrix_notes=dict(ci="ruff, mypy, bandit, pytest + couverture", tests="620 tests (unitaires, personas, intégration, e2e)",
                          docker="Compose applicatif + compose monitoring", orch="Airflow, 27 DAGs (25 actifs)",
                          tracking="MLflow registry, stage Production", monitoring="PSI quotidien, Evidently, Prometheus/Grafana",
                          serving="FastAPI + clé API", deploy="VPS, deploy/rollback scriptés, health checks",
                          iac="Asset Bundle Databricks ; branche Kubernetes dormante"),
        metrics=dict(head=["Décision / mesure", "Résultat", "Source"], rows=[
            ["1 modèle unique (38 features) vs 3 modèles spécialisés", "MAE 5,8 → 3,2 (−45 %)", "validation interne (dépôt de travail privé)"],
            ["Benchmark exploratoire : comptages véhicules, split temporel 80/20, 5 modèles",
             "XGBoost optimisé : MAE 6,97 · R² 0,71 (régression linéaire : MAE 15,5)", "notebook 05, dépôt de travail privé"],
            ["Couverture réseau", "~458 stations Vélo'v · ~101 k arêtes OSM", "README / schémas du dépôt public"],
        ], note="Décision d'architecture clé : séparer trafic, bus et Vélo'v. Les features de capacité routière valent 0 pour les vélos : "
                "dans un modèle unique, elles ajoutent du bruit et dégradent la précision."),
        snippets=[
            ("src/monitoring/psi.py — dérive PSI robuste, sans dépendance lourde",
             '''def _safe_psi_term(pct_ref: float, pct_curr: float, eps: float = 1e-6) -> float:
    """Un terme de la somme PSI, protégé contre log(0) et division par 0."""
    if pct_ref < eps and pct_curr < eps:
        return 0.0
    if pct_curr < eps:
        pct_curr = eps
    if pct_ref < eps:
        pct_ref = eps
    return (pct_curr - pct_ref) * np.log(pct_curr / pct_ref)'''),
            ("Exploitation — déploiement et retour arrière en une commande",
             '''make check-deploy-env        # .deploy.env en chmod 600 + variables critiques
make deploy-vps              # rsync + restart systemd
./scripts/healthcheck-vps.sh  # 20+ checks : conteneurs, disque, DB, endpoints
make rollback-vps            # retour à la release précédente'''),
        ],
        limits=[
            "Serveur unique : pas de haute disponibilité. La cible Kubernetes (EKS/GKE) existe sur une branche dormante.",
            "Prédiction des retards bus encore en phase d'analyse : la donnée SIRI doit s'accumuler avant de passer en production.",
            "Sauvegarde hors site : configuration rclone à finaliser.",
            "Variante Databricks en cours : semaine 1 livrée (Unity Catalog, ingestion Bronze, DLT), MLflow / Model Serving / Genie à venir.",
        ],
    ),
    # ------------------------------------------------------------------ STRIPE
    dict(
        slug="stripe-fraude-temps-reel",
        short="Stripe — fraude temps réel",
        kicker="Data Architecture · Streaming · Bloc 2 RNCP 38777",
        title="Plateforme polyglotte de détection de fraude temps réel",
        title_html='Paiements : scorer la fraude <span class="highlight">en moins d\'une seconde</span>',
        lead="Architecture de données unifiée façon Stripe : PostgreSQL transactionnel, CDC Debezium vers Kafka, "
             "feature store Redis, MongoDB, entrepôt Snowflake — avec XGBoost, MLflow, dérive Evidently, "
             "réentraînement automatique et une cible AWS entièrement décrite en Terraform.",
        kpis=[("< 1 s", "cible de scoring"), ("5", "briques de données"), ("0,995", "ROC-AUC offline"),
              ("3 jobs", "CI de bout en bout"), ("9", "modules Terraform")],
        links=[("Code source", GH + "BLOC2-STRIPE", True)],
        context=[
            "<em>Étude de cas de certification inspirée de Stripe, sur données synthétiques — sans lien avec l'entreprise.</em>",
            "Une plateforme de paiement doit bloquer une transaction frauduleuse <strong>avant</strong> de la valider, "
            "sans ralentir la base transactionnelle et sans que les analyses ne bloquent la production. "
            "Elle doit aussi respecter RGPD et PCI-DSS.",
            "La réponse : séparer les usages. PostgreSQL pour la transaction, Debezium + Kafka pour diffuser les changements, "
            "Redis pour les features temps réel, MongoDB pour les journaux, Snowflake pour l'analytique — et un modèle surveillé "
            "qui se réentraîne quand la réalité change.",
        ],
        rh=[
            "Sujet à fort enjeu financier : chaque fraude manquée coûte, chaque faux positif <strong>bloque un client</strong>.",
            "Choix d'architecture justifiés et chiffrés, y compris le <strong>coût cloud (FinOps)</strong> : ~3 100 $/mois en prod, ramenés à ~2 400 $ avec les leviers identifiés.",
            "Conformité intégrée dès la conception : aucun numéro de carte stocké, empreintes SHA-256, rétention limitée des journaux.",
            "Incidents réels documentés et résolus — la preuve d'une posture d'exploitation, pas seulement de développement.",
        ],
        tech=[
            "<strong>CDC Debezium</strong> sur le WAL PostgreSQL → Kafka (KRaft), write-back idempotent du score.",
            "<strong>Feature store Redis</strong> (vélocité 1 h / 24 h en sorted sets) et même vecteur de features à l'entraînement et à l'inférence : zéro <em>training/serving skew</em>.",
            "Split <strong>temporel</strong> anti-fuite, XGBoost avec <code>scale_pos_weight</code>, MLflow registry <code>fraud-detector</code>.",
            "Moniteur Evidently : réentraînement automatique si dérive &gt; 0,3, rappel &lt; 0,7 ou précision &lt; 0,5, avec délai de carence.",
            "CI qui monte <strong>toute la stack</strong> sans mock + notebook d'audit exécuté comme porte qualité ; Terraform AWS (VPC 3 AZ, RDS, MSK, ElastiCache, ECS Fargate, MWAA).",
        ],
        stages=[
            ("Source", "source", ["Producteur transactions (5 tx/s)"]),
            ("OLTP", "storage", ["PostgreSQL 16 (3NF, ACID)"]),
            ("Streaming", "ingest", ["Debezium CDC (WAL)", "Kafka KRaft"]),
            ("Scoring", "ml", ["Redis feature store", "Scorer temps réel", "XGBoost / règles"]),
            ("MLOps", "ops", ["MLflow registry", "Evidently + retrain"]),
            ("Stockage", "storage", ["MongoDB (logs, alertes)", "Snowflake OLAP"]),
            ("Restitution", "ui", ["Streamlit (auth)", "Airflow ETL 02:00"]),
        ],
        edges=[("s0n0", "s1n0", "INSERT", False), ("s1n0", "s2n0", "WAL", False), ("s2n0", "s2n1", "", False),
               ("s2n1", "s3n1", "", False), ("s3n0", "s3n1", "", False), ("s3n1", "s3n2", "", False),
               ("s3n1", "s1n0", "write-back", True), ("s3n2", "s4n0", "", True), ("s4n1", "s4n0", "retrain", True),
               ("s2n1", "s5n0", "", False), ("s1n0", "s6n1", "", True), ("s6n1", "s5n1", "", True), ("s5n0", "s6n0", "", False)],
        band=("GitHub Actions : lint · terraform validate · e2e sur stack complète · Terraform AWS (VPC, RDS, MSK, ElastiCache, ECS, MWAA)", "infra"),
        steps=[
            "Un producteur insère des transactions synthétiques (5 % de fraude injectée) dans PostgreSQL 16, configuré en réplication logique.",
            "Debezium lit le journal WAL et publie chaque changement dans Kafka (<code>stripe.public.transactions</code>).",
            "Le scorer enrichit chaque transaction avec les vélocités client stockées dans Redis, puis la note (règles ou XGBoost) : autoriser, revoir (≥ 0,60) ou bloquer (≥ 0,85).",
            "Le score est réécrit de façon idempotente dans PostgreSQL ; les événements et alertes partent dans Kafka puis MongoDB.",
            "Le moniteur compare toutes les 2 minutes les données récentes à la référence (Evidently) et la performance réellement servie ; il relance l'entraînement si nécessaire.",
            "Chaque nuit, Airflow exporte vers le modèle en étoile Snowflake et rafraîchit les vues matérialisées.",
            "Le dashboard Streamlit (authentifié) expose KPIs, alertes, dérive et comparaison règles / modèle.",
        ],
        extra_diagrams=[("stripe-architecture", "Architecture de données unifiée (implémentation réelle)"),
                        ("stripe-aws", "Cible AWS (Terraform)")],
        langs=[("Python", 48), ("HCL (Terraform)", 27), ("SQL", 7), ("YAML", 7), ("Shell", 4), ("JavaScript", 3)],
        tags=["PostgreSQL", "Debezium", "Kafka", "Redis", "MongoDB", "Snowflake", "XGBoost", "MLflow", "Evidently",
              "Airflow", "Streamlit", "Terraform", "AWS", "Docker", "GitHub Actions", "PCI-DSS", "FinOps"],
        stack=[
            ("PostgreSQL 16", "OLTP 3NF, rôles séparés, fonction d'anonymisation RGPD", "Modélisation transactionnelle"),
            ("Debezium 2.6 + Kafka 7.6", "Change Data Capture, topics scores / alertes / dead-letter", "Architecture événementielle"),
            ("Redis 7", "Feature store en ligne (vélocités)", "Features temps réel à faible latence"),
            ("MongoDB 7", "Journaux avec TTL, alertes, features, monitoring", "Modélisation NoSQL"),
            ("Snowflake", "Schéma en étoile, CLUSTER BY", "Modélisation OLAP (exécuté en dry-run)"),
            ("XGBoost + scikit-learn", "Classifieur de fraude, 7 features partagées", "ML sur données déséquilibrées"),
            ("MLflow 2.14", "Tracking + registry", "Cycle de vie des modèles"),
            ("Evidently 0.4", "Dérive + déclenchement du réentraînement", "Monitoring et boucle fermée"),
            ("Airflow 2.9", "ETL quotidien vers l'OLAP", "Orchestration batch"),
            ("Terraform 1.10", "VPC, RDS Multi-AZ, MSK, ElastiCache, Atlas, ECS, MWAA, KMS", "Infrastructure as Code"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="y", monitoring="y", serving="p", deploy="p", iac="y"),
        matrix_notes=dict(ci="lint, terraform validate, e2e stack complète", tests="16 checks e2e + 13 tests ML + notebook d'audit",
                          docker="8 services + profils Flink / Airflow", orch="Airflow (batch) + Kafka (flux)",
                          tracking="MLflow, modèle enregistré fraud-detector", monitoring="Evidently + précision/rappel servis, retrain auto",
                          serving="Scoring par consommateur Kafka (pas d'API REST)", deploy="Local Docker ; cible AWS validée, non appliquée",
                          iac="Terraform AWS, envs dev / prod"),
        metrics=dict(head=["Run (15/09/2026)", "Déclencheur", "Précision", "Rappel", "F1", "ROC-AUC"], rows=[
            ["15:53", "make ml-train", "0,95", "0,97", "0,96", "0,995"],
            ["17:10", "automatique (dérive 0,43)", "0,77", "0,97", "0,86", "0,990"],
        ], note="Mesures offline sur hold-out temporel. Précision réellement servie autour du réentraînement : 0,93 à 0,99 par minute. "
                "Leçon documentée : juger un modèle réentraîné sur sa performance <strong>servie</strong>, pas seulement sur une métrique offline."),
        snippets=[
            ("ml/monitor.py — boucle fermée : dérive ou dégradation ⇒ réentraînement",
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
            ("ml/train_fraud_model.py — split temporel pour éviter la fuite d'information",
             '''def temporal_train_test_split(df, X, y, test_frac=0.2):
    """Split train/test par ordre chronologique (pas aléatoire).
    Un split aléatoire mélangerait les fenêtres de vélocité passé/futur :
    le modèle "verrait" indirectement des transactions futures."""
    n = len(df)
    cut = int(n * (1 - test_frac))
    return X[:cut], X[cut:], y[:cut], y[cut:]'''),
        ],
        limits=[
            "Flink remplacé par un consommateur Python équivalent (PyFlink ne compile pas sur ARM64) ; le job PyFlink existe en profil optionnel.",
            "Snowflake exécuté en dry-run faute de compte ; Terraform validé mais jamais appliqué.",
            "Pas encore de porte de promotion ni de rollback automatique dans le registry MLflow.",
            "Écart offline / online observé sur une fenêtre (précision servie 0,52) : signalé par le notebook d'audit lui-même, piste de calibration.",
        ],
    ),
    # ------------------------------------------------------------------ BLOC3
    dict(
        slug="detection-fraude",
        short="Détection de fraude automatisée",
        kicker="ML en production · Alerting · Bloc 3 RNCP 38777",
        title="Détection automatique de fraude bancaire",
        title_html='Fraude carte : <span class="highlight">alerter en temps réel</span>, reporter chaque matin',
        lead="Pipeline conteneurisé qui interroge un flux de paiements chaque minute, score chaque transaction avec XGBoost "
             "via une API FastAPI, alerte sur Telegram au-delà d'un seuil métier et produit un rapport quotidien automatique.",
        kpis=[("0,83", "rappel (fraudes détectées)"), ("0,989", "ROC-AUC"), ("1 min", "cadence d'ingestion"),
              ("6", "services Docker"), ("22", "tests pytest")],
        links=[("Code source", GH + "BLOC3-FRAUD-DETECTION", True), ("Version 1 (RandomForest + MLflow)", GH + "anonymisation", False)],
        context=[
            "La fraude à la carte dépasse le milliard d'euros par an en Europe (BCE, 2019). Les équipes fraude ont besoin "
            "de trois choses : être <strong>notifiées instantanément</strong>, disposer <strong>chaque matin</strong> d'un bilan de la veille "
            "et d'une prédiction servie en continu par une API.",
            "Le projet répond aux trois besoins avec une infrastructure reproductible en deux commandes.",
        ],
        rh=[
            "Traduction directe d'un besoin métier en service automatisé : <strong>alerte, rapport, API</strong>.",
            "Arbitrage assumé : privilégier le <strong>rappel</strong> (ne pas laisser passer la fraude), avec un seuil réglable par l'équipe métier sans redéploiement.",
            "Capacité à remettre en cause son propre travail : la V1 a été abandonnée après analyse critique (features non reproductibles en production).",
        ],
        tech=[
            "Airflow : DAG temps réel (<code>*/1 * * * *</code>) avec XCom et reprise, DAG rapport quotidien à 07:00.",
            "FastAPI : <code>/predict</code>, <code>/health</code>, clé API optionnelle, <strong>seuil métier</strong> par variable d'environnement, repli visible sur un scoreur de secours.",
            "10 features métier reproductibles à l'inférence (montant, heure, week-end, géolocalisation marchand…), XGBoost pondéré (<code>scale_pos_weight</code> ≈ 27).",
            "Docker Compose 6 services avec health checks ; PostgreSQL 15 via SQLAlchemy 2 ; alertes Telegram / SMTP.",
        ],
        stages=[
            ("Sources", "source", ["API paiements temps réel", "Kaggle fraudTest (repli)"]),
            ("Orchestration", "ingest", ["DAG fraud_realtime_ingest", "DAG daily_report 07:00"]),
            ("Scoring", "serve", ["FastAPI /predict", "XGBoost + seuil 0,7"]),
            ("Stockage", "storage", ["PostgreSQL 15"]),
            ("Action", "ui", ["Alerte Telegram / email", "Rapport HTML quotidien", "Dashboard Streamlit"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", True), ("s1n0", "s2n0", "POST", False),
               ("s2n0", "s2n1", "", False), ("s2n0", "s3n0", "insert", False), ("s2n1", "s4n0", "≥ seuil", False),
               ("s1n1", "s3n0", "J-1", True), ("s1n1", "s4n1", "", False), ("s3n0", "s4n2", "", False)],
        band=("Docker Compose (postgres · fraud-api · airflow init/scheduler/webserver · dashboard) · pytest", "infra"),
        steps=[
            "Chaque minute, Airflow récupère les transactions courantes (API publique, repli sur un fichier Kaggle avec curseur persistant).",
            "Chaque transaction est envoyée à l'API FastAPI, qui construit les 10 features métier et calcule la probabilité de fraude.",
            "Au-delà du seuil métier (0,7), une alerte part sur Telegram (et par e-mail en option) ; tous les résultats sont stockés dans PostgreSQL.",
            "À 07:00, un second DAG génère le rapport HTML des fraudes de la veille.",
            "Un dashboard Streamlit affiche KPIs, distribution des probabilités, carte et top 20 des transactions à risque.",
        ],
        extra_diagrams=[("fraude-pipeline", "Pipeline détaillé (entraînement, temps réel, rapport)")],
        langs=[("Python", 85), ("Shell", 8), ("HTML", 4), ("YAML", 3)],
        tags=["XGBoost", "FastAPI", "Airflow", "PostgreSQL", "SQLAlchemy", "Pydantic", "Streamlit", "Docker", "Telegram API", "pytest"],
        stack=[
            ("XGBoost", "Classifieur sur 10 features métier", "Gestion du déséquilibre de classes"),
            ("FastAPI + Pydantic", "API de scoring, validation des entrées", "Service de modèle robuste"),
            ("Airflow 2.9", "Ingestion minute + rapport quotidien", "Orchestration planifiée"),
            ("PostgreSQL 15 + SQLAlchemy 2", "Historique des prédictions", "Persistance et requêtage"),
            ("Telegram Bot API / SMTP", "Notifications de fraude", "Boucler avec l'utilisateur métier"),
            ("Streamlit + Plotly", "Suivi en temps réel", "Restitution"),
            ("MLflow (V1)", "Tracking de la version RandomForest", "Suivi d'expériences"),
        ],
        matrix=dict(ci="n", tests="y", docker="y", orch="y", tracking="p", monitoring="n", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(tests="22 tests (API, rapport) ; 47 dans la V1", docker="Compose 6 services + health checks",
                          orch="2 DAGs Airflow", tracking="MLflow dans la V1, fichier de métriques en V2",
                          monitoring="Grafana + dérive prévus", serving="FastAPI", deploy="Reproductible localement en 2 commandes"),
        metrics=dict(head=["Modèle", "Rappel", "Précision", "F1", "ROC-AUC"], rows=[
            ["XGBoost features métier (V2, seuil 0,5)", "0,831", "0,373", "0,515", "0,989"],
            ["RandomForest features PCA (V1, abandonné)", "0,78", "0,88", "—", "—"],
        ], note="La V1 affichait une meilleure précision mais reposait sur des features PCA impossibles à reconstruire en production : "
                "ses probabilités plafonnaient à ~0,37 et elle ne détectait aucune fraude réelle. La V2 privilégie un modèle réellement servable."),
        snippets=[
            ("api/main.py — seuil métier au-dessus de la probabilité, repli explicite",
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
            "Précision modérée (0,37 au seuil 0,5) : calibration des probabilités (<code>CalibratedClassifierCV</code>) et entraînement sur les 555 k lignes prévus.",
            "Pas encore de CI ni de monitoring de dérive (Grafana + DAG de réentraînement mensuel planifiés).",
            "Le modèle n'est pas versionné dans le dépôt : un clone neuf sert le scoreur de secours tant que l'entraînement n'a pas été lancé.",
        ],
    ),
    # ------------------------------------------------------------------ RAG
    dict(
        slug="copilot-maintenance",
        short="Copilote maintenance (RAG local)",
        kicker="IA générative · RAG · LLM local",
        title="Industrial Knowledge Copilot — RAG 100 % local",
        title_html='Un copilote IA pour la maintenance, <span class="highlight">sans qu\'aucune donnée ne sorte</span>',
        lead="Assistant question-réponse sur 5 105 pages de catalogues techniques de roulements (Schaeffler, SKF, NTN-SNR, GGB) : "
             "recherche hybride dense + BM25, LLM Qwen2.5-7B exécuté localement via MLX, évaluation RAGAS et API instrumentée.",
        kpis=[("5 105", "pages indexées"), ("13", "catalogues PDF"), ("141", "tests"), ("0", "donnée envoyée au cloud")],
        links=[("Code source", GH + "maintenance", True)],
        context=[
            "Un technicien de maintenance perd du temps à chercher une tolérance, un couple de serrage ou une référence "
            "dans des catalogues de plusieurs centaines de pages. Les assistants IA en ligne posent un problème de "
            "<strong>confidentialité industrielle</strong>.",
            "Ce copilote répond en français ou en anglais, <strong>cite ses sources</strong> (catalogue et page) et tourne entièrement "
            "sur un poste Apple Silicon, sans clé API.",
        ],
        rh=[
            "IA générative appliquée à un vrai irritant terrain, issu de 20 ans en distribution industrielle.",
            "<strong>Confidentialité by design</strong> : aucune donnée ne quitte la machine, transparence documentée au sens de l'AI Act.",
            "Réponses sourcées et vérifiables : la confiance de l'utilisateur métier passe avant l'effet démo.",
        ],
        tech=[
            "Ingestion PyMuPDF → chunks de 500 tokens (overlap 50) → embeddings multilingues <strong>bge-m3</strong> (1024 dim) → ChromaDB.",
            "<strong>Recherche hybride</strong> dense + BM25 fusionnée par Reciprocal Rank Fusion, reranker cross-encoder optionnel.",
            "Génération Qwen2.5-7B-Instruct 4 bits via <strong>MLX</strong> (Metal), chaîne LangChain LCEL, prompts FR/EN, timeout 504 maîtrisé.",
            "FastAPI versionnée <code>/v1</code>, métriques Prometheus, logs JSON ; CI Ubuntu + macOS, tests d'intégration ChromaDB, CodeQL.",
        ],
        stages=[
            ("Sources", "source", ["13 catalogues PDF"]),
            ("Ingestion", "ingest", ["PyMuPDF", "Chunker 500/50"]),
            ("Indexation", "storage", ["bge-m3 embeddings", "ChromaDB", "Index BM25"]),
            ("Recherche", "process", ["Hybride RRF", "Reranker cross-encoder"]),
            ("Génération", "ml", ["Qwen2.5-7B (MLX)", "Chaîne LCEL"]),
            ("Service", "serve", ["FastAPI /v1/query", "Streamlit (chat + sources)", "/metrics Prometheus"]),
            ("Évaluation", "ops", ["RAGAS"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
               ("s2n0", "s2n1", "", False), ("s1n1", "s2n2", "", True), ("s2n1", "s3n0", "dense", False),
               ("s2n2", "s3n0", "sparse", False), ("s3n0", "s3n1", "", False), ("s3n1", "s4n1", "contexte", False),
               ("s4n0", "s4n1", "", False), ("s4n1", "s5n0", "", False), ("s5n1", "s5n0", "", False),
               ("s5n0", "s5n2", "", True), ("s6n0", "s4n1", "évalue", True)],
        band=("GitHub Actions (Ubuntu + macOS) · tests d'intégration ChromaDB · CodeQL · Docker multi-stage non-root", "infra"),
        steps=[
            "Les PDF sont lus page par page (numérotation conservée pour la citation) et découpés en chunks avec recouvrement.",
            "Chaque chunk est vectorisé par bge-m3 (multilingue) et stocké dans ChromaDB ; un index BM25 lexical est construit en parallèle.",
            "À chaque question, les deux recherches sont fusionnées par RRF (robuste aux échelles de score différentes), puis rerankées.",
            "Le LLM local génère une réponse ancrée dans le contexte, avec citation du catalogue et de la page.",
            "RAGAS mesure fidélité, pertinence, précision et rappel du contexte ; chaque évaluation est figée en snapshot horodaté.",
        ],
        extra_diagrams=[],
        langs=[("Python", 74), ("HTML", 10), ("CSS", 7), ("Shell", 3), ("YAML", 2), ("Makefile", 2)],
        tags=["RAG", "LLM", "MLX", "Qwen2.5", "bge-m3", "ChromaDB", "BM25", "LangChain", "RAGAS", "FastAPI",
              "Streamlit", "Prometheus", "CodeQL", "Docker"],
        stack=[
            ("MLX + Qwen2.5-7B-Instruct 4-bit", "Génération locale sur GPU Apple", "LLM on-device, sans API"),
            ("bge-m3 (sentence-transformers)", "Embeddings FR/EN 1024 dim", "Recherche sémantique multilingue"),
            ("ChromaDB", "Base vectorielle", "Stockage vectoriel"),
            ("rank-bm25 + RRF", "Recherche lexicale et fusion", "Retrieval hybride"),
            ("ms-marco-MiniLM", "Reranking cross-encoder", "Précision du top-k"),
            ("LangChain LCEL", "Chaîne retriever → prompt → LLM", "Orchestration LLM"),
            ("RAGAS", "Évaluation qualité RAG", "Mesurer au lieu de supposer"),
            ("FastAPI + Prometheus", "API versionnée, compteurs et histogrammes de latence", "Service instrumenté"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="n", tracking="p", monitoring="y", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(ci="lint + tests 2 OS, intégration, CodeQL", tests="141 tests", docker="API multi-stage non-root, ChromaDB en compose",
                          tracking="Snapshots d'évaluation RAGAS horodatés", monitoring="/metrics Prometheus, logs JSON",
                          serving="FastAPI /query /ingest /eval", deploy="Poste local (MLX nécessite Metal)"),
        snippets=[
            ("src/rag/retriever.py — fusion Reciprocal Rank Fusion dense + BM25",
             '''rrf_contrib = 1.0 / (_RRF_K0 + rank + 1)
if cid in chunk_map:
    chunk_map[cid]["rrf"] += rrf_contrib
    if chunk_map[cid]["chunk"].retrieval_method == "dense":
        chunk_map[cid]["chunk"].retrieval_method = "rrf"'''),
        ],
        limits=[
            "Scores RAGAS de référence encore à publier : le jeu de questions / réponses est prêt, les runs mesurés restent à figer.",
            "Agent à appels d'outils retiré (comparaison Qwen / Mistral peu concluante) au profit d'une chaîne RAG plus fiable.",
            "Déploiement limité à Apple Silicon (MLX) ; une variante vLLM / llama.cpp permettrait un serveur Linux.",
        ],
    ),
    # ------------------------------------------------------------------ MLINDUSTRIAL
    dict(
        slug="maintenance-predictive",
        short="Maintenance prédictive vibratoire",
        kicker="ML industriel · Signal · Jumeau numérique",
        title="Maintenance prédictive — diagnostic de roulements",
        title_html='Du labo à l\'atelier : <span class="highlight">détecter un roulement qui lâche</span>',
        lead="Détection de défauts de roulements sur le jeu de données Paderborn (32 roulements, 4 régimes) à partir de "
             "features physiques explicables, avec une question clé : un modèle entraîné sur des défauts artificiels "
             "tient-il sur des défauts réels ?",
        kpis=[("189", "tests"), ("0,738", "F1 macro XGBoost"), ("5,4 Go", "signaux bruts"), ("5 folds", "CV groupée par actif")],
        links=[("Code source", GH + "MLindustrial", True)],
        context=[
            "La plupart des démonstrations de maintenance prédictive testent un modèle sur les mêmes roulements que ceux "
            "vus à l'entraînement : les scores sont flatteurs et ne tiennent pas en atelier.",
            "Ce projet mesure honnêtement l'écart laboratoire / terrain, compare un capteur vibratoire au <strong>courant moteur "
            "déjà disponible sur chaque variateur</strong> (aucun capteur à ajouter) et privilégie des indicateurs qu'un responsable "
            "maintenance comprend.",
        ],
        rh=[
            "Expertise métier réelle (déploiements terrain IFM, Schaeffler, SKF) mise au service de la data.",
            "Raisonnement <strong>coût capteur / valeur</strong> : peut-on éviter d'instrumenter une machine ?",
            "Résultats négatifs publiés tels quels : la rigueur prime sur l'affichage.",
        ],
        tech=[
            "Features physiques : RMS, kurtosis, facteur de crête et <strong>fréquences de défaut BPFO / BPFI / BSF / FTF</strong> calculées depuis la géométrie.",
            "Splits par actif / condition / artificiel→réel, <code>StratifiedGroupKFold</code> et garde-fou <code>assert_no_asset_leakage</code>.",
            "TimescaleDB (hypertable features), MLflow adossé à PostgreSQL, hash du dataset pour la traçabilité, dérive Evidently.",
            "CI : matrice Python 3.11 / 3.12, audit « zéro mock », pipeline ML complet sur données réelles avec artefacts MLflow.",
            "Simulateurs physiques, simulation d'usine SimPy et export Asset Administration Shell (Industrie 4.0).",
        ],
        stages=[
            ("Source", "source", ["Paderborn .mat (5,4 Go)"]),
            ("Ingestion", "ingest", ["Loaders + contrôles physiques", "Parquet"]),
            ("Stockage", "storage", ["TimescaleDB (hypertable)"]),
            ("Features", "process", ["Temporel : RMS, kurtosis", "Fréquences BPFO/BPFI"]),
            ("Modèles", "ml", ["Seuils (baseline)", "XGBoost", "CV groupée par actif"]),
            ("Suivi", "ops", ["MLflow (Postgres)", "Evidently dérive"]),
            ("Restitution", "ui", ["Streamlit jumeau numérique", "Export AAS"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
               ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False), ("s3n0", "s4n0", "", False),
               ("s3n1", "s4n1", "", False), ("s4n2", "s4n1", "", True), ("s4n1", "s5n0", "log", False),
               ("s4n0", "s5n0", "", False), ("s5n1", "s6n0", "", True), ("s4n1", "s6n0", "", False), ("s6n0", "s6n1", "", True)],
        band=("uv · GitHub Actions (ruff, pytest, audit zéro mock, pipeline ML sur données réelles) · Docker Compose", "infra"),
        steps=[
            "Téléchargement des signaux Paderborn, parsing des noms de fichiers (roulement, régime, défaut) et contrôles de plausibilité physique.",
            "Stockage hiérarchique site → zone → machine → actif → roulement dans TimescaleDB.",
            "Calcul des indicateurs temporels et des fréquences caractéristiques de défaut à partir de la géométrie du roulement.",
            "Comparaison d'une baseline à seuils et de XGBoost, avec validation croisée groupée par actif (aucun roulement à la fois en train et en test).",
            "Suivi MLflow (hash du dataset, F1 macro, balanced accuracy) et rapport de dérive Evidently train / test.",
            "Restitution Streamlit : alertes, spectres, jumeau numérique d'usine, glossaire.",
        ],
        extra_diagrams=[],
        langs=[("Python", 84), ("YAML", 15), ("TOML", 1)],
        tags=["Signal processing", "SciPy", "XGBoost", "scikit-learn", "TimescaleDB", "MLflow", "Evidently", "Polars",
              "Streamlit", "SimPy", "uv", "Docker", "GitHub Actions", "Industrie 4.0"],
        stack=[
            ("NumPy / SciPy", "Traitement du signal, spectres, enveloppe", "Features physiques explicables"),
            ("XGBoost / scikit-learn", "Classification des défauts", "ML sur données industrielles"),
            ("TimescaleDB", "Séries temporelles, hypertable des features", "Stockage adapté aux capteurs"),
            ("MLflow", "Expériences baseline vs GBM, hash du dataset", "Traçabilité et reproductibilité"),
            ("Evidently", "Dérive train / test (KS)", "Détection de changement de distribution"),
            ("SimPy", "Simulation d'usine à événements discrets", "Jumeau numérique"),
            ("uv + ruff + pytest", "Gestion des dépendances, qualité", "Hygiène d'ingénierie"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="n", tracking="y", monitoring="y", serving="n", deploy="p", iac="n"),
        matrix_notes=dict(ci="CI + pipeline ML + releases taguées", tests="189 tests dont anti-fuite", docker="db, mlflow, app, dashboard",
                          tracking="MLflow adossé à PostgreSQL", monitoring="Evidently + dérive temporelle", deploy="Releases GitHub"),
        metrics=dict(head=["Modèle (CV 5 folds groupée par actif)", "F1 macro"], rows=[
            ["Seuil kurtosis", "0,682 ± 0,158"],
            ["Seuil facteur de crête", "0,576 ± 0,174"],
            ["XGBoost vibration (5 features)", "0,738 ± 0,208"],
            ["XGBoost vibration + courant (15 features)", "0,726 ± 0,222"],
            ["XGBoost courant seul (10 features)", "0,542 ± 0,121"],
        ], note="Conclusion honnête : à ce stade, XGBoost ne bat pas nettement une règle simple sur le kurtosis (intervalles qui se chevauchent). "
                "La phase 3 (entraînement sur défauts artificiels, test sur défauts réels) est la prochaine mesure."),
        snippets=[
            ("src/features/fault_frequencies.py — physique du roulement",
             '''def bpfo(n_balls, fr_hz, d_mm, big_d_mm, phi_deg=0.0):
    """Ball Pass Frequency Outer race - defaut bague exterieure."""
    return (n_balls / 2) * fr_hz * (1 - _geometry_factor(d_mm, big_d_mm, phi_deg))'''),
            ("src/data/splits.py — garde-fou contre la fuite entre train et test",
             '''def assert_no_asset_leakage(train_df, test_df, asset_col="asset_id"):
    leaked = set(train_df[asset_col]) & set(test_df[asset_col])
    if leaked:
        raise ValueError(f"Fuite de donnees : assets presents dans train ET test : {leaked}")'''),
        ],
        limits=[
            "Phase 3 (artificiel → réel) non encore exécutée : c'est la mesure qui validera l'intérêt terrain.",
            "Analyse d'enveloppe / kurtogramme désactivée tant qu'elle n'est pas stable.",
            "Pas d'API d'inférence : le livrable actuel est l'étude et le dashboard.",
        ],
    ),
    # ------------------------------------------------------------------ HVAC
    dict(
        slug="marche-hvac",
        short="Marché HVAC France",
        kicker="Data Engineering · Prévision · Énergie",
        title="Marché HVAC — prévision des installations de pompes à chaleur",
        title_html='Anticiper le marché des <span class="highlight">pompes à chaleur</span>, département par département',
        lead="Pipeline complet de l'open data à la prédiction : 5 collecteurs (ADEME DPE, Open-Meteo, INSEE, Eurostat, SITADEL), "
             "entrepôt en étoile, benchmark Ridge / LightGBM / Prophet / LSTM, API FastAPI, dashboard, Airflow et Kubernetes.",
        kpis=[("96", "départements"), ("5", "sources open data"), ("562", "tests"), ("5", "familles de modèles")],
        links=[("Code source", GH + "Projet-HVAC", True)],
        context=[
            "Pour un distributeur HVAC, savoir où et quand le marché des pompes à chaleur va accélérer conditionne stocks, "
            "force commerciale et partenariats installateurs. Les signaux existent (diagnostics énergétiques, permis de construire, "
            "météo, conjoncture) mais sont dispersés.",
            "Le projet les réunit chaque mois dans un pipeline reproductible et restitue une prévision par département.",
        ],
        rh=[
            "Sujet choisi dans <strong>mon secteur</strong> : les variables (MaPrimeRénov', CEE, type de logement) viennent de la connaissance terrain.",
            "Livrable exploitable par une direction commerciale : carte de France, prévisions, comparaison de modèles.",
            "Gouvernance documentée (RGPD, AI Act).",
        ],
        tech=[
            "Collecteurs en <strong>architecture plugin</strong> (<code>BaseCollector</code> + registre), sans clé API.",
            "Schéma en étoile SQLAlchemy (SQLite, PostgreSQL 16 ou SQL Server), détection d'outliers IQR / Z-score / Isolation Forest.",
            "Split temporel train / validation / test + <code>TimeSeriesSplit</code> ; explicabilité SHAP.",
            "FastAPI 6 endpoints, Streamlit 6 pages, Docker multi-stage non-root, DAG Airflow mensuel <strong>et</strong> CronJob Kubernetes équivalent.",
            "CI : pytest 3.11 / 3.12 avec couverture, ruff, build + smoke test Docker.",
        ],
        stages=[
            ("Sources", "source", ["ADEME DPE", "Open-Meteo", "INSEE · Eurostat", "SITADEL permis"]),
            ("Collecte", "ingest", ["Collecteurs plugin"]),
            ("Stockage", "storage", ["Data lake CSV", "Schéma en étoile SQL"]),
            ("Préparation", "process", ["Nettoyage + outliers", "Feature engineering"]),
            ("Modèles", "ml", ["Ridge · LightGBM", "Prophet · LSTM", "SHAP"]),
            ("Service", "serve", ["FastAPI", "Streamlit 6 pages"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False), ("s0n3", "s1n0", "", False),
               ("s1n0", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s3n0", "", False), ("s3n0", "s3n1", "", False),
               ("s3n1", "s4n0", "", False), ("s3n1", "s4n1", "", False), ("s4n1", "s4n2", "", True), ("s4n0", "s5n0", "pkl", False),
               ("s5n0", "s5n1", "", False)],
        band=("Airflow DAG mensuel (0 6 1 * *) ⇄ CronJob Kubernetes · Docker · GitHub Actions (pytest, ruff, smoke Docker) · Render", "infra"),
        steps=[
            "Le 1er de chaque mois, Airflow (ou le CronJob Kubernetes) lance les collecteurs sur les 96 départements.",
            "Les données brutes sont nettoyées, fusionnées et chargées dans un schéma en étoile ; les valeurs aberrantes sont détectées par trois méthodes.",
            "Le feature engineering produit lags, moyennes et écarts glissants à 3 et 6 mois.",
            "Cinq familles de modèles sont entraînées sur un découpage temporel, puis expliquées avec SHAP.",
            "Les modèles sont servis par FastAPI et visualisés dans un dashboard Streamlit (carte de France, prévisions, comparatif).",
        ],
        extra_diagrams=[],
        langs=[("Python", 94), ("SQL", 2), ("YAML", 2), ("Shell", 1), ("Makefile", 1)],
        tags=["Open data", "ETL", "SQLAlchemy", "LightGBM", "Prophet", "PyTorch LSTM", "SHAP", "FastAPI", "Streamlit",
              "Airflow", "Kubernetes", "Docker", "GitHub Actions"],
        stack=[
            ("requests / eurostat", "Collecte de 5 API publiques", "Ingestion multi-sources"),
            ("SQLAlchemy", "Schéma en étoile multi-SGBD", "Modélisation décisionnelle"),
            ("scikit-learn · LightGBM · Prophet · PyTorch", "Benchmark de 5 approches", "Choix de modèle argumenté"),
            ("SHAP", "Importance des variables", "Explicabilité pour le métier"),
            ("FastAPI + Streamlit", "API et dashboard", "Mise à disposition"),
            ("Airflow + Kubernetes CronJob", "Rafraîchissement mensuel", "Deux modes d'orchestration"),
            ("Docker multi-stage", "Images non-root, health checks", "Conteneurisation propre"),
        ],
        matrix=dict(ci="y", tests="y", docker="y", orch="y", tracking="n", monitoring="n", serving="y", deploy="p", iac="y"),
        matrix_notes=dict(ci="pytest 2 versions + couverture, ruff, smoke Docker", tests="562 tests",
                          docker="Multi-stage, non-root", orch="Airflow + CronJob K8s", tracking="Métriques en CSV/JSON (pas de MLflow)",
                          serving="FastAPI 6 endpoints", deploy="Blueprint Render", iac="Manifests Kubernetes (Deployment, Ingress, PVC, CronJob)"),
        snippets=[
            ("kubernetes/cronjob-pipeline.yaml — le DAG Airflow, version native Kubernetes",
             '''apiVersion: batch/v1
kind: CronJob
metadata:
  name: hvac-pipeline-monthly
spec:
  schedule: "0 6 1 * *"    # 1er du mois a 6h UTC
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 2
      activeDeadlineSeconds: 7200'''),
        ],
        limits=[
            "Audit post-projet : certaines moyennes glissantes incluent le mois courant de la cible, ce qui surestime les scores. "
            "Correctif identifié (décalage d'un mois) ; les métriques seront republiées après re-benchmark.",
            "Pas de tracking MLflow ni de suivi de dérive : prochaine brique à ajouter.",
        ],
    ),
    # ------------------------------------------------------------------ CARRIER
    dict(
        slug="carrier-reporting",
        short="Carrier — Reporting HVAC Europe",
        kicker="Expérience professionnelle · Impact mesurable",
        title="Reporting & analyse Master Data — Carrier",
        title_html='Carrier : <span class="highlight">−40 % de temps de traitement</span>, 100 K€/mois d\'erreurs détectées',
        lead="Dashboards Power BI Master Data & Business HVAC Europe : flux unifié depuis 5 sources SAP, détection d'anomalies "
             "critiques, automatisation Power Query et pilotage à l'échelle européenne, en contexte international FR/EN.",
        kpis=[("−40 %", "temps de traitement"), ("100 K€/mois", "erreurs détectées"), ("5", "sources SAP unifiées"), ("10 mois", "stage + CDD")],
        links=[],
        context=[
            "Dans un groupe industriel international, la qualité des données de référence (articles, prix, clients) conditionne "
            "la facturation, la marge et la relation client. Les erreurs sont coûteuses et souvent invisibles.",
            "Mission : unifier les extractions SAP, fiabiliser les données de référence et donner aux équipes européennes "
            "des tableaux de bord de pilotage.",
        ],
        rh=[
            "<strong>Impact chiffré</strong> : −40 % de temps de traitement et environ 100 K€ d'erreurs détectées chaque mois.",
            "Contexte <strong>international</strong> (FR/EN), équipes Customer Care et Master Data européennes.",
            "Double compétence mise en pratique : compréhension métier HVAC + outillage data.",
        ],
        tech=[
            "Modèle sémantique Power BI multi-sources SAP, mesures DAX de contrôle qualité.",
            "Automatisation des traitements récurrents avec Power Query et VBA.",
            "Règles de détection d'anomalies sur les données de référence.",
        ],
        stages=[
            ("Sources", "source", ["5 extractions SAP"]),
            ("Préparation", "ingest", ["Power Query (M)"]),
            ("Modèle", "storage", ["Modèle sémantique Power BI"]),
            ("Contrôles", "process", ["Mesures DAX", "Règles d'anomalies"]),
            ("Pilotage", "ui", ["Dashboards Master Data", "Dashboards Business HVAC"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s1n0", "s2n0", "", False), ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False),
               ("s3n0", "s4n1", "", False), ("s3n1", "s4n0", "", False)],
        band=None,
        steps=[
            "Consolidation de 5 sources SAP en un flux unique via Power Query.",
            "Modélisation sémantique et mesures DAX de pilotage et de contrôle.",
            "Détection des anomalies de données de référence et remontée aux équipes concernées.",
            "Diffusion de dashboards Master Data et Business HVAC à l'échelle européenne.",
        ],
        extra_diagrams=[],
        langs=None,
        langs_note="Projet réalisé en entreprise : code non public.",
        tags=["Power BI", "DAX", "Power Query", "SAP", "Excel VBA", "Master Data", "Data Quality"],
        stack=[
            ("Power BI", "Modèle sémantique et dashboards", "Restitution pour les décideurs"),
            ("DAX", "Mesures de pilotage et de contrôle", "Logique analytique"),
            ("Power Query", "Consolidation de 5 sources SAP", "Automatisation de la préparation"),
            ("SAP", "Données de référence et transactions", "Maîtrise des ERP"),
            ("Excel VBA", "Automatisation de tâches récurrentes", "Gain de productivité"),
        ],
        matrix=None,
        limits=[
            "Données et code confidentiels : cette page décrit la démarche sans exposer d'information interne.",
        ],
    ),
    # ------------------------------------------------------------------ CSV
    dict(
        slug="csvtraitement",
        short="Csvtraitement",
        kicker="Outil Python · Qualité de données ERP",
        title="Csvtraitement — réparer les exports ERP",
        title_html='Des exports ERP <span class="highlight">propres</span>, même à 500 000 lignes',
        lead="Application Python (interface graphique + CLI) qui détecte et corrige les défauts des exports ERP : colonnes décalées, "
             "formats décimaux FR/US mélangés, dates invalides, doublons, données personnelles — avec validation humaine avant export.",
        kpis=[("500 K+", "lignes traitées"), ("59", "tests"), ("6", "formats lus / écrits"), ("A→F", "score qualité")],
        links=[("Code source", GH + "Csvtraitement", True)],
        context=[
            "Tout analyste qui travaille avec SAP connaît le problème : un export CSV avec une colonne décalée, des montants "
            "« 1.234,56 » et « 1,234.56 » mélangés, des dates <code>00.00.0000</code> ou des <code>#REF!</code>. "
            "Le nettoyage manuel prend des heures et reste source d'erreurs.",
            "Csvtraitement automatise la détection, propose les corrections, et laisse l'utilisateur valider avant d'exporter.",
        ],
        rh=[
            "Né d'un irritant vécu au quotidien sur des extractions SAP.",
            "Gain de temps direct pour les équipes Achats, ADV, contrôle de gestion.",
            "Humain dans la boucle : aucune correction n'est appliquée sans validation.",
        ],
        tech=[
            "Lecture en <strong>streaming par blocs de 10 000 lignes</strong> ; Parquet lu en <code>iter_batches</code> : pas de saturation mémoire.",
            "Détection automatique de l'encodage et du séparateur (score moyenne / (1 + écart-type)), typage de colonnes sur échantillon.",
            "Doublons exacts et approchés (<code>SequenceMatcher</code> &gt; 85 % avec blocage par préfixe), réconciliation de fichiers, masquage de données personnelles (e-mail, téléphone, IBAN, NIR).",
            "Interface Tkinter 8 onglets, CLI batch, undo / redo, 27 modules journalisés, type hints et docstrings.",
        ],
        stages=[
            ("Entrée", "source", ["CSV · XLSX · ODS", "JSON · Parquet"]),
            ("Détection", "ingest", ["Encodage + séparateur", "Profilage 9 types"]),
            ("Analyse", "process", ["Décalages de colonnes", "Score qualité A→F", "Doublons exacts / flous"]),
            ("Correction", "ml", ["Dates, décimales FR/US", "Masquage PII"]),
            ("Validation", "ui", ["Revue humaine (GUI / CLI)"]),
            ("Export", "serve", ["XLSX annoté + rapport", "CSV · Parquet"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s1n0", "s1n1", "", False),
               ("s1n1", "s2n0", "", False), ("s1n1", "s2n1", "", False), ("s1n1", "s2n2", "", False),
               ("s2n0", "s3n0", "", False), ("s2n2", "s3n1", "", False), ("s3n0", "s4n0", "", False),
               ("s3n1", "s4n0", "", False), ("s4n0", "s5n0", "", False), ("s4n0", "s5n1", "", False)],
        band=("Traitement en streaming (blocs de 10 000 lignes) · pytest · logging", "infra"),
        steps=[
            "Lecture de n'importe quel format tabulaire, converti en flux CSV traité par blocs.",
            "Détection de l'encodage, du séparateur et du type de chaque colonne sur un échantillon représentatif.",
            "Repérage cellule par cellule des décalages de colonnes, calcul d'un score qualité pondéré, recherche de doublons.",
            "Proposition de corrections (dates, décimales, parenthèses comptables, réalignement) et masquage optionnel des données personnelles.",
            "Validation par l'utilisateur, puis export XLSX avec cellules corrigées surlignées et feuille de rapport.",
        ],
        extra_diagrams=[],
        langs=[("Python", 100)],
        tags=["Python", "Tkinter", "CLI", "Streaming", "Data Quality", "chardet", "xlsxwriter", "pyarrow", "pytest"],
        stack=[
            ("Python standard library", "csv, difflib, statistics, argparse, logging", "Solide sans dépendances lourdes"),
            ("chardet", "Détection d'encodage", "Robustesse aux exports hétérogènes"),
            ("xlsxwriter (constant_memory)", "Export Excel annoté", "Gros volumes sans saturation mémoire"),
            ("pyarrow", "Lecture / écriture Parquet", "Interopérabilité data"),
            ("Tkinter", "Interface graphique 8 onglets", "Outil utilisable par un non-développeur"),
            ("pytest", "59 tests sur détection, analyse, correction", "Fiabilité du cœur métier"),
        ],
        matrix=dict(ci="n", tests="y", docker="n", orch="n", tracking="n", monitoring="n", serving="n", deploy="p", iac="n"),
        matrix_notes=dict(tests="59 tests (détecteur, analyseur, correcteur)", deploy="Paquet installable + lanceur Windows"),
        snippets=[
            ("core/detector.py — le séparateur le plus régulier gagne",
             '''for sep in CANDIDATE_SEPARATORS:
    counts = [line.count(sep) for line in lines]

    # Ignorer si jamais présent
    if max(counts) == 0:
        continue

    avg_count = mean(counts)
    std_count = stdev(counts) if len(counts) > 1 else 0.0'''),
        ],
        limits=[
            "Pas encore de CI GitHub Actions ni d'image Docker.",
            "Couverture de tests concentrée sur le cœur (détection, analyse, correction) ; modules annexes à couvrir.",
        ],
    ),
    # ------------------------------------------------------------------ MCP
    dict(
        slug="mcp-open-data",
        short="Serveurs MCP open data",
        kicker="IA agentique · Model Context Protocol",
        title="Serveurs MCP pour l'open data français",
        title_html='Brancher un LLM sur <span class="highlight">l\'open data public</span>',
        lead="Deux serveurs Model Context Protocol qui permettent à un assistant IA (Claude Desktop, par exemple) d'interroger "
             "data.gouv.fr et data.grandlyon.com, y compris les couches géographiques WFS.",
        kpis=[("11", "outils exposés"), ("2", "portails open data"), ("stdio", "transport MCP")],
        links=[],
        context=[
            "Les LLM sont puissants mais ne connaissent pas les données publiques à jour. Le Model Context Protocol "
            "standardise la façon de leur donner des outils.",
            "Ces serveurs transforment les API de data.gouv.fr et du Grand Lyon en outils utilisables en langage naturel : "
            "« trouve les jeux de données sur la qualité de l'air à Lyon et montre-moi les 10 premières stations ».",
        ],
        rh=[
            "Veille active sur l'<strong>IA agentique</strong> : MCP est le standard émergent pour connecter les assistants aux données d'entreprise.",
            "Même principe transposable à un ERP ou un entrepôt interne.",
        ],
        tech=[
            "SDK <code>mcp</code> bas niveau : handlers <code>list_tools</code> / <code>call_tool</code>, transport stdio.",
            "data.gouv.fr : 6 outils (recherche et détail de jeux de données, ressources, organisations, nouveautés).",
            "Grand Lyon : 5 outils dont <strong>WFS 2.0 GetFeature</strong> avec filtre CQL, liste des couches, schéma d'une couche.",
            "Client httpx avec timeout, erreurs HTTP renvoyées proprement au LLM ; un Dockerfile par serveur.",
        ],
        stages=[
            ("Client", "ui", ["Assistant IA (client MCP)"]),
            ("Transport", "ingest", ["stdio"]),
            ("Serveurs", "serve", ["mcp-data-gouv (6 outils)", "mcp-data-lyon (5 outils)"]),
            ("API", "source", ["data.gouv.fr API v1", "Grand Lyon datapusher + WFS"]),
        ],
        edges=[("s0n0", "s1n0", "tool call", False), ("s1n0", "s2n0", "", False), ("s1n0", "s2n1", "", False),
               ("s2n0", "s3n0", "httpx", False), ("s2n1", "s3n1", "httpx", False)],
        band=("Docker (un conteneur par serveur, stdin ouvert)", "infra"),
        steps=[
            "L'assistant découvre les outils exposés par chaque serveur (nom, description, schéma JSON des arguments).",
            "Quand la question le nécessite, il appelle un outil ; le serveur interroge l'API publique correspondante.",
            "La réponse est mise en forme en Markdown et renvoyée au modèle, qui la synthétise pour l'utilisateur.",
        ],
        extra_diagrams=[],
        langs=[("Python", 100)],
        langs_note="Serveurs MCP uniquement.",
        tags=["MCP", "LLM", "Agents", "httpx", "WFS", "Open data", "Docker"],
        stack=[
            ("mcp (SDK Python)", "Déclaration et exécution des outils", "IA agentique standardisée"),
            ("httpx", "Appels HTTP avec timeout", "Intégration d'API"),
            ("OGC WFS 2.0", "Requêtes géographiques filtrées (CQL)", "Données SIG"),
            ("Docker", "Isolation de chaque serveur", "Distribution"),
        ],
        matrix=dict(ci="n", tests="n", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="p", iac="n"),
        matrix_notes=dict(docker="Dockerfile + compose par serveur", serving="Protocole MCP (stdio)", deploy="Local / Claude Desktop"),
        snippets=[
            ("mcp-data-lyon/server.py — requête WFS avec filtre CQL optionnel",
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
            "Pas encore de tests automatisés ni de journalisation.",
            "Transport stdio uniquement ; un transport HTTP (streamable) permettrait un déploiement serveur partagé.",
        ],
    ),
    # ------------------------------------------------------------------ SPOTIFY
    dict(
        slug="gouvernance-spotify",
        short="Gouvernance des données — Spotify",
        kicker="Data Governance · Conseil · Bloc 1 RNCP 38777",
        title="Stratégie de gouvernance des données — cas Spotify",
        title_html='Gouvernance des données : <span class="highlight">du diagnostic au plan d\'action</span>',
        lead="Mission de conseil pour un comité exécutif (cas d'étude Spotify, 450 M d'utilisateurs) : évaluation de maturité "
             "sur 9 dimensions, organigramme de gouvernance, plan de déploiement, budget et présentation exécutive.",
        kpis=[("9", "dimensions évaluées"), ("~2,4/5", "maturité initiale"), ("4", "livrables"), ("×3", "ROI visé")],
        links=[("Livrables", GH + "BLOC1-SPOTIFY", True)],
        context=[
            "Données en silos (marketing, produit, contenu, ingénierie), exposition RGPD / CCPA / PDPA avec des amendes pouvant "
            "atteindre 4 % du chiffre d'affaires mondial : l'entreprise doit structurer sa gouvernance.",
            "Cas d'étude pédagogique fondé sur un business case fourni : les chiffres sont ceux du cas, pas d'une mission réelle.",
        ],
        rh=[
            "Posture de <strong>conseil auprès d'une direction</strong> : diagnostic, recommandation, budget, décision demandée.",
            "Pilote ciblé de 6 mois sur un domaine (données d'engagement marketing) avant généralisation : approche pragmatique.",
            "Rôles clairs : DPO, CDO, data stewards, comité de gouvernance.",
        ],
        tech=[
            "Architecture cible : lakehouse Databricks + Unity Catalog comme socle commun.",
            "Outillage recommandé par besoin : catalogue (Collibra), qualité (dbt, Talend), conformité (OneTrust), sécurité (SIEM), cycle de vie ML (MLflow + Evidently).",
            "KPIs de gouvernance mesurables : −10 % de données manquantes, 100 % des consentements tracés, incidents détectés sous 24 h.",
        ],
        stages=[
            ("Sources", "source", ["Marketing", "Produit", "Contenu", "Ingénierie"]),
            ("Socle", "storage", ["Lakehouse Databricks", "Unity Catalog"]),
            ("Gouvernance", "process", ["Catalogue", "Qualité (dbt)", "Conformité RGPD", "Sécurité"]),
            ("ML", "ops", ["MLflow + Evidently"]),
            ("Organisation", "ui", ["Comité · CDO · DPO", "Data stewards"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False), ("s0n3", "s1n0", "", False),
               ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False), ("s1n1", "s2n1", "", False), ("s1n1", "s2n2", "", False),
               ("s1n1", "s2n3", "", False), ("s1n1", "s3n0", "", False), ("s2n2", "s4n0", "", True), ("s2n1", "s4n1", "", True)],
        band=("Déploiement : pilote 6 mois (marketing) → modèle centralisé → Centre d'excellence", "infra"),
        steps=[
            "Évaluation de maturité sur 9 dimensions : gouvernance, conformité et intégration au niveau « cadré », les autres à consolider.",
            "Conception de l'organisation : démarrage centralisé puis bascule vers un Centre d'excellence.",
            "Plan de mise en œuvre par vagues, priorités conformité d'abord, pilote sur les données d'engagement.",
            "Présentation exécutive avec budget, ROI attendu et décision demandée au comité.",
        ],
        extra_diagrams=[],
        langs=[("Livrables (Word, PDF, PowerPoint)", 100)],
        langs_note="Projet de conseil, sans code.",
        tags=["Data Governance", "RGPD", "Databricks", "Unity Catalog", "Collibra", "dbt", "MLflow", "Conduite du changement"],
        stack=[
            ("Databricks + Unity Catalog", "Socle lakehouse et contrôle d'accès", "Architecture cible"),
            ("Collibra", "Catalogue et lignage", "Gouvernance des métadonnées"),
            ("dbt / Talend", "Qualité des données", "Contrôles automatisés"),
            ("OneTrust", "Consentement et conformité", "RGPD / CCPA"),
            ("MLflow + Evidently", "Cycle de vie et dérive des modèles", "Gouvernance du ML"),
        ],
        matrix=None,
        limits=[
            "Cas d'étude de certification : recommandations non mises en œuvre.",
        ],
    ),
    # ------------------------------------------------------------------ PREDICTIRA
    dict(
        slug="predictira",
        short="PredictIRA",
        kicker="ML santé publique · Projet d'équipe",
        title="PredictIRA — prévoir les passages aux urgences",
        title_html='Anticiper les <span class="highlight">urgences respiratoires</span> avant la vague',
        lead="Prédiction hebdomadaire des passages aux urgences pour infections respiratoires aiguës par département, à partir "
             "de la météo, de la pollution, de l'indice grippal et des recherches Google Trends. Modèle LightGBM servi par Flask, "
             "puis industrialisé en API FastAPI conteneurisée.",
        kpis=[("28", "variables"), ("LightGBM", "modèle"), ("2", "applications (Flask, FastAPI)"), ("4", "équipiers")],
        links=[("Application Flask", GH + "PredictIRA", True), ("API FastAPI + Docker", GH + "industrialisation", False)],
        context=[
            "Les épidémies respiratoires saturent les urgences chaque hiver. Anticiper la charge d'une à deux semaines permet "
            "d'adapter les effectifs et les lits.",
            "Projet d'équipe de formation (M2i / Jedha) : conception du modèle, puis industrialisation en API.",
        ],
        rh=[
            "Travail en équipe de 4 sur un sujet d'intérêt public.",
            "Premier passage du notebook à une application utilisable, puis à un service conteneurisé.",
        ],
        tech=[
            "Variables environnementales (O3, PM2.5, PM10, NO2…), indice grippal et signaux de recherche ; encodage cyclique de la semaine.",
            "LightGBM + <code>StandardScaler</code> sérialisés, formulaire Flask prérempli par département / semaine.",
            "Industrialisation : endpoint FastAPI <code>POST /predict/</code>, image Docker, client HTML.",
        ],
        stages=[
            ("Sources", "source", ["Météo · pollution", "Indice grippal", "Google Trends"]),
            ("Préparation", "process", ["Features + scaler"]),
            ("Modèle", "ml", ["LightGBM"]),
            ("Service", "serve", ["Flask (formulaire)", "FastAPI + Docker"]),
        ],
        edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
               ("s1n0", "s2n0", "", False), ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False)],
        band=None,
        steps=[
            "Assemblage hebdomadaire des variables environnementales, épidémiologiques et de recherche par département.",
            "Normalisation et entraînement d'un modèle LightGBM de régression.",
            "Application Flask : l'utilisateur choisit département et semaine, ajuste les variables, obtient la prédiction.",
            "Industrialisation : même modèle exposé par une API FastAPI dans un conteneur Docker.",
        ],
        extra_diagrams=[],
        langs=[("HTML / CSS", 70), ("Python", 30)],
        tags=["LightGBM", "scikit-learn", "Flask", "FastAPI", "Docker", "Santé publique"],
        stack=[
            ("LightGBM", "Régression du nombre de passages", "Gradient boosting"),
            ("scikit-learn", "Normalisation", "Préparation des données"),
            ("Flask + Jinja", "Application web", "Premier produit utilisable"),
            ("FastAPI + Docker", "API de prédiction conteneurisée", "Industrialisation"),
        ],
        matrix=dict(ci="n", tests="n", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="n", iac="n"),
        matrix_notes=dict(docker="Image python:3.9 + uvicorn", serving="Flask puis FastAPI"),
        snippets=[
            ("industrialisation/api.py — l'API de prédiction minimale",
             '''@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction_ira": int(prediction[0])}'''),
        ],
        limits=[
            "Projet de début de formation : pas de tests, de validation de schéma ni de métriques publiées dans le dépôt.",
            "Ce que j'en ai retenu et appliqué ensuite : schémas Pydantic, tests, CI et suivi des modèles (voir LyonFlow et Stripe).",
        ],
    ),
]
