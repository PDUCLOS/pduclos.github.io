"""Vitrine marche-hvac (dépôt Projet-HVAC, branche feat/vitrine-marche-hvac).

Chiffres repris de docs/PORTFOLIO.md (session de vérification du 27/10/2026, Ryzen 9 3900X, CPU seul).
Les scores publiés auparavant (Ridge R² 0,9996) venaient d'une fuite de cible : ils sont remplacés
par les scores corrigés, comparés à des prévisions naïves.
"""

GH = "https://github.com/PDUCLOS/"
REPO = GH + "Projet-HVAC"
BRANCH = REPO + "/tree/feat/vitrine-marche-hvac"
MEDIA = "/media/marche-hvac"

# ---------------------------------------------------------------------------------------------- FR

_VIDEO_FR = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 34 · générée par <code>scripts/promo_video.py</code> à partir des vraies captures (narration de synthèse en français).</p>"""

_AUDIT_FR = """
<p style="margin-bottom:1.2rem">Les scores publiés à l'origine (Ridge : R² 0,9996, RMSE 9,2) étaient <strong>faux</strong>. Je les ai reproduits à l'identique,
puis j'en ai trouvé la cause : certaines variables contenaient déjà la valeur à prédire. Voici ce qui a été corrigé, et ce que valent vraiment les modèles.</p>
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · La fuite</span><ul>
        <li>Moyennes et écarts glissants calculés <strong>en incluant le mois à prédire</strong>.</li>
        <li><code>lag_1m + diff_1m</code> reconstruisait exactement la cible : Ridge trouvait la somme, d'où R² 0,9996.</li>
        <li>La validation croisée découpait des <strong>départements</strong> et non le temps (jeu trié par département).</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · Le correctif</span><ul>
        <li>Fenêtres, <code>diff_1m</code> et <code>pct_1m</code> calculés sur la série <strong>décalée d'un mois</strong>.</li>
        <li>Lignes triées par date avant <code>TimeSeriesSplit</code>.</li>
        <li><strong>3 tests anti-fuite</strong> (ils échouent sur l'ancien code) et 1 sur l'ordre des plis.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · Les vrais scores</span><ul>
        <li>Ridge sur les 12 mois de 2025 : <strong>R² 0,968, RMSE 83,5</strong>.</li>
        <li><strong>−24,5 % de RMSE</strong> par rapport à la persistance « comme le mois dernier », −21 % par rapport à la saisonnière.</li>
        <li>LightGBM ne bat pas la persistance en RMSE (+7,8 %), seulement en MAE.</li></ul></div>
</div>
<p class="code-caption">Le même audit a corrigé 5 tests en échec, 46 erreurs ruff qui auraient bloqué la CI, un plantage de SHAP (94 colonnes fournies contre 92 apprises)
et 2 défauts des manifestes Kubernetes (namespace et volume du dashboard).</p>"""

_SHOTS_FR = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-benchmark.webp" alt="Comparaison des modèles avec les prévisions naïves dans le dashboard" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Nouvelle section du dashboard : les modèles battent-ils une prévision naïve ? RMSE sur les 12 mois de 2025.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-predictions.webp" alt="Historique et prévision pour le Rhône" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Historique et prévision du Rhône. La chute du dernier mois vient des DPE encore en cours de publication par l'ADEME.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-carte.webp" alt="Carte de France des installations de pompes à chaleur" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Carte de France des DPE mentionnant une pompe à chaleur, par département.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-shap.webp" alt="Importance des variables SHAP pour LightGBM" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">SHAP sur LightGBM, après correctif (le calcul plantait sur un décalage de colonnes).</p></div>
</div>"""

FR_UPDATES = dict(
    lead="Pipeline complet de l'open data à la prédiction : 5 collecteurs (ADEME DPE, Open-Meteo, INSEE, Eurostat, SITADEL), "
         "entrepôt en étoile, benchmark Ridge / LightGBM / Prophet / LSTM, API FastAPI, dashboard, Airflow et Kubernetes. "
         "Un audit a trouvé une <strong>fuite de cible</strong> dans les scores d'origine : elle est corrigée, et le modèle "
         "est désormais comparé à des prévisions naïves.",
    kpis=[("−24 %", "d'erreur (RMSE) vs prévision naïve, 2025"), ("0,968", "R² Ridge sur 2025, après correctif"),
          ("96", "départements"), ("5", "sources open data"), ("559", "tests verts")],
    links=[("Code source", REPO, True), ("Branche vitrine (audit et correctifs)", BRANCH, False)],
    rh=[
        "Sujet choisi dans <strong>mon secteur</strong> : les variables (MaPrimeRénov', CEE, type de logement) viennent de la connaissance terrain.",
        "<strong>Honnêteté sur les résultats</strong> : j'ai audité mon propre projet, trouvé une fuite de cible qui gonflait les scores, "
        "et republié des chiffres plus modestes mais vrais.",
        "Livrable exploitable par une direction commerciale : carte de France, prévisions, comparaison avec une prévision naïve.",
        "Gouvernance documentée (RGPD, AI Act).",
    ],
    tech=[
        "Collecteurs en <strong>architecture plugin</strong> (<code>BaseCollector</code> + registre), sans clé API.",
        "Schéma en étoile SQLAlchemy (SQLite, PostgreSQL 16 ou SQL Server), détection d'outliers IQR / Z-score / Isolation Forest.",
        "Split temporel train / validation / test, <code>TimeSeriesSplit</code> sur des lignes triées par date, "
        "variables glissantes décalées d'un mois, <strong>tests anti-fuite</strong>.",
        "Benchmark contre deux <strong>prévisions naïves</strong> (persistance et saisonnière) ; explicabilité SHAP.",
        "FastAPI 6 endpoints, Streamlit 6 pages, Docker multi-stage non-root, DAG Airflow mensuel <strong>et</strong> CronJob Kubernetes équivalent.",
        "CI : pytest 3.11 / 3.12 avec couverture, ruff (46 erreurs corrigées), build + smoke test Docker.",
    ],
    steps=[
        "Le 1er de chaque mois, Airflow (ou le CronJob Kubernetes) lance les collecteurs sur les 96 départements.",
        "Les données brutes sont nettoyées, fusionnées et chargées dans un schéma en étoile ; les valeurs aberrantes sont détectées par trois méthodes.",
        "Le feature engineering produit lags, moyennes et écarts glissants à 3 et 6 mois, calculés sur la série décalée d'un mois "
        "pour ne jamais voir le mois à prédire.",
        "Cinq familles de modèles sont entraînées sur un découpage temporel (train ≤ juin 2024, validation S2 2024, test 2025 → février 2026), "
        "comparées à deux prévisions naïves, puis expliquées avec SHAP.",
        "Les modèles sont servis par FastAPI et visualisés dans un dashboard Streamlit (carte de France, prévisions, comparaison avec les prévisions naïves).",
    ],
    extra_diagrams=[("marche-hvac-pipeline", "Pipeline de données détaillé"),
                    ("marche-hvac-fuite-cible", "Le correctif de fuite de cible : avant / après"),
                    ("marche-hvac-protocole", "Protocole d'évaluation : découpage dans le temps et prévisions naïves"),
                    ("marche-hvac-deploiement", "Déploiement Kubernetes : une image, trois commandes")],
    matrix_notes=dict(ci="pytest 2 versions + couverture, ruff (46 erreurs corrigées), smoke Docker",
                      tests="565 tests : 559 réussis, 6 ignorés, 0 échec (dont 3 anti-fuite)",
                      docker="Multi-stage, non-root (build non relancé lors de l'audit)", orch="Airflow + CronJob K8s",
                      tracking="Métriques en CSV/JSON (pas de MLflow)",
                      serving="FastAPI 6 endpoints, testée en local", deploy="Blueprint Render",
                      iac="Manifests Kubernetes, rendu kustomize vérifié (8 ressources), non appliqués sur un cluster"),
    metrics=dict(head=["Modèle", "Test complet : RMSE · MAE · R²", "12 mois de 2025 : RMSE · MAE · R²"], rows=[
        ["Ridge (retenu)", "135,9 · 56,2 · 0,909", "83,5 · 40,8 · 0,968"],
        ["LightGBM", "149,6 · 58,0 · 0,889", "119,1 · 44,0 · 0,934"],
        ["Naïve saisonnière ŷ(t) = y(t-12)", "141,7 · 64,8 · 0,901", "105,6 · 55,0 · 0,948"],
        ["Naïve persistance ŷ(t) = y(t-1)", "148,4 · 63,3 · 0,891", "110,5 · 46,9 · 0,943"],
        ["Prophet (1 modèle par département)", "221,8 · 96,3 · 0,756", "—"],
        ["Ridge exogène (sans historique DPE)", "374,7 · 223,2 · 0,305", "372,5 · 210,8 · 0,355"],
        ["LSTM (exploratoire)", "441 à 459 · 180 à 191 · −0,04 à 0,04", "—"],
        ["Ridge avant correctif (fuite de cible)", "9,18 · — · 0,9996 (illusoire)", "—"],
    ], note="Benchmark du 27/10/2026 (<code>scripts/benchmark_leakage.py</code>), CPU seul. Unité : DPE mentionnant une pompe à chaleur, "
            "par département et par mois. Test : janvier 2025 → février 2026 (1 344 lignes) ; la vue 2025 exclut janvier et février 2026, "
            "sous-comptés car les DPE arrivent avec retard à l'ADEME. Validation croisée temporelle (3 plis) : Ridge RMSE 91,4 ± 14,0. "
            "<strong>Lecture</strong> : Ridge bat la persistance de 24,5 % en RMSE ; sans historique DPE, le modèle n'explique presque rien "
            "(R² 0,36) : le signal vient de l'historique récent du marché, pas de la météo ni de la conjoncture."),
    snippets=[
        ("src/processing/feature_engineering.py — fenêtres glissantes décalées d'un mois (correctif de fuite)",
         '''                mean_name = f"{col}_rmean_{window}m"
                df[mean_name] = df.groupby("dept")[col].transform(
                    lambda s: s.shift(1).rolling(window, min_periods=1).mean()
                ).round(2)'''),
        ("tests/test_processing/test_feature_engineering.py — le test anti-fuite : perturber y(t) ne doit rien changer aux variables du mois t",
         '''        perturbed_input.loc[mask, self.TARGET] += 1000
        perturbed = self._engineer(fe, perturbed_input)

        row = (base["dept"] == dept) & (base["date_id"] == month_t)
        derived = [
            c for c in base.columns
            if c.startswith(f"{self.TARGET}_")
        ]
        assert derived, "expected target-derived features"
        pd.testing.assert_frame_equal(
            base.loc[row, derived].reset_index(drop=True),
            perturbed.loc[row, derived].reset_index(drop=True),
        )'''),
        ("kubernetes/cronjob-pipeline.yaml — le DAG Airflow, version native Kubernetes",
         '''spec:
  schedule: "0 6 1 * *"    # 1er du mois a 6h UTC
  concurrencyPolicy: Forbid'''),
    ],
    limits=[
        "<strong>Proxy</strong> : un DPE suit une vente ou une location, pas une installation. Le modèle prévoit des pompes à chaleur constatées lors des diagnostics.",
        "<strong>Prévision multi-mois de l'API</strong> simplifiée : au-delà d'un mois, seule <code>lag_1m</code> est mise à jour, les autres retards et fenêtres ne sont pas recalculés. Identifié, non corrigé.",
        "<strong>Derniers mois incomplets</strong> : les DPE arrivent avec retard à l'ADEME (février 2026 collecté au quart) et le pipeline ne filtre pas encore les mois non consolidés.",
        "LSTM non déterministe, séquences construites sans coupure entre départements : il ne fait pas mieux qu'une moyenne.",
        "Volume Kubernetes en ReadWriteOnce partagé par l'API (2 répliques), le dashboard et le CronJob : incompatible avec un cluster multi-nœuds.",
        "Non vérifié lors de l'audit : <code>docker build</code>, <code>kubectl apply</code> sur un cluster, exécution du DAG Airflow, collecte complète des 15,9 M de DPE. "
        "Pas encore de validation sur des mois postérieurs à février 2026.",
        "Pas de tracking MLflow ni de suivi de dérive : prochaine brique à ajouter.",
    ],
    strengths=[
        "<strong>Connaissance terrain</strong> : variables choisies par le métier (MaPrimeRénov', CEE, type de logement).",
        "<strong>Audit honnête</strong> : fuite de cible trouvée et corrigée (R² 0,9996 illusoire → 0,968 sur 2025), tests anti-fuite.",
        "<strong>Utilité mesurée</strong> : Ridge fait 24 % d'erreur en moins que la prévision naïve « comme le mois dernier ».",
        "<strong>Prêt à déployer</strong> : 559 tests verts, Docker non-root, DAG Airflow mensuel et CronJob Kubernetes équivalent.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 34", _VIDEO_FR),
        ("audit", "Audit", "Ce que j'ai corrigé : une fuite de cible", _AUDIT_FR),
        ("demo", "Démo réelle", "Captures du dashboard en fonctionnement", _SHOTS_FR),
    ],
)

# ---------------------------------------------------------------------------------------------- EN

_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 34, narrated in French · generated by <code>scripts/promo_video.py</code> from real screenshots (synthetic voice).</p>"""

_AUDIT_EN = """
<p style="margin-bottom:1.2rem">The originally published scores (Ridge: R² 0.9996, RMSE 9.2) were <strong>wrong</strong>. I reproduced them exactly,
then found the cause: some features already contained the value to predict. Here is what was fixed, and what the models are really worth.</p>
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · The leak</span><ul>
        <li>Rolling means and standard deviations computed <strong>including the month to predict</strong>.</li>
        <li><code>lag_1m + diff_1m</code> rebuilt the target exactly: Ridge found the sum, hence R² 0.9996.</li>
        <li>Cross-validation split <strong>departments</strong>, not time (the dataset was sorted by department).</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · The fix</span><ul>
        <li>Windows, <code>diff_1m</code> and <code>pct_1m</code> computed on the series <strong>shifted by one month</strong>.</li>
        <li>Rows sorted by date before <code>TimeSeriesSplit</code>.</li>
        <li><strong>3 anti-leakage tests</strong> (they fail on the old code) and 1 on fold ordering.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · The real scores</span><ul>
        <li>Ridge over the 12 months of 2025: <strong>R² 0.968, RMSE 83.5</strong>.</li>
        <li><strong>−24.5% RMSE</strong> versus the “same as last month” persistence forecast, −21% versus the seasonal one.</li>
        <li>LightGBM does not beat persistence on RMSE (+7.8%), only on MAE.</li></ul></div>
</div>
<p class="code-caption">The same audit fixed 5 failing tests, 46 ruff errors that would have blocked CI, a SHAP crash (94 columns supplied versus 92 learned)
and 2 defects in the Kubernetes manifests (dashboard namespace and volume).</p>"""

_SHOTS_EN = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-benchmark.webp" alt="Model comparison against naive forecasts in the dashboard" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">New dashboard section: do the models beat a naive forecast? RMSE over the 12 months of 2025.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-predictions.webp" alt="History and forecast for the Rhône department" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">History and forecast for the Rhône. The drop in the last month comes from DPE records still being published by ADEME.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-carte.webp" alt="Map of France of heat pump installations" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Map of France of DPE records mentioning a heat pump, by department.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/demo-shap.webp" alt="SHAP feature importance for LightGBM" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">SHAP on LightGBM, after the fix (the computation crashed on a column mismatch).</p></div>
</div>"""

EN_UPDATES = dict(
    lead="Complete pipeline from open data to prediction: 5 collectors (ADEME DPE, Open-Meteo, INSEE, Eurostat, SITADEL), "
         "star-schema warehouse, Ridge / LightGBM / Prophet / LSTM benchmark, FastAPI API, dashboard, Airflow and Kubernetes. "
         "An audit found <strong>target leakage</strong> in the original scores: it is fixed, and the model is now compared "
         "with naive forecasts.",
    kpis=[("−24%", "error (RMSE) vs naive forecast, 2025"), ("0.968", "Ridge R² on 2025, after the fix"),
          ("96", "departments"), ("5", "open data sources"), ("559", "passing tests")],
    links=[("Source code", REPO, True), ("Showcase branch (audit and fixes)", BRANCH, False)],
    rh=[
        "A topic chosen from <strong>my own industry</strong>: the variables (MaPrimeRénov', CEE, housing type) come from field knowledge.",
        "<strong>Honesty about results</strong>: I audited my own project, found target leakage that inflated the scores, "
        "and republished more modest but true figures.",
        "A deliverable a sales leadership team can use: map of France, forecasts, comparison with a naive forecast.",
        "Documented governance (GDPR, AI Act).",
    ],
    tech=[
        "Collectors built on a <strong>plugin architecture</strong> (<code>BaseCollector</code> + registry), no API key required.",
        "SQLAlchemy star schema (SQLite, PostgreSQL 16 or SQL Server), outlier detection with IQR / Z-score / Isolation Forest.",
        "Temporal train / validation / test split, <code>TimeSeriesSplit</code> on date-sorted rows, "
        "rolling features shifted by one month, <strong>anti-leakage tests</strong>.",
        "Benchmark against two <strong>naive forecasts</strong> (persistence and seasonal); SHAP explainability.",
        "FastAPI with 6 endpoints, 6-page Streamlit app, multi-stage non-root Docker, monthly Airflow DAG <strong>and</strong> an equivalent Kubernetes CronJob.",
        "CI: pytest 3.11 / 3.12 with coverage, ruff (46 errors fixed), Docker build + smoke test.",
    ],
    steps=[
        "On the 1st of each month, Airflow (or the Kubernetes CronJob) runs the collectors across the 96 departments.",
        "Raw data is cleaned, merged and loaded into a star schema; outliers are detected with three methods.",
        "Feature engineering produces lags, rolling means and rolling standard deviations over 3 and 6 months, computed on the "
        "series shifted by one month so they never see the month to predict.",
        "Five model families are trained on a temporal split (train ≤ June 2024, validation H2 2024, test 2025 → February 2026), "
        "compared with two naive forecasts, then explained with SHAP.",
        "Models are served by FastAPI and visualized in a Streamlit dashboard (map of France, forecasts, comparison with naive forecasts).",
    ],
    extra_diagrams=[("marche-hvac-pipeline", "Detailed data pipeline (labels in French)"),
                    ("marche-hvac-fuite-cible", "The target-leakage fix: before / after (labels in French)"),
                    ("marche-hvac-protocole", "Evaluation protocol: time-based split and naive forecasts (labels in French)"),
                    ("marche-hvac-deploiement", "Kubernetes deployment: one image, three commands (labels in French)")],
    matrix_notes=dict(ci="pytest on 2 versions + coverage, ruff (46 errors fixed), Docker smoke test",
                      tests="565 tests: 559 passed, 6 skipped, 0 failed (including 3 anti-leakage)",
                      docker="Multi-stage, non-root (build not rerun during the audit)", orch="Airflow + K8s CronJob",
                      tracking="Metrics in CSV/JSON (no MLflow)",
                      serving="FastAPI, 6 endpoints, tested locally", deploy="Render Blueprint",
                      iac="Kubernetes manifests, kustomize render checked (8 resources), not applied to a cluster"),
    metrics=dict(head=["Model", "Full test: RMSE · MAE · R²", "12 months of 2025: RMSE · MAE · R²"], rows=[
        ["Ridge (selected)", "135.9 · 56.2 · 0.909", "83.5 · 40.8 · 0.968"],
        ["LightGBM", "149.6 · 58.0 · 0.889", "119.1 · 44.0 · 0.934"],
        ["Naive seasonal ŷ(t) = y(t-12)", "141.7 · 64.8 · 0.901", "105.6 · 55.0 · 0.948"],
        ["Naive persistence ŷ(t) = y(t-1)", "148.4 · 63.3 · 0.891", "110.5 · 46.9 · 0.943"],
        ["Prophet (1 model per department)", "221.8 · 96.3 · 0.756", "—"],
        ["Exogenous Ridge (no DPE history)", "374.7 · 223.2 · 0.305", "372.5 · 210.8 · 0.355"],
        ["LSTM (exploratory)", "441 to 459 · 180 to 191 · −0.04 to 0.04", "—"],
        ["Ridge before the fix (target leakage)", "9.18 · — · 0.9996 (illusory)", "—"],
    ], note="Benchmark of 27/10/2026 (<code>scripts/benchmark_leakage.py</code>), CPU only. Unit: DPE records mentioning a heat pump, "
            "per department and per month. Test: January 2025 → February 2026 (1,344 rows); the 2025 view excludes January and February 2026, "
            "undercounted because DPE records reach ADEME late. Temporal cross-validation (3 folds): Ridge RMSE 91.4 ± 14.0. "
            "<strong>Reading</strong>: Ridge beats persistence by 24.5% on RMSE; without DPE history the model explains almost nothing "
            "(R² 0.36): the signal comes from the recent market history, not from weather or economic conditions."),
    snippets=[
        ("src/processing/feature_engineering.py — rolling windows shifted by one month (leakage fix)",
         FR_UPDATES["snippets"][0][1]),
        ("tests/test_processing/test_feature_engineering.py — the anti-leakage test: perturbing y(t) must not change month t's features",
         FR_UPDATES["snippets"][1][1]),
        ("kubernetes/cronjob-pipeline.yaml — the Airflow DAG, Kubernetes-native version",
         '''spec:
  schedule: "0 6 1 * *"    # 1st of the month at 6:00 UTC
  concurrencyPolicy: Forbid'''),
    ],
    limits=[
        "<strong>Proxy</strong>: a DPE follows a sale or a rental, not an installation. The model forecasts heat pumps observed during diagnostics.",
        "<strong>Simplified multi-month API forecast</strong>: beyond one month, only <code>lag_1m</code> is updated; other lags and windows are not recomputed. Identified, not fixed.",
        "<strong>Incomplete last months</strong>: DPE records reach ADEME late (February 2026 only a quarter collected) and the pipeline does not yet filter unconsolidated months.",
        "Non-deterministic LSTM, sequences built without breaks between departments: it does no better than an average.",
        "ReadWriteOnce Kubernetes volume shared by the API (2 replicas), the dashboard and the CronJob: incompatible with a multi-node cluster.",
        "Not verified during the audit: <code>docker build</code>, <code>kubectl apply</code> on a cluster, running the Airflow DAG, full collection of the 15.9 M DPE records. "
        "No validation yet on months after February 2026.",
        "No MLflow tracking or drift monitoring: the next component to add.",
    ],
    strengths=[
        "<strong>Field knowledge</strong>: features chosen by domain expertise (MaPrimeRénov', CEE energy-saving certificates, housing type).",
        "<strong>Honest audit</strong>: target leakage found and fixed (illusory R² 0.9996 → 0.968 on 2025), anti-leakage tests.",
        "<strong>Measured usefulness</strong>: Ridge makes 24% less error than the “same as last month” naive forecast.",
        "<strong>Ready to deploy</strong>: 559 passing tests, non-root Docker, monthly Airflow DAG and equivalent Kubernetes CronJob.",
    ],
    custom_sections=[
        ("video", "Overview", "The project in 1 min 34", _VIDEO_EN),
        ("audit", "Audit", "What I fixed: target leakage", _AUDIT_EN),
        ("demo", "Live demo", "Screenshots of the running dashboard", _SHOTS_EN),
    ],
)
