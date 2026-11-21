"""Rhône Distribution Lakehouse : Snowflake (flux lent) + dbt, distributeur B2B fictif.

Faits repris du README du projet (~/rhone-distribution-lakehouse, novembre 2026).
Statut honnête : flux Snowflake construit et validé EN LOCAL (PostgreSQL + DuckDB + dbt, 64 tests) ;
scripts Snowflake écrits, première exécution sur Snowflake à venir ; Databricks et Power BI prévus.
Entreprise fictive, ERP simulé ; profil clients tiré d'un agrégat SIRENE réel (aucune donnée nominative).
"""

MEDIA = "/media/rhone-distribution"

_PIPE = f"""
<div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/pipeline.png" alt="Pipeline Rhône Distribution : ERP simulé, extract nocturne, Bronze, Silver et Gold dbt, Snowflake, Databricks, Power BI" loading="lazy" draggable="false" style="min-width:0"></div>
<p class="code-caption">Le schéma du projet : flux lent Snowflake (quotidien, agrégé, accès réglementés) et flux rapide Databricks (prévu).</p>"""

_ACCES = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Rôle</th><th>Agences visibles</th><th>Contacts clients (RGPD)</th><th>Coûts et marges</th></tr></thead>
    <tbody>
        <tr><td><code>RD_DAF</code></td><td>toutes</td><td>en clair</td><td>en clair</td></tr>
        <tr><td><code>RD_DIRECTION_COMMERCIALE</code></td><td>toutes</td><td>masqués</td><td>en clair</td></tr>
        <tr><td><code>RD_ANALYSTE</code></td><td>toutes</td><td>masqués</td><td>masqués</td></tr>
        <tr><td><code>RD_COMMERCIAL_&lt;AGENCE&gt;</code></td><td><strong>la sienne</strong></td><td>en clair</td><td>masqués</td></tr>
        <tr><td><code>RD_POWERBI_SVC</code></td><td>toutes (lecture Gold)</td><td>masqués</td><td>masqués</td></tr>
    </tbody></table></div>
<p style="margin-top:1rem">Row access policy par agence (table de correspondance rôle → agence), masking policies <code>pii_masking</code> et
<code>finance_masking</code>, tags de classification. dbt recrée les tables à chaque run : les policies sont rattachées par un
<strong>post-hook</strong>, à partir du <code>meta</code> déclaré dans le YAML des modèles. Bronze et Silver ne sont jamais exposés aux métiers.</p>
<p class="code-caption"><strong>Statut :</strong> scripts Snowflake écrits, pas encore exécutés sur un compte Snowflake : vérification rôle par rôle à faire.</p>"""

_QUALITE = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Anomalie injectée</th><th>Nombre</th></tr></thead>
    <tbody>
        <tr><td>prix à zéro</td><td>25</td></tr>
        <tr><td>quantité négative non marquée comme retour</td><td>12</td></tr>
        <tr><td>expédition antérieure à la commande</td><td>15</td></tr>
        <tr><td>facture orpheline (sans commande)</td><td>10</td></tr>
        <tr><td>client sans code postal</td><td>8</td></tr>
    </tbody></table></div>
<p style="margin-top:1rem">Le générateur injecte <strong>70 anomalies</strong> et écrit leur nombre exact dans un manifeste. La couche Silver les isole
en quarantaine, et un test dbt exige que la quarantaine retrouve <strong>exactement</strong> ce manifeste, ni plus ni moins.
Ce test a déjà servi : une première règle « prix à zéro » produisait 5 faux positifs (une vente annulée par un retour le même jour).
Le build a échoué, la règle a été corrigée.</p>"""

RHONE_DISTRIBUTION = dict(
    slug="rhone-distribution",
    short="Rhône Distribution — Snowflake + dbt",
    kicker="Snowflake · dbt · SQL · Gouvernance des accès",
    badge="PROJET PUBLIC, DBT VALIDÉ EN LOCAL",
    title="Rhône Distribution — un entrepôt Snowflake modélisé avec dbt",
    title_html='Snowflake et dbt : <span class="highlight">des données fiables, des accès réglementés</span>',
    lead="Un distributeur B2B lyonnais fictif (5 agences, environ 1 200 clients professionnels) veut piloter chiffre d'affaires, marge, "
         "DSO et taux de service, sans que chacun voie tout. Le flux Snowflake charge chaque nuit des données agrégées, dbt les "
         "transforme en couches Silver et Gold testées, et les accès sont réglementés par rôle : agence, données personnelles, coûts. "
         "Construit avec dbt Core et validé de bout en bout en local ; scripts Snowflake prêts, pas encore exécutés sur un compte Snowflake.",
    kpis=[("64", "tests dbt"), ("70 / 70", "anomalies injectées retrouvées"), ("5", "rôles d'accès Snowflake"),
          ("7 210", "établissements SIRENE pour le profil clients")],
    links=[("Code source", "https://github.com/PDUCLOS/rhone-distribution-lakehouse", True), ("Documentation dbt et lignage", "https://pduclos.github.io/rhone-distribution-lakehouse/", True), ("Accès réglementés", "#acces", False)],
    context=[
        "Un distributeur de fournitures industrielles (EPI, outillage, fixation, plomberie, électricité) veut un pilotage fiable : "
        "la DAF suit chiffre d'affaires, marge, DSO et balance âgée, la direction commerciale la performance par agence et par famille, "
        "et chaque commercial ne voit que ses clients, dans son agence, sans les coûts d'achat.",
        "<em>Données : Rhône Distribution est une entreprise fictive, son ERP est simulé par un générateur reproductible. Le profil des "
        "clients (secteurs NAF, tailles, communes) vient d'un agrégat SIRENE réel de 7 210 établissements du Rhône, de l'Ain, de l'Isère "
        "et de la Loire. Aucun nom ni SIREN réel n'est associé à un historique simulé.</em>",
    ],
    rh=[
        "<strong>La qualité prouvée, pas affirmée</strong> : 70 anomalies injectées, un test qui exige de les retrouver toutes, ni plus ni moins.",
        "<strong>La gouvernance dans le modèle</strong> : qui voit quoi est déclaré dans le YAML dbt et appliqué automatiquement.",
        "<strong>Des noms métier</strong> : dimensions et tables Gold nommées en français, prêtes pour Power BI.",
        "<strong>Un statut honnête</strong> : ce qui tourne en local, ce qui reste à exécuter sur Snowflake.",
    ],
    tech=[
        "ERP simulé dans <strong>PostgreSQL</strong>, extract nocturne agrégé au grain jour × client × produit × agence.",
        "<strong>Bronze</strong> (COPY INTO sur Snowflake, DuckDB en local) → <strong>Silver</strong> et <strong>Gold</strong> modélisés avec <strong>dbt</strong>.",
        "Table de faits <code>fct_ventes_jour</code> en <strong>incrémental</strong>, dimensions, agrégats financiers (balance âgée, DSO) et commerciaux.",
        "<strong>Row access policy</strong> par agence, <strong>masking policies</strong> sur les données personnelles et financières, tags de classification.",
        "Chargement Snowflake idempotent, procédure et Task planifiée, documentation dbt avec graphe de lignage.",
    ],
    stages=[
        ("Source", "source", ["ERP simulé (PostgreSQL)", "Profil SIRENE agrégé"]),
        ("Extract", "process", ["Extract nocturne agrégé"]),
        ("Bronze", "storage", ["COPY INTO Snowflake", "DuckDB en local"]),
        ("Silver (dbt)", "process", ["Nettoyage", "Quarantaine des anomalies"]),
        ("Gold (dbt)", "storage", ["Dimensions et faits", "Agrégats finance"]),
        ("Accès", "ops", ["Row access", "Masking, tags"]),
        ("Usage", "serve", ["Power BI (prévu)", "Features churn"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s1n0", "s2n0", "", False), ("s1n0", "s2n1", "", False),
           ("s2n0", "s3n0", "", False), ("s2n1", "s3n0", "", False), ("s3n0", "s3n1", "", False), ("s3n0", "s4n0", "", False),
           ("s4n0", "s4n1", "", False), ("s4n0", "s5n0", "", False), ("s5n0", "s5n1", "", False),
           ("s5n1", "s6n0", "", False), ("s4n0", "s6n1", "", False)],
    band=("Python · PostgreSQL · DuckDB · dbt · Snowflake (SQL, RBAC, row access, masking) · Make", "infra"),
    steps=[
        "<strong>Générer</strong> — ERP simulé reproductible (Parquet) et manifeste des anomalies injectées.",
        "<strong>Charger</strong> — base ERP PostgreSQL, puis extract nocturne agrégé.",
        "<strong>Transformer</strong> — Bronze, puis Silver et Gold avec dbt : 64 tests, dont la vérité terrain des anomalies.",
        "<strong>Sécuriser</strong> — rôles, row access et masking posés par le post-hook dbt.",
        "<strong>Exposer</strong> — tables Gold prêtes pour Power BI, snapshot de features pour un modèle de churn.",
    ],
    langs=[("SQL / dbt", 55), ("Python", 45)],
    tags=["Snowflake", "dbt", "SQL", "PostgreSQL", "DuckDB", "Row access policy", "Masking policy", "RGPD", "Qualité de données", "Python"],
    stack=[
        ("Snowflake", "Bronze, Silver, Gold, rôles, row access, masking, tags, Task", "Pilotage quotidien sur données agrégées, accès réglementés"),
        ("dbt", "Modèles Silver et Gold, 64 tests, post-hooks de sécurité, documentation et lignage", "Transformations versionnées, testées et documentées"),
        ("PostgreSQL", "ERP simulé", "Une vraie source transactionnelle à extraire"),
        ("DuckDB", "Bronze et build dbt en local", "Valider toute la chaîne sans compte cloud"),
        ("Python", "Générateur d'ERP, extract, chargeurs", "Données reproductibles à graine fixe"),
    ],
    matrix=dict(ci="y", tests="y", docker="n", orch="p", tracking="n", monitoring="n", serving="n", deploy="n", iac="n"),
    matrix_notes=dict(tests="64 tests dbt dont la vérité terrain des 70 anomalies", orch="Task Snowflake écrite ; chaîne lancée par make en local"),
    snippets=[],
    limits=[
        "Flux validé en local avec dbt Core (PostgreSQL + DuckDB), rejoué par la CI à chaque push. Scripts Snowflake écrits mais pas encore exécutés : la vérification des policies rôle par rôle reste à faire.",
        "Flux rapide Databricks, rapports Power BI et modèle de churn sous Snowpark ML : prévus, pas encore construits.",
        "Entreprise et historiques fictifs : les ordres de grandeur illustrent le fonctionnement, pas un résultat client.",
    ],
    custom_sections=[
        ("architecture", "Architecture", "Deux plateformes, chacune selon son délai", _PIPE),
        ("acces", "Gouvernance", "Qui voit quoi, appliqué par le modèle", _ACCES),
        ("qualite", "Qualité de données", "Une vérité terrain : 70 anomalies, 70 retrouvées", _QUALITE),
    ],
    strengths=[
        "<strong>Snowflake et dbt ensemble</strong> : couches Bronze, Silver, Gold, modèles incrémentaux, tests et lignage.",
        "<strong>Gouvernance des accès</strong> : row access par agence, masquage RGPD et financier, déclarés dans le modèle.",
        "<strong>Qualité vérifiable</strong> : chaque anomalie injectée est retrouvée par un test, et le test a déjà corrigé une règle fausse.",
    ],
)
