"""English version of rhone_distribution.RHONE_DISTRIBUTION (same slug, structure and figures)."""

from rhone_distribution import RHONE_DISTRIBUTION as _FR, MEDIA

_PIPE = f"""
<div class="pipeline-figure" style="padding:.6rem"><img src="{MEDIA}/pipeline.png" alt="Rhône Distribution pipeline: simulated ERP, nightly extract, Bronze, dbt Silver and Gold, Snowflake, Databricks, Power BI" loading="lazy" draggable="false" style="min-width:0"></div>
<p class="code-caption">The project diagram: a slow Snowflake flow (daily, aggregated, regulated access) and a fast Databricks flow (planned). Labels in French.</p>"""

_ACCES = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Role</th><th>Visible branches</th><th>Customer contacts (GDPR)</th><th>Costs and margins</th></tr></thead>
    <tbody>
        <tr><td><code>RD_DAF</code> (finance)</td><td>all</td><td>clear</td><td>clear</td></tr>
        <tr><td><code>RD_DIRECTION_COMMERCIALE</code> (sales management)</td><td>all</td><td>masked</td><td>clear</td></tr>
        <tr><td><code>RD_ANALYSTE</code></td><td>all</td><td>masked</td><td>masked</td></tr>
        <tr><td><code>RD_COMMERCIAL_&lt;AGENCE&gt;</code> (sales rep)</td><td><strong>own branch only</strong></td><td>clear</td><td>masked</td></tr>
        <tr><td><code>RD_POWERBI_SVC</code></td><td>all (Gold read-only)</td><td>masked</td><td>masked</td></tr>
    </tbody></table></div>
<p style="margin-top:1rem">Row access policy per branch (role → branch mapping table), <code>pii_masking</code> and <code>finance_masking</code>
masking policies, classification tags. dbt recreates tables on every run, so the policies are attached by a <strong>post-hook</strong>
driven by the <code>meta</code> declared in the model YAML. Bronze and Silver are never exposed to business users.</p>
<p class="code-caption"><strong>Status:</strong> Snowflake scripts written, not yet run on a Snowflake account: role-by-role checks still to do.</p>"""

_QUALITE = """
<div class="table-wrap"><table class="stack-table">
    <thead><tr><th>Injected anomaly</th><th>Count</th></tr></thead>
    <tbody>
        <tr><td>zero price</td><td>25</td></tr>
        <tr><td>negative quantity not flagged as a return</td><td>12</td></tr>
        <tr><td>shipment dated before the order</td><td>15</td></tr>
        <tr><td>orphan invoice (no order)</td><td>10</td></tr>
        <tr><td>customer without a postcode</td><td>8</td></tr>
    </tbody></table></div>
<p style="margin-top:1rem">The generator injects <strong>70 anomalies</strong> and writes their exact count to a manifest. The Silver layer quarantines
them, and a dbt test requires the quarantine to match that manifest <strong>exactly</strong>, no more, no less. The test has already
paid off: a first "zero price" rule produced 5 false positives (a sale cancelled by a same-day return). The build failed and the rule was fixed.</p>"""

RHONE_DISTRIBUTION_EN = dict(
    slug="rhone-distribution",
    short="Rhône Distribution — Snowflake + dbt",
    kicker="Snowflake · dbt · SQL · Access governance",
    badge="PUBLIC PROJECT, DBT VALIDATED LOCALLY",
    title="Rhône Distribution — a Snowflake warehouse modelled with dbt",
    title_html='Snowflake and dbt: <span class="highlight">reliable data, regulated access</span>',
    lead="A fictitious B2B distributor in Lyon (5 branches, about 1,200 business customers) wants to track revenue, margin, DSO and "
         "service level, without everyone seeing everything. The Snowflake flow loads aggregated data every night, dbt turns it into "
         "tested Silver and Gold layers, and access is regulated by role: branch, personal data, costs. "
         "Built with dbt Core and validated end to end locally; Snowflake scripts ready, not yet run on a Snowflake account.",
    kpis=[("64", "dbt tests"), ("70 / 70", "injected anomalies found"), ("5", "Snowflake access roles"),
          ("7,210", "SIRENE establishments behind the customer profile")],
    links=[("Source code", "https://github.com/PDUCLOS/rhone-distribution-lakehouse", True), ("dbt docs and lineage", "https://pduclos.github.io/rhone-distribution-lakehouse/", True), ("Regulated access", "#acces", False)],
    context=[
        "An industrial supplies distributor (PPE, tools, fasteners, plumbing, electrical) wants reliable reporting: finance tracks revenue, "
        "margin, DSO and aged balance, sales management tracks performance by branch and product family, and each sales rep sees only "
        "their own customers, in their own branch, without purchase costs.",
        "<em>Data: Rhône Distribution is a fictitious company and its ERP is simulated by a reproducible generator. The customer profile "
        "(NAF sectors, sizes, towns) comes from a real aggregate of 7,210 SIRENE establishments in the Rhône, Ain, Isère and Loire areas. "
        "No real company name or SIREN number is attached to a simulated history.</em>",
    ],
    rh=[
        "<strong>Quality proven, not claimed</strong>: 70 injected anomalies, and a test that requires finding all of them, no more, no less.",
        "<strong>Governance in the model</strong>: who sees what is declared in the dbt YAML and applied automatically.",
        "<strong>Business names</strong>: Gold dimensions and tables named in French, ready for Power BI.",
        "<strong>An honest status</strong>: what runs locally, and what still has to run on Snowflake.",
    ],
    tech=[
        "Simulated ERP in <strong>PostgreSQL</strong>, nightly extract aggregated to day × customer × product × branch.",
        "<strong>Bronze</strong> (COPY INTO on Snowflake, DuckDB locally) → <strong>Silver</strong> and <strong>Gold</strong> modelled with <strong>dbt</strong>.",
        "<strong>Incremental</strong> fact table <code>fct_ventes_jour</code>, dimensions, finance (aged balance, DSO) and sales aggregates.",
        "<strong>Row access policy</strong> per branch, <strong>masking policies</strong> on personal and financial data, classification tags.",
        "Idempotent Snowflake load, stored procedure and scheduled Task, dbt documentation with lineage graph.",
    ],
    stages=[
        ("Source", "source", ["Simulated ERP (PostgreSQL)", "Aggregated SIRENE profile"]),
        ("Extract", "process", ["Nightly aggregated extract"]),
        ("Bronze", "storage", ["COPY INTO Snowflake", "DuckDB locally"]),
        ("Silver (dbt)", "process", ["Cleaning", "Anomaly quarantine"]),
        ("Gold (dbt)", "storage", ["Dimensions and facts", "Finance aggregates"]),
        ("Access", "ops", ["Row access", "Masking, tags"]),
        ("Use", "serve", ["Power BI (planned)", "Churn features"]),
    ],
    edges=list(_FR["edges"]),
    band=("Python · PostgreSQL · DuckDB · dbt · Snowflake (SQL, RBAC, row access, masking) · Make", "infra"),
    steps=[
        "<strong>Generate</strong> — reproducible simulated ERP (Parquet) and manifest of injected anomalies.",
        "<strong>Load</strong> — PostgreSQL ERP database, then nightly aggregated extract.",
        "<strong>Transform</strong> — Bronze, then Silver and Gold with dbt: 64 tests, including the anomaly ground truth.",
        "<strong>Secure</strong> — roles, row access and masking applied by the dbt post-hook.",
        "<strong>Expose</strong> — Gold tables ready for Power BI, feature snapshot for a churn model.",
    ],
    langs=list(_FR["langs"]),
    tags=["Snowflake", "dbt", "SQL", "PostgreSQL", "DuckDB", "Row access policy", "Masking policy", "GDPR", "Data quality", "Python"],
    stack=[
        ("Snowflake", "Bronze, Silver, Gold, roles, row access, masking, tags, Task", "Daily reporting on aggregated data, regulated access"),
        ("dbt", "Silver and Gold models, 64 tests, security post-hooks, documentation and lineage", "Versioned, tested and documented transformations"),
        ("PostgreSQL", "Simulated ERP", "A real transactional source to extract from"),
        ("DuckDB", "Bronze and dbt build locally", "Validate the whole chain without a cloud account"),
        ("Python", "ERP generator, extract, loaders", "Reproducible data with a fixed seed"),
    ],
    matrix=dict(_FR["matrix"]),
    matrix_notes=dict(tests="64 dbt tests including the ground truth of the 70 anomalies", orch="Snowflake Task written; chain run with make locally"),
    snippets=[],
    limits=[
        "Flow validated locally with dbt Core (PostgreSQL + DuckDB), replayed by CI on every push. Snowflake scripts written but not yet run: role-by-role policy checks still to do.",
        "Fast Databricks flow, Power BI reports and Snowpark ML churn model: planned, not built yet.",
        "Fictitious company and histories: orders of magnitude illustrate how it works, not a client result.",
    ],
    custom_sections=[
        ("architecture", "Architecture", "Two platforms, each at its own pace", _PIPE),
        ("acces", "Governance", "Who sees what, enforced by the model", _ACCES),
        ("qualite", "Data quality", "A ground truth: 70 anomalies, 70 found", _QUALITE),
    ],
    strengths=[
        "<strong>Snowflake and dbt together</strong>: Bronze, Silver, Gold layers, incremental models, tests and lineage.",
        "<strong>Access governance</strong>: row access per branch, GDPR and financial masking, declared in the model.",
        "<strong>Verifiable quality</strong>: every injected anomaly is found by a test, and the test has already fixed a wrong rule.",
    ],
)
