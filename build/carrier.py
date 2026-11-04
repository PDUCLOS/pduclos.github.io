"""Carrier HVAC Europe — fiche détaillée (pipeline SAP → Power BI de mesure des délais usine, 12 entités, 3 usines).

Rien d'interne : noms génériques, aucun chiffre d'activité. Le titre de contrat reste « Data Analyst » (CLAIMS.md).
"""

from carrier_anim import anim

_TABLE = '<div class="table-wrap"><table class="stack-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'


def table(head, rows):
    return _TABLE.format(head="".join(f"<th>{h}</th>" for h in head),
                         rows="".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows))


_PROCESS = anim("journey", "fr") + table(["#", "Étape", "Acteur", "Jalon dans les données"], [
    ["1", "Devis, hors SAP", "Service commercial", "—"],
    ["2", "Intégration de la commande dans SAP via une passerelle avec le configurateur", "Commercial / SAP", "<strong>Date de création de la commande</strong>"],
    ["3", "Validation de l'encours client", "Service financier", "Commande validée ou bloquée"],
    ["4", "Création ou modification de l'article configuré, souvent quasi unique", "Master data", "Temps de traitement de l'article"],
    ["5", "Envoi à l'usine par passerelle, accusé de réception avec une date", "Usine", "<strong>Date accusée initiale (Date 1)</strong>"],
    ["6", "Fabrication, en retard ou en avance selon la charge ; reports éventuels", "Usine", "Date 2 (1 report), Date 3 (2 reports ou plus)"],
    ["7", "Mise à disposition sur parc, organisation de l'enlèvement avec accord écrit du client (grue de levage à prévoir)", "Customer service", "<strong>Date de mise à disposition</strong>, date d'expédition"],
    ["8", "Transit jusqu'au client, à la charge de Carrier", "Transport", "<strong>Date de livraison finale</strong>"],
]) + """<p style="margin-top:1rem">L'enjeu : l'usine doit mettre la machine à disposition <strong>avant</strong> la date qu'elle a accusée,
pour laisser au customer service le temps de transit. Ce temps est censé être renseigné dans SAP, ce qui n'est pas toujours le cas.
Chaque report oblige le customer service à replanifier l'enlèvement et à obtenir un nouvel accord écrit du client.</p>"""

_KPIS = anim("slip", "fr", "Glissement de mois : l'objectif commercial manqué à cause de l'usine") + table(["Indicateur", "Calcul", "Question à laquelle il répond"], [
    ["<strong>OTD usine</strong>", "Mise à disposition comparée à la date en vigueur, pour chacune des 3 usines", "L'usine tient-elle la date qu'elle donne ?"],
    ["<strong>Insatisfaction client</strong>", "Lignes en retard par rapport à la date accusée <em>initiale</em> (Date 1)", "Le client a-t-il été livré à la date qu'on lui avait promise ?"],
    ["<strong>Reports de date</strong>", "Lignes classées en 0, 1, 2 reports ou plus (Dates 1, 2, 3), écart en jours", "Quelle usine décale, et combien de fois ?"],
    ["<strong>Délai par étape</strong>", "Temps passé entre chaque jalon : finance, master data, accusé, fabrication, expédition, transit", "Où le temps se perd-il ?"],
    ["<strong>Charge customer service</strong>", "Replanifications d'enlèvement provoquées par les reports", "Combien coûtent les reports à l'équipe ?"],
    ["<strong>Glissement de mois</strong>", "Commandes prévues dans le mois et livrées au mois suivant, par usine, en chiffre d'affaires et bénéfice brut", "L'objectif commercial est-il manqué à cause de l'usine ?"],
]) + """<p style="margin-top:1rem">Le point de vue du client et celui de l'usine sont séparés : une usine peut tenir sa nouvelle date
et produire quand même une ligne insatisfaite, parce que le client avait planifié sa grue sur la date initiale.</p>"""

_DEVISES = anim("currency", "fr") + table(["Niveau", "Exemple : Pologne", "Point d'attention"], [
    ["Commande client (prix de vente)", "Zloty (PLN)", "Devise rarement indiquée dans l'export"],
    ["Commande de l'entité à l'usine", "Zloty (PLN)", "Même commande, autre montant"],
    ["Ordre côté usine, prix d'achat", "Euro (EUR)", "Le prix d'achat peut changer entre la commande et l'usine (hausse matière)"],
    ["Marge, bénéfice brut, chiffre d'affaires", "Euro (EUR)", "Carrier SAS reprend une marge pour la revente, le stockage et l'organisation de la livraison"],
    ["Consolidation groupe", "Dollar (USD)", "Chiffres européens consolidés pour les États-Unis"],
]) + """<p style="margin-top:1rem">Une même commande existe donc en monnaie locale côté entité et en euros côté usine : il fallait
savoir de quel côté venait chaque montant pour recalculer la marge réelle au moment où l'usine change son prix, et pas seulement à la commande.</p>"""

_COLLECTE = (anim("collect", "fr", "12 rapports, 12 SharePoint, une seule source à 8 h")
             + anim("columns", "fr", "240 colonnes ramenées à 80, typées et contrôlées"))

_MD = anim("tickets", "fr", "Le souci des tickets qui chevauchent les mois") + """<p>Problématique : les chiffres du service master data de Carrier SAS étaient faux. Ce projet a occupé la moitié de mon temps.
Il mesure l'activité du service, qui crée et modifie les articles dans SAP S/4HANA : une équipe encadre, forme et règle les
cas complexes ; une équipe spécialisée traite les demandes le plus vite possible.</p>
<p style="margin-top:1rem"><strong>Source.</strong> Chaque jour, un rapport ServiceNow de tous les tickets imputés au service, exporté depuis
une boîte mail vers un SharePoint, puis traité dans Power BI : création, prise en charge, traitement, clôture, motif, origine.</p>
<p style="margin-top:1rem"><strong>Le problème.</strong> Les tableaux de bord existants ne comptaient que les tickets clôturés.
Un ticket resté ouvert n'apparaissait nulle part ; un ticket ouvert sur plusieurs mois glissait d'un mois à l'autre, puis était
compté d'un coup au mois de création ou au mois de clôture, selon les cas. La charge de travail et le taux de réponse du service
étaient faussés. J'ai analysé comment les services comptaient les tickets, puis la règle a été refixée : <strong>chaque ticket est
compté dans son mois de création, et non de clôture</strong>. Les valeurs attendues sont retrouvées, et les tickets encore ouverts
restent visibles d'un mois à l'autre au lieu de disparaître.</p>""" + table(["Type de ticket", "Parcours", "Ce qu'il révèle"], [
    ["<strong>Simple</strong>", "Demande correcte : prise en charge, traitement et clôture en une fois, clôture quasi immédiate après le traitement", "Le cas le plus fréquent, celui à viser : demande juste, traitement rapide"],
    ["<strong>Aller-retour</strong>", "Demande mal formulée, renvoyée au demandeur, puis reprise par la master data", "Temps total bien plus long, à cause du formulaire"],
    ["<strong>Échanges multiples</strong>", "Plusieurs renvois avant d'aboutir, parfois sur plusieurs mois", "Les tickets qui faussaient les mois"],
]) + """<p style="margin-top:1rem"><strong>Ce que ça permet.</strong> Les requêtes sont typées par motif et par origine. On repère
les pays et les entités qui ont le plus de mal à formuler leur besoin dans le formulaire de création d'article, donc où former en
priorité pour obtenir des tickets simples dès le départ. Les tableaux de bord suivent l'activité dans la durée et vérifient si les
actions engagées réduisent le temps de traitement et les allers-retours.</p>"""

_ERCD = anim("pareto", "fr", "Pareto des erreurs : un nouveau contrôle s'intègre sans développement") + """<p>Problématique : les erreurs de création automatique d'articles envoyées par ERCD, l'activité pièces détachées de Carrier. ERCD pousse des
formulaires pré-remplis vers la master data, qui les injecte en masse dans SAP. Un collègue avait construit un fichier Excel qui
détecte, à chaque envoi, les données non conformes selon une liste de types d'erreurs prédéfinis.</p>
<p style="margin-top:1rem"><strong>Contrainte : uniquement M (Power Query) et DAX.</strong> Power Query lit le fichier de contrôle et
construit les tables croisées par type d'erreur. Le diagramme de Pareto n'existe pas tel quel dans Power BI : il faut préparer les
données (classement, cumul) pour qu'il soit exploitable. Une table de référence, un simple CSV, rattache chaque contrôle à sa catégorie.</p>""" + table(["Évolution", "Ce qu'il faut faire", "Résultat"], [
    ["Nouveau contrôle d'erreur", "Ajouter une ligne au CSV de référence, avec sa catégorie", "Automatique : l'erreur apparaît au bon endroit dans les Pareto"],
    ["Nouvelle catégorie d'erreur", "Développement spécifique dans le modèle", "Rare, car les catégories sont stables"],
]) + """<p style="margin-top:1rem"><strong>Ce que ça permet.</strong> Des plans d'action avec l'équipe ERCD pour supprimer définitivement
certains types d'erreurs, et le repérage, sur une période donnée, d'un nouveau type d'erreur qui apparaît, par exemple quand la personne
qui génère le fichier ne connaît pas certaines subtilités.</p>"""

_OVERVIEW = """<div class="cp3">
    <a class="cp3-card" href="#processus"><span>01</span><strong>OTD — délais usine</strong>
        <p><em>Problème</em> : 12 exports SAP hétérogènes, une promesse client invérifiable.</p>
        <p><em>Réponse</em> : une source unique à 8 h, l'OTD des 3 usines, les reports et leurs effets.</p></a>
    <a class="cp3-card" href="#master-data"><span>02</span><strong>ServiceNow — tickets master data</strong>
        <p><em>Problème</em> : seuls les tickets clôturés étaient comptés, la charge du service était faussée.</p>
        <p><em>Réponse</em> : tous les tickets suivis, typés par motif et origine, les besoins de formation repérés.</p></a>
    <a class="cp3-card" href="#erreurs-ercd"><span>03</span><strong>ERCD — Pareto des erreurs</strong>
        <p><em>Problème</em> : des erreurs à chaque envoi massif de pièces détachées, sans suivi exploitable.</p>
        <p><em>Réponse</em> : des Pareto en M et DAX, un nouveau contrôle ajouté par une ligne de CSV.</p></a>
</div>
<p style="margin-top:1rem">Les trois projets ont été menés en même temps, avec des sources, des utilisateurs et des objectifs
distincts. Ils sont présentés séparément ci-dessous.</p>"""

CARRIER = dict(
    slug="carrier-reporting",
    short="Carrier — Pilotage HVAC Europe",
    kicker="Expérience professionnelle · 12 mois · Mis en production",
    title="Carrier — trois projets data menés en parallèle, trois problématiques",
    title_html='Carrier : <span class="highlight">trois projets en parallèle</span>, trois problématiques, tous restés en service',
    lead="Data Analyst, 12 mois chez Carrier HVAC Europe, sur un périmètre SAP S/4HANA à 12 entités commerciales. "
         "J'ai mené trois projets en parallèle, chacun pour répondre à une problématique différente : "
         "1. mesurer si les 3 usines tiennent la date promise au client ; "
         "2. mesurer la vraie charge et le temps de réponse du service master data ; "
         "3. suivre et faire disparaître les erreurs de création automatique d'articles envoyées par ERCD.",
    kpis=[("3", "projets menés en parallèle"), ("12", "entités commerciales SAP S/4HANA"), ("3", "usines mesurées"),
          ("8 h", "données à jour chaque matin"), ("12 mois", "Data Analyst")],
    links=[],
    context=[
        "<strong>Projet 1 — OTD, délais usine.</strong> Une commande traverse le commerce, la finance, la master data, l'usine, le customer "
        "service et le transport ; l'usine peut reporter sa date plusieurs fois. Les données existaient dans 12 exports SAP de "
        "240 colonnes, sur 12 SharePoint, aux formats et devises différents. Il fallait en faire une mesure fiable de la promesse client.",
        "<strong>Projet 2 — ServiceNow, tickets master data.</strong> Les tableaux de bord existants ne comptaient que les tickets "
        "clôturés : les tickets ouverts sur plusieurs mois disparaissaient, et la charge comme le taux de réponse étaient faussés.",
        "<strong>Projet 3 — ERCD, Pareto des erreurs.</strong> Les envois massifs de l'activité pièces détachées généraient des "
        "erreurs de création d'articles ; il fallait les classer, les suivre dans le temps et pouvoir ajouter un contrôle sans développement.",
    ],
    rh=[
        "<strong>Trois problématiques, trois réponses</strong> : menées en parallèle, toutes mises en production et restées en service après mon départ.",
        "<strong>Projet 1 · OTD</strong> : le délai découpé par acteur, et l'insatisfaction client mesurée contre la date accusée initiale.",
        "<strong>Projet 2 · ServiceNow</strong> : tickets comptés au mois de création, et non de clôture ; la moitié de mon temps.",
        "<strong>Projet 3 · ERCD</strong> : un Pareto évolutif qui sert de base aux plans d'action avec ERCD.",
    ],
    tech=[
        "<strong>Projet 1 · OTD</strong> : Power Automate (12 SharePoint → 1, à jour à 8 h), Power Query (240 → 80 colonnes typées, "
        "1,5 Go ramenés à 800 Mo par cycle), lecture du code ABAP / SQL du rapport, harmonisation des formats et des devises, "
        "modèle TMDL et mesures DAX.",
        "<strong>Projet 2 · ServiceNow</strong> : rapport quotidien des tickets ServiceNow (boîte mail → SharePoint → Power BI), suivi des tickets ouverts "
        "d'un mois à l'autre, typage par motif et origine, temps de prise en charge, de traitement et de clôture.",
        "<strong>Projet 3 · ERCD</strong> : uniquement M et DAX ; tables croisées par type d'erreur, Pareto préparé dans les données, "
        "table de référence CSV qui rattache chaque contrôle à sa catégorie.",
    ],
    stages=[
        ("Sources", "source", ["Rapport SAP S/4HANA (CSV, 240 col.)", "Passerelle usines → SAP (Dates 1, 2, 3)"]),
        ("Collecte", "ingest", ["Power Automate : 12 SharePoint → 1", "Lot quotidien, à jour à 8 h"]),
        ("Préparation", "process", ["Power Query : 240 → 80 colonnes", "Typage explicite"]),
        ("Qualification", "ops", ["Lecture du code ABAP (SQL)", "Anomalies d'export → DSI"]),
        ("Harmonisation", "process", ["Formats des 12 pays", "Devises PLN → EUR → USD", "Hiérarchie entité → usine → ligne"]),
        ("Modèle", "storage", ["Modèle sémantique TMDL", "Mesures DAX"]),
        ("Pilotage", "ui", ["OTD des 3 usines", "Reports 0 / 1 / 2+", "Insatisfaction (AR initial)", "Glissement de mois, CA et BB"]),
    ],
    edges=[("s0n0", "s1n0", "×12", False), ("s0n1", "s1n0", "dates", False), ("s1n1", "s2n0", "déclenche", True),
           ("s1n0", "s2n0", "", False), ("s2n0", "s3n0", "", False), ("s2n1", "s3n1", "", False),
           ("s3n0", "s4n0", "", False), ("s3n0", "s4n1", "", False), ("s3n1", "s4n2", "", False),
           ("s4n0", "s5n0", "", False), ("s4n1", "s5n1", "taux", False), ("s4n2", "s5n0", "", False),
           ("s5n0", "s6n0", "", False), ("s5n1", "s6n1", "", False), ("s5n1", "s6n2", "", False), ("s5n1", "s6n3", "", False)],
    band=("SAP S/4HANA · SharePoint · Power Automate · Power Query (M) · Power BI (DAX, TMDL) · équipes européennes FR / EN", "infra"),
    steps=[
        "<strong>Source</strong> — chaque entité génère dans SAP S/4HANA un rapport CSV de 240 colonnes ; les dates accusées et "
        "modifiées (Dates 1, 2, 3) arrivent des usines par une passerelle.",
        "<strong>Collecte</strong> — Power Automate déplace et range les 12 rapports, posés sur 12 SharePoint, en un seul endroit, "
        "puis déclenche la mise à jour, chaque jour à heure fixe.",
        "<strong>Préparation</strong> — Power Query garde les 80 colonnes utiles et type chacune explicitement pour retrouver la structure réelle du fichier.",
        "<strong>Qualification</strong> — le code du rapport donne la source et l'intitulé de chaque colonne ; les anomalies d'export "
        "sont documentées et remontées à la DSI.",
        "<strong>Harmonisation</strong> — formats nationaux alignés, devises reconstituées, données hiérarchisées par entité, usine, commande et ligne.",
        "<strong>Pilotage</strong> — modèle Power BI et mesures DAX : OTD, reports, insatisfaction, délai par étape, glissements de mois.",
    ],
    extra_diagrams=[],
    langs=None,
    langs_note="Projet réalisé en entreprise : code non public.",
    tags=["Power BI", "DAX", "Power Query", "TMDL", "Power Automate", "SharePoint", "SAP S/4HANA", "ABAP / SQL", "ServiceNow",
          "OTD", "Pareto", "Master Data", "Data Quality", "Multidevise"],
    stack=[
        ("SAP S/4HANA", "P1 : rapport de 240 colonnes par entité, passerelle usines", "Lire le code du rapport pour qualifier la donnée"),
        ("Power Automate", "P1 : 12 SharePoint regroupés, mise à jour quotidienne", "Une source unique, à heure fixe"),
        ("Power Query (M)", "P1 : 240 → 80 colonnes typées · P2 : rapport de tickets · P3 : lecture du fichier de contrôle", "Préparation et réduction à la source"),
        ("DAX", "P1 : OTD, reports, glissements · P2 : charge, temps de réponse · P3 : Pareto", "Logique analytique"),
        ("Power BI / TMDL", "Modèles sémantiques et tableaux de bord des trois projets", "Restitution pour l'Europe"),
        ("SharePoint", "P1 : 12 rapports pays · P2 : rapport de tickets quotidien", "Point de dépôt des sources"),
    ],
    matrix=None,
    limits=[
        "Données et code confidentiels : cette page décrit la démarche sans exposer d'information interne ni chiffre d'activité.",
        "Le nombre de reports est classé en trois groupes (0, 1, 2 ou plus) : le rapport ne conserve pas chaque modification au-delà de la deuxième.",
    ],
    pipe_label="Projet 1 · Pipeline",
    pipe_title="Projet 1 · OTD — le pipeline des délais usine, de SAP au tableau de bord",
    custom_sections=[
        ("projets", "Trois projets", "Trois projets en parallèle, trois problématiques différentes", _OVERVIEW),
        ("processus", "Projet 1 · Processus", "Projet 1 · OTD — de la commande à la livraison", _PROCESS),
        ("collecte", "Projet 1 · Collecte", "Projet 1 · OTD — des exports SAP à une source fiable", _COLLECTE),
        ("indicateurs", "Projet 1 · Indicateurs", "Projet 1 · OTD — ce que mesurent les tableaux de bord", _KPIS),
        ("devises", "Projet 1 · Devises", "Projet 1 · OTD — une commande, trois devises", _DEVISES),
    ],
    custom_after=[
        ("master-data", "Projet 2 · ServiceNow", "Projet 2 · ServiceNow — la vraie charge du service master data", _MD),
        ("erreurs-ercd", "Projet 3 · Erreurs ERCD", "Projet 3 · ERCD — un Pareto évolutif des erreurs de création d'articles", _ERCD),
    ],
    strengths=[
        "<strong>Trois projets en parallèle</strong> : trois problématiques, trois dispositifs en production, restés en service après mon départ.",
        "<strong>Projet 1 · OTD — la promesse client mesurée</strong> : 12 exports uniformisés, code du rapport SAP relu, retard attribué à chaque acteur.",
        "<strong>Projet 2 · ServiceNow — des chiffres enfin justes</strong> : tous les tickets comptés, y compris ceux ouverts sur plusieurs mois.",
        "<strong>Projet 3 · ERCD — conçu pour évoluer</strong> : un nouveau contrôle d'erreur s'ajoute par une ligne dans un CSV, sans développement.",
    ],
)
