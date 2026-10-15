"""Purchasing analytics project, written from a business-analyst angle (anonymised: no company, supplier, site or amount). English version."""

LEVERS = [
    ("G1", "Negotiate on the <strong>volume-weighted</strong> increase, not on the advertised average", "0.3 to 0.8 pt of increase avoided on the spend under review", "Quantified argument, item by item"),
    ("G2", "Pay the <strong>agreed price</strong>: gap between price paid in the ERP and price due", "0.10 to 0.50% of spend", "Separates a simple delay in applying the price from a truly unexplained gap"),
    ("G3", "Align entities on the <strong>best price in the group</strong>", "30 to 50% of the gap between sites", "Never a €0 price when data is missing"),
    ("G4", "Enforce <strong>special prices</strong>: increase caps, volume commitments, undeclared agreements", "0.5 to 1.5% of the spend concerned", "Negotiation sentence written out with its source"),
    ("G5", "Give <strong>time back to the buyer</strong>", "1.5 to 3 days per price review", "Time reinvested in negotiation, not in copying data"),
    ("G6", "<strong>Buy ahead of the increase</strong> up to the point where stock costs more than it saves", "benefit ∝ increase² / holding cost", "Capped by shelf life and provisioning rules"),
]
lever_rows = "".join(f"<tr><td>{c}</td><td>{l}</td><td>{o}</td><td>{n}</td></tr>" for c, l, o, n in LEVERS)

STAKEHOLDERS = [
    ("Buyer", "Negotiate fast, with indisputable figures", "Negotiation file, one-page memo, review queue sorted by stake"),
    ("Procurement lead / product owner", "Decide on thresholds, rules and priorities", "Rules in configuration, decision log"),
    ("Procurement leadership", "Manage supplier performance and savings", "Quarterly scorecards, consolidated Board, realized savings"),
    ("Finance / management control", "Reliable figures", "Every amount traceable to its source; no guessed values"),
    ("IT department", "Security, operations, cost", "Read-only access to ERPs, role-based access profiles, backups, lossless updates"),
]
stake_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in STAKEHOLDERS)

ACHATS = dict(
    slug="achats-negociation",
    short="Procurement — prices & scorecards",
    kicker="Ongoing project · Project Manager · Procurement",
    badge="ONGOING PROJECT · END-TO-END PROJECT MANAGER",
    title="Procurement negotiation support platform",
    title_html='Procurement Project Manager: turning every price increase into a <span class="highlight">quantified argument</span>',
    lead="A real project, ongoing within an industrial Procurement department. I <strong>run the project end to end</strong>: "
         "scoping and business analysis, business case, specifications, architecture, development of the Python / DuckDB engine and the "
         "R/Shiny interface, user acceptance testing with buyers, deployment — and its go-to-market, with the commercial website.",
    kpis=[("≈ 1%", "of tracked spend (central gain)"), ("1.71", "interface contract delivered"), ("133", "backlog items tracked"),
          ("≈ 4,650", "automated tests"), ("6", "quantified gain levers")],
    links=[("Commercial website (Buyvera)", "https://buyvera.fr/en/", True),
           ("Sales presentation (in French)", "/presentations/plateforme-tarifs.html", False),
           ("Technical presentation (in French)", "/presentations/hausses-tarifaires.html", False)],
    context=[
        "<strong>This project is real and ongoing.</strong> I manage it end to end, from requirements gathering "
        "to production rollout and the sales presentation. <em>Anonymised presentation: no real company, supplier, site or amount; "
        "the numerical examples come from the demo dataset, which is entirely fictitious. Code not public.</em>",
        "A Procurement department receives dozens of price reviews every year, in every format (Excel, CSV, PDF). "
        "Today, the buyer spends <strong>1 to 3 days per review</strong> reformatting the file, matching items "
        "to the ERP and quantifying the impact — and often negotiates on the increase <em>advertised</em> by the supplier.",
        "The project supports two processes: analysis of <strong>supplier price lists</strong> (from receipt to negotiation file) "
        "and quarterly <strong>supplier scorecards</strong> (no more re-keying; the buyer keeps only the judgment calls).",
    ],
    rh=[
        "<strong>End-to-end Project Manager</strong> on a real project: requirements, specifications, architecture, development, user acceptance testing, deployment, go-to-market.",
        "<strong>Quantified business case</strong> in three scenarios (low / central / high): from 0.5% to 2.3% of tracked spend, payback from the first quarter.",
        "Failure conditions spelled out in black and white: unreliable volumes, unmatched master data, unfavorable balance of power, alerts not followed up.",
        "Proposed organization: a team of 8, including <strong>two business profiles</strong> deemed essential to success.",
    ],
    tech=[
        "Python 3.12 engine driven by YAML configuration: adding a supplier is a matter of <strong>configuration, not code</strong>.",
        "<strong>Matching cascade</strong> L0 exact → L1 rules → L2 fuzzy (rapidfuzz) → L3 human review, versioned and reversible master data.",
        "DuckDB warehouse (≈ 120 tables, 91 interface views under a versioned contract), read-only R/Shiny interface, 8 access profiles enforced server-side.",
        "Quality: ≈ 3,850 Python tests (pytest-xdist), ≈ 800 R tests (testthat), GitHub Actions CI Python 3.12 / 3.13 + ruff, access control tested.",
        "Guiding principle: what the engine cannot read stays <strong>empty, with its reason</strong> — never zero, never guessed.",
    ],
    custom_sections=[
        ("nouveautes", "Latest releases", "Interface contract 1.65 → 1.71: what was just delivered",
         '<p style="margin-bottom:1.5rem">The project moves forward through versions of the interface contract between the engine and the screen. '
         "Here are the last seven, and what is being prepared for the next one.</p>"
         '<div class="three-col" style="margin-bottom:1.2rem">'
         '<div class="arg-card arg-card--tech"><span class="arg-label">Price list reading & quality</span><ul>'
         "<li><strong>Strict item keys</strong>: a collision is detected, never silently merged (B-111).</li>"
         "<li><strong>Effective date per line</strong> (B-112) and <strong>dimension plausibility checks</strong> (B-113).</li>"
         "<li><strong>Unusual families</strong> detected, with file encoding diagnostics (B-114).</li>"
         "<li><strong>Items to create and duplicates</strong> grouped by dimensions, purchase prices to update, bulk rejection of likely new items (B-116).</li>"
         "<li><strong>Supplementary price list</strong> with a partial price list alert (B-121); matrix column for an unknown entity blocked (B-122).</li></ul></div>"
         '<div class="arg-card arg-card--tech"><span class="arg-label">Table-based PDFs & master data</span><ul>'
         "<li><strong>Table-based PDF price lists</strong>: extraction, then validated upload; 0.90 confidence threshold and 24 documented PDF rules (B-05).</li>"
         "<li><strong>Family mapping table</strong>: six-column CSV / XLSX import, annotated template, preview by default, applied on confirmation, "
         "reversible (B-132).</li>"
         "<li>Data typing chosen by the user and checked on both sources: “007” stays “007”.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Safe operations</span><ul>'
         "<li><strong>Demo database purge</strong> in four steps: plan, approval, execution, status (B-120).</li>"
         "<li>Safeguards: demo or test environment only, single-use token, confirmation phrase, dual administrator approval.</li>"
         "<li>Verified backup before any purge, <strong>automatic restore</strong> if the operation fails.</li></ul></div></div>"
         '<div class="three-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Identity & documentation</span><ul>'
         "<li>The product is called <strong>Buyvera</strong> on screen (buyvera.fr); the project remains anonymous.</li>"
         "<li>Documentation rebuilt: <strong>four draw.io architecture diagrams</strong> (below) and a group-level simulation.</li>"
         "<li><strong>Local LLM assistant</strong>, optional and can be switched off: specification, pipeline and model study written (B-118); nothing is developed before a decision.</li>"
         "<li><strong>IT budget and gains</strong> recalculated in a formula-driven workbook (B-133).</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">In progress — contract 1.72</span><ul>'
         "<li>Guided restore after a purge; listing and organizing backups, with their organization diagram.</li>"
         "<li>Transfer package to another machine.</li>"
         "<li>Automatic backup: scheduling templates, status and stale-backup alert.</li></ul></div>"
         '<div class="arg-card arg-card--rh"><span class="arg-label">Known defects, tracked in the backlog</span><ul>'
         "<li>B-123: 42 correct links suspended for “inconsistent price”.</li>"
         "<li>B-127: savings include quarantined lines.</li>"
         "<li>B-119: minor interface defects.</li>"
         "<li><em>Defects are named and quantified, not hidden: that is the project rule.</em></li></ul></div></div>"),
        ("presentations", "Go-to-market", "Commercial website and project presentations",
         '<p style="margin-bottom:1.5rem">The product has its own <strong>bilingual commercial website</strong> (Astro, Buyvera brand — buyvera.fr) and two decks '
         "that I designed and presented: one to <strong>sell</strong>, the other to <strong>get a decision</strong> from leadership.</p>"
         '<a class="deck-card" href="https://buyvera.fr/en/" style="margin-bottom:1.5rem"><img src="/presentations/buyvera-home.webp" alt="Home page of the Buyvera commercial website" loading="lazy" width="1600" height="900">'
         '<div><span class="project-tag" style="color:var(--accent-warm)">Commercial website · FR / EN · 33 pages</span>'
         "<h3>Buyvera — every acquisition brings its prices, keep the best ones</h3>"
         "<p>Static Astro site: accessible animations (pause, keyboard, no JS), no inline scripts, fictitious sample data, "
         "nothing promised that isn't delivered.</p></div></a>"
         '<div class="deck-cards">'
         '<a class="deck-card" href="/presentations/plateforme-tarifs.html"><img src="/presentations/plateforme-tarifs/01.webp" alt="First slide of the sales presentation" loading="lazy" width="1600" height="900">'
         '<div><span class="project-tag" style="color:var(--accent-warm)">Sales presentation · 38 slides (in French)</span>'
         "<h3>Price platform — going into negotiation informed</h3><p>Stakes, six functional chapters, differentiation, acknowledged limitations.</p></div></a>"
         '<a class="deck-card" href="/presentations/hausses-tarifaires.html"><img src="/presentations/hausses-tarifaires/01.webp" alt="First slide of the technical presentation" loading="lazy" width="1600" height="900">'
         '<div><span class="project-tag" style="color:var(--accent-warm)">Technical presentation · 21 slides (in French)</span>'
         "<h3>Price increases — the foundation is built</h3><p>Findings, pipeline, calculations, delivery status, costing, risks, decisions.</p></div></a>"
         "</div>"),
        ("mon-role", "My role", "I manage the whole project",
         '<div class="three-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Scoping & business analysis</span><ul>'
         "<li><strong>Requirements gathering</strong> with buyers and Procurement leadership; mapping of the current and target processes.</li>"
         "<li><strong>24 business rules</strong> formalized (RG-xx), with their edge cases, followed by a full critical review of the rules.</li>"
         "<li>Versioned <strong>specifications</strong> (v3) and <strong>requirements traceability</strong> down to the tests.</li>"
         "<li><strong>Business case</strong>: 6 quantified levers in 3 scenarios, explicit failure conditions.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Steering & follow-up</span><ul>'
         "<li><strong>Backlog of 133 items</strong> described precisely enough to be estimated, prioritized with the business lead.</li>"
         "<li><strong>Dated, traced decisions</strong> (frozen scope, trade-offs, architecture choices).</li>"
         "<li><strong>Regular progress checks</strong> and dated code reviews: what is actually delivered, not what is announced.</li>"
         "<li><strong>User acceptance testing</strong> on replayed real files, report handed to the buyer for sign-off; go / no-go milestones.</li>"
         "<li><strong>Steering of delegated work packages</strong>: each package has its written request, acceptance criteria and review checklist.</li></ul></div>"
         '<div class="arg-card arg-card--tech"><span class="arg-label">Delivery & go-to-market</span><ul>'
         "<li><strong>Architecture and development</strong>: Python / DuckDB engine, R/Shiny interface, ≈ 4,650 tests, continuous integration.</li>"
         "<li><strong>Deployment</strong>: reliability plan, backups, lossless updates, access profiles.</li>"
         "<li><strong>Sales and decision presentations</strong>, designed and delivered.</li>"
         '<li>Bilingual <strong>commercial website</strong> for the product (Astro): <a href="https://buyvera.fr/en/" style="color:var(--accent)">see it →</a></li></ul></div></div>'),
        ("parties-prenantes", "Stakeholders", "Who needs what",
         '<div class="table-wrap"><table class="stack-table"><thead><tr><th>Stakeholder</th><th>Need</th><th>Response provided</th></tr></thead>'
         f"<tbody>{stake_rows}</tbody></table></div>"),
        ("processus", "As-is / to-be process", "From the supplier file to the negotiation memo",
         '<div class="two-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Today (as-is)</span><ul>'
         "<li>Manual reformatting and item matching: 1 to 2 days.</li>"
         "<li>Year-over-year comparison and impact quantification: 0.5 to 1 day.</li>"
         "<li>Arguments and memo: 0.5 day.</li>"
         "<li>Checking that the price is applied in the ERP: rarely done.</li>"
         "<li>Negotiation on the average increase announced by the supplier.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Target (to-be)</span><ul>'
         "<li>File uploaded as is; template recognized and remembered: 30 min.</li>"
         "<li>Automatic matching; the buyer only reviews doubtful cases.</li>"
         "<li>Volume-weighted increase, annualized impact, Pareto: automatic.</li>"
         "<li>One-page memo and Excel support produced: 15 min.</li>"
         "<li>ERP price application gaps detected and quantified every month.</li></ul></div></div>"
         '<p style="margin-top:1.5rem">Example from the demo (fictitious data): a price list announced at <strong>+4.80%</strong> '
         "only weighs <strong>+2.08%</strong> once weighted by volumes and the discount grid — and the impact comes down to a handful of items.</p>"),
        ("business-case", "Business case", "Six gain levers, quantified and bounded",
         '<div class="table-wrap"><table class="stack-table"><thead><tr><th>#</th><th>Lever</th><th>Order of magnitude</th><th>What makes it credible</th></tr></thead>'
         f"<tbody>{lever_rows}</tbody></table></div>"
         '<div class="kpi-row" style="margin-top:1.5rem">'
         '<div class="kpi"><b>0.47%</b><span>low scenario</span></div>'
         '<div class="kpi"><b>1.15%</b><span>central scenario</span></div>'
         '<div class="kpi"><b>2.29%</b><span>high scenario</span></div>'
         '<div class="kpi"><b>Q1</b><span>return on investment</span></div></div>'
         "<p>Gains expressed as a share of tracked spend. They always separate what is <strong>measured</strong> (on the demo) from "
         "what is <strong>estimated</strong> (assumptions to be confirmed on real data), and the method for replacing estimates with "
         "actual figures from the first campaign onward is documented.</p>"
         '<p>Prerequisite for every other gain: <strong>reading prices without error</strong>. Replaying a corpus of price lists revealed ten silent '
         "reading errors (an ignored “price per 1,000” basis = a price a thousand times too low; a US-format date = a three-month gap). "
         "Each one now has its own regression test.</p>"),
        ("risques", "Risks & success conditions", "What would make these figures wrong",
         '<div class="two-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Identified failure conditions</span><ul>'
         "<li><strong>Unreliable ERP volumes</strong>: the weighting collapses (the tool then refuses to quantify).</li>"
         "<li><strong>Unmatched master data</strong>: no comparison possible — the first workstream, in buyer time.</li>"
         "<li><strong>Unfavorable balance of power</strong>: the tool provides the argument, not the leverage.</li>"
         "<li><strong>Alerts not acted upon</strong>: a gap that is detected but never corrected yields nothing.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Deployment plan (6 months, 8 work packages)</span><ul>'
         "<li>L0 scoping and access → L1 ERP connection → L2 master data migration → L3 user acceptance testing on real data.</li>"
         "<li>L4 interface and access profiles → L5 savings and negotiation → L6 industrialization → L7 rollout and training.</li>"
         "<li>Go / no-go milestones: one entity connected (M2), one supplier validated end to end by the buyer (M3).</li>"
         "<li>Functional scope frozen, documentation delivered with each work package.</li></ul></div></div>"),
    ],
    stages=[
        ("Sources", "source", ["Supplier price lists (xlsx, csv, pdf)", "Entity ERPs", "ECB exchange rates"]),
        ("Ingestion", "ingest", ["Template + unique key", "Pre-read report"]),
        ("Normalization", "process", ["Currencies, units", "Item reference masks"]),
        ("Matching", "ml", ["L0 → L2 cascade", "Human review (L3)"]),
        ("Analysis", "process", ["Volume-weighted increase", "Special prices, ERP gaps"]),
        ("Warehouse", "storage", ["DuckDB + log"]),
        ("Output", "ui", ["R/Shiny interface", "Memo + Excel file", "Scorecards + Board"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s1n0", "s1n1", "", False),
           ("s1n1", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s3n0", "", False),
           ("s3n0", "s3n1", "doubt", True), ("s3n0", "s4n0", "", False), ("s3n1", "s4n0", "", False),
           ("s4n0", "s4n1", "", False), ("s4n1", "s5n0", "", False), ("s5n0", "s6n0", "read-only", False),
           ("s6n0", "s6n1", "", False), ("s6n1", "s6n2", "", False)],
    band=("YAML configuration per supplier · pytest (≈ 3,850) · testthat (≈ 800) · GitHub Actions · read-only ERP", "infra"),
    steps=[
        "<strong>Upload</strong> — the file is received as is, fingerprinted and archived; a duplicate is rejected.",
        "<strong>Understand</strong> — template recognized, unique key detected, reading report presented before any calculation.",
        "<strong>Match</strong> — each supplier item is linked to the ERP item through the cascade; the buyer only reviews doubtful cases, once.",
        "<strong>Analyze</strong> — weighted increase, annualized impact, Pareto, discounts, special price caps, ERP application gaps; outliers go to quarantine.",
        "<strong>Negotiate</strong> — one-page memo, Excel support and correction request; every figure points back to its source.",
    ],
    extra_diagrams=[("achats-arch-pipeline", "Data pipeline: from price list file to decisions (10 steps)"),
                    ("achats-arch-logique", "Layers, house rules, profiles and permissions"),
                    ("achats-arch-deploiement", "Deployment and continuous integration: today, target, LLM option"),
                    ("achats-parcours", "Journey of a price list — and what the tool refuses to do"),
                    ("achats-cascade", "Matching cascade to ERP items"),
                    ("achats-architecture", "Architecture and data flows")],
    langs=[("Python", 78), ("R", 18), ("YAML", 3), ("JavaScript", 1)],
    tags=["Business Analysis", "Procurement", "Business case", "Business rules", "Specifications", "Python", "DuckDB",
          "R / Shiny", "rapidfuzz", "pandas", "YAML", "pytest", "GitHub Actions"],
    stack=[
        ("Business analysis", "Business rules, edge cases, critical review of the rules (critical defects, gaps)", "Formalize what the buyer does implicitly"),
        ("Business case", "6 quantified levers in 3 scenarios, failure conditions", "Well-argued investment decision"),
        ("Specifications + backlog", "Traced requirements, estimable work packages, go / no-go milestones", "Project steering"),
        ("Python + pandas", "Reading, normalization and analysis engine", "Industrialize business rules"),
        ("rapidfuzz", "Fuzzy matching of item references", "Robust matching with safeguards"),
        ("DuckDB", "File-based analytical warehouse, views under contract", "Serverless embedded analytics"),
        ("R / Shiny", "Buyer workstation, 5 profiles", "Business interface"),
        ("YAML", "One configuration file per supplier", "Scalability without development"),
        ("pytest · testthat · GitHub Actions", "≈ 3,850 Python tests + ≈ 800 R tests, multi-version CI", "Reliable figures"),
    ],
    matrix=dict(ci="y", tests="y", docker="p", orch="p", tracking="n", monitoring="p", serving="y", deploy="p", iac="n"),
    matrix_notes=dict(ci="Python 3.12 / 3.13, ruff; R testthat", tests="≈ 3,850 Python tests + ≈ 800 R tests",
                      docker="Containerized multi-user deployment planned", orch="Schedulable, replayable campaigns",
                      monitoring="Log of all operations, ingestion register", serving="R/Shiny interface",
                      deploy="Full replayable demo; rollout in work packages"),
    snippets=[
        ("tarifs/rattachement.py — L3 level of the cascade: fuzzy matching with stated reasons",
         '''# L3 — fuzzy matching (RG-07). `score_cutoff`: rapidfuzz drops candidates below the display
# threshold early; same result as filtering afterwards, with far less work.
choix = process.extract(refnorm, idx["cles"], scorer=fuzz.ratio, limit=int(s["nb_candidats"]) + 1,
                        score_cutoff=float(s.get("seuil_candidat_min", 0)))
cands = [{"reference_erp": par_norm[c], "score": round(sc, 1),
          "rapproche": f"{sc:.0f}% similarity on the normalized reference",
          "separe": f"{refnorm} ≠ {c}"} for c, sc, _ in choix if sc >= s.get("seuil_candidat_min", 0)]'''),
    ],
    limits=[
        "Containerized multi-user deployment (B-92) and corporate directory integration still in the backlog.",
        "Known and tracked defects: B-123 (links wrongly suspended), B-127 (savings and quarantine), B-119 (interface).",
        "Only one rich industry profile (industrial) besides the generic profile; interface in French.",
        "Gains remain estimates until the first campaign on real data has taken place — the measurement method is ready.",
        "Critical review of business rules completed: critical defects identified (price tiers, discounts, encodings) and fixed one by one, each with a dedicated test.",
    ],
)
