"""Animations de la fiche Carrier : données et textes FR / EN, joués par assets/site.js ([data-ca]).

Scénarios illustratifs : jours, montants et taux sont fictifs (aucun chiffre interne).
"""
import html
import json

_UI = {
    "fr": dict(play="▶ Lancer", replay="↻ Rejouer", day="Jour", fict="Scénario illustratif, valeurs fictives."),
    "en": dict(play="▶ Play", replay="↻ Replay", day="Day", fict="Illustrative scenario, fictitious values."),
}

_JOURNEY = {
    "fr": dict(
        stations=[["Devis", "Commercial"], ["Commande SAP", "Commercial"], ["Encours", "Finance"], ["Article", "Master data"],
                  ["Accusé", "Usine"], ["Fabrication", "Usine"], ["Mise à dispo.", "Customer service"], ["Livraison", "Transport"]],
        flags=dict(d1="Date 1", d2="Date 2", d3="Date 3", avail="Dispo.", deliv="Livrée"),
        max=110,
        scenarios=[
            dict(label="Avec 2 reports", events=[
                dict(day=0, st=0, txt="Devis accepté par le client, hors SAP."),
                dict(day=3, st=1, txt="Commande intégrée dans SAP via la passerelle avec le configurateur."),
                dict(day=5, st=2, txt="Encours client validé par la finance."),
                dict(day=11, st=3, txt="Article configuré créé par la master data."),
                dict(day=18, st=4, txt="L'usine accuse la commande : livraison promise au jour 70 (Date 1).", set=dict(d1=70)),
                dict(day=30, st=5, txt="Fabrication lancée."),
                dict(day=45, st=5, bad=True, txt="1er report de l'usine : Date 2 = jour 84. Le customer service replanifie l'enlèvement et obtient un nouvel accord écrit du client (grue).", set=dict(d2=84)),
                dict(day=62, st=5, bad=True, txt="2e report : Date 3 = jour 98. Nouvelle replanification, nouvel accord écrit.", set=dict(d3=98)),
                dict(day=94, st=6, txt="Machine mise à disposition sur parc ; le customer service organise l'expédition.", set=dict(avail=94)),
                dict(day=100, st=7, bad=True, txt="Livrée au client après 6 jours de transit : 2 jours après la date en vigueur, le transit n'était pas couvert.", set=dict(deliv=100)),
            ], result=[["OTD usine", "Tenu : dispo. jour 94 ≤ Date 3", True],
                       ["Client", "Insatisfait : +30 jours sur la Date 1", False],
                       ["Reports", "2 (classe « 2 ou plus »)", False],
                       ["Customer service", "2 replanifications, 2 accords écrits", False],
                       ["Mois", "Prévue en M3, livrée en M4 : CA et BB glissent", False]]),
            dict(label="Sans report", events=[
                dict(day=0, st=0, txt="Devis accepté par le client, hors SAP."),
                dict(day=3, st=1, txt="Commande intégrée dans SAP via la passerelle avec le configurateur."),
                dict(day=5, st=2, txt="Encours client validé par la finance."),
                dict(day=11, st=3, txt="Article configuré créé par la master data."),
                dict(day=18, st=4, txt="L'usine accuse la commande : livraison promise au jour 70 (Date 1).", set=dict(d1=70)),
                dict(day=30, st=5, txt="Fabrication lancée."),
                dict(day=60, st=6, txt="Machine mise à disposition avec la marge nécessaire au transit.", set=dict(avail=60)),
                dict(day=68, st=7, txt="Livrée au jour 68, avant la date promise.", set=dict(deliv=68)),
            ], result=[["OTD usine", "Tenu", True], ["Client", "Satisfait : livré avant la Date 1", True],
                       ["Reports", "0", True], ["Customer service", "1 seule planification", True],
                       ["Mois", "Livrée dans le mois prévu", True]]),
        ]),
    "en": dict(
        stations=[["Quote", "Sales"], ["SAP order", "Sales"], ["Credit", "Finance"], ["Item", "Master data"],
                  ["Acknowledgment", "Factory"], ["Manufacturing", "Factory"], ["Availability", "Customer service"], ["Delivery", "Transport"]],
        flags=dict(d1="Date 1", d2="Date 2", d3="Date 3", avail="Avail.", deliv="Delivered"),
        max=110,
        scenarios=[
            dict(label="With 2 reschedules", events=[
                dict(day=0, st=0, txt="Quote accepted by the customer, outside SAP."),
                dict(day=3, st=1, txt="Order entered in SAP through the configurator gateway."),
                dict(day=5, st=2, txt="Customer credit approved by finance."),
                dict(day=11, st=3, txt="Configured item created by master data."),
                dict(day=18, st=4, txt="The factory acknowledges the order: delivery promised on day 70 (Date 1).", set=dict(d1=70)),
                dict(day=30, st=5, txt="Manufacturing starts."),
                dict(day=45, st=5, bad=True, txt="1st factory reschedule: Date 2 = day 84. Customer service replans the pickup and gets a new written agreement from the customer (crane).", set=dict(d2=84)),
                dict(day=62, st=5, bad=True, txt="2nd reschedule: Date 3 = day 98. New replanning, new written agreement.", set=dict(d3=98)),
                dict(day=94, st=6, txt="Machine made available on the yard; customer service organizes shipping.", set=dict(avail=94)),
                dict(day=100, st=7, bad=True, txt="Delivered after 6 days of transit: 2 days after the current date, transit was not covered.", set=dict(deliv=100)),
            ], result=[["Factory OTD", "Kept: available day 94 ≤ Date 3", True],
                       ["Customer", "Dissatisfied: +30 days vs Date 1", False],
                       ["Reschedules", "2 (“2 or more” class)", False],
                       ["Customer service", "2 replannings, 2 written agreements", False],
                       ["Month", "Planned in M3, delivered in M4: revenue and GP slip", False]]),
            dict(label="No reschedule", events=[
                dict(day=0, st=0, txt="Quote accepted by the customer, outside SAP."),
                dict(day=3, st=1, txt="Order entered in SAP through the configurator gateway."),
                dict(day=5, st=2, txt="Customer credit approved by finance."),
                dict(day=11, st=3, txt="Configured item created by master data."),
                dict(day=18, st=4, txt="The factory acknowledges the order: delivery promised on day 70 (Date 1).", set=dict(d1=70)),
                dict(day=30, st=5, txt="Manufacturing starts."),
                dict(day=60, st=6, txt="Machine made available with the margin needed for transit.", set=dict(avail=60)),
                dict(day=68, st=7, txt="Delivered on day 68, before the promised date.", set=dict(deliv=68)),
            ], result=[["Factory OTD", "Kept", True], ["Customer", "Satisfied: delivered before Date 1", True],
                       ["Reschedules", "0", True], ["Customer service", "A single planning", True],
                       ["Month", "Delivered in the planned month", True]]),
        ]),
}

_COLLECT = {
    "fr": dict(src="SharePoint", hub="Power Automate", clock=["06:00", "08:00"],
               out=["OTD des 3 usines", "Reports de date", "Glissement de mois"],
               txt=["Chaque matin, 12 rapports SAP attendent sur 12 SharePoint différents, un par entité commerciale.",
                    "Power Automate les déplace et les range en un seul endroit.",
                    "La mise à jour est lancée en lot, à heure fixe.",
                    "À 8 h, les tableaux de bord sont à jour dans les 12 pays."]),
    "en": dict(src="SharePoint", hub="Power Automate", clock=["06:00", "08:00"],
               out=["OTD of the 3 factories", "Date reschedules", "Month slippage"],
               txt=["Every morning, 12 SAP reports wait on 12 different SharePoint sites, one per sales entity.",
                    "Power Automate moves and files them in one place.",
                    "The refresh runs as a batch, at a fixed time.",
                    "At 8 am, dashboards are up to date in all 12 countries."]),
}

_COLUMNS = {
    "fr": dict(total=240, kept=80, unit="colonnes",
               types=[["Date", 12, "t1"], ["Montant", 14, "t2"], ["Quantité", 8, "t3"], ["Code", 20, "t4"], ["Texte", 26, "t5"]],
               anomalies=["Décimales au format différent selon le pays", "Dates vides ou invalides",
                          "Intitulé qui ne correspond pas au champ source", "Montant sans devise indiquée"],
               fixed="identifiée, documentée, remontée à la DSI",
               txt=["L'export SAP arrive avec 240 colonnes.", "Power Query n'en garde que 80, celles dont le métier a besoin.",
                    "Chaque colonne reçoit un type explicite : la structure réelle du fichier réapparaît.",
                    "Le contrôle fait ressortir les anomalies d'export.",
                    "Chaque anomalie est rattachée à sa source dans le code du rapport et remontée à la DSI."]),
    "en": dict(total=240, kept=80, unit="columns",
               types=[["Date", 12, "t1"], ["Amount", 14, "t2"], ["Quantity", 8, "t3"], ["Code", 20, "t4"], ["Text", 26, "t5"]],
               anomalies=["Decimal format differs by country", "Empty or invalid dates",
                          "Label that does not match the source field", "Amount with no currency stated"],
               fixed="identified, documented, reported to IT",
               txt=["The SAP export arrives with 240 columns.", "Power Query keeps only 80, the ones the business needs.",
                    "Each column gets an explicit type: the file's real structure reappears.",
                    "Checks bring out the export anomalies.",
                    "Each anomaly is traced to its source in the report code and reported to IT."]),
}

_CURRENCY = {
    "fr": dict(
        cards=[["Prix de vente client", "400 000", "PLN"], ["Converti en euros", "93 000", "EUR"],
               ["Prix d'achat usine", "70 000", "EUR"], ["Bénéfice brut", "23 000", "EUR"], ["Consolidation US", "20 300", "USD"]],
        steps=[dict(show=[0], txt="Pologne : le client commande en zlotys, et l'export n'indique pas la devise."),
               dict(show=[1], txt="Le montant est ramené en euros (taux fictif) pour être comparable entre pays."),
               dict(show=[2], txt="L'usine facture l'entité en euros : c'est le prix d'achat."),
               dict(show=[3], bar=[3, 100], txt="Le bénéfice brut et le chiffre d'affaires sont reportés en euros."),
               dict(set=[[2, "74 200"], [3, "18 800"]], warn=[2, 3], bar=[3, 82], txt="Hausse matière : l'usine relève son prix d'achat de 6 %. Le prix de vente en zlotys ne bouge pas, la marge baisse."),
               dict(show=[4], txt="Les chiffres européens sont consolidés en dollars pour les États-Unis.")]),
    "en": dict(
        cards=[["Customer selling price", "400,000", "PLN"], ["Converted to euros", "93,000", "EUR"],
               ["Factory purchase price", "70,000", "EUR"], ["Gross profit", "23,000", "EUR"], ["US consolidation", "20,300", "USD"]],
        steps=[dict(show=[0], txt="Poland: the customer orders in zlotys, and the export does not state the currency."),
               dict(show=[1], txt="The amount is brought back to euros (fictitious rate) to compare countries."),
               dict(show=[2], txt="The factory invoices the entity in euros: that is the purchase price."),
               dict(show=[3], bar=[3, 100], txt="Gross profit and revenue are reported in euros."),
               dict(set=[[2, "74,200"], [3, "18,800"]], warn=[2, 3], bar=[3, 82], txt="Raw material increase: the factory raises its purchase price by 6%. The zloty selling price does not move, the margin drops."),
               dict(show=[4], txt="European figures are consolidated in US dollars for the United States.")]),
}

_SLIP = {
    "fr": dict(months=["Mois M", "M+1", "M+2"], orders=10, prefix="C", delivered="livrées", planned="prévues",
               moves=[[2, 1], [5, 1], [7, 1], [9, 2]],
               txt=["10 commandes sont prévues en livraison ce mois-ci : c'est l'objectif commercial.",
                    "Les usines reportent : chaque commande décalée part sur le mois suivant.",
                    "Résultat : 6 commandes livrées sur 10 en M. L'objectif est manqué, et la cause est l'usine, pas le commerce."]),
    "en": dict(months=["Month M", "M+1", "M+2"], orders=10, prefix="O", delivered="delivered", planned="planned",
               moves=[[2, 1], [5, 1], [7, 1], [9, 2]],
               txt=["10 orders are planned for delivery this month: that is the sales target.",
                    "Factories reschedule: each delayed order moves to the next month.",
                    "Result: 6 of 10 orders delivered in M. The target is missed, and the cause is the factory, not sales."]),
}

_PARETO = {
    "fr": dict(cats=[["Unité de mesure", 42], ["Désignation", 25], ["Groupe marchandises", 14], ["Poids / dimensions", 8],
                     ["Fournisseur", 5], ["Prix", 4], ["Code douane", 2]],
               add=[6, 30], cum="cumul", rule="80 %",
               txt=["Chaque envoi de ERCD est contrôlé : les erreurs détectées sont comptées par catégorie.",
                    "Pareto : catégories triées, courbe du cumul. Quelques catégories concentrent l'essentiel des erreurs.",
                    "Un nouveau contrôle est ajouté au fichier de référence (CSV) et rattaché à une catégorie existante.",
                    "Sans toucher au modèle, ses erreurs apparaissent au bon endroit : la catégorie remonte dans le Pareto."]),
    "en": dict(cats=[["Unit of measure", 42], ["Description", 25], ["Material group", 14], ["Weight / dimensions", 8],
                     ["Supplier", 5], ["Price", 4], ["Customs code", 2]],
               add=[6, 30], cum="cumulative", rule="80%",
               txt=["Every ERCD upload is checked: detected errors are counted by category.",
                    "Pareto: categories sorted, cumulative curve. A few categories hold most of the errors.",
                    "A new check is added to the reference file (CSV) and mapped to an existing category.",
                    "Without touching the model, its errors show up in the right place: the category moves up the Pareto."]),
}

_TK = [["T1", 3, 9, "simple"], ["T2", 12, 16, "simple"], ["T3", 20, 41, "aller"], ["T4", 25, 82, "multi"],
       ["T5", 36, 40, "simple"], ["T6", 52, 71, "aller"], ["T7", 66, None, "open"], ["T8", 75, 79, "simple"]]
_TICKETS = {
    "fr": dict(months=["Mois 1", "Mois 2", "Mois 3"], max=90, tickets=_TK,
               types=dict(simple="Simple", aller="Aller-retour", multi="Échanges multiples", open="Encore ouvert"),
               rows=["Vue « clôturés uniquement »", "Règle refixée : mois de création"], hidden="invisible", running="en cours",
               txt=["8 tickets arrivent au service sur 3 mois. Certains se règlent en une fois, d'autres chevauchent un ou plusieurs mois.",
                    "Vue des anciens tableaux de bord : seuls les tickets clôturés comptent, au mois de leur clôture. T7, encore ouvert, n'apparaît nulle part.",
                    "Le souci des chevauchements : T3, créé au mois 1 et clos au mois 2, sous-estime la charge du mois 1 et gonfle le mois 2. T4, ouvert près de 2 mois, n'apparaît qu'au mois 3.",
                    "Règle refixée : chaque ticket est compté dans son mois de création. Le mois 1 retrouve ses 4 tickets, et T7 reste visible, en cours.",
                    "Résultat : la charge réelle de chaque mois et le temps de réponse du service redeviennent justes, ticket par ticket."]),
    "en": dict(months=["Month 1", "Month 2", "Month 3"], max=90, tickets=_TK,
               types=dict(simple="Simple", aller="Round trip", multi="Multiple exchanges", open="Still open"),
               rows=["“Closed only” view", "Reset rule: creation month"], hidden="invisible", running="open",
               txt=["8 tickets reach the service over 3 months. Some are solved in one go, others overlap one or more months.",
                    "View of the old dashboards: only closed tickets count, in their closure month. T7, still open, appears nowhere.",
                    "The overlap problem: T3, created in month 1 and closed in month 2, understates month 1's workload and inflates month 2. T4, open nearly 2 months, only shows up in month 3.",
                    "Reset rule: each ticket is counted in its creation month. Month 1 gets its 4 tickets back, and T7 stays visible, still open.",
                    "Result: each month's real workload and the service's response time are right again, ticket by ticket."]),
}

_DATA = dict(tickets=_TICKETS, pareto=_PARETO, journey=_JOURNEY, collect=_COLLECT, columns=_COLUMNS, currency=_CURRENCY, slip=_SLIP)


def anim(kind, lang="fr", title=""):
    ui = _UI[lang]
    data = dict(_DATA[kind][lang], ui=ui)
    scen = ""
    if kind == "journey":
        scen = "".join(f'<button type="button" class="ca-scen" data-s="{i}" aria-pressed="{str(i == 0).lower()}">{html.escape(s["label"])}</button>'
                       for i, s in enumerate(data["scenarios"]))
    return f"""
<div class="ca" data-ca="{kind}" data-json="{html.escape(json.dumps(data, ensure_ascii=False))}">
    <div class="ca-bar"><button type="button" class="pl-play ca-play">{ui['play']}</button>{scen}<span class="ca-note">{ui['fict']}</span></div>
    {f'<h4 class="ca-title">{html.escape(title)}</h4>' if title else ''}
    <div class="ca-stage"></div>
    <p class="ca-log" aria-live="polite"></p>
</div>"""
