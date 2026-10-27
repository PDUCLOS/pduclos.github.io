"""Maintenance prédictive vibratoire (dépôt MLindustrial) : vitrine du 2026-10-27.

Chiffres issus de docs/PORTFOLIO.md (branche feat/vitrine-maintenance-predictive), mesurés le 27/10/2026
sur Ryzen 9 3900X / RTX 4070 Ti SUPER, Python 3.12.3. Fusionné par projects.py / projects_en.py.
"""

GH = "https://github.com/PDUCLOS/"
REPO = GH + "MLindustrial"
BRANCH = REPO + "/tree/feat/vitrine-maintenance-predictive"
MEDIA = "/media/maintenance-predictive"

# ---------------------------------------------------------------------------------------------- FR

_VIDEO = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 58 · vidéo narrée générée par <code>scripts/promo_video.py</code> à partir des vraies captures de l'API et du dashboard.</p>"""

_SHOTS = f"""
<p style="margin-bottom:1.2rem">Le modèle servi est réentraîné sur 29 roulements (2 319 mesures) ; trois roulements sont tenus à l'écart
et choisis avant tout résultat : K006 (sain), KI08 (défaut artificiel), KA22 (défaut réel).</p>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-artificiel.webp" alt="Page de démo de l'API : roulement KI08 à défaut artificiel détecté à 99,6 %" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">KI08, défaut artificiel jamais vu : détecté, P(défaut) = 0,9961.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-reel-manque.webp" alt="Page de démo de l'API : roulement KA22 à défaut réel classé sain à tort" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">KA22, défaut réel : classé sain à tort (P(défaut) = 0,1198). L'erreur est montrée, pas cachée ; la règle kurtosis, elle, le détecte sur cette mesure.</p></div>
</div>
<div class="table-wrap" style="margin-top:1.5rem"><table class="stack-table">
    <thead><tr><th>Mesure</th><th>Vérité</th><th>XGBoost</th><th>P(défaut)</th><th>Règle kurtosis (≤ 13,3845 ⇒ défaut)</th></tr></thead>
    <tbody>
        <tr><td>K006 N15_M07_F10</td><td>sain</td><td>sain ✔</td><td>0,0094</td><td>sain ✔</td></tr>
        <tr><td>K006 N09_M07_F10</td><td>sain</td><td>sain ✔</td><td>0,0083</td><td>sain ✔</td></tr>
        <tr><td>KI08 N15_M07_F10</td><td>artificiel</td><td>défaut ✔</td><td>0,9961</td><td>défaut ✔</td></tr>
        <tr><td>KI08 N09_M07_F10</td><td>artificiel</td><td>défaut ✔</td><td>0,9778</td><td>sain ✘</td></tr>
        <tr><td>KA22 N15_M07_F10</td><td><strong>réel</strong></td><td>sain ✘</td><td>0,1198</td><td>défaut ✔</td></tr>
        <tr><td>KA22 N09_M07_F10</td><td><strong>réel</strong></td><td>sain ✘</td><td>0,0229</td><td>sain ✘</td></tr>
    </tbody></table></div>
<div class="two-col" style="margin-top:2rem;align-items:start">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/dashboard-indicateurs.webp" alt="Dashboard Streamlit : distribution des indicateurs vibratoires par état de santé" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Dashboard Streamlit sur les 32 roulements : 7 677 signaux, 46 062 indicateurs calculés.</p></div>
    <div class="arg-card arg-card--tech" style="min-width:0"><span class="arg-label">Temps mesurés (CPU)</span><ul>
        <li>5 indicateurs sur une mesure de 256 001 points : <strong>23,2 ms</strong> (médiane de 50).</li>
        <li>Prédiction XGBoost unitaire : <strong>0,91 ms</strong> ; en lot sur 2 559 mesures : 3,3 ms.</li>
        <li><code>POST /predict</code> de bout en bout : 317 ms, dominés par le JSON de 256 000 flottants.</li>
        <li>Entraînement complet : 154 ms sur CPU, 365 ms sur GPU : <strong>le GPU n'apporte rien à cette échelle</strong>.</li>
        <li>Modèle exporté : 279 048 octets (JSON XGBoost).</li></ul></div>
</div>"""

_TRANSFER = """
<p style="margin-bottom:1.2rem">La question du projet : un modèle appris sur des défauts <strong>usinés en laboratoire</strong> reconnaît-il des défauts
<strong>apparus en fonctionnement</strong> ? Entraînement sur 12 roulements à défaut artificiel + 3 sains (1 199 mesures), test sur
14 roulements à défaut réel + les 3 autres sains (1 360 mesures), répété sur les 20 partitions 3 / 3 des 6 sains.
Contrôle : mêmes sains, défauts réels appris en validation croisée groupée.</p>
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Scénario</th><th>F1 macro</th><th>Balanced accuracy</th><th>Rappel défauts</th><th>Rappel sains</th></tr></thead>
    <tbody>
        <tr><td>Artificiel → réel</td><td><strong>0,620 ± 0,102</strong></td><td>0,646 ± 0,109</td><td>0,809 ± 0,098</td><td>0,484 ± 0,229</td></tr>
        <tr><td>Contrôle réel → réel</td><td><strong>0,694 ± 0,107</strong></td><td>0,690 ± 0,105</td><td>0,930 ± 0,030</td><td>0,449 ± 0,218</td></tr>
    </tbody></table></div>
<div class="two-col" style="margin-top:1.5rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">Lecture</span><ul>
        <li>Entraîné sur des défauts usinés, le modèle manque <strong>environ 1 défaut réel sur 5</strong>, contre environ 1 sur 14 s'il a vu des défauts réels.</li>
        <li>La reconnaissance des sains reste faible dans les deux cas : il n'y a que 6 roulements sains.</li>
        <li>Mesure exploratoire, à confirmer avec l'analyse d'enveloppe.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Un biais évité</span><ul>
        <li>La fonction existante <code>split_artificial_to_real()</code> mettait tous les sains en entraînement : le test ne contenait qu'une classe et le F1 macro n'était pas interprétable.</li>
        <li>Le banc répartit donc les sains entre entraînement et test, et appelle <code>assert_no_asset_leakage</code> à chaque partition.</li></ul></div>
</div>"""

_FIXES = """
<p style="margin-bottom:1.2rem">Avant d'ajouter quoi que ce soit, j'ai relancé l'existant sur les 2 560 fichiers officiels (5,4 Go d'archives,
22,4 Go extraits). Ingestion complète en 473 s : 2 559 mesures retenues, 1 fichier illisible écarté et listé. Les baselines sont reproduites
au millième ; XGBoost vibration donne 0,734 ± 0,206 contre 0,738 publié, un écart environ 50 fois plus petit que l'écart-type.</p>
<div class="three-col">
    <div class="arg-card arg-card--tech"><span class="arg-label">Tests et CI</span><ul>
        <li><strong>CI lint cassée</strong> : ruff 0.16.5 activait 67 règles de plus ; jeu de règles épinglé dans <code>pyproject.toml</code>.</li>
        <li><strong>Deux tests qui ne testaient rien</strong> (résultat sans <code>assert</code>, <code>pytest.raises(Exception)</code> trop large).</li>
        <li>Un test d'intégration <strong>toujours ignoré</strong> charge maintenant un vrai fichier .mat.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Exécution hors Docker</span><ul>
        <li>TimescaleDB n'est plus obligatoire : repli en table classique avec avertissement sur PostgreSQL.</li>
        <li>Dashboard : adresse MLflow codée en dur remplacée par <code>MLFLOW_TRACKING_URI</code> (onglets Alertes et Résultats vides sinon).</li>
        <li>Service : <code>xgb.Booster</code> au lieu de <code>XGBClassifier</code>, qui exigeait scikit-learn dans l'image.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Ajouts</span><ul>
        <li>API <strong>FastAPI</strong> + page de démo, mêmes fonctions d'indicateurs qu'à l'entraînement, 9 tests.</li>
        <li><code>Dockerfile.api</code>, manifestes <strong>Kubernetes</strong> (kustomize : local 6 objets, prod 8 objets).</li>
        <li>Banc reproductible, schémas d'architecture, vitrine et vidéo. <strong>223 tests passés</strong>, 0 échec.</li></ul></div>
</div>"""

FR_UPDATES = dict(
    kicker="ML industriel · Signal · MLOps",
    lead="Diagnostic de défauts sur les 32 roulements réels du banc Paderborn à partir de 5 indicateurs vibratoires explicables, "
         "avec une validation qui ne mélange jamais un roulement entre entraînement et test, et une mesure chiffrée de l'écart "
         "entre défauts de laboratoire et défauts réels. Modèle servi par une API FastAPI, conteneurisable et déployable sur Kubernetes.",
    kpis=[("223", "tests (0 échec)"), ("0,734", "F1 macro XGBoost, CV groupée"), ("0,62", "F1 macro artificiel → réel"),
          ("23,2 ms", "indicateurs par mesure, CPU"), ("5,4 Go", "archives Paderborn")],
    links=[("Code source", REPO, True), ("Branche vitrine", BRANCH, False)],
    context=[
        "La plupart des démonstrations de maintenance prédictive testent un modèle sur les mêmes roulements que ceux "
        "vus à l'entraînement : les scores sont flatteurs et ne tiennent pas en atelier.",
        "Ce projet mesure l'écart laboratoire / terrain, compare un capteur vibratoire au <strong>courant moteur "
        "déjà disponible sur chaque variateur</strong> (aucun capteur à ajouter) et privilégie des indicateurs qu'un responsable "
        "maintenance comprend.",
        "Résultat mesuré : entraîné sur des défauts usinés, le modèle manque <strong>environ 1 défaut réel sur 5</strong>, "
        "contre environ 1 sur 14 lorsqu'il a vu des défauts réels. Et il ne bat pas nettement une simple règle sur le kurtosis.",
    ],
    rh=[
        "Expertise métier réelle (déploiements terrain IFM, Schaeffler, SKF) mise au service de la data.",
        "Raisonnement <strong>coût capteur / valeur</strong> : peut-on éviter d'instrumenter une machine ?",
        "Résultats publiés tels quels, y compris quand le modèle se trompe sur un défaut réel ou ne bat pas une règle simple.",
        "Projet repris et vérifié : chiffres reproduits, tests défaillants corrigés, livré jusqu'à l'API et Kubernetes.",
    ],
    tech=[
        "5 indicateurs temporels (RMS, crête à crête, facteur de crête, kurtosis, asymétrie) ; fréquences de défaut "
        "<strong>BPFO / BPFI / BSF / FTF</strong> calculées depuis la géométrie, analyse d'enveloppe encore désactivée.",
        "<code>StratifiedGroupKFold</code> groupé par roulement et garde-fou <code>assert_no_asset_leakage</code> ; "
        "banc artificiel → réel sur 20 partitions des roulements sains.",
        "PostgreSQL / TimescaleDB (repli sans l'extension), MLflow, hash du dataset pour la traçabilité, dérive Evidently.",
        "Service <strong>FastAPI</strong> (<code>/predict</code> + page de démo) avec les mêmes fonctions d'indicateurs qu'à l'entraînement ; "
        "<code>Dockerfile.api</code> et manifestes <strong>kustomize</strong> local / prod.",
        "CI : ruff (règles épinglées), 223 tests, smoke test du pipeline ML sur 2 roulements réels (K001, KA01).",
        "Simulateurs physiques, simulation d'usine SimPy et export Asset Administration Shell (Industrie 4.0).",
    ],
    stages=[
        ("Source", "source", ["Paderborn .mat (5,4 Go)"]),
        ("Ingestion", "ingest", ["Loaders + contrôles physiques", "Parquet"]),
        ("Stockage", "storage", ["PostgreSQL / TimescaleDB"]),
        ("Features", "process", ["Temporel : RMS, kurtosis", "Fréquences BPFO/BPFI"]),
        ("Modèles", "ml", ["Seuils (baseline)", "XGBoost", "CV groupée par roulement"]),
        ("Suivi", "ops", ["MLflow", "Evidently dérive"]),
        ("Restitution", "ui", ["Streamlit jumeau numérique", "Export AAS"]),
        ("Service", "serve", ["FastAPI /predict + démo", "Kubernetes (kustomize)"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
           ("s2n0", "s3n0", "", False), ("s2n0", "s3n1", "", False), ("s3n0", "s4n0", "", False),
           ("s3n1", "s4n1", "", False), ("s4n2", "s4n1", "", True), ("s4n1", "s5n0", "log", False),
           ("s4n0", "s5n0", "", False), ("s5n1", "s6n0", "", True), ("s4n1", "s6n0", "", False), ("s6n0", "s6n1", "", True),
           ("s4n1", "s7n0", "modèle exporté", False), ("s7n0", "s7n1", "", True)],
    band=("uv · GitHub Actions (ruff, pytest, smoke test ML sur 2 roulements réels) · Docker Compose · Dockerfile.api · kustomize", "infra"),
    steps=[
        "Téléchargement des 32 archives Paderborn (5,4 Go, 22,4 Go extraits), parsing des noms de fichiers (roulement, régime, défaut) et contrôles de plausibilité physique ; 1 fichier illisible écarté et listé.",
        "Ingestion complète en 473 s : 2 559 mesures, 7 677 signaux, 46 062 indicateurs, stockés site → zone → machine → actif → roulement.",
        "Calcul des indicateurs temporels et des fréquences caractéristiques de défaut à partir de la géométrie du roulement.",
        "Comparaison d'une baseline à seuils et de XGBoost, en validation croisée groupée par roulement (aucun roulement à la fois en train et en test).",
        "Banc artificiel → réel : entraînement sur défauts usinés, test sur défauts réels, sains répartis sur 20 partitions.",
        "Suivi MLflow (hash du dataset, F1 macro, balanced accuracy) et rapport de dérive Evidently train / test.",
        "Export du modèle (29 roulements, 3 tenus à l'écart pour la démo) et service FastAPI ; image et manifestes Kubernetes.",
        "Restitution Streamlit : alertes, indicateurs, jumeau numérique d'usine, glossaire.",
    ],
    extra_diagrams=[("maintenance-predictive-pipeline", "Pipeline données et ML"),
                    ("maintenance-predictive-evaluation", "Protocole d'évaluation : CV groupée et artificiel → réel"),
                    ("maintenance-predictive-service-kubernetes", "Service d'inférence et Kubernetes"),
                    ("maintenance-predictive-signal-indicateurs", "Du signal vibratoire aux indicateurs")],
    tags=["Signal processing", "SciPy", "XGBoost", "scikit-learn", "PostgreSQL", "TimescaleDB", "MLflow", "Evidently", "Polars",
          "Streamlit", "FastAPI", "Docker", "Kubernetes", "SimPy", "uv", "GitHub Actions", "Industrie 4.0"],
    stack=[
        ("NumPy / SciPy", "Traitement du signal, indicateurs temporels, spectres", "Features physiques explicables"),
        ("XGBoost / scikit-learn", "Classification des défauts, CV groupée par roulement", "ML sur données industrielles"),
        ("PostgreSQL / TimescaleDB", "Mesures et indicateurs ; hypertable si l'extension est présente", "Stockage adapté aux capteurs"),
        ("MLflow", "Expériences baseline vs GBM, hash du dataset", "Traçabilité et reproductibilité"),
        ("Evidently", "Dérive train / test (KS)", "Détection de changement de distribution"),
        ("FastAPI", "API /predict et page de démo sur mesures réelles", "Service de modèles"),
        ("Docker + Kubernetes (kustomize)", "Image API dédiée, overlays local / prod", "Déploiement"),
        ("SimPy", "Simulation d'usine à événements discrets", "Jumeau numérique"),
        ("uv + ruff + pytest", "Dépendances verrouillées, qualité, 223 tests", "Hygiène d'ingénierie"),
    ],
    matrix=dict(ci="y", tests="y", docker="p", orch="n", tracking="y", monitoring="y", serving="y", deploy="p", iac="n"),
    matrix_notes=dict(ci="ruff + pytest + smoke test ML sur 2 roulements réels", tests="223 tests dont anti-fuite et 9 tests API",
                      docker="Dockerfile.api et Compose ; build non vérifié dans cette session (image simulée en venv vierge)",
                      tracking="MLflow, hash du dataset", monitoring="Evidently + dérive temporelle",
                      serving="FastAPI /predict + page de démo", deploy="Manifestes kustomize local / prod rendus, non appliqués sur cluster"),
    metrics=dict(head=["Approche", "F1 macro mesuré", "Publié auparavant"], rows=[
        ["Seuil kurtosis (CV 5 folds groupée par roulement)", "0,682 ± 0,158", "0,682 ± 0,158"],
        ["Seuil facteur de crête", "0,576 ± 0,174", "0,576 ± 0,174"],
        ["Seuil RMS", "0,430 ± 0,090", "0,430 ± 0,090"],
        ["XGBoost vibration (5 indicateurs)", "0,734 ± 0,206", "0,738 ± 0,208"],
        ["XGBoost vibration + courant (15 indicateurs)", "0,726 ± 0,219", "0,726 ± 0,222"],
        ["XGBoost courant seul (10 indicateurs)", "0,550 ± 0,123", "0,542 ± 0,121"],
        ["Artificiel → réel (20 partitions des sains)", "0,620 ± 0,102", "—"],
        ["Contrôle réel → réel", "0,694 ± 0,107", "—"],
    ], note="Mesures du 27/10/2026. Les baselines, déterministes, sont reproduites au millième ; les petits écarts XGBoost viennent "
            "vraisemblablement de la version de la bibliothèque (xgboost 3.4.1) et ne changent aucune conclusion. "
            "Conclusion honnête : XGBoost ne bat pas nettement une règle simple sur le kurtosis (intervalles qui se chevauchent, "
            "F1 par fold de 0,473 à 0,978), et l'écart entre défauts artificiels et réels est réel."),
    snippets=[
        ("src/data/splits.py — garde-fou contre la fuite entre train et test",
         '''def assert_no_asset_leakage(
    train_df: pd.DataFrame, test_df: pd.DataFrame, asset_col: str = "asset_id"
) -> None:
    """Garde-fou : leve une erreur si un asset_id apparait dans train ET test."""
    leaked = set(train_df[asset_col]) & set(test_df[asset_col])
    if leaked:
        raise ValueError(f"Fuite de donnees : assets presents dans train ET test : {leaked}")'''),
        ("scripts/bench_vitrine.py — généralisation artificiel → réel",
         '''    for train_h in itertools.combinations(healthy, 3):
        h_train = df[df["code"].isin(train_h)]
        h_test = df[(df["origin"] == "na") & ~df["code"].isin(train_h)]

        # (a) artificiel -> reel
        train = pd.concat([art, h_train])
        test = pd.concat([real, h_test])
        assert_no_asset_leakage(train, test, asset_col="asset_id")
        m = train_gbm(train[FEATURE_ORDER].to_numpy(), train["label"].to_numpy())
        transfer.append(scores(test["label"], m.predict(test[FEATURE_ORDER].to_numpy())))'''),
        ("src/serving/predictor.py — inférence avec les mêmes indicateurs qu'à l'entraînement",
         '''    def features_from_signal(self, signal: np.ndarray) -> dict[str, float]:
        x = np.asarray(signal, dtype=np.float64)
        if x.ndim != 1 or x.size < MIN_SAMPLES:
            raise ValueError(f"signal 1D d'au moins {MIN_SAMPLES} echantillons attendu")
        if not np.all(np.isfinite(x)):
            raise ValueError("signal contenant des valeurs non finies")
        return {f"vibration_{k}": v for k, v in time_domain_features(x).items()}'''),
    ],
    limits=[
        "Un seul banc, un seul modèle de roulement (6203), 32 roulements dont 6 sains : écarts-types de 0,10 à 0,21 sur le F1 macro ; aucune garantie de transfert vers une autre machine.",
        "Indicateurs temporels seuls : l'analyse d'enveloppe (BPFO / BPFI) reste désactivée tant que la sélection de bande (kurtogramme) n'est pas stabilisée.",
        "Régimes mélangés : la généralisation vers un régime de fonctionnement inconnu n'est pas mesurée.",
        "Le banc artificiel → réel est exploratoire ; la phase 3 complète attend la décision sur le kurtogramme.",
        "Non vérifié dans cette session : <code>docker build</code> / <code>docker compose up</code>, hypertable TimescaleDB, déploiement sur un cluster réel, mémoire de l'API en conteneur, CI GitHub Actions (vérifiée localement).",
        "Données sous licence CC BY-NC 4.0 (usage non commercial, citation de Lessmeier et al., 2016).",
    ],
    strengths=[
        "<strong>Validation sans fuite</strong> : CV groupée par roulement et garde-fou <code>assert_no_asset_leakage</code>, y compris dans le banc artificiel → réel.",
        "<strong>Écart labo / terrain chiffré</strong> : 0,620 F1 macro en artificiel → réel contre 0,694 en contrôle ; ~1 défaut réel manqué sur 5.",
        "<strong>Chiffres reproduits avant d'être publiés</strong> : baselines au millième, XGBoost à 0,004 près, 6 défauts réels corrigés.",
        "<strong>Du signal à l'API</strong> : 5 indicateurs explicables en 23,2 ms, FastAPI, image dédiée et manifestes Kubernetes.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 58", _VIDEO),
        ("demo", "Démo réelle", "Trois roulements jamais vus par le modèle servi", _SHOTS),
        ("artificiel-reel", "Résultat clé", "Défauts de laboratoire contre défauts réels", _TRANSFER),
        ("corrections", "Reprise", "Ce que j'ai vérifié, corrigé et ajouté", _FIXES),
    ],
)

# ---------------------------------------------------------------------------------------------- EN

_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 58 · narrated video generated by <code>scripts/promo_video.py</code> from real captures of the API and the dashboard.</p>"""

_SHOTS_EN = f"""
<p style="margin-bottom:1.2rem">The served model is retrained on 29 bearings (2,319 measurements); three bearings are held out
and were chosen before any result: K006 (healthy), KI08 (artificial fault), KA22 (real fault).</p>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-artificiel.webp" alt="API demo page: bearing KI08 with an artificial fault detected at 99.6%" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">KI08, artificial fault never seen: detected, P(fault) = 0.9961.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-reel-manque.webp" alt="API demo page: bearing KA22 with a real fault wrongly classified as healthy" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">KA22, real fault: wrongly classified as healthy (P(fault) = 0.1198). The error is shown, not hidden; the kurtosis rule does catch it on this measurement.</p></div>
</div>
<div class="table-wrap" style="margin-top:1.5rem"><table class="stack-table">
    <thead><tr><th>Measurement</th><th>Ground truth</th><th>XGBoost</th><th>P(fault)</th><th>Kurtosis rule (≤ 13.3845 ⇒ fault)</th></tr></thead>
    <tbody>
        <tr><td>K006 N15_M07_F10</td><td>healthy</td><td>healthy ✔</td><td>0.0094</td><td>healthy ✔</td></tr>
        <tr><td>K006 N09_M07_F10</td><td>healthy</td><td>healthy ✔</td><td>0.0083</td><td>healthy ✔</td></tr>
        <tr><td>KI08 N15_M07_F10</td><td>artificial</td><td>fault ✔</td><td>0.9961</td><td>fault ✔</td></tr>
        <tr><td>KI08 N09_M07_F10</td><td>artificial</td><td>fault ✔</td><td>0.9778</td><td>healthy ✘</td></tr>
        <tr><td>KA22 N15_M07_F10</td><td><strong>real</strong></td><td>healthy ✘</td><td>0.1198</td><td>fault ✔</td></tr>
        <tr><td>KA22 N09_M07_F10</td><td><strong>real</strong></td><td>healthy ✘</td><td>0.0229</td><td>healthy ✘</td></tr>
    </tbody></table></div>
<div class="two-col" style="margin-top:2rem;align-items:start">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/dashboard-indicateurs.webp" alt="Streamlit dashboard: distribution of vibration indicators by health state" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Streamlit dashboard on the 32 bearings: 7,677 signals, 46,062 computed indicators.</p></div>
    <div class="arg-card arg-card--tech" style="min-width:0"><span class="arg-label">Measured timings (CPU)</span><ul>
        <li>5 indicators on a 256,001-point measurement: <strong>23.2 ms</strong> (median of 50).</li>
        <li>Single XGBoost prediction: <strong>0.91 ms</strong>; batch of 2,559 measurements: 3.3 ms.</li>
        <li>End-to-end <code>POST /predict</code>: 317 ms, dominated by the JSON of 256,000 floats.</li>
        <li>Full training: 154 ms on CPU, 365 ms on GPU: <strong>the GPU brings nothing at this scale</strong>.</li>
        <li>Exported model: 279,048 bytes (XGBoost JSON).</li></ul></div>
</div>"""

_TRANSFER_EN = """
<p style="margin-bottom:1.2rem">The project's question: does a model trained on faults <strong>machined in a lab</strong> recognize faults
<strong>that developed in operation</strong>? Training on 12 bearings with artificial faults + 3 healthy (1,199 measurements), testing on
14 bearings with real faults + the 3 other healthy ones (1,360 measurements), repeated over the 20 possible 3 / 3 splits of the 6 healthy bearings.
Control: same healthy bearings, real faults learned with grouped cross-validation.</p>
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Scenario</th><th>Macro F1</th><th>Balanced accuracy</th><th>Fault recall</th><th>Healthy recall</th></tr></thead>
    <tbody>
        <tr><td>Artificial → real</td><td><strong>0.620 ± 0.102</strong></td><td>0.646 ± 0.109</td><td>0.809 ± 0.098</td><td>0.484 ± 0.229</td></tr>
        <tr><td>Control real → real</td><td><strong>0.694 ± 0.107</strong></td><td>0.690 ± 0.105</td><td>0.930 ± 0.030</td><td>0.449 ± 0.218</td></tr>
    </tbody></table></div>
<div class="two-col" style="margin-top:1.5rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">Reading</span><ul>
        <li>Trained on machined faults, the model misses <strong>about 1 real fault in 5</strong>, versus about 1 in 14 when it has seen real faults.</li>
        <li>Recognition of healthy bearings stays weak in both cases: there are only 6 healthy bearings.</li>
        <li>Exploratory measurement, to be confirmed with envelope analysis.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">A bias avoided</span><ul>
        <li>The existing <code>split_artificial_to_real()</code> function put all healthy bearings in training: the test set held a single class and macro F1 was meaningless.</li>
        <li>The benchmark therefore splits healthy bearings between train and test, and calls <code>assert_no_asset_leakage</code> on every split.</li></ul></div>
</div>"""

_FIXES_EN = """
<p style="margin-bottom:1.2rem">Before adding anything, I re-ran the existing code on the 2,560 official files (5.4 GB of archives,
22.4 GB extracted). Full ingestion in 473 s: 2,559 measurements kept, 1 unreadable file excluded and listed. The baselines are reproduced
to the thousandth; vibration XGBoost gives 0.734 ± 0.206 versus 0.738 published, a gap about 50 times smaller than the standard deviation.</p>
<div class="three-col">
    <div class="arg-card arg-card--tech"><span class="arg-label">Tests and CI</span><ul>
        <li><strong>Broken lint CI</strong>: ruff 0.16.5 enabled 67 extra rules; rule set pinned in <code>pyproject.toml</code>.</li>
        <li><strong>Two tests that tested nothing</strong> (result without <code>assert</code>, overly broad <code>pytest.raises(Exception)</code>).</li>
        <li>An integration test that was <strong>always skipped</strong> now loads a real .mat file.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Running outside Docker</span><ul>
        <li>TimescaleDB is no longer mandatory: falls back to a regular table with a warning on PostgreSQL.</li>
        <li>Dashboard: hard-coded MLflow address replaced by <code>MLFLOW_TRACKING_URI</code> (Alerts and Results tabs were empty otherwise).</li>
        <li>Service: <code>xgb.Booster</code> instead of <code>XGBClassifier</code>, which required scikit-learn in the image.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Additions</span><ul>
        <li><strong>FastAPI</strong> API + demo page, same indicator functions as in training, 9 tests.</li>
        <li><code>Dockerfile.api</code>, <strong>Kubernetes</strong> manifests (kustomize: local 6 objects, prod 8 objects).</li>
        <li>Reproducible benchmark, architecture diagrams, showcase page and video. <strong>223 tests passed</strong>, 0 failures.</li></ul></div>
</div>"""

EN_UPDATES = dict(
    kicker="Industrial ML · Signal · MLOps",
    lead="Fault diagnosis on the 32 real bearings of the Paderborn test rig from 5 explainable vibration indicators, "
         "with a validation that never puts the same bearing in both training and test, and a quantified measurement of the gap "
         "between lab-made and real faults. The model is served by a FastAPI API, containerizable and deployable on Kubernetes.",
    kpis=[("223", "tests (0 failures)"), ("0.734", "XGBoost macro F1, grouped CV"), ("0.62", "macro F1 artificial → real"),
          ("23.2 ms", "indicators per measurement, CPU"), ("5.4 GB", "Paderborn archives")],
    links=[("Source code", REPO, True), ("Showcase branch", BRANCH, False)],
    context=[
        "Most predictive maintenance demos test a model on the same bearings it saw during "
        "training: the scores look great and don't hold up on the shop floor.",
        "This project measures the lab / field gap, compares a vibration sensor with the <strong>motor current "
        "already available on every drive</strong> (no extra sensor needed) and favors indicators a maintenance manager "
        "can understand.",
        "Measured result: trained on machined faults, the model misses <strong>about 1 real fault in 5</strong>, "
        "versus about 1 in 14 when it has seen real faults. And it does not clearly beat a simple kurtosis rule.",
    ],
    rh=[
        "Real domain expertise (field deployments with IFM, Schaeffler, SKF) put to work for data.",
        "<strong>Sensor cost / value</strong> reasoning: can we avoid instrumenting a machine?",
        "Results published as they are, including when the model misses a real fault or fails to beat a simple rule.",
        "Project taken over and verified: figures reproduced, failing tests fixed, delivered all the way to an API and Kubernetes.",
    ],
    tech=[
        "5 time-domain indicators (RMS, peak-to-peak, crest factor, kurtosis, skewness); <strong>BPFO / BPFI / BSF / FTF</strong> "
        "fault frequencies computed from the geometry, envelope analysis still disabled.",
        "<code>StratifiedGroupKFold</code> grouped by bearing and an <code>assert_no_asset_leakage</code> safeguard; "
        "artificial → real benchmark over 20 splits of the healthy bearings.",
        "PostgreSQL / TimescaleDB (fallback without the extension), MLflow, dataset hash for traceability, Evidently drift.",
        "<strong>FastAPI</strong> service (<code>/predict</code> + demo page) using the same indicator functions as training; "
        "<code>Dockerfile.api</code> and <strong>kustomize</strong> local / prod manifests.",
        "CI: ruff (pinned rules), 223 tests, ML pipeline smoke test on 2 real bearings (K001, KA01).",
        "Physical simulators, SimPy factory simulation and Asset Administration Shell export (Industry 4.0).",
    ],
    stages=[
        ("Source", "source", ["Paderborn .mat (5.4 GB)"]),
        ("Ingestion", "ingest", ["Loaders + physical checks", "Parquet"]),
        ("Storage", "storage", ["PostgreSQL / TimescaleDB"]),
        ("Features", "process", ["Time domain: RMS, kurtosis", "BPFO/BPFI frequencies"]),
        ("Models", "ml", ["Thresholds (baseline)", "XGBoost", "CV grouped by bearing"]),
        ("Tracking", "ops", ["MLflow", "Evidently drift"]),
        ("Delivery", "ui", ["Streamlit digital twin", "AAS export"]),
        ("Serving", "serve", ["FastAPI /predict + demo", "Kubernetes (kustomize)"]),
    ],
    edges=FR_UPDATES["edges"][:-2] + [("s4n1", "s7n0", "exported model", False), ("s7n0", "s7n1", "", True)],
    band=("uv · GitHub Actions (ruff, pytest, ML smoke test on 2 real bearings) · Docker Compose · Dockerfile.api · kustomize", "infra"),
    steps=[
        "Download of the 32 Paderborn archives (5.4 GB, 22.4 GB extracted), parsing of file names (bearing, operating condition, fault) and physical plausibility checks; 1 unreadable file excluded and listed.",
        "Full ingestion in 473 s: 2,559 measurements, 7,677 signals, 46,062 indicators, stored site → area → machine → asset → bearing.",
        "Computation of time-domain indicators and characteristic fault frequencies from the bearing geometry.",
        "Comparison of a threshold baseline and XGBoost, with cross-validation grouped by bearing (no bearing in both train and test).",
        "Artificial → real benchmark: training on machined faults, testing on real faults, healthy bearings spread over 20 splits.",
        "MLflow tracking (dataset hash, macro F1, balanced accuracy) and Evidently train / test drift report.",
        "Model export (29 bearings, 3 held out for the demo) and FastAPI service; image and Kubernetes manifests.",
        "Streamlit delivery: alerts, indicators, factory digital twin, glossary.",
    ],
    extra_diagrams=[("maintenance-predictive-pipeline", "Data and ML pipeline"),
                    ("maintenance-predictive-evaluation", "Evaluation protocol: grouped CV and artificial → real"),
                    ("maintenance-predictive-service-kubernetes", "Inference service and Kubernetes"),
                    ("maintenance-predictive-signal-indicateurs", "From vibration signal to indicators")],
    tags=["Signal processing", "SciPy", "XGBoost", "scikit-learn", "PostgreSQL", "TimescaleDB", "MLflow", "Evidently", "Polars",
          "Streamlit", "FastAPI", "Docker", "Kubernetes", "SimPy", "uv", "GitHub Actions", "Industry 4.0"],
    stack=[
        ("NumPy / SciPy", "Signal processing, time-domain indicators, spectra", "Explainable physical features"),
        ("XGBoost / scikit-learn", "Fault classification, CV grouped by bearing", "ML on industrial data"),
        ("PostgreSQL / TimescaleDB", "Measurements and indicators; hypertable when the extension is present", "Storage suited to sensor data"),
        ("MLflow", "Baseline vs GBM experiments, dataset hash", "Traceability and reproducibility"),
        ("Evidently", "Train / test drift (KS)", "Detecting distribution shift"),
        ("FastAPI", "/predict API and demo page on real measurements", "Model serving"),
        ("Docker + Kubernetes (kustomize)", "Dedicated API image, local / prod overlays", "Deployment"),
        ("SimPy", "Discrete-event factory simulation", "Digital twin"),
        ("uv + ruff + pytest", "Locked dependencies, code quality, 223 tests", "Engineering hygiene"),
    ],
    matrix=dict(FR_UPDATES["matrix"]),
    matrix_notes=dict(ci="ruff + pytest + ML smoke test on 2 real bearings", tests="223 tests including anti-leakage and 9 API tests",
                      docker="Dockerfile.api and Compose; build not verified in this session (image simulated in a clean venv)",
                      tracking="MLflow, dataset hash", monitoring="Evidently + temporal drift",
                      serving="FastAPI /predict + demo page", deploy="kustomize local / prod manifests rendered, not applied to a cluster"),
    metrics=dict(head=["Approach", "Measured macro F1", "Previously published"], rows=[
        ["Kurtosis threshold (5-fold CV grouped by bearing)", "0.682 ± 0.158", "0.682 ± 0.158"],
        ["Crest factor threshold", "0.576 ± 0.174", "0.576 ± 0.174"],
        ["RMS threshold", "0.430 ± 0.090", "0.430 ± 0.090"],
        ["XGBoost vibration (5 indicators)", "0.734 ± 0.206", "0.738 ± 0.208"],
        ["XGBoost vibration + current (15 indicators)", "0.726 ± 0.219", "0.726 ± 0.222"],
        ["XGBoost current only (10 indicators)", "0.550 ± 0.123", "0.542 ± 0.121"],
        ["Artificial → real (20 splits of healthy bearings)", "0.620 ± 0.102", "—"],
        ["Control real → real", "0.694 ± 0.107", "—"],
    ], note="Measured on 27/10/2026. The deterministic baselines are reproduced to the thousandth; the small XGBoost differences most "
            "likely come from the library version (xgboost 3.4.1) and change no conclusion. "
            "Honest conclusion: XGBoost does not clearly beat a simple kurtosis rule (overlapping intervals, per-fold F1 "
            "from 0.473 to 0.978), and the gap between artificial and real faults is real."),
    snippets=[
        ("src/data/splits.py — safeguard against train/test leakage", FR_UPDATES["snippets"][0][1]),
        ("scripts/bench_vitrine.py — artificial → real generalization", FR_UPDATES["snippets"][1][1]),
        ("src/serving/predictor.py — inference with the same indicators as training", FR_UPDATES["snippets"][2][1]),
    ],
    limits=[
        "A single test rig, a single bearing model (6203), 32 bearings of which 6 healthy: standard deviations of 0.10 to 0.21 on macro F1; no guarantee of transfer to another machine.",
        "Time-domain indicators only: envelope analysis (BPFO / BPFI) stays disabled until band selection (kurtogram) is stable.",
        "Mixed operating conditions: generalization to an unseen operating condition is not measured.",
        "The artificial → real benchmark is exploratory; the full phase 3 awaits the kurtogram decision.",
        "Not verified in this session: <code>docker build</code> / <code>docker compose up</code>, TimescaleDB hypertable, deployment to a real cluster, API memory in a container, GitHub Actions CI (verified locally).",
        "Data under CC BY-NC 4.0 license (non-commercial use, citing Lessmeier et al., 2016).",
    ],
    strengths=[
        "<strong>Leak-free validation</strong>: CV grouped by bearing and an <code>assert_no_asset_leakage</code> safeguard, including in the artificial → real benchmark.",
        "<strong>Lab / field gap quantified</strong>: 0.620 macro F1 artificial → real versus 0.694 for the control; ~1 real fault in 5 missed.",
        "<strong>Figures reproduced before being published</strong>: baselines to the thousandth, XGBoost within 0.004, 6 real failures fixed.",
        "<strong>From signal to API</strong>: 5 explainable indicators in 23.2 ms, FastAPI, dedicated image and Kubernetes manifests.",
    ],
    custom_sections=[
        ("video", "Overview", "The project in 1 min 58", _VIDEO_EN),
        ("demo", "Live demo", "Three bearings never seen by the served model", _SHOTS_EN),
        ("artificiel-reel", "Key result", "Lab-made faults versus real faults", _TRANSFER_EN),
        ("corrections", "Takeover", "What I verified, fixed and added", _FIXES_EN),
    ],
)
