"""HTML viewers for the anonymised slide decks of the purchasing project (slides exported as WebP + transcript.json)."""
import json
from pathlib import Path
from render import head, nav, FOOTER, arrow, e

DECKS = [
    dict(slug="plateforme-tarifs", kind="Présentation commerciale",
         title="Plateforme tarifs — entrer en négociation en sachant",
         lead="La présentation qui vend le produit à une direction Achats : enjeux, six chapitres fonctionnels du fichier reçu "
              "au pilotage du service, différenciation, limites assumées et prochaine étape.",
         audience="Direction Achats, acheteurs, décideurs",
         points=["Structurée en 6 chapitres, chacun répondant à une question d'acheteur",
                 "Chaque promesse adossée à un écran qui existe — et une page « ce qui n'est pas encore livré »",
                 "Écrans issus de la démonstration (données fictives)"]),
    dict(slug="hausses-tarifaires", kind="Présentation technique & demande de décision",
         title="Hausses tarifaires — le socle est construit",
         lead="La note de décision présentée à la direction : constat chiffré, difficultés structurelles, chaîne de traitement, "
              "calculs clés, état de réalisation, chiffrage en jours, risques et trois décisions demandées.",
         audience="Direction Achats, DSI, sponsor du projet",
         points=["Suivi de projet : réalisé / à décider / plus tard, chiffré en jours",
                 "Risques explicites et la façon de les tenir",
                 "Indicateurs de succès mesurables, traçabilité vers le cahier des charges"]),
]

SITE = Path(__file__).resolve().parent.parent


def deck_page(deck, projects):
    slug = deck["slug"]
    path = f"/presentations/{slug}.html"
    slides = json.loads((SITE / "presentations" / slug / "transcript.json").read_text(encoding="utf-8"))
    n = len(slides)
    figs = []
    for i, blocks in enumerate(slides, 1):
        title = blocks[1] if len(blocks) > 1 and blocks[0].isupper() else (blocks[0] if blocks else f"Slide {i}")
        text = "".join(f"<p>{e(b).replace(chr(10), '<br>')}</p>" for b in blocks)
        figs.append(f"""
            <figure class="slide reveal" id="s{i}">
                <button class="slide-img" data-i="{i - 1}" aria-label="Agrandir la slide {i}">
                    <img src="/presentations/{slug}/{i:02d}.webp" alt="Slide {i} — {e(title)}" loading="{'eager' if i <= 2 else 'lazy'}" width="1600" height="900">
                </button>
                <figcaption><span class="slide-num">{i:02d} / {n:02d}</span>
                    <details><summary>Transcription</summary><div class="slide-text">{text}</div></details></figcaption>
            </figure>""")
    other = [d for d in DECKS if d["slug"] != slug][0]
    body = f"""
    <header class="page-hero">
        <div class="hero-bg-grid"></div>
        <div class="hero-glow hero-glow-1"></div>
        <div class="hero-content">
            <div class="breadcrumb"><a href="/">Accueil</a> / <a href="/projets/achats-negociation.html">Projet Achats</a> / {e(deck['kind'])}</div>
            <div class="live-badge" style="position:static;display:inline-flex;margin-bottom:1.2rem"><span class="live-dot"></span> PROJET EN COURS · BUSINESS ANALYST</div>
            <span class="project-tag" style="color:var(--accent-warm)">{e(deck['kind'])} · {n} slides</span>
            <h1>{e(deck['title'])}</h1>
            <p class="lead">{deck['lead']}</p>
            <div class="kpi-row">
                <div class="kpi"><b>{n}</b><span>slides</span></div>
                <div class="kpi"><b style="font-size:1rem;line-height:1.4">{e(deck['audience'])}</b><span>public visé</span></div>
            </div>
            <div class="btn-row">
                <button class="contact-btn contact-btn-primary" id="deck-play">▶ Mode présentation</button>
                <a class="contact-btn contact-btn-secondary" href="/projets/achats-negociation.html">← Le projet</a>
                <a class="contact-btn contact-btn-secondary" href="/presentations/{other['slug']}.html">{e(other['kind'])} {arrow()}</a>
            </div>
        </div>
    </header>
    <section class="page-section">
        <div class="section-container">
            <div class="arg-card arg-card--rh" style="margin-bottom:2.5rem"><span class="arg-label">Ce que montre ce support</span><ul>
                {''.join(f'<li>{p}</li>' for p in deck['points'])}
                <li><em>Version anonymisée pour le portfolio : nom de l'entreprise, fournisseurs, entités et sites retirés ; notes du présentateur non publiées.</em></li></ul></div>
            <div class="deck">{''.join(figs)}</div>
        </div>
    </section>
    <div class="lightbox" id="lightbox" hidden>
        <button class="lb-close" aria-label="Fermer">✕</button>
        <button class="lb-prev" aria-label="Slide précédente">‹</button>
        <img id="lb-img" alt="">
        <button class="lb-next" aria-label="Slide suivante">›</button>
        <div class="lb-count" id="lb-count"></div>
    </div>
    <script>
    (function () {{
        var n = {n}, i = 0, slug = "{slug}";
        var lb = document.getElementById('lightbox'), img = document.getElementById('lb-img'), cnt = document.getElementById('lb-count');
        function pad(k) {{ return (k < 10 ? '0' : '') + k; }}
        function show(k) {{
            i = (k + n) % n;
            img.src = '/presentations/' + slug + '/' + pad(i + 1) + '.webp';
            img.alt = document.querySelectorAll('.slide img')[i].alt;
            cnt.textContent = pad(i + 1) + ' / ' + pad(n);
            new Image().src = '/presentations/' + slug + '/' + pad(((i + 1) % n) + 1) + '.webp';
        }}
        function open(k) {{ show(k); lb.hidden = false; document.body.style.overflow = 'hidden';
            if (lb.requestFullscreen) lb.requestFullscreen().catch(function () {{}}); }}
        function close() {{ lb.hidden = true; document.body.style.overflow = '';
            if (document.fullscreenElement) document.exitFullscreen().catch(function () {{}});
            var t = document.getElementById('s' + (i + 1)); if (t) t.scrollIntoView({{block: 'center'}}); }}
        document.getElementById('deck-play').addEventListener('click', function () {{ open(0); }});
        document.querySelectorAll('.slide-img').forEach(function (b) {{
            b.addEventListener('click', function () {{ open(+b.dataset.i); }}); }});
        lb.querySelector('.lb-close').addEventListener('click', close);
        lb.querySelector('.lb-prev').addEventListener('click', function () {{ show(i - 1); }});
        lb.querySelector('.lb-next').addEventListener('click', function () {{ show(i + 1); }});
        document.addEventListener('fullscreenchange', function () {{ if (!document.fullscreenElement && !lb.hidden) close(); }});
        document.addEventListener('keydown', function (ev) {{
            if (lb.hidden) return;
            if (ev.key === 'ArrowRight' || ev.key === ' ' || ev.key === 'PageDown') {{ ev.preventDefault(); show(i + 1); }}
            else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') {{ ev.preventDefault(); show(i - 1); }}
            else if (ev.key === 'Escape') close();
            else if (ev.key === 'Home') show(0); else if (ev.key === 'End') show(n - 1);
        }});
        var x0 = null;
        lb.addEventListener('touchstart', function (ev) {{ x0 = ev.touches[0].clientX; }}, {{passive: true}});
        lb.addEventListener('touchend', function (ev) {{
            if (x0 === null) return; var dx = ev.changedTouches[0].clientX - x0;
            if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); x0 = null; }});
    }})();
    </script>
"""
    return head(f"{deck['title']} — Patrice Duclos", deck["lead"], path) + nav(projects, path) + body + FOOTER
