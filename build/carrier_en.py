"""English version of carrier.CARRIER (same slug, structure and figures)."""

from carrier import CARRIER as _FR, table
from carrier_anim import anim

_PROCESS = anim("journey", "en") + table(["#", "Step", "Who", "Milestone in the data"], [
    ["1", "Quote, outside SAP", "Sales", "—"],
    ["2", "Order entered in SAP through a gateway with the configurator", "Sales / SAP", "<strong>Order creation date</strong>"],
    ["3", "Customer credit check", "Finance", "Order released or blocked"],
    ["4", "Creation or update of the configured item, often almost unique", "Master data", "Item processing time"],
    ["5", "Order sent to the factory through a gateway, acknowledged with a date", "Factory", "<strong>Initial acknowledged date (Date 1)</strong>"],
    ["6", "Manufacturing, late or early depending on load; possible reschedules", "Factory", "Date 2 (1 reschedule), Date 3 (2 or more)"],
    ["7", "Machine made available on the yard, pickup organized with the customer's written agreement (crane to book)", "Customer service", "<strong>Availability date</strong>, shipping date"],
    ["8", "Transit to the customer, paid by Carrier", "Transport", "<strong>Final delivery date</strong>"],
]) + """<p style="margin-top:1rem">The key point: the factory must make the machine available <strong>before</strong> the date it
acknowledged, to leave customer service the transit time. That time is supposed to be recorded in SAP, which is not always the case.
Every reschedule forces customer service to replan the pickup and get a new written agreement from the customer.</p>"""

_KPIS = anim("slip", "en", "Month slippage: the sales target missed because of the factory") + table(["Indicator", "Calculation", "Question it answers"], [
    ["<strong>Factory OTD</strong>", "Availability compared with the current date, for each of the 3 factories", "Does the factory keep the date it gives?"],
    ["<strong>Customer dissatisfaction</strong>", "Lines late against the <em>initial</em> acknowledged date (Date 1)", "Was the customer delivered on the date first promised?"],
    ["<strong>Date reschedules</strong>", "Lines grouped as 0, 1, 2 or more reschedules (Dates 1, 2, 3), gap in days", "Which factory reschedules, and how often?"],
    ["<strong>Lead time per step</strong>", "Time between milestones: finance, master data, acknowledgment, manufacturing, shipping, transit", "Where is the time lost?"],
    ["<strong>Customer service workload</strong>", "Pickup replanning caused by reschedules", "What do reschedules cost the team?"],
    ["<strong>Month slippage</strong>", "Orders planned in the month and delivered the next, by factory, in revenue and gross profit", "Is the sales target missed because of the factory?"],
]) + """<p style="margin-top:1rem">The customer's view and the factory's view are kept apart: a factory can keep its new date and
still produce a dissatisfied line, because the customer had booked the crane for the initial date.</p>"""

_DEVISES = anim("currency", "en") + table(["Level", "Example: Poland", "Watch point"], [
    ["Customer order (selling price)", "Zloty (PLN)", "Currency rarely stated in the export"],
    ["Entity's order to the factory", "Zloty (PLN)", "Same order, different amount"],
    ["Factory order, purchase price", "Euro (EUR)", "The purchase price can change between the order and the factory (raw material increase)"],
    ["Margin, gross profit, revenue", "Euro (EUR)", "Carrier SAS takes a margin for resale, storage and organizing delivery"],
    ["Group consolidation", "US dollar (USD)", "European figures consolidated for the United States"],
]) + """<p style="margin-top:1rem">The same order therefore exists in local currency on the entity side and in euros on the factory
side: each amount had to be traced to its side to recompute the real margin when the factory changes its price, not only at order time.</p>"""

_COLLECTE = (anim("collect", "en", "12 reports, 12 SharePoint sites, one source at 8 am")
             + anim("columns", "en", "240 columns cut to 80, typed and checked"))

_MD = anim("tickets", "en", "The problem with tickets that overlap months") + """<p>Problem: the figures of the Carrier SAS master data service were wrong. This project took half of my time.
It measures the activity of the service, which creates and updates items in SAP S/4HANA: one team supervises, trains and solves
complex cases; a specialized team handles requests as fast as possible.</p>
<p style="margin-top:1rem"><strong>Source.</strong> Every day, a ServiceNow report of all tickets assigned to the service, exported from a
mailbox to a SharePoint site, then processed in Power BI: creation, pickup, processing, closure, reason, origin.</p>
<p style="margin-top:1rem"><strong>The problem.</strong> Existing dashboards only counted closed tickets. A ticket still open
appeared nowhere; a ticket open for several months slipped from month to month, then was counted all at once in its creation or
closure month, depending on the case. The service's workload and response rate were distorted. I analyzed how the services counted
tickets, then the rule was reset: <strong>each ticket is counted in its creation month, not its closure month</strong>. The expected values
are matched, and tickets still open stay visible from one month to the next instead of disappearing.</p>""" + table(["Ticket type", "Path", "What it shows"], [
    ["<strong>Simple</strong>", "Correct request: picked up, processed and closed in one go, closure almost right after processing", "The most frequent case, the one to aim for: right request, fast processing"],
    ["<strong>Round trip</strong>", "Poorly worded request, sent back to the requester, then taken up again by master data", "Much longer total time, caused by the form"],
    ["<strong>Multiple exchanges</strong>", "Several returns before completion, sometimes over several months", "The tickets that distorted the months"],
]) + """<p style="margin-top:1rem"><strong>What it enables.</strong> Requests are typed by reason and origin. It shows which countries
and entities struggle most to state their need in the item creation form, so where to train first to get simple tickets from the
start. Dashboards track activity over time and check whether the actions taken reduce processing time and round trips.</p>"""

_ERCD = anim("pareto", "en", "Error Pareto: a new check fits in without development") + """<p>Problem: errors in automatic item creation sent by ERCD, Carrier's spare parts business. ERCD pushes pre-filled forms to master data, which
mass-loads them into SAP. A colleague had built an Excel file that detects, at every upload, non-compliant data against a list of
predefined error types.</p>
<p style="margin-top:1rem"><strong>Constraint: M (Power Query) and DAX only.</strong> Power Query reads the check file and builds the
cross-tables by error type. Power BI has no ready-made Pareto chart: the data must be prepared (ranking, cumulative total) to make it
usable. A reference table, a plain CSV, maps each check to its category.</p>""" + table(["Change", "What it takes", "Result"], [
    ["New error check", "Add a line to the reference CSV, with its category", "Automatic: the error shows up in the right place in the Paretos"],
    ["New error category", "Specific development in the model", "Rare, since categories are stable"],
]) + """<p style="margin-top:1rem"><strong>What it enables.</strong> Action plans with the ERCD team to eliminate some error types for good,
and spotting, over a given period, a new error type as it appears, for example when the person generating the file does not know
some subtleties.</p>"""

_STAGES = [
    ("Sources", "source", ["SAP S/4HANA report (CSV, 240 col.)", "Factory → SAP gateway (Dates 1, 2, 3)"]),
    ("Collection", "ingest", ["Power Automate: 12 SharePoint → 1", "Daily batch, up to date at 8 am"]),
    ("Preparation", "process", ["Power Query: 240 → 80 columns", "Explicit typing"]),
    ("Qualification", "ops", ["Reading the ABAP code (SQL)", "Export anomalies → IT"]),
    ("Harmonization", "process", ["Formats of the 12 countries", "Currencies PLN → EUR → USD", "Entity → factory → line hierarchy"]),
    ("Model", "storage", ["TMDL semantic model", "DAX measures"]),
    ("Management", "ui", ["OTD of the 3 factories", "Reschedules 0 / 1 / 2+", "Dissatisfaction (initial ack.)", "Month slippage, revenue and GP"]),
]

_OVERVIEW = """<div class="cp3">
    <a class="cp3-card" href="#processus"><span>01</span><strong>OTD — factory lead times</strong>
        <p><em>Problem</em>: 12 heterogeneous SAP exports, a customer promise nobody could check.</p>
        <p><em>Answer</em>: one source at 8 am, OTD of the 3 factories, reschedules and their effects.</p></a>
    <a class="cp3-card" href="#master-data"><span>02</span><strong>ServiceNow — master data tickets</strong>
        <p><em>Problem</em>: only closed tickets were counted, so the service's workload was distorted.</p>
        <p><em>Answer</em>: every ticket tracked, typed by reason and origin, training needs identified.</p></a>
    <a class="cp3-card" href="#erreurs-ercd"><span>03</span><strong>ERCD — error Pareto</strong>
        <p><em>Problem</em>: errors at every spare parts mass upload, with no usable tracking.</p>
        <p><em>Answer</em>: Paretos in M and DAX, a new check added with one CSV line.</p></a>
</div>
<p style="margin-top:1rem">The three projects ran at the same time, with separate sources, users and goals. They are presented
separately below.</p>"""

CARRIER_EN = dict(
    slug="carrier-reporting",
    short="Carrier — HVAC Europe performance management",
    kicker="Professional experience · 12 months · In production",
    title="Carrier — three data projects run in parallel, three problems",
    title_html='Carrier: <span class="highlight">three projects in parallel</span>, three problems, all still in use',
    lead="Data Analyst, 12 months at Carrier HVAC Europe, on an SAP S/4HANA scope of 12 sales entities. I ran three projects in "
         "parallel, each answering a different problem: "
         "1. measure whether the 3 factories keep the date promised to the customer; "
         "2. measure the real workload and response time of the master data service; "
         "3. track and eliminate automatic item creation errors sent by ERCD.",
    kpis=[("3", "projects run in parallel"), ("12", "SAP S/4HANA sales entities"), ("3", "factories measured"),
          ("8 am", "data up to date every morning"), ("12 months", "Data Analyst")],
    links=[],
    context=[
        "<strong>Project 1 — OTD, factory lead times.</strong> An order goes through sales, finance, master data, the factory, customer "
        "service and transport; the factory can reschedule several times. The data existed in 12 SAP exports of 240 columns, on 12 "
        "SharePoint sites, with different formats and currencies. It had to become a reliable measure of the customer promise.",
        "<strong>Project 2 — ServiceNow, master data tickets.</strong> Existing dashboards only counted closed tickets: tickets open for several "
        "months disappeared, and both workload and response rate were distorted.",
        "<strong>Project 3 — ERCD, error Pareto.</strong> Mass uploads from the spare parts business generated item creation errors; "
        "they had to be classified, tracked over time, and new checks had to be addable without development.",
    ],
    rh=[
        "<strong>Three problems, three answers</strong>: run in parallel, all put into production and still in use after I left.",
        "<strong>Project 1 · OTD</strong>: lead time split by actor, customer dissatisfaction measured against the initial acknowledged date.",
        "<strong>Project 2 · ServiceNow</strong>: tickets counted in their creation month, not their closure month; half of my time.",
        "<strong>Project 3 · ERCD</strong>: an evolving Pareto used as the basis for action plans with ERCD.",
    ],
    tech=[
        "<strong>Project 1 · OTD</strong>: Power Automate (12 SharePoint → 1, up to date at 8 am), Power Query (240 → 80 typed columns, "
        "1.5 GB reduced to 800 MB per cycle), reading the report's ABAP / SQL code, format and currency harmonization, TMDL model and DAX measures.",
        "<strong>Project 2 · ServiceNow</strong>: daily ServiceNow ticket report (mailbox → SharePoint → Power BI), tracking of tickets open from month to month, "
        "typing by reason and origin, pickup, processing and closure times.",
        "<strong>Project 3 · ERCD</strong>: M and DAX only; cross-tables by error type, Pareto prepared in the data, reference CSV mapping each check to its category.",
    ],
    stages=_STAGES,
    edges=[(a, b, {"déclenche": "triggers", "taux": "rates"}.get(l, l), d) for a, b, l, d in _FR["edges"]],
    band=("SAP S/4HANA · SharePoint · Power Automate · Power Query (M) · Power BI (DAX, TMDL) · European teams FR / EN", "infra"),
    steps=[
        "<strong>Source</strong> — each entity generates a 240-column CSV report in SAP S/4HANA; acknowledged and modified dates "
        "(Dates 1, 2, 3) come from the factories through a gateway.",
        "<strong>Collection</strong> — Power Automate moves and files the 12 reports, stored on 12 SharePoint sites, in one place, "
        "then triggers the refresh, every day at a fixed time.",
        "<strong>Preparation</strong> — Power Query keeps the 80 useful columns and types each one explicitly to recover the file's real structure.",
        "<strong>Qualification</strong> — the report code gives the source and label of each column; export anomalies are documented and reported to IT.",
        "<strong>Harmonization</strong> — national formats aligned, currencies rebuilt, data organized by entity, factory, order and line.",
        "<strong>Management</strong> — Power BI model and DAX measures: OTD, reschedules, dissatisfaction, lead time per step, month slippage.",
    ],
    extra_diagrams=[],
    langs=None,
    langs_note="Company project: code not public.",
    tags=["Power BI", "DAX", "Power Query", "TMDL", "Power Automate", "SharePoint", "SAP S/4HANA", "ABAP / SQL", "ServiceNow",
          "OTD", "Pareto", "Master Data", "Data Quality", "Multi-currency"],
    stack=[
        ("SAP S/4HANA", "P1: 240-column report per entity, factory gateway", "Reading the report code to qualify the data"),
        ("Power Automate", "P1: 12 SharePoint sites gathered, daily refresh", "A single source, at a fixed time"),
        ("Power Query (M)", "P1: 240 → 80 typed columns · P2: ticket report · P3: reading the check file", "Preparation and reduction at source"),
        ("DAX", "P1: OTD, reschedules, slippage · P2: workload, response time · P3: Pareto", "Analytical logic"),
        ("Power BI / TMDL", "Semantic models and dashboards for all three projects", "Reporting for Europe"),
        ("SharePoint", "P1: 12 country reports · P2: daily ticket report", "Drop point for the sources"),
    ],
    matrix=None,
    limits=[
        "Confidential data and code: this page describes the approach without disclosing internal information or business figures.",
        "Reschedules are grouped in three classes (0, 1, 2 or more): the report does not keep each change beyond the second.",
    ],
    pipe_label="Project 1 · Pipeline",
    pipe_title="Project 1 · OTD — the factory lead-time pipeline, from SAP to the dashboard",
    custom_sections=[
        ("projets", "Three projects", "Three projects in parallel, three different problems", _OVERVIEW),
        ("processus", "Project 1 · Process", "Project 1 · OTD — from order to delivery", _PROCESS),
        ("collecte", "Project 1 · Collection", "Project 1 · OTD — from SAP exports to a reliable source", _COLLECTE),
        ("indicateurs", "Project 1 · Indicators", "Project 1 · OTD — what the dashboards measure", _KPIS),
        ("devises", "Project 1 · Currencies", "Project 1 · OTD — one order, three currencies", _DEVISES),
    ],
    custom_after=[
        ("master-data", "Project 2 · ServiceNow", "Project 2 · ServiceNow — the real workload of the master data service", _MD),
        ("erreurs-ercd", "Project 3 · ERCD errors", "Project 3 · ERCD — an evolving Pareto of item creation errors", _ERCD),
    ],
    strengths=[
        "<strong>Three projects in parallel</strong>: three problems, three solutions in production, still in use after I left.",
        "<strong>Project 1 · OTD — the customer promise measured</strong>: 12 exports standardized, SAP report code reviewed, delay assigned to each actor.",
        "<strong>Project 2 · ServiceNow — figures that are finally right</strong>: every ticket counted, including those open for several months.",
        "<strong>Project 3 · ERCD — built to evolve</strong>: a new error check is added with one line in a CSV, no development.",
    ],
)
