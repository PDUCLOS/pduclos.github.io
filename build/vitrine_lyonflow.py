"""LyonFlow : mises à jour issues de la vitrine (dépôt lyonflowfull, branche feat/vitrine-lyonflow).

Source : docs/PORTFOLIO.md du dépôt, vérifications et mesures du 27/10/2026
(Windows 11, Ryzen 9 3900X, Python 3.12.3, xgboost 3.4.1). Les chiffres non revérifiés
(MAE −45 %, benchmark R² 0,71, registre MLflow de production, 59 widgets) sont retirés des KPI.
"""

GH = "https://github.com/PDUCLOS/"
MEDIA = "/media/lyonflow"
BRANCH = GH + "lyonflowfull/tree/feat/vitrine-lyonflow"

# ---------------------------------------------------------------- FR
_VIDEO = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 45 · 10 scènes, narration de synthèse, à partir des captures et schémas de la vitrine.</p>"""

_SHOTS = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-statut-service.webp" alt="Page Statut du service : base injoignable, voyants en Indéterminé" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Page « Statut du service » après correctif : base volontairement injoignable, les 4 voyants passent en « Indéterminé » au lieu d'afficher une trace Python.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-accueil.webp" alt="Accueil Streamlit avec les 3 personas" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Accueil Streamlit : 3 personas (usager, opérateur TCL, élu). Défaut visible et non corrigé : une balise <code>&lt;/div&gt;</code> s'affiche sous deux cartes.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-api.webp" alt="Swagger de l'API FastAPI LyonFlow" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">API FastAPI : 9 routes (santé, modèles, prédiction trafic et Vélo'v, recommandation, itinéraire, goulots, RGPD, login).</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">Captures prises sur l'API et le dashboard lancés depuis le dépôt, <strong>sans base de données</strong> : elles montrent l'application et ses états dégradés, pas des données réelles.</p>"""

_FIXES = """
<div class="two-col">
    <div class="arg-card arg-card--tech"><span class="arg-label">Vérifier les chiffres</span><ul>
        <li><strong>27 DAGs</strong> confirmés (28 appels <code>DAG(...)</code>, dont 1 legacy).</li>
        <li>Tests : <strong>650 verts</strong> sur 674 collectés (et non 620), puis <strong>653</strong> avec 3 tests de sécurité ajoutés ; 0 échec.</li>
        <li>« Retrain toutes les 30 min » était <strong>inexact</strong> : vitesse entraînée chaque jour à 03:38 (le DAG horaire est en pause depuis le 01/07/2026), Vélo'v chaque heure à :50 ; inférence toutes les 15 min.</li>
        <li>7 groupes d'alertes Prometheus confirmés (17 règles).</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Corriger</span><ul>
        <li><strong>Tests non portables sous Windows</strong> : lecture de fichiers sans encodage (<code>UnicodeDecodeError</code>), corrigée par <code>encoding="utf-8"</code>.</li>
        <li><strong>Page « Statut du service »</strong> : base injoignable, elle affichait une trace Python complète. Le voyant Alertes et les derniers incidents suivent maintenant la règle des 3 autres voyants.</li>
        <li><strong>Rate limit contournable</strong> : l'API prenait la première IP de <code>X-Forwarded-For</code>, choisie par le client. Elle prend désormais la dernière, ajoutée par nginx.</li>
        <li><strong>Kubernetes</strong> : la base kustomize de la branche dormante ne se construisait plus. Réalignée sur <code>main</code> dans <code>deploy/k8s</code> ; UIs Prometheus / Alertmanager / Airflow protégées.</li></ul></div>
</div>"""

FR_UPDATES = dict(
    lead="Plateforme MLOps de bout en bout pour la mobilité lyonnaise : 9 sources open data, architecture Medallion "
         "sur PostgreSQL/PostGIS, 27 DAGs Airflow, XGBoost quantile (P10/P50/P90) à H+1h, suivi MLflow, dérive PSI, "
         "routage pgRouting et un dashboard à 3 personas. Déployée sur VPS ; cible Kubernetes rendue par kustomize.",
    kpis=[("9", "sources open data"), ("27", "DAGs Airflow"), ("653", "tests pytest verts, 0 échec"),
          ("5,4 ms", "prédiction P10/P50/P90 (médiane)"), ("18", "pages Streamlit, 3 personas")],
    links=[("Code source", GH + "lyonflowfull", True),
           ("Branche vitrine", BRANCH, False),
           ("Variante Databricks", GH + "databrickslyonflow", False)],
    tech=[
        "Medallion Bronze/Silver/Gold sur <strong>PostgreSQL 16 + PostGIS + pgRouting</strong>, SQL paramétré partout, zéro credential en dur.",
        "<strong>27 DAGs Airflow</strong> (collecte 5 min → 6 h, transforms, ML, maintenance), archivage MinIO S3.",
        "<strong>XGBoost quantile</strong> (P10/P50/P90) : vitesse entraînée chaque jour, Vélo'v chaque heure, inférence toutes les 15 min ; suivi <strong>MLflow</strong> avec repli sur un modèle local.",
        "Dérive <strong>PSI</strong> maison (rapport quotidien), Evidently en option ; Prometheus + Grafana + Alertmanager, 7 groupes d'alertes.",
        "CI GitHub Actions : ruff, mypy, bandit, pytest + couverture. Déploiement <code>make deploy-vps</code> / <code>rollback-vps</code>, Nginx seul point exposé.",
        "Cible <strong>Kubernetes</strong> : kustomize <code>base</code> + overlays dev / prod + composant monitoring, rendu validé sans erreur.",
    ],
    steps=[
        "<strong>Collecte</strong> — 9 sources ouvertes, DAGs Airflow cadencés de 5 min (trafic, bus, Vélo'v) à 6 h (vigilance météo).",
        "<strong>Bronze</strong> — stockage brut JSONB immuable : on peut toujours rejouer l'historique.",
        "<strong>Silver</strong> — déduplication (<code>DISTINCT ON</code>), parsing SIRI, reprojection géographique (4326 / 2154), filtrage des capteurs défaillants.",
        "<strong>Gold</strong> — features ML (lags, moyennes glissantes, calendrier scolaire, météo) et vues matérialisées métier (goulots, retards par tronçon).",
        "<strong>Modélisation</strong> — XGBoost quantile vitesse H+1h (entraînement quotidien à 03:38, inférence toutes les 15 min), XGBoost Vélo'v H+1h (réentraînement horaire), routage voiture <code>pgr_dijkstra</code>.",
        "<strong>MLOps</strong> — suivi MLflow, comparaison aux données TomTom, rapport de dérive PSI quotidien (05:30) affiché aux personas. Le réentraînement est planifié, pas déclenché par la dérive.",
        "<strong>Restitution</strong> — API FastAPI (prédiction, itinéraire, goulots, RGPD) et dashboard Streamlit de 18 pages pour 3 personas.",
    ],
    extra_diagrams=[("lyonflow-vue-ensemble", "Vue d'ensemble : du flux open data à la décision"),
                    ("lyonflow-cycle-mlops", "Cycle de vie du modèle : planifications réelles des DAGs"),
                    ("lyonflow-kubernetes", "Cible Kubernetes (kustomize, non déployée)"),
                    ("lyonflow-infra", "Infrastructure de production (VPS, conteneurs)")],
    stack=[
        ("Apache Airflow 2.9", "27 DAGs : collecte, transforms Medallion, entraînement, inférence, maintenance", "Orchestration de production, dépendances et reprises"),
        ("PostgreSQL 16 + PostGIS", "Schémas bronze / silver / gold / osm / rgpd", "Modélisation Medallion, SQL spatial, vues matérialisées"),
        ("pgRouting 3.7", "Itinéraire voiture sur le réseau OSM", "Algorithmes de graphe dans la base"),
        ("XGBoost (régression quantile)", "Vitesse trafic et disponibilité Vélo'v à H+1h, intervalles P10/P90", "Séries temporelles, incertitude de prévision"),
        ("MLflow 2.12", "Tracking ; chargement <code>models:/xgb_speed_h60/Production</code> avec repli local", "Cycle de vie des modèles"),
        ("PSI (+ Evidently en option)", "Rapport de dérive quotidien", "Monitoring de modèles en production"),
        ("FastAPI", "9 routes : prédiction, itinéraire, goulots, RGPD, login", "Service de modèles"),
        ("Streamlit", "18 pages, 3 personas", "Restitution orientée décision"),
        ("Docker · Nginx · systemd", "Stack conteneurisée, reverse proxy unique, TLS", "Déploiement et durcissement serveur"),
        ("Kubernetes (kustomize)", "base + overlays dev / prod, composant monitoring, SealedSecret en prod", "Portabilité vers un cluster"),
        ("Prometheus · Grafana · Alertmanager", "7 groupes d'alertes, 17 règles", "Observabilité"),
        ("MinIO", "Archivage S3 des données Silver", "Gestion du cycle de vie des données"),
        ("Databricks (variante)", "Delta Lake, DLT <code>expect_or_drop</code>, Unity Catalog, Asset Bundles", "Portabilité vers un lakehouse managé"),
    ],
    matrix_notes=dict(ci="ruff, mypy, bandit, pytest + couverture",
                      tests="653 verts, 1 ignoré, 23 d'intégration désélectionnés",
                      docker="Compose applicatif + compose monitoring",
                      orch="Airflow, 27 DAGs (retrain horaire vitesse en pause)",
                      tracking="MLflow ; registre de production non revérifié",
                      monitoring="PSI quotidien, Evidently optionnel, Prometheus/Grafana",
                      serving="FastAPI + clé API", deploy="VPS, deploy/rollback scriptés, health checks",
                      iac="kustomize dev / prod validé (non déployé) ; Asset Bundle Databricks"),
    metrics=dict(head=["Mesure", "Résultat", "Conditions"], rows=[
        ["Suite pytest (config du dépôt)", "650 verts, 1 ignoré, 23 désélectionnés, 0 échec (18,4 s) ; 653 avec les tests de sécurité", "1 ignoré = PostgreSQL absent"],
        ["Entraînement des 3 modèles quantiles (200 arbres, profondeur 6)", "8,19 s", "49 985 lignes synthétiques, 11 features, CPU"],
        ["<code>predict()</code> d'un capteur (P10 + P50 + P90)", "médiane 5,43 ms · p95 15,29 ms · p99 46,57 ms", "1 000 appels"],
        ["Prédiction P50 en lot", "14,78 ms / 10 000 lignes", "même modèle"],
        ["Modèle sérialisé", "2 680 Ko", "dict de 3 modèles"],
        ["PSI, décalage +0,25 σ / +0,5 σ / +1 σ", "0,0626 stable / 0,2377 significatif / 0,9491 significatif", "20 000 points, 10 buckets"],
        ["<code>GET /health</code>", "médiane 26,9 ms · p95 55,1 ms", "200 appels, base injoignable"],
        ["<code>kubectl kustomize</code> overlays dev / prod", "1 759 / 1 972 lignes, 0 erreur", "aucun pod démarré"],
    ], note="Mesures du 27/10/2026 sur Ryzen 9 3900X. Le jeu synthétique mesure le <strong>coût</strong> du modèle, pas sa "
            "<strong>qualité</strong> : aucune erreur de prédiction n'est publiée. Les gains de précision annoncés auparavant "
            "(MAE 5,8 → 3,2, benchmark R² 0,71) viennent d'un dépôt de travail privé et n'ont pas été revérifiés."),
    snippets=[
        ("src/models/xgboost_speed.py — intervalles de confiance par régression quantile",
         '''        quantiles = {"p10": 0.1, "p50": 0.5, "p90": 0.9}
        models: dict[str, xgb.XGBRegressor] = {}
        metrics: dict[str, float] = {}
        for label, alpha in quantiles.items():
            model = xgb.XGBRegressor(
                n_estimators=n_estimators,
                max_depth=max_depth,
                learning_rate=learning_rate,
                objective="reg:quantileerror",
                quantile_alpha=alpha,
                random_state=42,
                n_jobs=-1,
            )'''),
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
        ("dashboard/pages/Usager_5_Statut_Service.py — un voyant « Indéterminé » plutôt qu'une trace Python",
         '''def _kpi_alerts() -> dict | None:
    """KPI #4 — Alertes actives 6h.

    Comme les 3 autres voyants : si la base ne répond pas, le voyant passe
    en « Indéterminé » au lieu d'afficher une trace Python à l'usager.
    """
    try:
        df = cached_recent_alerts(hours=6, limit=50)
    except DashboardDataError:
        logger.warning("Statut service : alertes indisponibles (DB injoignable)")
        return None
    n_total = len(df)
    n_critical = int((df["severity"] == "critical").sum()) if "severity" in df.columns else 0
    return {"n_total": n_total, "n_critical": n_critical}'''),
        ("deploy/k8s/overlays/prod/kustomization.yaml — monitoring activé en production seulement",
         '''resources:
  - ../../base

components:
  - ../../components/monitoring'''),
    ],
    limits=[
        "Serveur unique : pas de haute disponibilité. La cible Kubernetes est rendue (kustomize) mais pas encore déployée : image à publier, MinIO, cert-manager, DAGs à valider sous KubernetesExecutor.",
        "Le fonctionnement en production sur le VPS, le registre MLflow et toute métrique de précision n'ont pas été revérifiés lors de la mise à jour de cette fiche.",
        "<code>POST /api/v1/recommend</code> renvoie encore un exemple codé en dur ; <code>GET /api/v1/models</code> affiche des métriques figées quand MLflow est injoignable.",
        "Défauts d'interface non corrigés : balise <code>&lt;/div&gt;</code> visible et texte tronqué sur l'accueil ; numéros de version incohérents (README, <code>/health</code>, OpenAPI).",
        "Prédiction des retards bus encore en phase d'analyse : la donnée SIRI doit s'accumuler avant de passer en production.",
        "Variante Databricks en cours : semaine 1 livrée (Unity Catalog, ingestion Bronze, DLT), MLflow / Model Serving / Genie à venir.",
    ],
    strengths=[
        "<strong>Du flux brut à la décision</strong> : 9 sources, Medallion sur PostgreSQL, 27 DAGs Airflow, 3 personas (usager, opérateur, élu).",
        "<strong>Prévision avec incertitude</strong> : XGBoost quantile P10/P50/P90, 5,4 ms par capteur, inférence toutes les 15 min.",
        "<strong>Boucle MLOps instrumentée</strong> : MLflow, dérive PSI quotidienne, alertes Prometheus, déploiement et retour arrière en une commande.",
        "<strong>Chiffres revérifiés</strong> : 653 tests verts, cadences lues dans le code, erreurs de la fiche précédente corrigées et failles réparées.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 45", _VIDEO),
        ("demo", "Démo réelle", "Captures prises sur l'application lancée depuis le dépôt", _SHOTS),
        ("verification", "Revue", "Ce que j'ai vérifié et corrigé", _FIXES),
    ],
)

# ---------------------------------------------------------------- EN
_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 45, narrated in French · 10 scenes, synthetic voice, built from the showcase screenshots and diagrams.</p>"""

_SHOTS_EN = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-statut-service.webp" alt="Service status page: database unreachable, indicators set to Undetermined" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">“Service status” page after the fix: database deliberately unreachable, the 4 indicators switch to “Undetermined” instead of showing a Python traceback.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-accueil.webp" alt="Streamlit home page with the 3 personas" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Streamlit home page: 3 personas (commuter, TCL operator, elected official). Visible, unfixed defect: a <code>&lt;/div&gt;</code> tag is shown under two cards.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-api.webp" alt="Swagger of the LyonFlow FastAPI API" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">FastAPI API: 9 routes (health, models, traffic and Vélo'v prediction, recommendation, itinerary, bottlenecks, GDPR, login).</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">Screenshots taken on the API and dashboard started from the repository <strong>without a database</strong>: they show the application and its degraded states, not real data.</p>"""

_FIXES_EN = """
<div class="two-col">
    <div class="arg-card arg-card--tech"><span class="arg-label">Checking the figures</span><ul>
        <li><strong>27 DAGs</strong> confirmed (28 <code>DAG(...)</code> calls, 1 of them legacy).</li>
        <li>Tests: <strong>650 passing</strong> out of 674 collected (not 620), then <strong>653</strong> with 3 added security tests; 0 failures.</li>
        <li>“Retrain every 30 min” was <strong>inaccurate</strong>: speed is trained daily at 03:38 (the hourly DAG has been paused since 07/01/2026), Vélo'v hourly at :50; inference every 15 min.</li>
        <li>7 Prometheus alert groups confirmed (17 rules).</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Fixing</span><ul>
        <li><strong>Tests not portable to Windows</strong>: files read without an encoding (<code>UnicodeDecodeError</code>), fixed with <code>encoding="utf-8"</code>.</li>
        <li><strong>“Service status” page</strong>: with the database unreachable it showed a full Python traceback. The Alerts indicator and latest incidents now follow the same rule as the other 3 indicators.</li>
        <li><strong>Bypassable rate limit</strong>: the API took the first IP of <code>X-Forwarded-For</code>, which the client chooses. It now takes the last one, added by nginx.</li>
        <li><strong>Kubernetes</strong>: the kustomize base on the dormant branch no longer built. Realigned with <code>main</code> in <code>deploy/k8s</code>; Prometheus / Alertmanager / Airflow UIs protected.</li></ul></div>
</div>"""

EN_UPDATES = dict(
    lead="End-to-end MLOps platform for Lyon mobility: 9 open data sources, Medallion architecture on "
         "PostgreSQL/PostGIS, 27 Airflow DAGs, quantile XGBoost (P10/P50/P90) one hour ahead, MLflow tracking, PSI drift, "
         "pgRouting routing and a dashboard for 3 personas. Deployed on a VPS; Kubernetes target rendered with kustomize.",
    kpis=[("9", "open data sources"), ("27", "Airflow DAGs"), ("653", "passing pytest tests, 0 failures"),
          ("5.4 ms", "P10/P50/P90 prediction (median)"), ("18", "Streamlit pages, 3 personas")],
    links=[("Source code", GH + "lyonflowfull", True),
           ("Showcase branch", BRANCH, False),
           ("Databricks variant", GH + "databrickslyonflow", False)],
    tech=[
        "Medallion Bronze/Silver/Gold on <strong>PostgreSQL 16 + PostGIS + pgRouting</strong>, parameterized SQL throughout, zero hard-coded credentials.",
        "<strong>27 Airflow DAGs</strong> (collection every 5 min → 6 h, transforms, ML, maintenance), MinIO S3 archiving.",
        "<strong>Quantile XGBoost</strong> (P10/P50/P90): speed trained daily, Vélo'v hourly, inference every 15 min; <strong>MLflow</strong> tracking with fallback to a local model.",
        "Custom <strong>PSI</strong> drift (daily report), Evidently optional; Prometheus + Grafana + Alertmanager, 7 alert groups.",
        "GitHub Actions CI: ruff, mypy, bandit, pytest + coverage. Deployment via <code>make deploy-vps</code> / <code>rollback-vps</code>, Nginx as the only exposed entry point.",
        "<strong>Kubernetes</strong> target: kustomize <code>base</code> + dev / prod overlays + monitoring component, rendering validated with no errors.",
    ],
    steps=[
        "<strong>Collection</strong> — 9 open sources, Airflow DAGs scheduled from every 5 min (traffic, buses, Vélo'v) to every 6 h (weather alerts).",
        "<strong>Bronze</strong> — immutable raw JSONB storage: history can always be replayed.",
        "<strong>Silver</strong> — deduplication (<code>DISTINCT ON</code>), SIRI parsing, geographic reprojection (4326 / 2154), filtering of faulty sensors.",
        "<strong>Gold</strong> — ML features (lags, rolling averages, school calendar, weather) and business materialized views (bottlenecks, delays by road segment).",
        "<strong>Modeling</strong> — quantile XGBoost speed H+1h (daily training at 03:38, inference every 15 min), XGBoost Vélo'v H+1h (hourly retraining), car routing with <code>pgr_dijkstra</code>.",
        "<strong>MLOps</strong> — MLflow tracking, comparison with TomTom data, daily PSI drift report (05:30) shown to the personas. Retraining is scheduled, not triggered by drift.",
        "<strong>Delivery</strong> — FastAPI API (prediction, itinerary, bottlenecks, GDPR) and an 18-page Streamlit dashboard for 3 personas.",
    ],
    extra_diagrams=[("lyonflow-vue-ensemble", "Overview: from open data feed to decision"),
                    ("lyonflow-cycle-mlops", "Model lifecycle: actual DAG schedules"),
                    ("lyonflow-kubernetes", "Kubernetes target (kustomize, not deployed)"),
                    ("lyonflow-infra", "Production infrastructure (VPS, containers)")],
    stack=[
        ("Apache Airflow 2.9", "27 DAGs: collection, Medallion transforms, training, inference, maintenance", "Production orchestration, dependencies and retries"),
        ("PostgreSQL 16 + PostGIS", "bronze / silver / gold / osm / rgpd schemas", "Medallion modeling, spatial SQL, materialized views"),
        ("pgRouting 3.7", "Car routing over the OSM network", "Graph algorithms inside the database"),
        ("XGBoost (quantile regression)", "Traffic speed and Vélo'v availability at H+1h, P10/P90 intervals", "Time series, forecast uncertainty"),
        ("MLflow 2.12", "Tracking; loads <code>models:/xgb_speed_h60/Production</code> with a local fallback", "Model lifecycle"),
        ("PSI (+ optional Evidently)", "Daily drift report", "Production model monitoring"),
        ("FastAPI", "9 routes: prediction, itinerary, bottlenecks, GDPR, login", "Model serving"),
        ("Streamlit", "18 pages, 3 personas", "Decision-oriented delivery"),
        ("Docker · Nginx · systemd", "Containerized stack, single reverse proxy, TLS", "Deployment and server hardening"),
        ("Kubernetes (kustomize)", "base + dev / prod overlays, monitoring component, SealedSecret in prod", "Portability to a cluster"),
        ("Prometheus · Grafana · Alertmanager", "7 alert groups, 17 rules", "Observability"),
        ("MinIO", "S3 archiving of Silver data", "Data lifecycle management"),
        ("Databricks (variant)", "Delta Lake, DLT <code>expect_or_drop</code>, Unity Catalog, Asset Bundles", "Portability to a managed lakehouse"),
    ],
    matrix_notes=dict(ci="ruff, mypy, bandit, pytest + coverage",
                      tests="653 passing, 1 skipped, 23 integration tests deselected",
                      docker="Application Compose + monitoring Compose",
                      orch="Airflow, 27 DAGs (hourly speed retrain paused)",
                      tracking="MLflow; production registry not re-checked",
                      monitoring="Daily PSI, optional Evidently, Prometheus/Grafana",
                      serving="FastAPI + API key", deploy="VPS, scripted deploy/rollback, health checks",
                      iac="kustomize dev / prod validated (not deployed); Databricks Asset Bundle"),
    metrics=dict(head=["Measurement", "Result", "Conditions"], rows=[
        ["pytest suite (repository config)", "650 passed, 1 skipped, 23 deselected, 0 failed (18.4 s); 653 with the security tests", "1 skipped = PostgreSQL absent"],
        ["Training the 3 quantile models (200 trees, depth 6)", "8.19 s", "49,985 synthetic rows, 11 features, CPU"],
        ["<code>predict()</code> for one sensor (P10 + P50 + P90)", "median 5.43 ms · p95 15.29 ms · p99 46.57 ms", "1,000 calls"],
        ["Batch P50 prediction", "14.78 ms / 10,000 rows", "same model"],
        ["Serialized model", "2,680 KB", "dict of 3 models"],
        ["PSI, shift +0.25 σ / +0.5 σ / +1 σ", "0.0626 stable / 0.2377 significant / 0.9491 significant", "20,000 points, 10 buckets"],
        ["<code>GET /health</code>", "median 26.9 ms · p95 55.1 ms", "200 calls, database unreachable"],
        ["<code>kubectl kustomize</code> dev / prod overlays", "1,759 / 1,972 lines, 0 errors", "no pod started"],
    ], note="Measured on 10/27/2026 on a Ryzen 9 3900X. The synthetic dataset measures the model's <strong>cost</strong>, not its "
            "<strong>quality</strong>: no prediction error is published. Accuracy gains reported earlier "
            "(MAE 5.8 → 3.2, benchmark R² 0.71) come from a private working repository and were not re-checked."),
    snippets=[
        ("src/models/xgboost_speed.py — confidence intervals through quantile regression",
         FR_UPDATES["snippets"][0][1]),
        ("src/monitoring/psi.py — robust PSI drift, no heavy dependency",
         FR_UPDATES["snippets"][1][1]),
        ("dashboard/pages/Usager_5_Statut_Service.py — an “Undetermined” indicator rather than a Python traceback",
         FR_UPDATES["snippets"][2][1]),
        ("deploy/k8s/overlays/prod/kustomization.yaml — monitoring enabled in production only",
         FR_UPDATES["snippets"][3][1]),
    ],
    limits=[
        "Single server: no high availability. The Kubernetes target is rendered (kustomize) but not yet deployed: image to publish, MinIO, cert-manager, DAGs to validate under KubernetesExecutor.",
        "Production operation on the VPS, the MLflow registry and every accuracy metric were not re-checked when this page was updated.",
        "<code>POST /api/v1/recommend</code> still returns a hard-coded example; <code>GET /api/v1/models</code> shows frozen metrics when MLflow is unreachable.",
        "Unfixed UI defects: a visible <code>&lt;/div&gt;</code> tag and truncated text on the home page; inconsistent version numbers (README, <code>/health</code>, OpenAPI).",
        "Bus delay prediction is still in the analysis phase: SIRI data needs to accumulate before going to production.",
        "Databricks variant in progress: week 1 delivered (Unity Catalog, Bronze ingestion, DLT), MLflow / Model Serving / Genie to come.",
    ],
    strengths=[
        "<strong>From raw feed to decision</strong>: 9 sources, Medallion on PostgreSQL, 27 Airflow DAGs, 3 personas (commuter, operator, elected official).",
        "<strong>Forecasts with uncertainty</strong>: quantile XGBoost P10/P50/P90, 5.4 ms per sensor, inference every 15 min.",
        "<strong>Instrumented MLOps loop</strong>: MLflow, daily PSI drift, Prometheus alerts, one-command deployment and rollback.",
        "<strong>Re-checked figures</strong>: 653 passing tests, schedules read from the code, errors in the previous page corrected and flaws fixed.",
    ],
    custom_sections=[
        ("video", "Presentation", "The project in 1 min 45", _VIDEO_EN),
        ("demo", "Real demo", "Screenshots of the application started from the repository", _SHOTS_EN),
        ("verification", "Review", "What I checked and fixed", _FIXES_EN),
    ],
)
