"""French / English: page paths and interface strings shared by the generated pages."""

# French path -> English path (pages that exist in both languages)
PATHS = {
    "/": "/en/",
    "/projets/": "/en/projects/",
    "/competences.html": "/en/skills.html",
    "/stack.html": "/en/stack.html",
    "/profil-rh.html": "/en/recruiters.html",
    "/profil-tech.html": "/en/tech-profile.html",
}
FR_OF = {v: k for k, v in PATHS.items()}


def project_path(slug, lang):
    return f"/en/projects/{slug}.html" if lang == "en" else f"/projets/{slug}.html"


def alt_path(path, lang):
    """Counterpart of `path` (written in `lang`) in the other language, or None."""
    if lang == "fr":
        if path.startswith("/projets/") and path.endswith(".html"):
            return "/en/projects/" + path[len("/projets/"):]
        return PATHS.get(path)
    if path.startswith("/en/projects/") and path.endswith(".html"):
        return "/projets/" + path[len("/en/projects/"):]
    return FR_OF.get(path)


def home(lang):
    return "/en/" if lang == "en" else "/"


T = {
    "fr": dict(
        home="Accueil", projects="Projets", all_projects="Tous les projets", all_projects_sub="vue d'ensemble · matrice MLOps",
        nav_about="Parcours", nav_skills="Compétences", nav_stack="Stack MLOps", nav_rh="Recruteurs", nav_tech="Profil technique",
        nav_contact="Contact", buyvera="Site commercial — Buyvera", buyvera_sub="projet achats · site produit bilingue",
        deck_sales="Présentation commerciale", deck_sales_sub="projet achats · 38 slides",
        deck_tech="Présentation technique", deck_tech_sub="projet achats · 21 slides",
        switch_label="English version", switch_text="EN",
        footer="Data Analyst · Data Scientist · MLOps — Lyon",
        # project page
        p_30s="En 30 secondes", p_30s_title="Le problème, la réponse, la preuve",
        p_rh="Pour le recruteur · valeur business", p_tech="Pour l'équipe technique · ce que le code prouve",
        p_pipe_label="Pipeline & architecture", p_pipe_title="Architecture de bout en bout",
        p_pipe_intro="Pipeline reconstitué à partir de l'analyse du dépôt : chaque brique correspond à du code réel. "
                     "Animez le flux, cliquez une brique pour suivre ses dépendances, ou ouvrez les schémas d'architecture.",
        p_steps="Étape par étape", p_pf_label="Points forts", p_pf_title="Les points forts de la solution",
        p_drawio="Schéma draw.io du pipeline",
        p_stack_label="Outils & langages", p_stack_title="Stack technique et pourquoi ces choix",
        p_langs="Langages (part du code)", p_langs_note="Lignes de code hors notebooks, calculées sur le dépôt.",
        p_keywords="Mots-clés", p_tool="Outil", p_role="Rôle dans le projet", p_shows="Ce que ça démontre",
        p_mlops_label="Maturité MLOps", p_mlops_title="Industrialisation : ce qui est en place",
        p_practice="Pratique", p_status="Statut", p_detail="Détail",
        p_res_label="Résultats", p_res_title="Métriques mesurées",
        p_code_label="Extraits de code", p_code_title="Le code qui fait la différence",
        p_lim_label="Regard critique", p_lim_title="Limites connues et prochaines étapes",
        p_lim_intro="Documenter honnêtement les limites fait partie du travail : c'est ce qui permet "
                    "à une équipe de décider en connaissance de cause.",
        p_prev="← Projet précédent", p_next="Projet suivant →",
        fig_full="⤢ Plein écran (SVG)", fig_dl="⬇ Fichier .drawio", fig_open="✎ Ouvrir dans draw.io",
        # pipeline
        pl_live="▶ Pipeline interactif", pl_play="▶ Animer le flux de données", pl_reset="Tout afficher",
        pl_hint="Cliquez une brique pour voir ce qu'elle reçoit et ce qu'elle alimente.",
        pl_flow="flux de données", pl_loop="boucle de suivi / réentraînement",
        pl_zoom="molette / glisser pour naviguer", gh_desc="Dépôt public sur GitHub",
        # shared tables
        matrix_project="Projet", matrix_caption="● implémenté · ◐ partiel · — absent — établi à partir du code de chaque dépôt.",
    ),
    "en": dict(
        home="Home", projects="Projects", all_projects="All projects", all_projects_sub="overview · MLOps matrix",
        nav_about="Background", nav_skills="Skills", nav_stack="MLOps stack", nav_rh="Recruiters", nav_tech="Tech profile",
        nav_contact="Contact", buyvera="Product website — Buyvera", buyvera_sub="procurement project · bilingual site",
        deck_sales="Sales deck (in French)", deck_sales_sub="procurement project · 38 slides",
        deck_tech="Technical deck (in French)", deck_tech_sub="procurement project · 21 slides",
        switch_label="Version française", switch_text="FR",
        footer="Data Analyst · Data Scientist · MLOps — Lyon, France",
        p_30s="In 30 seconds", p_30s_title="The problem, the answer, the proof",
        p_rh="For recruiters · business value", p_tech="For tech teams · what the code proves",
        p_pipe_label="Pipeline & architecture", p_pipe_title="End-to-end architecture",
        p_pipe_intro="Pipeline rebuilt from an analysis of the repository: every block maps to real code. "
                     "Play the data flow, click a block to follow its dependencies, or open the architecture diagrams.",
        p_steps="Step by step", p_pf_label="Key strengths", p_pf_title="Key strengths of the solution",
        p_drawio="Pipeline diagram (draw.io)",
        p_stack_label="Tools & languages", p_stack_title="Tech stack and why these choices",
        p_langs="Languages (share of code)", p_langs_note="Lines of code excluding notebooks, measured on the repository.",
        p_keywords="Keywords", p_tool="Tool", p_role="Role in the project", p_shows="What it demonstrates",
        p_mlops_label="MLOps maturity", p_mlops_title="Industrialization: what is in place",
        p_practice="Practice", p_status="Status", p_detail="Detail",
        p_res_label="Results", p_res_title="Measured metrics",
        p_code_label="Code excerpts", p_code_title="The code that makes the difference",
        p_lim_label="Critical review", p_lim_title="Known limitations and next steps",
        p_lim_intro="Documenting limitations honestly is part of the job: it lets a team make informed decisions.",
        p_prev="← Previous project", p_next="Next project →",
        fig_full="⤢ Full screen (SVG)", fig_dl="⬇ .drawio file", fig_open="✎ Open in draw.io",
        pl_live="▶ Interactive pipeline", pl_play="▶ Play the data flow", pl_reset="Show all",
        pl_hint="Click a block to see what feeds it and what it feeds.",
        pl_flow="data flow", pl_loop="monitoring / retraining loop",
        pl_zoom="scroll / drag to navigate", gh_desc="Public repository on GitHub",
        matrix_project="Project", matrix_caption="● implemented · ◐ partial · — absent — assessed from each repository's code.",
    ),
}

# MLOps matrix columns and status labels
MATRIX_COLS = {
    "fr": [("ci", "CI/CD"), ("tests", "Tests"), ("docker", "Docker"), ("orch", "Orchestration"),
           ("tracking", "Tracking / registry"), ("monitoring", "Monitoring / drift"),
           ("serving", "API"), ("deploy", "Déploiement"), ("iac", "IaC / K8s")],
    "en": [("ci", "CI/CD"), ("tests", "Tests"), ("docker", "Docker"), ("orch", "Orchestration"),
           ("tracking", "Tracking / registry"), ("monitoring", "Monitoring / drift"),
           ("serving", "API"), ("deploy", "Deployment"), ("iac", "IaC / K8s")],
}
MARK_LABEL = {"fr": {"y": "Implémenté", "p": "Partiel", "n": "Absent"},
              "en": {"y": "Implemented", "p": "Partial", "n": "Absent"}}
