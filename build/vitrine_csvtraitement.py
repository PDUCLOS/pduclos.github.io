"""Vitrine Csvtraitement (branche feat/vitrine-csvtraitement) : surcharges FR / EN.

Source unique : docs/PORTFOLIO.md du dépôt Csvtraitement, mesures du 27/10/2026
(Ryzen 9 3900X, 32 Go, Windows 11, Python 3.12, un cœur ; fichiers synthétiques, graine 42).
Fusionné par projects.py / projects_en.py avec dict.update.
"""

GH = "https://github.com/PDUCLOS/"
REPO = GH + "Csvtraitement"
BRANCH = REPO + "/tree/feat/vitrine-csvtraitement"
MEDIA = "/media/csvtraitement"

_IMG = 'loading="lazy" draggable="false" style="min-width:0"'


# ------------------------------------------------------------------ FR
_VIDEO_FR = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 54 · générée par <code>scripts/promo_video.py</code> (narration de synthèse, fond sonore synthétisé). Toutes les données affichées sont synthétiques.</p>"""

_SHOTS_FR = f"""
<div class="pipeline-figure" style="padding:.6rem;margin-bottom:.4rem;min-width:0"><img src="{MEDIA}/avant-apres.webp" alt="Ligne 30 avant et après correction" {_IMG}></div>
<p class="code-caption" style="margin-bottom:1.6rem">Ligne 30 : la quantité manque, tout est décalé d'une colonne. Après correction : cellule vide insérée au bon endroit, dates ISO, montants numériques.</p>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-anomalies.webp" alt="Onglet Anomalies : décalages de colonnes détectés" {_IMG}></div>
        <p class="code-caption">Onglet Anomalies : chaque ligne décalée, le type (colonne en trop / manquante) et la colonne où commence le décalage.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-doublons.webp" alt="Onglet Doublons : groupes exacts et flous" {_IMG}></div>
        <p class="code-caption">Onglet Doublons : doublons exacts et quasi-doublons (similarité &gt; 85 %), avec la colonne qui diffère.</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">Captures réelles de l'interface Tkinter (<code>scripts/capture_gui.py</code>) sur l'export de démonstration synthétique de 1 000 lignes.</p>"""

_PERF_FR = """
<div class="table-wrap"><table class="stack-table">
<thead><tr><th>Lignes</th><th>Fichier</th><th>Cœur (détection → export CSV)</th><th>Score qualité</th><th>Export XLSX</th><th>Pic mémoire</th></tr></thead>
<tbody>
<tr><td>10 000</td><td>1,4 Mo</td><td>0,97 s</td><td>0,61 s</td><td>1,77 s</td><td>110 Mo</td></tr>
<tr><td>100 000</td><td>14 Mo</td><td>7,28 s</td><td>6,12 s</td><td>13,8 s</td><td>516 Mo</td></tr>
<tr><td>500 000</td><td>71 Mo</td><td>35,3 s</td><td>31,3 s</td><td>69,2 s</td><td>2,22 Go</td></tr>
<tr><td>1 000 000</td><td>142 Mo</td><td><strong>63,5 s</strong></td><td>52,3 s</td><td>133,8 s</td><td>2,42 Go</td></tr>
</tbody></table></div>
<p class="code-caption" style="margin-top:.8rem">Un processus par taille, sur un cœur, machine partagée avec d'autres traitements : ce sont des ordres de grandeur. Débit du cœur : 10 300 à 15 700 lignes/s.
La lecture est en flux, mais les corrections sont gardées en mémoire pour la revue humaine (preview, undo) : 1,47 Go après corrections à 1 M de lignes.</p>"""

_FIXES_FR = """
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · Mesurer avec une vérité terrain</span><ul>
        <li>Générateur d'exports ERP synthétiques : 11 colonnes façon SAP, <strong>8 types d'anomalies injectées</strong> et connues.</li>
        <li>Banc de 10 000 à <strong>1 000 000 de lignes</strong> : temps, mémoire, taux de détection, faux positifs.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · Corriger ce que la mesure révèle</span><ul>
        <li><strong>CLI inutilisable</strong> : toute analyse levait <code>UnboundLocalError</code>.</li>
        <li><strong>Doublons flous quadratiques</strong> : un seul bloc dès que la 1re colonne a un préfixe constant ; 240 s → 2,0 s sur 10 000 lignes.</li>
        <li><strong>Texte perdu au réalignement</strong> (« Martinez;SARL » perdait « SARL ») : 32 % → 100 % de lignes restituées.</li>
        <li><strong>Valeurs masquées jamais nettoyées</strong> (<code>#REF!</code> exporté tel quel) ; <code>--compare</code> / <code>--reconcile</code> : 0/2 → 2/2 écarts trouvés.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · Vérifier</span><ul>
        <li><strong>100 %</strong> des décalages trouvés, <strong>0</strong> faux positif, taux identiques de 10 000 à 1 000 000 de lignes.</li>
        <li><strong>84 tests</strong> pytest verts (59 au départ, tous verts aussi).</li>
        <li>README corrigé : il annonçait une licence MIT, le fichier LICENSE est « tous droits réservés ».</li></ul></div>
</div>"""

FR_UPDATES = dict(
    title_html='Des exports ERP <span class="highlight">propres</span>, même à un million de lignes',
    lead="Application Python (interface Tkinter + CLI) qui détecte et corrige les défauts des exports ERP : colonnes décalées, "
         "décimales FR/US, dates invalides, valeurs masquées, doublons, données personnelles — avec revue humaine avant export. "
         "Testée sur 1 000 000 de lignes avec vérité terrain.",
    kpis=[("1 M", "lignes traitées en 63 s"), ("100 %", "décalages trouvés, 0 faux positif"),
          ("×120", "doublons flous plus rapides"), ("84", "tests")],
    links=[("Code source", REPO, True), ("Branche vitrine (vidéo, schémas, mesures)", BRANCH, False)],
    context=[
        "Tout analyste qui travaille avec SAP connaît le problème : un export CSV avec une colonne décalée, des montants "
        "« 1.234,56 » et « 1,234.56 » mélangés, des dates <code>00.00.0000</code> ou des <code>#REF!</code>. "
        "Le nettoyage manuel prend des heures et reste source d'erreurs.",
        "Csvtraitement automatise la détection, propose les corrections, et laisse l'utilisateur valider avant d'exporter. "
        "Pour savoir ce qu'il vaut vraiment, il a été mesuré sur des exports synthétiques dont chaque défaut injecté est connu : "
        "la mesure a révélé six défauts du code, corrigés depuis.",
    ],
    rh=[
        "Né d'un irritant vécu au quotidien sur des extractions SAP.",
        "Gain de temps direct pour les équipes Achats, ADV, contrôle de gestion.",
        "Humain dans la boucle dans l'interface : aucune correction appliquée sans validation, undo / redo.",
        "<strong>Démarche de vérification</strong> : affirmations de la fiche reprises une à une, mesurées, corrigées quand elles étaient fausses.",
    ],
    tech=[
        "Lecture en <strong>flux par blocs de 10 000 lignes</strong> (<code>csv.reader</code>) ; Parquet lu en <code>iter_batches</code>.",
        "Détection automatique de l'encodage et du séparateur (score moyenne / (1 + écart-type)), typage de colonnes sur échantillon.",
        "Réalignement des lignes décalées : un champ texte coupé par un séparateur non échappé est <strong>recollé</strong>, pas tronqué.",
        "Doublons exacts et flous : <strong>blocage multi-clés</strong> sur les colonnes discriminantes + préfiltre <code>difflib</code> (mêmes décisions que <code>ratio()</code>).",
        "Masquage de données personnelles (e-mail, téléphone, IBAN, NIR), colonnes PII détectées automatiquement.",
        "Interface Tkinter 8 onglets, CLI batch ; image Docker CLI et CronJob Kubernetes (kustomize) pour le traitement de nuit.",
    ],
    steps=[
        "Lecture de n'importe quel format tabulaire (6 lus : CSV, XLSX, XLS, ODS, JSON, Parquet), converti en flux CSV traité par blocs.",
        "Détection de l'encodage, du séparateur et du type de chaque colonne sur un échantillon (1 000 premières + 1 000 lignes aléatoires).",
        "Repérage cellule par cellule des décalages de colonnes, score qualité pondéré, recherche de doublons exacts et flous.",
        "Corrections proposées (dates ISO, décimales, parenthèses comptables, valeurs masquées, réalignement) et masquage optionnel des données personnelles.",
        "Validation par l'utilisateur, puis export (5 formats écrits) — en XLSX, cellules corrigées surlignées et feuille de rapport.",
        "Sur un serveur : la même CLI, sans interface, planifiée chaque nuit par un CronJob Kubernetes.",
    ],
    extra_diagrams=[
        ("csvtraitement-pipeline", "Pipeline : du fichier ERP « sale » au fichier corrigé, en 6 étapes"),
        ("csvtraitement-memoire", "Ce qui est lu en flux, et ce qui reste en mémoire"),
        ("csvtraitement-doublons", "Doublons flous : blocage multi-clés et préfiltre, 240 s → 2,0 s"),
        ("csvtraitement-deploiement", "Déploiement : un traitement par lots (CronJob), pas un serveur"),
    ],
    tags=["Python", "Tkinter", "CLI", "Streaming", "Data Quality", "chardet", "xlsxwriter", "pyarrow", "pytest",
          "Docker", "Kubernetes"],
    stack=[
        ("Python standard library", "csv, difflib, statistics, argparse, logging", "Solide sans dépendances lourdes"),
        ("chardet", "Détection d'encodage", "Robustesse aux exports hétérogènes"),
        ("xlsxwriter (constant_memory)", "Export Excel annoté", "Gros volumes en écriture"),
        ("pyarrow", "Lecture / écriture Parquet", "Interopérabilité data"),
        ("Tkinter", "Interface graphique 8 onglets", "Outil utilisable par un non-développeur"),
        ("pytest", "84 tests, dont bout en bout sur exports synthétiques avec vérité terrain", "Fiabilité mesurée"),
        ("Docker + Kubernetes (kustomize)", "Image CLI non root, CronJob nocturne, PVC", "Industrialisation du traitement par lots"),
    ],
    matrix=dict(ci="n", tests="y", docker="p", orch="p", tracking="n", monitoring="n", serving="n", deploy="p", iac="p"),
    matrix_notes=dict(tests="84 tests pytest (détection, correction, bout en bout avec vérité terrain)",
                      docker="Dockerfile CLI (python:3.12-slim, non root) ; build non vérifié",
                      orch="CronJob Kubernetes nocturne (02:00, Forbid)",
                      deploy="Manifestes rendus par kubectl kustomize ; non appliqués sur un cluster",
                      iac="kustomize : base + overlays local / cloud (Azure Files)"),
    metrics=dict(head=["Anomalie injectée (100 000 lignes)", "Injectées", "Résultat", "Faux positifs"], rows=[
        ["Colonne en trop (séparateur non échappé)", "990", "990 détectées, morceaux recollés", "0"],
        ["Colonne manquante", "513", "513 détectées, cellule vide au bon endroit", "0"],
        ["Ligne décalée restituée à l'identique", "1 503", "1 503 (100 %)", "—"],
        ["Date invalide 00.00.0000", "974", "974 vidées", "0"],
        ["Valeur masquée (#REF!, N/A, NULL, -, ??)", "994", "994 vidées", "0"],
        ["Montant au format US", "1 963", "1 963 au bon format en sortie", "0"],
        ["Parenthèses comptables (1.234,56)", "520", "520 → négatif", "0"],
        ["Doublon exact", "464", "464", "0"],
        ["Quasi-doublon (2 lettres inversées)", "197", "197", "0"],
    ], note="Mesuré le 27/10/2026 sur un export synthétique façon SAP (11 colonnes, séparateur <code>;</code>, décimales FR). "
            "Taux identiques à 10 000, 500 000 et 1 000 000 de lignes (doublons non mesurés à 1 M). "
            "À 1 M : 15 046 / 15 046 lignes décalées restituées à l'identique (32 % avant correctif)."),
    snippets=[
        ("core/dedup.py — préfiltre : bornes supérieures bon marché avant ratio(), mêmes décisions",
         '''    sm = SequenceMatcher(None, s1, s2)
    if threshold > 0.0:
        bound = sm.real_quick_ratio()
        if bound < threshold:
            return bound
        bound = sm.quick_ratio()
        if bound < threshold:
            return bound
    return sm.ratio()'''),
        ("core/fixer.py — recoller un champ texte coupé par un séparateur non échappé",
         '''        if (merge_text and 0 < col < len(cells)
                and profiles[col - 1].dominant_category == 'text'):
            # Cas typique ERP : séparateur non échappé dans un champ texte
            # ("Dupont;Fils") -> on recolle les deux morceaux au lieu d'en perdre un.
            merged = cells[col - 1] + separator + cells[col]
            new_cells = cells[:col - 1] + [merged] + cells[col + 1:]'''),
    ],
    limits=[
        "<strong>Mémoire</strong> : la lecture est en flux, mais chaque ligne modifiée est gardée pour la revue (preview, undo) ; "
        "la mémoire croît linéairement (1,47 Go après corrections à 1 M de lignes, pic 2,4 Go avec export XLSX). Piste : mode batch « compteurs seuls ».",
        "<strong>Données uniquement synthétiques</strong> : pas encore testé sur de vrais exports (encodages mixtes, en-têtes multiples, sous-totaux).",
        "<strong>Score qualité indulgent</strong> : 92,7/100 (A) sur un fichier dont 6,5 % des lignes sont défectueuses ; suivre plutôt le taux de lignes non conformes.",
        "<strong>Ambiguïté</strong> : une cellule manquante voisine d'une valeur masquée ne peut pas être placée avec certitude (4 cas sur 1 503 lors d'un run exploratoire) ; "
        "le résultat final est juste, mais la position du trou est arbitraire.",
        "<strong>Espaces</strong> : l'espace qui suit un séparateur est supprimé à la lecture (« Martinez; SARL » devient « Martinez;SARL »).",
        "<strong>Doublons</strong> : l'index garde toutes les lignes en mémoire ; non mesuré à 1 M de lignes.",
        "<strong>Formats</strong> : 6 lus, 5 écrits (pas de XLS) ; lecture XLS non testée faute de fichier.",
        "<strong>CLI</strong> : avec <code>--fix</code>, les corrections sont appliquées directement (rapport JSON), sans revue humaine.",
        "<strong>Déploiement non vérifié</strong> : <code>docker build</code> / <code>docker run</code> non exécutés, aucun cluster disponible ; "
        "la limite de 2 Gi est déduite des pics mesurés. Pas de CI GitHub Actions.",
    ],
    strengths=[
        "<strong>Mesuré, pas affirmé</strong> : 1 000 000 de lignes en 63,5 s, avec une vérité terrain sur 8 types d'anomalies.",
        "<strong>Zéro faux positif</strong> : 100 % des décalages de colonnes trouvés, 100 % des lignes décalées restituées à l'identique.",
        "<strong>Performance corrigée</strong> : doublons flous ×120 plus rapides (240 s → 2,0 s), 15/15 quasi-doublons trouvés au lieu de 14/15.",
        "<strong>Humain dans la boucle</strong> : revue des corrections dans l'interface, undo / redo, export XLSX annoté.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 54", _VIDEO_FR),
        ("demo", "Démo réelle", "Captures de l'interface sur un export de démonstration", _SHOTS_FR),
        ("demarche", "Démarche", "Mesurer, corriger, vérifier", _FIXES_FR),
        ("volumes", "Volumes", "Temps et mémoire de 10 000 à 1 000 000 de lignes", _PERF_FR),
    ],
)


# ------------------------------------------------------------------ EN
_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 54, narrated in French · generated by <code>scripts/promo_video.py</code> (synthetic voice, synthesized background sound). All data shown is synthetic.</p>"""

_SHOTS_EN = f"""
<div class="pipeline-figure" style="padding:.6rem;margin-bottom:.4rem;min-width:0"><img src="{MEDIA}/avant-apres.webp" alt="Row 30 before and after correction" {_IMG}></div>
<p class="code-caption" style="margin-bottom:1.6rem">Row 30: the quantity is missing, everything is shifted by one column. After correction: empty cell inserted at the right place, ISO dates, numeric amounts.</p>
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-anomalies.webp" alt="Anomalies tab: detected column shifts" {_IMG}></div>
        <p class="code-caption">Anomalies tab: each shifted row, its type (extra / missing column) and the column where the shift starts.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-doublons.webp" alt="Duplicates tab: exact and fuzzy groups" {_IMG}></div>
        <p class="code-caption">Duplicates tab: exact duplicates and near-duplicates (similarity &gt; 85%), with the column that differs.</p></div>
</div>
<p class="code-caption" style="margin-top:1rem">Real screenshots of the Tkinter interface (French UI, <code>scripts/capture_gui.py</code>) on the 1,000-row synthetic demo export.</p>"""

_PERF_EN = """
<div class="table-wrap"><table class="stack-table">
<thead><tr><th>Rows</th><th>File</th><th>Core (detection → CSV export)</th><th>Quality score</th><th>XLSX export</th><th>Peak memory</th></tr></thead>
<tbody>
<tr><td>10,000</td><td>1.4 MB</td><td>0.97 s</td><td>0.61 s</td><td>1.77 s</td><td>110 MB</td></tr>
<tr><td>100,000</td><td>14 MB</td><td>7.28 s</td><td>6.12 s</td><td>13.8 s</td><td>516 MB</td></tr>
<tr><td>500,000</td><td>71 MB</td><td>35.3 s</td><td>31.3 s</td><td>69.2 s</td><td>2.22 GB</td></tr>
<tr><td>1,000,000</td><td>142 MB</td><td><strong>63.5 s</strong></td><td>52.3 s</td><td>133.8 s</td><td>2.42 GB</td></tr>
</tbody></table></div>
<p class="code-caption" style="margin-top:.8rem">One process per size, on a single core, on a machine shared with other workloads: these are orders of magnitude. Core throughput: 10,300 to 15,700 rows/s.
Reading is streamed, but corrections are kept in memory for human review (preview, undo): 1.47 GB after corrections at 1M rows.</p>"""

_FIXES_EN = """
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · Measure against ground truth</span><ul>
        <li>Synthetic ERP export generator: 11 SAP-style columns, <strong>8 known injected anomaly types</strong>.</li>
        <li>Benchmark from 10,000 to <strong>1,000,000 rows</strong>: time, memory, detection rate, false positives.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · Fix what the measurement reveals</span><ul>
        <li><strong>Unusable CLI</strong>: every analysis raised <code>UnboundLocalError</code>.</li>
        <li><strong>Quadratic fuzzy duplicates</strong>: a single block as soon as the 1st column has a constant prefix; 240 s → 2.0 s on 10,000 rows.</li>
        <li><strong>Text lost during realignment</strong> (“Martinez;SARL” lost “SARL”): 32% → 100% of rows restored.</li>
        <li><strong>Masked values never cleaned</strong> (<code>#REF!</code> exported as is); <code>--compare</code> / <code>--reconcile</code>: 0/2 → 2/2 differences found.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · Verify</span><ul>
        <li><strong>100%</strong> of column shifts found, <strong>0</strong> false positives, identical rates from 10,000 to 1,000,000 rows.</li>
        <li><strong>84 pytest tests</strong> passing (59 initially, all passing too).</li>
        <li>README fixed: it advertised an MIT license, while the LICENSE file is “all rights reserved”.</li></ul></div>
</div>"""

EN_UPDATES = dict(
    title_html='<span class="highlight">Clean</span> ERP exports, even at one million rows',
    lead="Python application (Tkinter GUI + CLI) that detects and fixes defects in ERP exports: shifted columns, "
         "FR/US decimals, invalid dates, masked values, duplicates, personal data — with human review before export. "
         "Tested on 1,000,000 rows against ground truth.",
    kpis=[("1M", "rows processed in 63 s"), ("100%", "column shifts found, 0 false positives"),
          ("×120", "faster fuzzy duplicates"), ("84", "tests")],
    links=[("Source code", REPO, True), ("Showcase branch (video, diagrams, measurements)", BRANCH, False)],
    context=[
        "Every analyst who works with SAP knows the problem: a CSV export with a shifted column, amounts "
        "“1.234,56” and “1,234.56” mixed together, dates like <code>00.00.0000</code> or <code>#REF!</code> errors. "
        "Manual cleanup takes hours and remains error-prone.",
        "Csvtraitement automates detection, suggests corrections, and lets the user validate before exporting. "
        "To find out what it is really worth, it was measured on synthetic exports where every injected defect is known: "
        "the measurement revealed six bugs in the code, fixed since.",
    ],
    rh=[
        "Born from a day-to-day pain point with SAP extracts.",
        "Direct time savings for Procurement, sales administration and management control / finance teams.",
        "Human in the loop in the GUI: no correction applied without validation, undo / redo.",
        "<strong>Verification mindset</strong>: each claim of the project page re-checked, measured, and corrected when it was wrong.",
    ],
    tech=[
        "<strong>Streaming reads in 10,000-row chunks</strong> (<code>csv.reader</code>); Parquet read with <code>iter_batches</code>.",
        "Automatic encoding and separator detection (score mean / (1 + standard deviation)), column typing on a sample.",
        "Realignment of shifted rows: a text field split by an unescaped separator is <strong>stitched back</strong>, not truncated.",
        "Exact and fuzzy duplicates: <strong>multi-key blocking</strong> on discriminating columns + <code>difflib</code> prefilter (same decisions as <code>ratio()</code>).",
        "Personal data masking (email, phone, IBAN, French social security number), PII columns detected automatically.",
        "8-tab Tkinter interface, batch CLI; CLI Docker image and Kubernetes CronJob (kustomize) for nightly processing.",
    ],
    steps=[
        "Reads any tabular format (6 read: CSV, XLSX, XLS, ODS, JSON, Parquet), converted into a CSV stream processed in chunks.",
        "Detects the encoding, separator and type of each column on a sample (first 1,000 + 1,000 random rows).",
        "Cell-by-cell detection of column shifts, weighted quality score, exact and fuzzy duplicate search.",
        "Suggested corrections (ISO dates, decimals, accounting parentheses, masked values, realignment) and optional masking of personal data.",
        "User validation, then export (5 formats written) — in XLSX, corrected cells highlighted and a report sheet.",
        "On a server: the same CLI, without GUI, scheduled every night by a Kubernetes CronJob.",
    ],
    extra_diagrams=[
        ("csvtraitement-pipeline", "Pipeline: from a “dirty” ERP file to a corrected file, in 6 steps (French labels)"),
        ("csvtraitement-memoire", "What is streamed, and what stays in memory (French labels)"),
        ("csvtraitement-doublons", "Fuzzy duplicates: multi-key blocking and prefilter, 240 s → 2.0 s (French labels)"),
        ("csvtraitement-deploiement", "Deployment: a batch job (CronJob), not a server (French labels)"),
    ],
    tags=["Python", "Tkinter", "CLI", "Streaming", "Data Quality", "chardet", "xlsxwriter", "pyarrow", "pytest",
          "Docker", "Kubernetes"],
    stack=[
        ("Python standard library", "csv, difflib, statistics, argparse, logging", "Robust without heavy dependencies"),
        ("chardet", "Encoding detection", "Resilience to heterogeneous exports"),
        ("xlsxwriter (constant_memory)", "Annotated Excel export", "Large-volume writes"),
        ("pyarrow", "Parquet read / write", "Data interoperability"),
        ("Tkinter", "8-tab graphical interface", "A tool non-developers can use"),
        ("pytest", "84 tests, including end-to-end on synthetic exports with ground truth", "Measured reliability"),
        ("Docker + Kubernetes (kustomize)", "Non-root CLI image, nightly CronJob, PVC", "Industrialized batch processing"),
    ],
    matrix=dict(ci="n", tests="y", docker="p", orch="p", tracking="n", monitoring="n", serving="n", deploy="p", iac="p"),
    matrix_notes=dict(tests="84 pytest tests (detection, correction, end-to-end with ground truth)",
                      docker="CLI Dockerfile (python:3.12-slim, non-root); build not verified",
                      orch="Nightly Kubernetes CronJob (02:00, Forbid)",
                      deploy="Manifests rendered with kubectl kustomize; not applied to a cluster",
                      iac="kustomize: base + local / cloud overlays (Azure Files)"),
    metrics=dict(head=["Injected anomaly (100,000 rows)", "Injected", "Result", "False positives"], rows=[
        ["Extra column (unescaped separator)", "990", "990 detected, pieces stitched back", "0"],
        ["Missing column", "513", "513 detected, empty cell at the right place", "0"],
        ["Shifted row restored identically", "1,503", "1,503 (100%)", "—"],
        ["Invalid date 00.00.0000", "974", "974 cleared", "0"],
        ["Masked value (#REF!, N/A, NULL, -, ??)", "994", "994 cleared", "0"],
        ["US-format amount", "1,963", "1,963 in the right format on output", "0"],
        ["Accounting parentheses (1.234,56)", "520", "520 → negative", "0"],
        ["Exact duplicate", "464", "464", "0"],
        ["Near-duplicate (2 swapped letters)", "197", "197", "0"],
    ], note="Measured on 27/10/2026 on a synthetic SAP-style export (11 columns, <code>;</code> separator, FR decimals). "
            "Identical rates at 10,000, 500,000 and 1,000,000 rows (duplicates not measured at 1M). "
            "At 1M: 15,046 / 15,046 shifted rows restored identically (32% before the fix)."),
    snippets=[
        ("core/dedup.py — prefilter: cheap upper bounds before ratio(), same decisions",
         '''    sm = SequenceMatcher(None, s1, s2)
    if threshold > 0.0:
        bound = sm.real_quick_ratio()
        if bound < threshold:
            return bound
        bound = sm.quick_ratio()
        if bound < threshold:
            return bound
    return sm.ratio()'''),
        ("core/fixer.py — stitching back a text field split by an unescaped separator",
         '''        if (merge_text and 0 < col < len(cells)
                and profiles[col - 1].dominant_category == 'text'):
            # Typical ERP case: unescaped separator inside a text field
            # ("Dupont;Fils") -> stitch both pieces back instead of losing one.
            merged = cells[col - 1] + separator + cells[col]
            new_cells = cells[:col - 1] + [merged] + cells[col + 1:]'''),
    ],
    limits=[
        "<strong>Memory</strong>: reading is streamed, but every modified row is kept for review (preview, undo); "
        "memory grows linearly (1.47 GB after corrections at 1M rows, 2.4 GB peak with XLSX export). Next step: a “counters only” batch mode.",
        "<strong>Synthetic data only</strong>: not yet tested on real exports (mixed encodings, multiple headers, subtotals).",
        "<strong>Lenient quality score</strong>: 92.7/100 (A) on a file where 6.5% of rows are defective; track the non-compliant row rate instead.",
        "<strong>Ambiguity</strong>: a missing cell next to a masked value cannot be placed with certainty (4 cases out of 1,503 in an exploratory run); "
        "the final result is correct, but the position of the gap is arbitrary.",
        "<strong>Whitespace</strong>: the space following a separator is dropped on read (“Martinez; SARL” becomes “Martinez;SARL”).",
        "<strong>Duplicates</strong>: the index keeps all rows in memory; not measured at 1M rows.",
        "<strong>Formats</strong>: 6 read, 5 written (no XLS); XLS reading untested for lack of a file.",
        "<strong>CLI</strong>: with <code>--fix</code>, corrections are applied directly (JSON report), without human review.",
        "<strong>Deployment not verified</strong>: <code>docker build</code> / <code>docker run</code> not executed, no cluster available; "
        "the 2 Gi limit is derived from measured peaks. No GitHub Actions CI.",
    ],
    strengths=[
        "<strong>Measured, not claimed</strong>: 1,000,000 rows in 63.5 s, with ground truth on 8 anomaly types.",
        "<strong>Zero false positives</strong>: 100% of column shifts found, 100% of shifted rows restored identically.",
        "<strong>Performance fixed</strong>: fuzzy duplicates ×120 faster (240 s → 2.0 s), 15/15 near-duplicates found instead of 14/15.",
        "<strong>Human in the loop</strong>: review of corrections in the GUI, undo / redo, annotated XLSX export.",
    ],
    custom_sections=[
        ("video", "Overview", "The project in 1 min 54", _VIDEO_EN),
        ("demo", "Real demo", "Interface screenshots on a demo export", _SHOTS_EN),
        ("approach", "Approach", "Measure, fix, verify", _FIXES_EN),
        ("volumes", "Volumes", "Time and memory from 10,000 to 1,000,000 rows", _PERF_EN),
    ],
)
