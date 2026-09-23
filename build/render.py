"""Shared page chrome (head, nav, footer) for the multi-page portfolio."""
import html

SITE = "https://pduclos.github.io"
REPO_RAW = "https://raw.githubusercontent.com/PDUCLOS/pduclos.github.io/main"

e = lambda s: html.escape(str(s), quote=True)


def head(title, description, path):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{e(description)}">
    <meta property="og:title" content="{e(title)}">
    <meta property="og:description" content="{e(description)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE}{path}">
    <link rel="canonical" href="{SITE}{path}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css?v=2">
</head>
<body>
"""


def nav(projects, current=""):
    """projects: list of dicts with slug, short, kicker. current: path of the active page."""
    items = []
    for p in projects:
        href = f"/projets/{p['slug']}.html"
        cur = ' aria-current="page"' if current == href else ""
        items.append(f'<li><a href="{href}"{cur}>{e(p["short"])}<small>{e(p["kicker"])}</small></a></li>')
    def link(href, label, cls=""):
        cur = ' aria-current="page"' if current == href else ""
        c = f' class="{cls}"' if cls else ""
        return f'<li><a href="{href}"{c}{cur}>{label}</a></li>'
    return f"""    <nav>
        <a href="/" class="nav-logo">P<span>.</span>D</a>
        <button class="nav-toggle" aria-label="Menu">
            <span></span><span></span><span></span>
        </button>
        <ul class="nav-links">
            {link('/#about', 'Parcours')}
            <li class="has-dropdown">
                <a href="/projets/" class="dropdown-toggle"{' aria-current="page"' if current.startswith('/projets/') else ''}>Projets</a>
                <ul class="dropdown">
                    <li><a href="/projets/">Tous les projets<small>vue d'ensemble · matrice MLOps</small></a></li>
                    <li class="dropdown-sep" aria-hidden="true"></li>
                    {''.join(items)}
                </ul>
            </li>
            {link('/stack.html', 'Stack MLOps')}
            {link('/profil-rh.html', 'Recruteurs')}
            {link('/profil-tech.html', 'Profil technique')}
            {link('/#contact', 'Contact', 'nav-cta')}
        </ul>
    </nav>
"""


FOOTER = """
    <footer>
        © 2026 Patrice Duclos — Data Analyst · Data Scientist · MLOps — Lyon ·
        <a href="https://github.com/PDUCLOS" style="color:var(--accent);text-decoration:none">GitHub</a> ·
        <a href="https://www.linkedin.com/in/patrice-duclos-04819b96" style="color:var(--accent);text-decoration:none">LinkedIn</a>
    </footer>
    <script src="/assets/site.js?v=2"></script>
</body>
</html>
"""


def badges(items):
    return "".join(f'<span class="tech-badge">{e(t)}</span>' for t in items)


def arrow():
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
