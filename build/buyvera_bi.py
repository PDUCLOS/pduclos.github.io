"""Buyvera BI (dépôt public buyvera-bi) : Power BI d'aide à la négociation des hausses fournisseurs.

Chiffres repris du README et de docs/portfolio/BUYVERA_BI_PORTFOLIO.md (novembre 2026).
Ce sont des résultats de démonstration : indices matières INSEE réels, tarifs, volumes, sites et fournisseurs fictifs.
"""

GH = "https://github.com/PDUCLOS/"
MEDIA = "/media/buyvera-bi"


def _shot(name, alt, caption):
    return (f'<div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/{name}.webp" alt="{alt}" '
            f'loading="lazy" draggable="false" style="min-width:0"></div><p class="code-caption">{caption}</p></div>')


_VIDEO = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">2 min, sans voix off · générée par script (Pillow, FFmpeg) à partir des vraies captures du rapport,
sur un seul fournisseur fictif suivi du début à la fin : la lettre de hausse, les références, le 80/20, les alertes,
la fiche négociation, les prix payés dans le groupe, les gains et le budget 2027.<br><strong>Montants fictifs du jeu de démonstration, pas des résultats.</strong></p>
<div style="display:flex;gap:1.2rem;align-items:center;flex-wrap:wrap;margin-top:1.6rem">
    <video controls preload="none" poster="{MEDIA}/social-poster.webp" style="width:min(100%,280px);aspect-ratio:9/16;border-radius:12px;border:1px solid var(--border);background:#0f1830">
        <source src="{MEDIA}/social.mp4" type="video/mp4">
    </video>
    <p class="code-caption" style="flex:1;min-width:200px">Version réseaux sociaux · 24 s, verticale, lisible sans le son : un message toutes les deux secondes.</p>
</div>"""

_SHOTS = '<div class="two-col" style="row-gap:1.6rem">' + "".join([
    _shot("parcours", "Page d'accueil du rapport : parcours de négociation en 5 étapes",
          "Parcours : 5 étapes (détecter, chiffrer, cibler, comprendre, négocier), chacune avec son chiffre clé et un bouton vers sa page."),
    _shot("synthese", "Synthèse de campagne", "Synthèse : combien d'euros renégocier, chez qui, sur quelles familles."),
    _shot("fournisseurs", "Nuage demandé × justifié par fournisseur", "Fournisseurs : hausse demandée face à la hausse justifiée par les matières, animée de 2024 à 2026."),
    _shot("alertes", "Alertes matières", "Alertes matières : signal à 3 mois, plafond justifié pour la campagne suivante, plan d'action."),
    _shot("fiche_negociation", "Fiche négociation avec simulateur", "Fiche négociation : argument rédigé, décalage prix / coût matière et simulateur de contre-proposition."),
    _shot("prix_payes", "Prix payés dans le groupe", "Prix payés : surcoût de chaque site face au meilleur prix du groupe, tarifs mal appliqués dans les ERP."),
    _shot("gains", "Gains de négociation", "Gains : économies obtenues face au potentiel chiffré avant chaque campagne."),
    _shot("previsions", "Page Prévisions (machine learning)", "Prévisions : plafond 2027 avec sa fourchette, volumes, segments fournisseurs, lignes anormales."),
]) + f'</div><p class="code-caption" style="margin-top:1.2rem"><strong>Captures et vidéos : montants fictifs du jeu de démonstration, pas des résultats.</strong></p>'

_ML = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Cas d'usage</th><th>Méthode d'évaluation</th><th>Usage acheteur</th></tr></thead>
    <tbody>
        <tr><td>Indices matières à 1-6 mois (INSEE, réels)</td><td>LightGBM et lissage comparés au naïf (« le mois prochain ressemble au dernier ») : <strong>le naïf gagne</strong>, il est retenu avec une fourchette tirée des erreurs passées</td><td>Plafond justifiable de la campagne suivante, avec sa fourchette</td></tr>
        <tr><td>Volumes par famille</td><td>Holt-Winters comparé au naïf saisonnier, gardé seulement s'il fait mieux</td><td>Quantités à anticiper avant la hausse</td></tr>
        <tr><td>Segmentation fournisseurs</td><td>KMeans, confronté aux comportements injectés dans les données de démonstration</td><td>Cibler opportunistes et effets cliquet</td></tr>
        <tr><td>Lignes tarifaires anormales</td><td>Isolation Forest, alertes vérifiées contre les profils fournisseurs</td><td>Lignes à vérifier en priorité</td></tr>
    </tbody></table></div>
<p style="margin-top:1rem">Chaque modèle passe un backtest chronologique (réentraîné à chaque date sur le seul passé) contre une référence naïve,
et n'est gardé que s'il la bat. Sur les cours de métaux, aucun modèle ne fait mieux que le naïf : l'outil le dit, et donne une
fourchette plutôt qu'une fausse précision.</p>"""

BUYVERA_BI = dict(
    slug="buyvera-bi",
    short="Buyvera BI — Power BI achats",
    kicker="Power BI · DAX · TMDL · Machine learning",
    title="Buyvera BI — cette hausse fournisseur est-elle justifiée ?",
    title_html='Power BI : cette hausse fournisseur <span class="highlight">est-elle justifiée ?</span>',
    lead="Projet Power BI de bout en bout pour les acheteurs industriels : il confronte chaque tarif aux cours réels des matières "
         "(indices INSEE), chiffre ce qui est renégociable, alerte avant le fournisseur, vérifie que chaque site du groupe paie "
         "le meilleur prix et mesure ce que la négociation a rapporté. Modèle généré par script en PBIP / TMDL, 103 mesures DAX, "
         "sécurité par ligne, machine learning testé contre une référence naïve.",
    kpis=[("103", "mesures DAX"), ("26", "tables, relations à sens unique"), ("13", "pages de rapport"),
          ("2", "rôles de sécurité par ligne"), ("0 écart", "Power BI / Python sur 5 chiffres clés")],
    links=[("Code source", GH + "buyvera-bi", True), ("Vidéo de présentation", "#video", False)],
    context=[
        "Chaque année, les fournisseurs annoncent une hausse « à cause des matières premières ». L'acheteur négocie souvent "
        "à l'aveugle : aucun lien chiffré entre la hausse demandée et l'évolution réelle des matières qui composent le produit, "
        "des baisses rarement répercutées (effet cliquet), un fournisseur qui connaît les cours avant lui, et, dans un groupe "
        "qui a racheté des sites, le même article payé plus cher d'un site à l'autre.",
        "Buyvera BI suit les questions que l'acheteur se pose avant un rendez-vous, dans l'ordre : détecter, chiffrer, cibler, "
        "comprendre, négocier, puis aligner les prix du groupe et prouver les gains. <em>Démonstration : indices matières "
        "INSEE réels ; tarifs, volumes, sites et fournisseurs fictifs, générés avec une graine fixe.</em>",
    ],
    rh=[
        "<strong>Une question métier avant les données</strong> : la logique vient de 20 ans de terrain B2B industriel.",
        "<strong>Un parcours, pas un tableau de chiffres</strong> : 5 étapes qui suivent la préparation d'un rendez-vous fournisseur, jusqu'à la contre-proposition.",
        "<strong>Démonstration complète</strong> : de la lettre de hausse du fournisseur à la contre-proposition, puis aux gains, sur un jeu de données fictif.",
        "<strong>Honnêteté sur le ML</strong> : le projet montre où le machine learning n'apporte rien, et le prouve par un backtest.",
    ],
    tech=[
        "Modèle en étoile <strong>PBIP / TMDL</strong> entièrement généré par script et versionné dans Git : 26 tables, 26 relations un-vers-plusieurs à filtrage unidirectionnel, 13 pages.",
        "Table pont article × matière <strong>sans relation bidirectionnelle</strong> : hausse justifiée calculée article par article puis pondérée par les volumes.",
        "<strong>Précalcul Python</strong> des hausses par article × campagne × fenêtre × décalage : les mesures répondent en une seconde, au centime près.",
        "<strong>Sécurité par ligne</strong> (rôles Acheteur et Direction, <code>USERPRINCIPALNAME()</code>), testée ; chaque table, colonne et mesure documentée.",
        "Contrôles bloquants, tests DAX sur le moteur local de Power BI Desktop, contrôle croisé Power BI / Python à l'écart nul sur 5 chiffres clés.",
    ],
    stages=[
        ("Sources", "source", ["INSEE BDM (API SDMX)", "Données fictives à graine fixe"]),
        ("Préparation", "process", ["Précalcul des hausses", "Groupe et négociations"]),
        ("Machine learning", "ml", ["Prévisions et fourchettes", "Segments et anomalies"]),
        ("Contrôles", "ops", ["Contrôles bloquants", "Tests DAX + recalcul Python"]),
        ("Modèle", "storage", ["PBIP / TMDL généré", "103 mesures DAX", "Sécurité par ligne"]),
        ("Restitution", "serve", ["Rapport 13 pages", "Fiche négociation", "Tableau de bord Claude"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n1", "s1n1", "", False),
           ("s0n0", "s2n0", "", False), ("s1n0", "s2n0", "", False), ("s1n1", "s2n1", "", False),
           ("s1n0", "s3n0", "", False), ("s2n0", "s3n0", "", False), ("s2n1", "s3n0", "", False),
           ("s3n0", "s4n0", "", False), ("s4n0", "s4n1", "", False), ("s4n1", "s4n2", "", False),
           ("s4n1", "s5n0", "", False), ("s4n1", "s5n1", "", False), ("s1n0", "s5n2", "mêmes CSV", False),
           ("s4n1", "s3n1", "écart nul", True)],
    band=("Python (pandas, NumPy) · scikit-learn, statsmodels, LightGBM · Power BI Desktop · Git / GitHub · vidéo générée par script", "infra"),
    steps=[
        "<strong>Indices réels</strong> — 7 séries INSEE mensuelles (cuivre, aluminium, nickel, zinc, métaux ferreux, naphta) récupérées par l'API SDMX.",
        "<strong>Données de démonstration</strong> — 3 000 articles, 10 142 lignes de tarifs, 62 095 lignes d'achats ; hausse demandée = hausse justifiée + biais du profil fournisseur + bruit.",
        "<strong>Précalcul</strong> — hausses par article, vision groupe sur 3 sites, résultats de négociation ; puis machine learning (prévisions, segments, anomalies).",
        "<strong>Contrôles</strong> — comportements injectés retrouvés automatiquement, tests DAX, recalcul Python des chiffres clés.",
        "<strong>Power BI</strong> — modèle et rapport générés par script au format PBIP, ouverts dans Power BI Desktop sans licence Pro.",
    ],
    extra_diagrams=[("buyvera-bi-architecture", "Pipeline et modèle du projet")],
    langs=[("Python", 60), ("TMDL / DAX", 40)],
    langs_note="≈ 4 230 lignes de Python (pipeline, ML, contrôles, génération du rapport) et ≈ 2 870 lignes de TMDL (modèle et mesures).",
    tags=["Power BI", "DAX", "TMDL / PBIP", "Sécurité par ligne", "Python", "pandas", "INSEE SDMX", "scikit-learn",
          "statsmodels", "LightGBM", "Achats"],
    stack=[
        ("Power BI Desktop", "Rapport de 13 pages, navigation par parcours, info-bulles, segments synchronisés", "Livrer une interface qu'un acheteur ouvre avant son rendez-vous"),
        ("DAX", "103 mesures rangées par dossier, simulateur de contre-proposition", "Mesures exactes sur une table pont, sans double compte"),
        ("TMDL / PBIP", "Modèle et rapport générés par script, versionnés dans Git", "BI traitée comme du code : revue, historique, reproductibilité"),
        ("Sécurité par ligne", "Rôles Acheteur et Direction", "Chaque acheteur ne voit que ses familles, testé"),
        ("Python (pandas, NumPy)", "API INSEE, données fictives, précalcul, contrôles", "Pipeline reproductible à graine fixe"),
        ("scikit-learn, statsmodels, LightGBM", "Prévisions, segmentation, anomalies", "Modèles gardés seulement s'ils battent une référence naïve"),
        ("Tableau de bord Claude", "Même analyse à partir des mêmes CSV", "Note à la direction ou préparation de rendez-vous"),
    ],
    matrix=dict(ci="n", tests="y", docker="n", orch="p", tracking="n", monitoring="n", serving="n", deploy="n", iac="n"),
    matrix_notes=dict(tests="Contrôles bloquants, tests DAX, recalcul Python à l'écart nul", orch="Scripts Python enchaînés, sans orchestrateur"),
    snippets=[],
    limits=[
        "Tarifs, volumes, sites et fournisseurs fictifs : les montants illustrent le fonctionnement, pas un résultat client.",
        "Pas d'orchestrateur ni d'intégration continue : le pipeline est une suite de scripts lancés dans l'ordre.",
        "Fonctionne dans Power BI Desktop ; la publication sur le service Power BI (rafraîchissement planifié) reste à faire.",
        "Hypothèse affichée pour la part non matière (main-d'œuvre, énergie) : +2 % par an.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 2 minutes", _VIDEO),
        ("ecrans", "Les écrans", "Un parcours de négociation, pas un tableau de chiffres", _SHOTS),
        ("ml", "Machine learning", "Ce que l'historique permet vraiment de prédire", _ML),
    ],
    strengths=[
        "<strong>Le fait contre l'argument</strong> : chaque hausse comparée aux cours réels des matières qui composent l'article.",
        "<strong>BI industrialisée</strong> : modèle PBIP / TMDL généré par script, versionné, documenté, sécurité par ligne testée.",
        "<strong>Chiffres vérifiés</strong> : définitions uniques en Python et en DAX, contrôle croisé à l'écart nul.",
        "<strong>ML sans esbroufe</strong> : chaque modèle passe un backtest contre une référence naïve, et le naïf gagne quand il le mérite.",
    ],
)
