"""PredictIRA — vitrine du 2026-10-27 (branche feat/vitrine-predictira).

Source unique : docs/PORTFOLIO.md du dépôt PredictIRA (chiffres mesurés sur 2024, Ryzen 9 3900X, Python 3.12.3,
LightGBM 4.7.0). Fusionné par projects.py / projects_en.py avec dict.update sur la fiche « predictira ».
"""

GH = "https://github.com/PDUCLOS/"
BRANCH = "feat/vitrine-predictira"
MEDIA = "/media/predictira"

# --------------------------------------------------------------------------- FR

_VIDEO_FR = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 59 · générée par <code>scripts/promo_video.py</code> à partir des vraies captures (narration de synthèse).</p>"""

_SHOTS_FR = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-prediction.webp" alt="Formulaire de prédiction prérempli pour le Rhône, 2024-S05" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Interface d'origine corrigée : Rhône, 2024-S05, 1 363,57 passages prédits pour 1 738 observés.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-swagger.webp" alt="Swagger de l'API PredictIRA 2.0.0" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">API v2 : <code>POST /predict</code>, <code>/predict/batch</code> (1 à 1 000 lignes), schéma Pydantic de 24 champs obligatoires.</p></div>
</div>"""

_RESULTS_FR = f"""
<p>Test : 2024-S01 → S39, 11 départements d'Auvergne-Rhône-Alpes, <strong>429 semaines</strong>, très probablement hors entraînement
(le scaler livré a été ajusté sur 2 733 lignes d'année moyenne 2021,9 ; non démontrable sans les données d'entraînement).
La référence est la <strong>persistance S-1</strong> : « même valeur que la semaine précédente ».</p>
<div class="three-col" style="margin:1.2rem 0">
    <div class="arg-card arg-card--tech"><span class="arg-label">Le modèle seul</span><ul>
        <li>MAE <strong>41,2</strong> passages / semaine, R² <strong>0,926</strong>, WAPE 16,1 %.</li>
        <li>La persistance fait <strong>légèrement mieux</strong> : MAE 39,5, R² 0,930.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Selon la saison</span><ul>
        <li>Hiver (S01–S13) : modèle 65,9, persistance 68,7.</li>
        <li>Printemps-été (S14–S39) : modèle 28,9, persistance 24,9.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">La piste</span><ul>
        <li>Erreurs complémentaires : la moyenne 50/50 non ajustée donne MAE <strong>30,6</strong> (−26 %).</li>
        <li>Évaluée sur la période qui l'a suggérée : <strong>une piste, pas un résultat validé</strong>.</li></ul></div>
</div>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/eval-series.webp" alt="Séries 2024 observé, LightGBM et persistance pour le Rhône, l'Isère et le Cantal" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Observé, modèle et persistance S-1 sur 2024 (Rhône, Isère, Cantal).</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/eval-scatter.webp" alt="Nuage observé contre prédit, 429 semaines" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Observé contre prédit, 429 semaines. MAE par département : de 16,4 (Cantal) à 121,3 (Rhône).</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">Le modèle à 28 variables du dépôt « industrialisation » a été mesuré puis écarté : MAE 510,3, biais +487,5.
Prochaine étape naturelle : réentraîner avec la valeur S-1 comme variable.</p>"""

_FIXES_FR = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Constat (reproduit)</th><th>Correction</th></tr></thead>
    <tbody>
        <tr><td>Préremplissage par égalité exacte de <code>week_cos</code> : <strong>9 semaines sur 39 sans résultat</strong> (arrondi flottant), S27 → S25 et S29 → S23 (même cosinus pour s et 52 − s).</td>
            <td>Semaine reconstruite par le rang puis contrôlée par le cosinus ; un test rejoue l'ancien filtre.</td></tr>
        <tr><td>Champ caché <code>week_cos</code> rempli avec le numéro brut de la semaine (ex. 10).</td>
            <td>Cosinus calculé dans le navigateur ; erreur 404 affichée.</td></tr>
        <tr><td>Puy-de-Dôme (63) proposé dans l'interface, absent des données.</td>
            <td>Liste des départements générée depuis les données.</td></tr>
        <tr><td>Champ vide → NaN : une prédiction était quand même renvoyée.</td>
            <td>Pydantic : 400 (champ vide), 422 (non numérique, hors bornes, inconnu).</td></tr>
        <tr><td>Dépôt « industrialisation » : le client envoie 5 variables inconnues du modèle et en omet 5 ; LightGBM prédit par position (1 115 passages, valeur sans signification).</td>
            <td>Client corrigé ; l'API renvoie 422 avec la liste des variables manquantes / inconnues.</td></tr>
        <tr><td>Modèles livrés en pickle (exécution de code possible au chargement).</td>
            <td>Export texte LightGBM + JSON, lecture des pickles sous liste blanche ; plus aucun pickle chargé à l'exécution.</td></tr>
    </tbody></table></div>"""

FR_UPDATES = dict(
    kicker="ML santé publique · Projet d'équipe relancé en 2026",
    title="PredictIRA — estimer les passages aux urgences respiratoires",
    title_html='Estimer les <span class="highlight">urgences respiratoires</span> de la semaine, et le mesurer honnêtement',
    lead="Estimation hebdomadaire des passages aux urgences pour infections respiratoires aiguës, par département, à partir des "
         "recherches Google de symptômes, de la pollution, de la météo et de l'indice grippal. Projet d'équipe relancé en 2026 : "
         "mesuré sur 429 semaines de 2024, six défauts corrigés, API FastAPI validée, déployable sur Kubernetes.",
    kpis=[("0,926", "R² sur 2024 (hors entraînement)"), ("41", "MAE, passages / semaine"),
          ("24", "variables"), ("13", "tests")],
    links=[("Code source (v2)", GH + "PredictIRA/tree/" + BRANCH, True),
           ("Dépôt d'origine", GH + "PredictIRA", False),
           ("Dépôt « industrialisation »", GH + "industrialisation/tree/" + BRANCH, False)],
    context=[
        "Les épidémies respiratoires saturent les urgences chaque hiver, et les données hospitalières consolidées arrivent "
        "avec retard. L'objectif : <strong>estimer la charge de la semaine en cours</strong> à partir de signaux disponibles "
        "tout de suite (recherches de symptômes, pollution, météo, indice grippal).",
        "Projet d'équipe de formation (M2i) à 4, relancé en 2026 : audit, mesure sur 2024 comparée à une référence naïve, "
        "corrections, nouvelle API et déploiement Kubernetes.",
    ],
    rh=[
        "<strong>Honnêteté sur le résultat</strong> : comparé à « même valeur que la semaine précédente », le modèle seul fait "
        "légèrement moins bien sur 2024 (MAE 41,2 contre 39,5). C'est écrit, et la piste qui en découle aussi.",
        "<strong>Reprise d'un projet existant</strong> : six défauts reproduits avant d'être corrigés, chacun couvert par un test ou une validation.",
        "Travail en équipe de 4 sur un sujet d'intérêt public.",
    ],
    tech=[
        "LightGBM (100 arbres) sur <strong>24 variables</strong> : 12 symptômes Google Trends, CO, NO₂, O₃, PM2.5, SO₂, IQA, pression, T° max, indice grippal, département, année, semaine (<code>week_cos</code>).",
        "<strong>Audit des pickles</strong> (<code>pickletools</code>), unpickler à liste blanche, export en texte LightGBM + JSON : plus aucun pickle chargé à l'exécution.",
        "API <strong>FastAPI</strong> : schéma Pydantic (24 champs obligatoires, bornes physiques, champs inconnus refusés), lot de 1 à 1 000 lignes ; interface Flask d'origine montée sur <code>/</code> (a2wsgi).",
        "Évaluation reproductible (<code>scripts/evaluate.py</code>) ; latence d'inférence 0,431 ms p50 par ligne, <code>POST /api/predict</code> 7,05 ms p50 de bout en bout.",
        "Dockerfile <code>python:3.12-slim</code> non root, kustomize base + overlays <code>local</code> / <code>cloud</code> (HPA 2 → 6, NetworkPolicy, PDB).",
    ],
    stages=[
        ("Sources", "source", ["Google Trends (12 symptômes)", "Air · météo", "Indice grippal"]),
        ("Préparation", "process", ["Table département × semaine", "StandardScaler (JSON)"]),
        ("Modèle", "ml", ["LightGBM 24 variables"]),
        ("Mesure", "ops", ["2024 vs persistance S-1"]),
        ("Service", "serve", ["FastAPI /api (Pydantic)", "Flask / (a2wsgi)"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
           ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False), ("s2n0", "s3n0", "évalue", True),
           ("s2n0", "s4n0", "", False), ("s2n0", "s4n1", "", False)],
    band=("Docker python:3.12-slim (non root) · 13 tests pytest · kustomize local / cloud", "infra"),
    steps=[
        "<strong>Table hebdomadaire</strong> — département × semaine, semaine encodée par <code>week_cos</code> (reconstruite par le rang, puis contrôlée).",
        "<strong>Normalisation</strong> — <code>StandardScaler</code> livré, relu sous liste blanche et exporté en JSON.",
        "<strong>Modèle</strong> — LightGBM 24 variables exporté en texte : estimation des passages de la semaine (nowcasting).",
        "<strong>Mesure</strong> — 429 semaines de 2024 comparées à la persistance S-1, par période et par département.",
        "<strong>Service</strong> — une seule application : API FastAPI validée par Pydantic sur <code>/api</code>, interface Flask d'origine sur <code>/</code>.",
        "<strong>Déploiement</strong> — image Docker non root, manifestes kustomize rendus et validés.",
    ],
    extra_diagrams=[("predictira-app", "Architecture applicative : un conteneur, deux interfaces, un modèle sans pickle"),
                    ("predictira-donnees-evaluation", "Données, modèle et évaluation honnête sur 2024"),
                    ("predictira-kubernetes", "Déploiement Kubernetes : kustomize base + overlays local / cloud"),
                    ("predictira-audit", "Audit 2026 : constats et corrections")],
    tags=["LightGBM", "FastAPI", "Pydantic", "Flask", "Docker", "Kubernetes", "pytest", "Évaluation", "Santé publique"],
    stack=[
        ("LightGBM", "Régression du nombre de passages, modèle exporté en texte", "Gradient boosting"),
        ("scikit-learn (StandardScaler)", "Normalisation, relue sous liste blanche puis exportée en JSON", "Préparation des données"),
        ("FastAPI + Pydantic", "API /predict et /predict/batch, schéma strict de 24 champs", "Service de modèles"),
        ("Flask + a2wsgi", "Interface d'origine montée dans la même application", "Reprise de l'existant"),
        ("pytest", "13 tests, dont le rejeu de l'ancien filtre et le refus d'un pickle malveillant", "Non-régression"),
        ("Docker", "python:3.12-slim, non root, healthcheck", "Conteneurisation"),
        ("Kubernetes (kustomize)", "HPA, PDB, NetworkPolicy, overlays local / cloud", "Déploiement"),
    ],
    matrix=dict(ci="n", tests="y", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="p", iac="p"),
    matrix_notes=dict(tests="13 tests pytest", docker="Dockerfile python:3.12-slim non root ; build non vérifié (moteur arrêté)",
                      serving="FastAPI + Pydantic, Flask monté sur /",
                      deploy="Manifestes validés (kubectl kustomize), non appliqués sur cluster",
                      iac="kustomize base + overlays local / cloud"),
    metrics=dict(head=["Modèle", "MAE", "RMSE", "R²", "WAPE", "Biais moyen"], rows=[
        ["LightGBM 24 variables (application Flask)", "41,2", "69,5", "0,926", "16,1 %", "−2,5"],
        ["Référence : persistance S-1", "39,5", "67,8", "0,930", "15,4 %", "+11,4"],
        ["Exploratoire : moyenne 50/50 modèle + persistance", "30,6", "50,0", "0,962", "11,9 %", "+4,5"],
        ["LightGBM 28 variables (dépôt « industrialisation »)", "510,3", "534,7", "−3,358", "198,8 %", "+487,5"],
    ], note="Test : 2024-S01 → S39, 11 départements, 429 semaines ; cible moyenne observée 256,7 passages / semaine. "
            "Seul, le modèle ne bat pas la persistance ; la moyenne 50/50, choisie a priori, est évaluée sur la période "
            "qui l'a suggérée : c'est une piste, pas un résultat validé."),
    snippets=[
        ("Code d'origine (app.py) — le filtre défectueux",
         '''def get_data(year, week, dept):
    week_cos = cos(2 * pi * week / 52)
    print (week_cos)
    # Filtrer le DataFrame
    filtered_df = df[(df["year"] == year) & (df["week_cos"] == week_cos) & (df["dept"] == dept)]'''),
        ("predictira/data.py — la correction",
         '''def load_dataset(root: str | Path) -> pd.DataFrame:
    df = pd.read_csv(Path(root) / "df_Test_Indust.csv")
    # week_cos seul est ambigu : cos(2π·w/52) = cos(2π·(52-w)/52), donc S30 et S22 sont
    # indiscernables. Le fichier est trié chronologiquement par département (2024-S01→S39,
    # puis la ligne 2023-S52) : on reconstruit la semaine par le rang, puis on vérifie le cosinus.
    df["week"] = df.groupby(["dept", "year"]).cumcount() + 1
    df.loc[df["year"] == 2023, "week"] = 52
    expected = np.cos(2 * np.pi * df["week"] / 52)
    if not np.allclose(expected, df["week_cos"], atol=1e-9):
        raise ValueError("Ordre des semaines incohérent avec week_cos")
    return df'''),
        ("predictira/safe_load.py — pickles hérités lus sous liste blanche",
         '''class _AllowListUnpickler(numpy_pickle.NumpyUnpickler):
    def find_class(self, module, name):
        if (module, name) not in ALLOWED:
            raise pickle.UnpicklingError(f"classe interdite dans le pickle : {module}.{name}")
        return super().find_class(module, name)'''),
        ("predictira/api.py — l'endpoint de prédiction validé",
         '''@api.post("/predict", response_model=Prediction)
def predict(features: Features) -> Prediction:
    value = float(model.predict_frame(pd.DataFrame([features.model_dump()]))[0])
    return Prediction(prediction=round(value, 1), modele=MODEL_NAME)'''),
    ],
    limits=[
        "Nowcasting : le modèle estime la semaine courante à partir de ses propres signaux ; ce n'est pas une prévision à J+7.",
        "Seul, il ne bat pas la persistance S-1 sur 2024 (MAE 41,2 contre 39,5) ; la combinaison des deux est la piste d'amélioration, non validée.",
        "11 départements d'Auvergne-Rhône-Alpes seulement ; le département est une variable numérique (31,5 % du gain) : aucune généralisation possible à d'autres départements.",
        "39 semaines de test, dont 13 d'hiver : estimation de l'erreur hivernale fragile. Semaine encodée sans sinus : s et 52 − s sont indiscernables pour le modèle.",
        "Aucune source de données citée et pas de données d'entraînement : réentraînement impossible, absence de 2024 dans l'entraînement probable mais non démontrable.",
        "<code>docker build</code> non exécuté pendant la session (contenu de l'image testé dans un environnement vierge) ; Kubernetes validé par rendu seulement.",
    ],
    strengths=[
        "<strong>Mesure honnête</strong> : 429 semaines de 2024 comparées à une référence naïve ; le modèle seul ne la bat pas, et c'est affiché.",
        "<strong>Une piste chiffrée</strong> : erreurs complémentaires, la moyenne modèle + persistance réduit la MAE de 26 % (à valider).",
        "<strong>Audit qui rend le projet fiable</strong> : six défauts reproduits et corrigés, plus aucun pickle chargé, 13 tests.",
        "<strong>Du projet de formation au service</strong> : API FastAPI validée par Pydantic, image Docker non root, kustomize local / cloud.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 59", _VIDEO_FR),
        ("resultats", "Résultats mesurés", "Le modèle face à « même valeur que la semaine précédente »", _RESULTS_FR),
        ("corrections", "Audit 2026", "Six défauts reproduits, puis corrigés", _FIXES_FR),
        ("demo", "Démo réelle", "Captures prises sur l'application en fonctionnement", _SHOTS_FR),
    ],
)

# --------------------------------------------------------------------------- EN

_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 59, narrated in French · generated by <code>scripts/promo_video.py</code> from real screenshots (synthetic voice).</p>"""

_SHOTS_EN = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-prediction.webp" alt="Prediction form prefilled for the Rhône, 2024-W05" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Original interface, fixed: Rhône, 2024-W05, 1,363.57 visits predicted vs 1,738 observed.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-swagger.webp" alt="Swagger page of the PredictIRA 2.0.0 API" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">v2 API: <code>POST /predict</code>, <code>/predict/batch</code> (1 to 1,000 rows), Pydantic schema with 24 required fields.</p></div>
</div>"""

_RESULTS_EN = f"""
<p>Test: 2024-W01 → W39, 11 departments of Auvergne-Rhône-Alpes, <strong>429 weeks</strong>, very likely outside training
(the shipped scaler was fitted on 2,733 rows with a mean year of 2021.9; not provable without the training data).
The baseline is <strong>W-1 persistence</strong>: “same value as last week”.</p>
<div class="three-col" style="margin:1.2rem 0">
    <div class="arg-card arg-card--tech"><span class="arg-label">The model alone</span><ul>
        <li>MAE <strong>41.2</strong> visits / week, R² <strong>0.926</strong>, WAPE 16.1%.</li>
        <li>Persistence does <strong>slightly better</strong>: MAE 39.5, R² 0.930.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">By season</span><ul>
        <li>Winter (W01–W13): model 65.9, persistence 68.7.</li>
        <li>Spring-summer (W14–W39): model 28.9, persistence 24.9.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">The lead</span><ul>
        <li>Complementary errors: the untuned 50/50 average gives MAE <strong>30.6</strong> (−26%).</li>
        <li>Evaluated on the period that suggested it: <strong>a lead, not a validated result</strong>.</li></ul></div>
</div>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/eval-series.webp" alt="2024 series: observed, LightGBM and persistence for the Rhône, Isère and Cantal" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Observed, model and W-1 persistence over 2024 (Rhône, Isère, Cantal; chart labels in French).</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/eval-scatter.webp" alt="Observed vs predicted scatter, 429 weeks" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Observed vs predicted, 429 weeks. MAE by department: from 16.4 (Cantal) to 121.3 (Rhône).</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">The 28-feature model from the “industrialisation” repository was measured, then discarded: MAE 510.3, bias +487.5.
Natural next step: retrain with the W-1 value as a feature.</p>"""

_FIXES_EN = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Finding (reproduced)</th><th>Fix</th></tr></thead>
    <tbody>
        <tr><td>Prefill by exact equality on <code>week_cos</code>: <strong>9 weeks out of 39 returned nothing</strong> (floating-point rounding), W27 → W25 and W29 → W23 (same cosine for w and 52 − w).</td>
            <td>Week rebuilt from row order, then checked against the cosine; a test replays the old filter.</td></tr>
        <tr><td>Hidden <code>week_cos</code> field filled with the raw week number (e.g. 10).</td>
            <td>Cosine computed in the browser; 404 error shown.</td></tr>
        <tr><td>Puy-de-Dôme (63) offered in the interface, absent from the data.</td>
            <td>Department list generated from the data.</td></tr>
        <tr><td>Empty field → NaN: a prediction was returned anyway.</td>
            <td>Pydantic: 400 (empty field), 422 (non-numeric, out of bounds, unknown).</td></tr>
        <tr><td>“industrialisation” repository: the client sends 5 features unknown to the model and omits 5; LightGBM predicts by position (1,115 visits, a meaningless value).</td>
            <td>Client fixed; the API returns 422 listing missing / unknown features.</td></tr>
        <tr><td>Models shipped as pickles (code execution possible on load).</td>
            <td>LightGBM text + JSON export, pickles read through an allow-list; no pickle is loaded at runtime anymore.</td></tr>
    </tbody></table></div>"""

EN_UPDATES = dict(
    kicker="Public health ML · Team project, revived in 2026",
    title="PredictIRA — estimating respiratory emergency department visits",
    title_html='Estimating this week\'s <span class="highlight">respiratory emergencies</span>, and measuring it honestly',
    lead="Weekly estimate of emergency department visits for acute respiratory infections, by French department, based on "
         "Google symptom searches, pollution, weather and the flu index. Team project revived in 2026: measured on 429 weeks "
         "of 2024, six defects fixed, validated FastAPI API, deployable on Kubernetes.",
    kpis=[("0.926", "R² on 2024 (outside training)"), ("41", "MAE, visits / week"),
          ("24", "features"), ("13", "tests")],
    links=[("Source code (v2)", GH + "PredictIRA/tree/" + BRANCH, True),
           ("Original repository", GH + "PredictIRA", False),
           ("“industrialisation” repository", GH + "industrialisation/tree/" + BRANCH, False)],
    context=[
        "Respiratory epidemics overwhelm emergency departments every winter, and consolidated hospital data arrives late. "
        "The goal: <strong>estimate the load of the current week</strong> from signals available right away "
        "(symptom searches, pollution, weather, flu index).",
        "Training team project (M2i) in a group of 4, revived in 2026: audit, measurement on 2024 against a naive baseline, "
        "fixes, a new API and Kubernetes deployment.",
    ],
    rh=[
        "<strong>Honest about the result</strong>: against “same value as last week”, the model alone does slightly worse "
        "on 2024 (MAE 41.2 vs 39.5). That is stated, along with the lead it opens.",
        "<strong>Taking over an existing project</strong>: six defects reproduced before being fixed, each covered by a test or a validation.",
        "Teamwork in a group of 4 on a public-interest topic.",
    ],
    tech=[
        "LightGBM (100 trees) on <strong>24 features</strong>: 12 Google Trends symptoms, CO, NO₂, O₃, PM2.5, SO₂, AQI, pressure, max temperature, flu index, department, year, week (<code>week_cos</code>).",
        "<strong>Pickle audit</strong> (<code>pickletools</code>), allow-list unpickler, export to LightGBM text + JSON: no pickle is loaded at runtime anymore.",
        "<strong>FastAPI</strong> API: Pydantic schema (24 required fields, physical bounds, unknown fields rejected), batches of 1 to 1,000 rows; original Flask interface mounted on <code>/</code> (a2wsgi).",
        "Reproducible evaluation (<code>scripts/evaluate.py</code>); inference latency 0.431 ms p50 per row, <code>POST /api/predict</code> 7.05 ms p50 end to end.",
        "<code>python:3.12-slim</code> non-root Dockerfile, kustomize base + <code>local</code> / <code>cloud</code> overlays (HPA 2 → 6, NetworkPolicy, PDB).",
    ],
    stages=[
        ("Sources", "source", ["Google Trends (12 symptoms)", "Air quality · weather", "Flu index"]),
        ("Preparation", "process", ["Department × week table", "StandardScaler (JSON)"]),
        ("Model", "ml", ["LightGBM, 24 features"]),
        ("Measurement", "ops", ["2024 vs W-1 persistence"]),
        ("Service", "serve", ["FastAPI /api (Pydantic)", "Flask / (a2wsgi)"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
           ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False), ("s2n0", "s3n0", "evaluates", True),
           ("s2n0", "s4n0", "", False), ("s2n0", "s4n1", "", False)],
    band=("Docker python:3.12-slim (non-root) · 13 pytest tests · kustomize local / cloud", "infra"),
    steps=[
        "<strong>Weekly table</strong> — department × week, week encoded as <code>week_cos</code> (rebuilt from row order, then checked).",
        "<strong>Normalization</strong> — shipped <code>StandardScaler</code>, read through an allow-list and exported to JSON.",
        "<strong>Model</strong> — 24-feature LightGBM exported as text: estimate of the week's visits (nowcasting).",
        "<strong>Measurement</strong> — 429 weeks of 2024 compared with W-1 persistence, by period and by department.",
        "<strong>Service</strong> — a single application: Pydantic-validated FastAPI API on <code>/api</code>, original Flask interface on <code>/</code>.",
        "<strong>Deployment</strong> — non-root Docker image, kustomize manifests rendered and validated.",
    ],
    extra_diagrams=[("predictira-app", "Application architecture: one container, two interfaces, a pickle-free model (labels in French)"),
                    ("predictira-donnees-evaluation", "Data, model and honest evaluation on 2024 (labels in French)"),
                    ("predictira-kubernetes", "Kubernetes deployment: kustomize base + local / cloud overlays (labels in French)"),
                    ("predictira-audit", "2026 audit: findings and fixes (labels in French)")],
    tags=["LightGBM", "FastAPI", "Pydantic", "Flask", "Docker", "Kubernetes", "pytest", "Evaluation", "Public health"],
    stack=[
        ("LightGBM", "Regression of visit counts, model exported as text", "Gradient boosting"),
        ("scikit-learn (StandardScaler)", "Normalization, read through an allow-list then exported to JSON", "Data preparation"),
        ("FastAPI + Pydantic", "/predict and /predict/batch API, strict 24-field schema", "Model serving"),
        ("Flask + a2wsgi", "Original interface mounted in the same application", "Taking over existing code"),
        ("pytest", "13 tests, including a replay of the old filter and rejection of a malicious pickle", "Non-regression"),
        ("Docker", "python:3.12-slim, non-root, healthcheck", "Containerization"),
        ("Kubernetes (kustomize)", "HPA, PDB, NetworkPolicy, local / cloud overlays", "Deployment"),
    ],
    matrix=dict(ci="n", tests="y", docker="y", orch="n", tracking="n", monitoring="n", serving="y", deploy="p", iac="p"),
    matrix_notes=dict(tests="13 pytest tests", docker="python:3.12-slim non-root Dockerfile; build not verified (engine stopped)",
                      serving="FastAPI + Pydantic, Flask mounted on /",
                      deploy="Manifests validated (kubectl kustomize), not applied to a cluster",
                      iac="kustomize base + local / cloud overlays"),
    metrics=dict(head=["Model", "MAE", "RMSE", "R²", "WAPE", "Mean bias"], rows=[
        ["LightGBM, 24 features (Flask application)", "41.2", "69.5", "0.926", "16.1%", "−2.5"],
        ["Baseline: W-1 persistence", "39.5", "67.8", "0.930", "15.4%", "+11.4"],
        ["Exploratory: 50/50 average of model + persistence", "30.6", "50.0", "0.962", "11.9%", "+4.5"],
        ["LightGBM, 28 features (“industrialisation” repository)", "510.3", "534.7", "−3.358", "198.8%", "+487.5"],
    ], note="Test: 2024-W01 → W39, 11 departments, 429 weeks; mean observed target 256.7 visits / week. "
            "On its own, the model does not beat persistence; the 50/50 average, chosen a priori, is evaluated on the period "
            "that suggested it: it is a lead, not a validated result."),
    snippets=[
        ("Original code (app.py) — the faulty filter",
         FR_UPDATES["snippets"][0][1]),
        ("predictira/data.py — the fix (comments in French)",
         FR_UPDATES["snippets"][1][1]),
        ("predictira/safe_load.py — legacy pickles read through an allow-list",
         FR_UPDATES["snippets"][2][1]),
        ("predictira/api.py — the validated prediction endpoint",
         FR_UPDATES["snippets"][3][1]),
    ],
    limits=[
        "Nowcasting: the model estimates the current week from that week's own signals; it is not a 7-day-ahead forecast.",
        "On its own it does not beat W-1 persistence on 2024 (MAE 41.2 vs 39.5); combining both is the improvement lead, not yet validated.",
        "Only 11 departments of Auvergne-Rhône-Alpes; the department is a numeric feature (31.5% of gain): no generalization to other departments.",
        "39 test weeks, 13 of them in winter: the winter error estimate is fragile. Week encoded without a sine: weeks w and 52 − w are indistinguishable to the model.",
        "No data source cited and no training data: retraining is impossible; 2024 being absent from training is likely but not provable.",
        "<code>docker build</code> not run during the session (image contents tested in a clean environment); Kubernetes validated by rendering only.",
    ],
    strengths=[
        "<strong>Honest measurement</strong>: 429 weeks of 2024 compared with a naive baseline; the model alone does not beat it, and that is shown.",
        "<strong>A quantified lead</strong>: complementary errors, the model + persistence average cuts MAE by 26% (to be validated).",
        "<strong>An audit that makes the project reliable</strong>: six defects reproduced and fixed, no pickle loaded anymore, 13 tests.",
        "<strong>From training project to service</strong>: Pydantic-validated FastAPI API, non-root Docker image, local / cloud kustomize.",
    ],
    custom_sections=[
        ("video", "Overview", "The project in 1 min 59", _VIDEO_EN),
        ("results", "Measured results", "The model vs “same value as last week”", _RESULTS_EN),
        ("fixes", "2026 audit", "Six defects reproduced, then fixed", _FIXES_EN),
        ("demo", "Live demo", "Screenshots taken on the running application", _SHOTS_EN),
    ],
)
