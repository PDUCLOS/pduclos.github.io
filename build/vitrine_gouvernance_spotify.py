"""Vitrine gouvernance-spotify (dépôt BLOC1-SPOTIFY, branche feat/vitrine-gouvernance-spotify).

Source unique : docs/PORTFOLIO.md du dépôt (chiffres mesurés ou recomptés le 27/10/2026).
Les livrables jury sont inchangés ; le démonstrateur et l'audit ont été ajoutés ensuite.
FR_UPDATES et EN_UPDATES sont fusionnés par dict.update dans la fiche existante du slug.
"""

GH = "https://github.com/PDUCLOS/"
REPO = GH + "BLOC1-SPOTIFY"
BRANCH = REPO + "/tree/feat/vitrine-gouvernance-spotify"
MEDIA = "/media/gouvernance-spotify"

# ---------------------------------------------------------------------------------------------- FR

_VIDEO_FR = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 55 · générée par <code>scripts/promo_video.py</code> (narration de synthèse). Contrôlée par extraction d'images et <code>ffprobe</code>, sans écoute humaine de la narration.</p>"""

_AJOUTS_FR = """
<p>Le dossier remis au jury ne contenait pas de code. Pour le rendre vérifiable sans inventer de service à déployer, deux outils ont été ajoutés après coup, sur une branche dédiée. <strong>Les six livrables jury n'ont pas été modifiés</strong> : les écarts trouvés sont signalés, pas corrigés.</p>
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--rh"><span class="arg-label">Livrables jury (inchangés)</span><ul>
        <li>Évaluation de maturité sur <strong>9 dimensions</strong>, notées de 1 à 5.</li>
        <li>Organigramme et note d'argumentation : sponsor, CDO, comité, DPO, RSSI, juridique, <strong>4 data stewards</strong>.</li>
        <li>Politique : <strong>9 principes, 4 niveaux de classification, 7 KPIs</strong> ; plan de mise en œuvre ; présentation de <strong>14 slides</strong>.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Ajouté · démonstrateur</span><ul>
        <li><code>python -m gouvernance</code> : <strong>21 contrôles</strong> (11 qualité, 6 conformité RGPD / CCPA, 4 catalogue) en SQL sur DuckDB.</li>
        <li>5 000 utilisateurs et 50 148 événements <strong>synthétiques</strong>, défauts injectés à des taux connus (graine 38777).</li>
        <li><strong>12 contrôles conformes avant remédiation, 18 après</strong> ; <strong>40 tests</strong> pytest verts.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Ajouté · audit des livrables</span><ul>
        <li><code>audit_livrables.py</code> relit les vrais fichiers Word et PowerPoint et recalcule maturité, budget et décomptes.</li>
        <li><strong>12 points : 7 cohérents, 5 signalés</strong> (3 écarts chiffrés, 1 non traçable, 1 à harmoniser).</li></ul></div>
</div>"""

_SHOTS_FR = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-rapport.webp" alt="Rapport du démonstrateur : KPIs et 21 contrôles avant et après remédiation" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Rapport généré par <code>python -m gouvernance</code> : KPIs de pilotage, puis les 21 contrôles avant et après remédiation. Données 100 % synthétiques.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/livrable-maturite.webp" alt="Slide 3 de la présentation : diagnostic de maturité" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Slide 3 de la présentation jury, sans retouche. Le graphique donne 2,4 / 5, alors que le document d'évaluation calcule 21 / 9 = 2,33 : 6 notes sur 9 diffèrent. Écart relevé par l'audit.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/livrable-organigramme.webp" alt="Slide 6 de la présentation : organigramme de gouvernance" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Slide 6 : organisation de la gouvernance, du sponsor exécutif aux data stewards par domaine.</p></div>
</div>"""

_AUDIT_FR = """
<div class="two-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">Écarts relevés dans les livrables (non corrigés)</span><ul>
        <li><strong>Maturité</strong> : 2,33 dans le document d'évaluation (« environ 2,3 »), 2,4 sur le graphique de la slide 3 (22 / 9 = 2,44).</li>
        <li><strong>Budget pilote</strong> : la ligne « intégration +30–50 % des licences » vaut 80–130 K$, soit 30 % des deux bornes. Appliquée telle qu'écrite : 351–645 K$ au lieu de 350–560 K$ (haut de fourchette sous-estimé de 85 K$).</li>
        <li><strong>« 14 contrôles de conformité »</strong> (slide 5) : aucune liste ni matrice correspondante dans le dépôt.</li>
        <li><strong>Calendrier</strong> : plan terminé à M18, politique à M24 ; bascule vers le Center of Excellence en phase 2 (7–12 mois) dans la politique, à M12 dans les slides.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Ce que la remédiation a fait (et refuse de maquiller)</span><ul>
        <li>147 pays complétés depuis les abonnements, 144 doublons supprimés, 764 événements en quarantaine, 478 événements purgés (> 24 mois).</li>
        <li>65 consentements sans preuve traités comme absents, 55 lignes d'audience retirées faute de consentement, 29 e-mails en clair pseudonymisés, 1 colonne hors catalogue supprimée.</li>
        <li>Non corrigés, volontairement : année de naissance manquante (à recollecter), lignage absent, DSAR en retard et violations notifiées hors délai — ce sont des défauts de processus, pas de données.</li></ul></div>
</div>
<h3>Pourquoi ni Docker ni Kubernetes</h3>
<p>Le livrable est un dossier de conseil, et le démonstrateur un traitement par lots de deux secondes, sans service, sans état ni utilisateur concurrent. Un conteneur n'apporterait aucune preuve supplémentaire. Passage à l'échelle mesuré : 50 000 utilisateurs et 501 513 événements, contrôles en 1,36 s, remédiation et recontrôle en 1,37 s.</p>"""

FR_UPDATES = dict(
    lead="Mission de conseil pour un comité exécutif (cas d'étude Spotify, 450 M d'utilisateurs) : évaluation de maturité "
         "sur 9 dimensions, organigramme de gouvernance, politique, plan de déploiement, budget et présentation exécutive. "
         "Complétée ensuite par un démonstrateur exécutable de la politique (Python, SQL DuckDB) et un audit chiffré des livrables.",
    kpis=[("9", "dimensions évaluées"), ("≈ 2,3/5", "maturité initiale"), ("21", "contrôles exécutables"),
          ("12 → 18", "contrôles conformes après remédiation"), ("40", "tests")],
    links=[("Vitrine (branche)", BRANCH, True), ("Dépôt", REPO, False)],
    context=[
        "Données en silos (marketing, produit, contenu, ingénierie), exposition RGPD / CCPA / PDPA avec des amendes pouvant "
        "atteindre 4 % du chiffre d'affaires mondial : l'entreprise doit structurer sa gouvernance.",
        "Cas d'étude pédagogique fondé sur un business case fourni : les chiffres sont ceux du cas, pas d'une mission réelle.",
        "Le dossier remis au jury (6 fichiers pour 4 étapes) ne contenait pas de code. Il a été complété ensuite, sans modifier "
        "les livrables, par un <strong>démonstrateur</strong> qui exécute les règles de la politique sur des données synthétiques "
        "et par un <strong>audit automatique</strong> qui recompte les chiffres des livrables.",
    ],
    rh=[
        "Posture de <strong>conseil auprès d'une direction</strong> : diagnostic, recommandation, budget, décision demandée.",
        "Pilote ciblé de 6 mois sur un domaine (données d'engagement marketing) avant généralisation : approche pragmatique.",
        "Rôles clairs : DPO, CDO, data stewards, comité de gouvernance.",
        "<strong>Honnêteté sur ses propres livrables</strong> : l'audit relève 5 points à revoir, signalés sans retoucher la version jury.",
    ],
    tech=[
        "Architecture cible : lakehouse Databricks + Unity Catalog comme socle commun.",
        "Outillage recommandé par besoin : catalogue (Collibra), qualité (dbt, Talend), conformité (OneTrust), sécurité (SIEM), cycle de vie ML (MLflow + Evidently).",
        "KPIs de gouvernance mesurables : −10 % de données manquantes, 100 % des consentements tracés, incidents détectés sous 24 h.",
        "Démonstrateur : <strong>21 contrôles SQL</strong> sur DuckDB (qualité, RGPD / CCPA, catalogue), remédiation puis recontrôle avec les mêmes règles, <strong>40 tests</strong> pytest.",
    ],
    band=("Pilote 6 mois (Marketing, pilotage centralisé) → 3 vagues jusqu'à M18 → Center of Excellence", "infra"),
    steps=[
        "Évaluation de maturité sur 9 dimensions : gouvernance, conformité et intégration au niveau « cadré » selon le document d'évaluation (moyenne ≈ 2,3 / 5).",
        "Conception de l'organisation : pilotage centralisé pendant le pilote, puis bascule vers un Center of Excellence.",
        "Plan de mise en œuvre : pilote de 6 mois sur les données d'engagement marketing, puis 3 vagues (M7–M18), conformité d'abord.",
        "Présentation exécutive de 14 slides avec budget, valeur attendue et décision demandée au comité.",
        "Ajouté ensuite — démonstrateur : génération de données synthétiques, 21 contrôles, remédiation, recontrôle et rapport avant / après.",
        "Ajouté ensuite — audit des livrables : 12 points recalculés sur les vrais fichiers, 7 cohérents et 5 signalés.",
    ],
    extra_diagrams=[
        ("gouvernance-spotify-organisation", "Organisation : sponsor, CDO, comité, DPO et data stewards"),
        ("gouvernance-spotify-flux-outillage", "Flux de données et outillage cible"),
        ("gouvernance-spotify-feuille-de-route", "Feuille de route : pilote, vagues, Center of Excellence"),
        ("gouvernance-spotify-demonstrateur", "Démonstrateur exécutable : contrôles, remédiation, audit des livrables"),
    ],
    langs=[("Python", 73), ("HTML (vitrine)", 23), ("TOML (catalogue)", 4)],
    langs_note="Dossier de conseil (Word, PDF, PowerPoint) + démonstrateur Python / SQL DuckDB sur données synthétiques. "
               "Part calculée sur les lignes du démonstrateur et de la vitrine, hors livrables.",
    tags=["Data Governance", "RGPD", "Databricks", "Unity Catalog", "Collibra", "dbt", "MLflow", "Conduite du changement",
          "DuckDB", "SQL", "Python", "pytest", "Qualité des données"],
    stack=[
        ("Databricks + Unity Catalog", "Socle lakehouse et contrôle d'accès", "Architecture cible"),
        ("Collibra", "Catalogue et lignage", "Gouvernance des métadonnées"),
        ("dbt / Talend", "Qualité des données", "Contrôles automatisés"),
        ("OneTrust", "Consentement et conformité", "RGPD / CCPA"),
        ("MLflow + Evidently", "Cycle de vie et dérive des modèles", "Gouvernance du ML"),
        ("DuckDB 2.0.0", "Démonstrateur : tient le rôle du lakehouse (schémas raw et clean)", "Simulation, non déployé"),
        ("SQL (conventions des tests dbt)", "21 contrôles qualité, RGPD / CCPA et catalogue", "Règles exécutables"),
        ("catalog.toml", "Responsable, classification, base légale, rétention par jeu de données", "Rôle de Collibra, simulé"),
        ("pytest", "40 tests : défauts détectés, remédiation, audit sur les vrais fichiers", "Non-régression"),
    ],
    metrics=dict(head=["KPI (source)", "Avant", "Après", "Cible"], rows=[
        ["Score qualité, moyenne des 11 contrôles (politique §6.2)", "98,3 %", "98,7 %", "≥ 95 % — atteint"],
        ["Cellules vides sur colonnes critiques (plan §4.6)", "0,42 %", "0,36 %", "−10 % — atteint (−14,9 %)"],
        ["Consentements tracés (plan §4.6)", "97,9 %", "100,0 %", "100 % — atteint"],
        ["DSAR dans les délais légaux (politique §6.2)", "96,5 %", "96,5 %", "100 % — non atteint (volontaire)"],
        ["Violations notifiées sous 72 h (RGPD art. 33)", "60,0 %", "60,0 %", "100 % — non atteint (volontaire)"],
    ], note="Démonstrateur exécuté le 27/10/2026 (Python 3.12, DuckDB 2.0.0) : 5 000 utilisateurs, 50 148 événements synthétiques, "
            "défauts injectés à des taux connus. Ces KPIs mesurent le démonstrateur, <strong>pas Spotify</strong>. "
            "Génération 1,37 s, contrôles 0,82 s, remédiation et recontrôle 0,46 s, audit des livrables 0,35 s."),
    snippets=[
        ("gouvernance/checks.py — une règle de la politique devient un contrôle SQL",
         '''Check("C01", "conformite", "consentement", "Consentement tracé (horodatage + canal)", "Plan, KPI pilote « 100 % »",
      "users", f"{blank('consent_ts')} OR {blank('consent_source')}", scope="consent_marketing = 'true'", threshold=1.0),
Check("C02", "conformite", "consentement", "Audience de campagne : consentement présent", "RGPD art. 6-1-a et 7",
      "campaign_audience",
      "user_id NOT IN (SELECT user_id FROM {s}.users WHERE consent_marketing = 'true' "
      f"AND NOT ({blank('consent_ts')}))", threshold=1.0),'''),
        ("Exécution", '''python -m gouvernance                  # 5 000 utilisateurs, rapport avant / après
python -m gouvernance --users 50000    # passage à l'échelle (501 513 événements)
python -m pytest                       # 40 tests'''),
    ],
    limits=[
        "Cas d'étude de certification : recommandations (organisation, outils, budget) non mises en œuvre ; prix éditeurs repris des sources citées dans le plan, non revérifiés.",
        "Démonstrateur sur données synthétiques ; outils cibles simulés (Databricks par DuckDB, dbt / Talend par des requêtes SQL, Collibra par <code>catalog.toml</code>), aucun n'a été installé ni testé.",
        "Le « score qualité » est une moyenne de taux de réussite : il reste à 98 % alors que le contrôle « année de naissance » est à 91,7 %.",
        "Écarts relevés entre la présentation et le document d'évaluation (2,4 vs 2,3), et sur le budget pilote : signalés et non corrigés dans les livrables jury.",
        "« ROI > 3× » annoncé dans la présentation, sans calcul dans le dépôt.",
        "Pas de Docker ni de Kubernetes, volontairement : pas de service à déployer. Vitrine GitHub Pages non vérifiée en ligne (branche non fusionnée).",
    ],
    strengths=[
        "<strong>Posture de conseil</strong> : diagnostic sur 9 dimensions, recommandation, budget, décision demandée.",
        "<strong>Pragmatique</strong> : pilote de 6 mois sur un domaine avant généralisation.",
        "<strong>Rôles clairs</strong> : DPO, CDO, data stewards, comité de gouvernance.",
        "<strong>Vérifiable</strong> : la politique devient 21 contrôles exécutables ; 12 conformes avant remédiation, 18 après.",
        "<strong>Rigueur</strong> : un audit automatique relit les chiffres des livrables avant le comité.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 55", _VIDEO_FR),
        ("ajouts", "Livrables et ajouts", "Ce qui a été remis au jury, ce qui a été ajouté", _AJOUTS_FR),
        ("demo", "Démo réelle", "Rapport du démonstrateur et livrables sans retouche", _SHOTS_FR),
        ("audit", "Résultats", "Ce que l'audit et la remédiation ont trouvé", _AUDIT_FR),
    ],
)

# ---------------------------------------------------------------------------------------------- EN

_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 55, narrated in French · generated by <code>scripts/promo_video.py</code> (synthetic voice). Checked by frame extraction and <code>ffprobe</code>, without a human listening pass on the narration.</p>"""

_AJOUTS_EN = """
<p>The file submitted to the jury contained no code. To make it verifiable without inventing a service to deploy, two tools were added afterwards on a dedicated branch. <strong>The six jury deliverables were not modified</strong>: the discrepancies found are reported, not corrected.</p>
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--rh"><span class="arg-label">Jury deliverables (unchanged)</span><ul>
        <li>Maturity assessment across <strong>9 dimensions</strong>, scored 1 to 5.</li>
        <li>Org chart and rationale note: sponsor, CDO, committee, DPO, CISO, legal, <strong>4 data stewards</strong>.</li>
        <li>Policy: <strong>9 principles, 4 classification levels, 7 KPIs</strong>; implementation plan; <strong>14-slide</strong> presentation.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Added · demonstrator</span><ul>
        <li><code>python -m gouvernance</code>: <strong>21 checks</strong> (11 quality, 6 GDPR / CCPA compliance, 4 catalog) in SQL on DuckDB.</li>
        <li>5,000 users and 50,148 <strong>synthetic</strong> events, defects injected at known rates (seed 38777).</li>
        <li><strong>12 checks passing before remediation, 18 after</strong>; <strong>40 pytest tests</strong> green.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">Added · deliverables audit</span><ul>
        <li><code>audit_livrables.py</code> reads the actual Word and PowerPoint files and recomputes maturity, budget and counts.</li>
        <li><strong>12 points: 7 consistent, 5 flagged</strong> (3 numeric discrepancies, 1 untraceable, 1 to align).</li></ul></div>
</div>"""

_SHOTS_EN = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/demo-rapport.webp" alt="Demonstrator report: KPIs and 21 checks before and after remediation" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Report generated by <code>python -m gouvernance</code> (in French): steering KPIs, then the 21 checks before and after remediation. 100% synthetic data.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/livrable-maturite.webp" alt="Slide 3 of the presentation: maturity assessment" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Slide 3 of the jury presentation, unedited. The chart shows 2.4 / 5, while the assessment document computes 21 / 9 = 2.33: 6 of the 9 scores differ. Discrepancy flagged by the audit.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem"><img src="{MEDIA}/livrable-organigramme.webp" alt="Slide 6 of the presentation: governance org chart" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Slide 6: governance organization, from the executive sponsor to the per-domain data stewards.</p></div>
</div>"""

_AUDIT_EN = """
<div class="two-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">Discrepancies found in the deliverables (not corrected)</span><ul>
        <li><strong>Maturity</strong>: 2.33 in the assessment document (“about 2.3”), 2.4 on the slide 3 chart (22 / 9 = 2.44).</li>
        <li><strong>Pilot budget</strong>: the line “integration +30–50% of licences” is 80–130 K$, i.e. 30% of both bounds. Applied as written: 351–645 K$ instead of 350–560 K$ (upper bound underestimated by 85 K$).</li>
        <li><strong>“14 compliance controls”</strong> (slide 5): no matching list or matrix in the repository.</li>
        <li><strong>Timeline</strong>: plan ends at M18, policy at M24; switch to the Center of Excellence in phase 2 (months 7–12) in the policy, at M12 in the slides.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">What remediation did (and refuses to paper over)</span><ul>
        <li>147 countries filled in from subscriptions, 144 duplicates removed, 764 events quarantined, 478 events purged (> 24 months).</li>
        <li>65 consents without proof treated as absent, 55 audience rows removed for lack of consent, 29 plain-text e-mails pseudonymized, 1 non-catalogued column dropped.</li>
        <li>Deliberately not fixed: missing birth year (to be re-collected), missing lineage, late DSARs and breaches notified late — these are process defects, not data defects.</li></ul></div>
</div>
<h3>Why neither Docker nor Kubernetes</h3>
<p>The deliverable is a consulting file, and the demonstrator is a two-second batch job with no service, no state and no concurrent users. A container would add no further evidence. Measured scale-up: 50,000 users and 501,513 events, checks in 1.36 s, remediation and re-check in 1.37 s.</p>"""

EN_UPDATES = dict(
    lead="Consulting engagement for an executive committee (Spotify case study, 450M users): maturity assessment "
         "across 9 dimensions, governance org chart, policy, rollout plan, budget and executive presentation. "
         "Later complemented by an executable demonstrator of the policy (Python, DuckDB SQL) and a quantified audit of the deliverables.",
    kpis=[("9", "dimensions assessed"), ("≈ 2.3/5", "initial maturity"), ("21", "executable checks"),
          ("12 → 18", "checks passing after remediation"), ("40", "tests")],
    links=[("Showcase (branch)", BRANCH, True), ("Repository", REPO, False)],
    context=[
        "Siloed data (marketing, product, content, engineering) and GDPR / CCPA / PDPA exposure with fines of up to "
        "4% of global revenue: the company needs to structure its governance.",
        "Educational case study based on a provided business case: the figures come from the case, not from a real engagement.",
        "The file submitted to the jury (6 files for 4 stages) contained no code. It was later complemented, without changing "
        "the deliverables, by a <strong>demonstrator</strong> that runs the policy rules on synthetic data "
        "and an <strong>automated audit</strong> that recounts the figures in the deliverables.",
    ],
    rh=[
        "<strong>Advisory role with senior leadership</strong>: assessment, recommendation, budget, decision requested.",
        "Targeted 6-month pilot on one domain (marketing engagement data) before scaling: a pragmatic approach.",
        "Clear roles: DPO, CDO, data stewards, governance committee.",
        "<strong>Candid about its own deliverables</strong>: the audit flags 5 points to review, reported without touching the jury version.",
    ],
    tech=[
        "Target architecture: Databricks lakehouse + Unity Catalog as a common foundation.",
        "Tooling recommended per need: catalog (Collibra), quality (dbt, Talend), compliance (OneTrust), security (SIEM), ML lifecycle (MLflow + Evidently).",
        "Measurable governance KPIs: −10% missing data, 100% of consents tracked, incidents detected within 24 h.",
        "Demonstrator: <strong>21 SQL checks</strong> on DuckDB (quality, GDPR / CCPA, catalog), remediation then re-check with the same rules, <strong>40 pytest tests</strong>.",
    ],
    band=("6-month pilot (Marketing, centralized steering) → 3 waves up to M18 → Center of Excellence", "infra"),
    steps=[
        "Maturity assessment across 9 dimensions: governance, compliance and integration at the “defined” level according to the assessment document (average ≈ 2.3 / 5).",
        "Organization design: centralized steering during the pilot, then transition to a Center of Excellence.",
        "Implementation plan: 6-month pilot on marketing engagement data, then 3 waves (M7–M18), compliance first.",
        "14-slide executive presentation with budget, expected value and the decision requested from the committee.",
        "Added later — demonstrator: synthetic data generation, 21 checks, remediation, re-check and before / after report.",
        "Added later — deliverables audit: 12 points recomputed on the actual files, 7 consistent and 5 flagged.",
    ],
    extra_diagrams=[
        ("gouvernance-spotify-organisation", "Organization: sponsor, CDO, committee, DPO and data stewards"),
        ("gouvernance-spotify-flux-outillage", "Data flows and target tooling"),
        ("gouvernance-spotify-feuille-de-route", "Roadmap: pilot, waves, Center of Excellence"),
        ("gouvernance-spotify-demonstrateur", "Executable demonstrator: checks, remediation, deliverables audit"),
    ],
    langs=[("Python", 73), ("HTML (showcase)", 23), ("TOML (catalog)", 4)],
    langs_note="Consulting file (Word, PDF, PowerPoint) + Python / DuckDB SQL demonstrator on synthetic data. "
               "Share computed on the lines of the demonstrator and showcase, excluding deliverables.",
    tags=["Data Governance", "GDPR", "Databricks", "Unity Catalog", "Collibra", "dbt", "MLflow", "Change management",
          "DuckDB", "SQL", "Python", "pytest", "Data quality"],
    stack=[
        ("Databricks + Unity Catalog", "Lakehouse foundation and access control", "Target architecture"),
        ("Collibra", "Catalog and lineage", "Metadata governance"),
        ("dbt / Talend", "Data quality", "Automated controls"),
        ("OneTrust", "Consent and compliance", "GDPR / CCPA"),
        ("MLflow + Evidently", "Model lifecycle and drift", "ML governance"),
        ("DuckDB 2.0.0", "Demonstrator: plays the lakehouse role (raw and clean schemas)", "Simulation, not deployed"),
        ("SQL (dbt test conventions)", "21 quality, GDPR / CCPA and catalog checks", "Executable rules"),
        ("catalog.toml", "Owner, classification, legal basis, retention per dataset", "Collibra's role, simulated"),
        ("pytest", "40 tests: defects detected, remediation, audit on the actual files", "Non-regression"),
    ],
    metrics=dict(head=["KPI (source)", "Before", "After", "Target"], rows=[
        ["Quality score, average of the 11 checks (policy §6.2)", "98.3%", "98.7%", "≥ 95% — met"],
        ["Empty cells in critical columns (plan §4.6)", "0.42%", "0.36%", "−10% — met (−14.9%)"],
        ["Consents tracked (plan §4.6)", "97.9%", "100.0%", "100% — met"],
        ["DSARs within legal deadlines (policy §6.2)", "96.5%", "96.5%", "100% — not met (deliberate)"],
        ["Breaches notified within 72 h (GDPR art. 33)", "60.0%", "60.0%", "100% — not met (deliberate)"],
    ], note="Demonstrator run on 27/10/2026 (Python 3.12, DuckDB 2.0.0): 5,000 users, 50,148 synthetic events, "
            "defects injected at known rates. These KPIs measure the demonstrator, <strong>not Spotify</strong>. "
            "Generation 1.37 s, checks 0.82 s, remediation and re-check 0.46 s, deliverables audit 0.35 s."),
    snippets=[
        ("gouvernance/checks.py — a policy rule becomes a SQL check",
         FR_UPDATES["snippets"][0][1]),
        ("Running it", '''python -m gouvernance                  # 5,000 users, before / after report
python -m gouvernance --users 50000    # scale-up (501,513 events)
python -m pytest                       # 40 tests'''),
    ],
    limits=[
        "Certification case study: recommendations (organization, tools, budget) not implemented; vendor prices taken from the sources cited in the plan, not re-checked.",
        "Demonstrator on synthetic data; target tools simulated (Databricks by DuckDB, dbt / Talend by SQL queries, Collibra by <code>catalog.toml</code>), none installed or tested.",
        "The “quality score” is an average of pass rates: it stays at 98% while the “birth year” check is at 91.7%.",
        "Discrepancies between the presentation and the assessment document (2.4 vs 2.3), and in the pilot budget: reported and not corrected in the jury deliverables.",
        "“ROI > 3×” stated in the presentation, with no calculation in the repository.",
        "No Docker or Kubernetes, deliberately: there is no service to deploy. GitHub Pages showcase not verified online (branch not merged).",
    ],
    strengths=[
        "<strong>Advisory approach</strong>: assessment across 9 dimensions, recommendation, budget, decision requested.",
        "<strong>Pragmatic</strong>: 6-month pilot on one domain before scaling.",
        "<strong>Clear roles</strong>: DPO, CDO, data stewards, governance committee.",
        "<strong>Verifiable</strong>: the policy becomes 21 executable checks; 12 passing before remediation, 18 after.",
        "<strong>Rigor</strong>: an automated audit re-reads the figures in the deliverables before the committee.",
    ],
    custom_sections=[
        ("video", "Presentation", "The project in 1 min 55", _VIDEO_EN),
        ("ajouts", "Deliverables and additions", "What was submitted to the jury, what was added", _AJOUTS_EN),
        ("demo", "Real demo", "Demonstrator report and unedited deliverables", _SHOTS_EN),
        ("audit", "Results", "What the audit and remediation found", _AUDIT_EN),
    ],
)
