(function () {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.querySelector('.nav-links');
    if (toggle && links) {
        toggle.addEventListener('click', function () { links.classList.toggle('active'); });
        links.addEventListener('click', function (e) {
            if (e.target.closest('a') && !e.target.classList.contains('dropdown-toggle')) links.classList.remove('active');
        });
    }

    var reveals = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {
        reveals.forEach(function (el) { el.classList.add('visible'); });
        return;
    }
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry, index) {
            if (entry.isIntersecting) {
                setTimeout(function () { entry.target.classList.add('visible'); }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    reveals.forEach(function (el) { observer.observe(el); });
})();

/* ---------- Pipeline interactif (pages projets) ---------- */
(function () {
    var NS = 'http://www.w3.org/2000/svg';
    var EN = (document.documentElement.lang || '').slice(0, 2) === 'en';
    var L = EN ? { step: 'Step', from: 'fed by:', entry: 'pipeline entry point', to: 'feeds:', end: 'final output', up: 'block(s) upstream', down: 'downstream', upd: 'updated' }
               : { step: 'Étape', from: 'reçoit de :', entry: 'point d\'entrée du pipeline', to: 'alimente :', end: 'restitution finale', up: 'brique(s) en amont', down: 'en aval', upd: 'màj' };
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function initPipeline(root) {
        var dataEl = root.querySelector('.pl-data');
        var edges = dataEl ? JSON.parse(dataEl.textContent) : [];
        var canvas = root.querySelector('.pl-canvas');
        var svg = root.querySelector('.pl-edges');
        var info = root.querySelector('.pl-info');
        var nodes = {};
        root.querySelectorAll('.pl-node').forEach(function (n) { nodes[n.dataset.id] = n; });
        var col = function (id) { return +id.slice(1, id.indexOf('n')); };
        var paths = [];

        var scroller = root.querySelector('.pl-scroll');
        var nCols = root.querySelectorAll('.pl-col').length;
        function layout() {
            // horizontal si chaque colonne dispose d'au moins ~118 px, sinon étapes empilées (flux de haut en bas)
            var w = scroller.clientWidth;
            root.classList.toggle('vertical', w < nCols * 118);
            root.classList.toggle('compact', w >= nCols * 118 && w < nCols * 150);
        }
        function draw() {
            if (!canvas.offsetWidth) return;
            layout();
            var vertical = root.classList.contains('vertical');
            svg.innerHTML = '';
            paths = [];
            var c = canvas.getBoundingClientRect();
            var back = 0;
            edges.forEach(function (ed) {
                var a = nodes[ed.a], b = nodes[ed.b];
                if (!a || !b) return;
                var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
                var d, lx, ly;
                if (vertical) {
                    if (col(ed.b) > col(ed.a)) {
                        var vx1 = ra.left + ra.width / 2 - c.left, vy1 = ra.bottom - c.top;
                        var vx2 = rb.left + rb.width / 2 - c.left, vy2 = rb.top - c.top;
                        var vk = Math.max(20, (vy2 - vy1) / 2);
                        d = 'M' + vx1 + ',' + vy1 + ' C' + vx1 + ',' + (vy1 + vk) + ' ' + vx2 + ',' + (vy2 - vk) + ' ' + vx2 + ',' + vy2;
                        lx = (vx1 + vx2) / 2 + 4; ly = (vy1 + vy2) / 2;
                    } else if (col(ed.b) === col(ed.a)) {
                        var left = ra.left < rb.left;
                        var hy = ra.top + ra.height / 2 - c.top;
                        var hx1 = (left ? ra.right : ra.left) - c.left, hx2 = (left ? rb.left : rb.right) - c.left;
                        d = 'M' + hx1 + ',' + hy + ' L' + hx2 + ',' + (rb.top + rb.height / 2 - c.top);
                        lx = (hx1 + hx2) / 2; ly = hy - 6;
                    } else {
                        // boucle de retour : longe le bord droit du canevas
                        back++;
                        var rx = c.width - 10 - back * 7;
                        var ry1 = ra.top + ra.height / 2 - c.top, ry2 = rb.top + rb.height / 2 - c.top;
                        d = 'M' + (ra.right - c.left) + ',' + ry1 + ' C' + rx + ',' + ry1 + ' ' + rx + ',' + ry2 + ' ' + (rb.right - c.left) + ',' + ry2;
                        lx = rx - 4; ly = (ry1 + ry2) / 2;
                    }
                } else if (col(ed.b) > col(ed.a)) {
                    var x1 = ra.right - c.left, y1 = ra.top + ra.height / 2 - c.top;
                    var x2 = rb.left - c.left, y2 = rb.top + rb.height / 2 - c.top;
                    var k = Math.max(30, (x2 - x1) / 2);
                    d = 'M' + x1 + ',' + y1 + ' C' + (x1 + k) + ',' + y1 + ' ' + (x2 - k) + ',' + y2 + ' ' + x2 + ',' + y2;
                    lx = (x1 + x2) / 2; ly = (y1 + y2) / 2 - 4;
                } else if (col(ed.b) === col(ed.a)) {
                    var top = ra.top < rb.top;
                    var xs = ra.left + ra.width / 2 - c.left;
                    var y1s = (top ? ra.bottom : ra.top) - c.top, y2s = (top ? rb.top : rb.bottom) - c.top;
                    d = 'M' + xs + ',' + y1s + ' L' + xs + ',' + y2s;
                    lx = xs + 6; ly = (y1s + y2s) / 2;
                } else {
                    back++;
                    var bx1 = ra.left + ra.width / 2 - c.left, by1 = ra.top - c.top;
                    var bx2 = rb.left + rb.width / 2 - c.left, by2 = rb.top - c.top;
                    var lift = Math.min(by1, by2) - 14 - back * 8;
                    d = 'M' + bx1 + ',' + by1 + ' C' + bx1 + ',' + lift + ' ' + bx2 + ',' + lift + ' ' + bx2 + ',' + by2;
                    lx = (bx1 + bx2) / 2; ly = lift + 4;
                }
                var p = document.createElementNS(NS, 'path');
                p.setAttribute('d', d);
                p.setAttribute('class', 'pl-edge' + (ed.d ? ' dash' : ''));
                svg.appendChild(p);
                var t = null;
                if (ed.l) {
                    t = document.createElementNS(NS, 'text');
                    t.setAttribute('x', lx); t.setAttribute('y', ly);
                    t.setAttribute('text-anchor', 'middle');
                    t.setAttribute('class', 'pl-elabel');
                    t.textContent = ed.l;
                    svg.appendChild(t);
                }
                paths.push({ el: p, label: t, a: ed.a, b: ed.b });
            });
            if (sel) highlight(sel, true);
        }

        function walk(start, dir) {
            var seen = {}, stack = [start];
            while (stack.length) {
                var cur = stack.pop();
                edges.forEach(function (ed) {
                    var from = dir === 'down' ? ed.a : ed.b, to = dir === 'down' ? ed.b : ed.a;
                    // boucles de retour (pointillés) : on ne les suit pas pour garder un sens de lecture clair
                    if (from === cur && !ed.d && !seen[to] && to !== start) { seen[to] = 1; stack.push(to); }
                });
            }
            return seen;
        }

        var sel = null;
        function clear() {
            sel = null;
            root.classList.remove('focus');
            Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove('sel', 'up', 'down'); });
            paths.forEach(function (p) { p.el.classList.remove('flow'); if (p.label) p.label.classList.remove('on'); });
            root.querySelector('.pl-reset').hidden = true;
            info.innerHTML = '';
        }
        function names(ids) {
            return ids.map(function (k) { return '<b>' + nodes[k].textContent + '</b>'; }).join(', ');
        }
        function highlight(id, silent) {
            var up = walk(id, 'up'), down = walk(id, 'down');
            edges.forEach(function (ed) { if (ed.a === id) down[ed.b] = down[ed.b] || 1; if (ed.b === id) up[ed.a] = up[ed.a] || 1; });
            sel = id;
            root.classList.add('focus');
            Object.keys(nodes).forEach(function (k) {
                nodes[k].classList.toggle('sel', k === id);
                nodes[k].classList.toggle('up', !!up[k]);
                nodes[k].classList.toggle('down', !!down[k]);
            });
            var chain = Object.assign({}, up, down); chain[id] = 1;
            paths.forEach(function (p) {
                var on = (p.a === id || p.b === id) || (chain[p.a] && chain[p.b] && !(up[p.a] && down[p.b]) && !(down[p.a] && up[p.b]));
                p.el.classList.toggle('flow', !!on);
                if (p.label) p.label.classList.toggle('on', !!on);
            });
            root.querySelector('.pl-reset').hidden = false;
            if (silent) return;
            var n = nodes[id], colEl = n.closest('.pl-col');
            var stage = colEl.querySelector('h4').textContent.replace(/^\d+/, '');
            var inn = edges.filter(function (e) { return e.b === id; }).map(function (e) { return e.a; });
            var out = edges.filter(function (e) { return e.a === id; }).map(function (e) { return e.b; });
            info.style.borderLeftColor = getComputedStyle(colEl).getPropertyValue('--k');
            info.innerHTML = '<span class="pl-k" style="color:' + info.style.borderLeftColor + '">' + L.step + ' · ' + stage + '</span><br><b>' + n.textContent + '</b>' +
                (inn.length ? '<br>← ' + L.from + ' ' + names(inn) : '<br>← ' + L.entry) +
                (out.length ? '<br>→ ' + L.to + ' ' + names(out) : '<br>→ ' + L.end) +
                '<br><small>' + Object.keys(up).length + ' ' + L.up + ' · ' + Object.keys(down).length + ' ' + L.down + '</small>';
        }

        root.querySelectorAll('.pl-node').forEach(function (n) {
            n.addEventListener('click', function () { sel === n.dataset.id ? clear() : highlight(n.dataset.id); });
        });
        root.querySelector('.pl-reset').addEventListener('click', clear);

        var play = root.querySelector('.pl-play');
        play.addEventListener('click', function () {
            clear();
            var cols = root.querySelectorAll('.pl-col');
            play.disabled = true;
            root.classList.add('focus');
            var i = 0;
            (function step() {
                cols.forEach(function (c) { c.classList.remove('live'); });
                if (i >= cols.length) {
                    play.disabled = false; root.classList.remove('focus');
                    paths.forEach(function (p) { p.el.classList.add('flow'); });
                    setTimeout(function () { if (!sel) paths.forEach(function (p) { p.el.classList.remove('flow'); }); }, 2500);
                    info.innerHTML = '';
                    return;
                }
                cols[i].classList.add('live');
                cols[i].querySelectorAll('.pl-node').forEach(function (n) { n.classList.add('down'); });
                paths.forEach(function (p) { if (col(p.a) === i - 1 || (col(p.b) === i && col(p.a) < i)) p.el.classList.add('flow'); });
                info.innerHTML = '<span class="pl-k" style="color:' + getComputedStyle(cols[i]).getPropertyValue('--k') + '">' + L.step + ' ' + (i + 1) + ' / ' + cols.length + '</span><br><b>' +
                    cols[i].querySelector('h4').textContent.replace(/^\d+/, '') + '</b> — ' + names([].map.call(cols[i].querySelectorAll('.pl-node'), function (n) { return n.dataset.id; }));
                i++;
                setTimeout(step, reduce ? 600 : 1300);
            })();
        });

        // onglets : pipeline interactif / schémas draw.io
        var tabs = root.querySelectorAll('.pl-tab'), panels = root.querySelectorAll('.pl-panel');
        function show(name) {
            tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.tab === name ? 'true' : 'false'); });
            panels.forEach(function (p) { p.hidden = p.dataset.panel !== name; });
            if (name === 'live') draw();
        }
        tabs.forEach(function (t) { t.addEventListener('click', function () { show(t.dataset.tab); }); });

        // zoom / déplacement des schémas
        root.querySelectorAll('.pl-panel[data-panel^="d"]').forEach(function (panel) {
            var fig = panel.querySelector('.pipeline-figure'), img = fig.querySelector('img');
            var s = 1, x = 0, y = 0, drag = null;
            function apply() { img.style.transform = 'translate(' + x + 'px,' + y + 'px) scale(' + s + ')'; }
            function zoom(f) { s = Math.min(6, Math.max(0.5, s * f)); apply(); }
            panel.querySelectorAll('[data-z]').forEach(function (b) {
                b.addEventListener('click', function () {
                    if (b.dataset.z === 'in') zoom(1.3); else if (b.dataset.z === 'out') zoom(1 / 1.3); else { s = 1; x = y = 0; apply(); }
                });
            });
            fig.addEventListener('wheel', function (ev) { ev.preventDefault(); zoom(ev.deltaY < 0 ? 1.12 : 1 / 1.12); }, { passive: false });
            fig.addEventListener('pointerdown', function (ev) { drag = { x: ev.clientX - x, y: ev.clientY - y }; fig.classList.add('dragging'); fig.setPointerCapture(ev.pointerId); });
            fig.addEventListener('pointermove', function (ev) { if (drag) { x = ev.clientX - drag.x; y = ev.clientY - drag.y; apply(); } });
            ['pointerup', 'pointercancel'].forEach(function (t) { fig.addEventListener(t, function () { drag = null; fig.classList.remove('dragging'); }); });
        });

        root.classList.add('ready');
        show('live');
        if ('ResizeObserver' in window) new ResizeObserver(function () { draw(); }).observe(scroller);
        else window.addEventListener('resize', draw);
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
    }
    document.querySelectorAll('[data-pl]').forEach(initPipeline);

    // dépôts GitHub : langage, dernière mise à jour, étoiles (API publique, mise en cache par session)
    var months = EN ? ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                    : ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'];
    document.querySelectorAll('.gh-card[data-repo]').forEach(function (card) {
        var repo = card.dataset.repo, key = 'gh:' + repo;
        function fill(r) {
            if (r.description) card.querySelector('.gh-desc').textContent = r.description;
            if (r.language) card.querySelector('[data-k="lang"]').textContent = '● ' + r.language;
            if (r.pushed_at) { var d = new Date(r.pushed_at); card.querySelector('[data-k="push"]').textContent = L.upd + ' ' + (EN ? months[d.getMonth()] + ' ' + d.getDate() + ', ' : d.getDate() + ' ' + months[d.getMonth()] + ' ') + d.getFullYear(); }
            if (r.stargazers_count) card.querySelector('[data-k="stars"]').textContent = '★ ' + r.stargazers_count;
        }
        var cached = null;
        try { cached = JSON.parse(sessionStorage.getItem(key)); } catch (e) {}
        if (cached) return fill(cached);
        fetch('https://api.github.com/repos/' + repo).then(function (r) { return r.ok ? r.json() : null; }).then(function (r) {
            if (!r) return;
            var keep = { description: r.description, language: r.language, pushed_at: r.pushed_at, stargazers_count: r.stargazers_count };
            try { sessionStorage.setItem(key, JSON.stringify(keep)); } catch (e) {}
            fill(keep);
        }).catch(function () {});
    });
})();

/* ---------- Compétences (RNCP 38777) ---------- */
(function () {
    var cards = document.querySelectorAll('.cp-card');
    if (!cards.length) return;
    var tabs = document.querySelectorAll('.cp-tab'), input = document.querySelector('.cp-search input');
    var empty = document.querySelector('.cp-empty');
    var filter = 'all';
    function apply() {
        var q = (input.value || '').trim().toLowerCase(), any = false;
        cards.forEach(function (c) {
            var inBloc = filter === 'all' || c.dataset.bloc === filter, hits = 0;
            c.querySelectorAll('.cp-tool').forEach(function (t) {
                var m = !q || t.dataset.name.indexOf(q) !== -1 || t.textContent.toLowerCase().indexOf(q) !== -1;
                t.hidden = !m; t.classList.toggle('match', !!q && m); if (m) hits++;
            });
            c.hidden = !inBloc || (q && !hits);
            if (!c.hidden) any = true;
        });
        empty.hidden = any;
    }
    function select(code, scroll) {
        filter = code;
        tabs.forEach(function (t) { t.setAttribute('aria-pressed', t.dataset.filter === code ? 'true' : 'false'); });
        apply();
        if (scroll) document.getElementById('explorer').scrollIntoView({ behavior: 'smooth' });
        var c = document.querySelector('.cp-card[data-bloc="' + code + '"]');
        if (c) { c.classList.remove('flash'); void c.offsetWidth; c.classList.add('flash'); }
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { select(t.dataset.filter); }); });
    input.addEventListener('input', apply);
    document.querySelectorAll('.cp-radar [data-bloc]').forEach(function (el) {
        el.addEventListener('click', function () { select(el.getAttribute('data-bloc'), true); });
    });
    if (location.hash) {
        var code = decodeURIComponent(location.hash.slice(1)).toUpperCase();
        if (document.querySelector('.cp-card[data-bloc="' + code + '"]')) select(code, true);
    }
    // barres de niveau animées à l'apparition
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (es) {
            es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
        }, { threshold: 0.15 });
        cards.forEach(function (c) { io.observe(c); });
    }
    // matrice : mise en évidence de colonne
    var matrix = document.querySelector('.cp-matrix');
    if (matrix) {
        matrix.addEventListener('mouseover', function (ev) {
            var cell = ev.target.closest('[data-bloc]');
            matrix.querySelectorAll('.col-on').forEach(function (x) { x.classList.remove('col-on'); });
            matrix.classList.toggle('col-focus', !!cell);
            if (cell) matrix.querySelectorAll('[data-bloc="' + cell.dataset.bloc + '"]').forEach(function (x) { x.classList.add('col-on'); });
        });
        matrix.addEventListener('mouseleave', function () {
            matrix.classList.remove('col-focus');
            matrix.querySelectorAll('.col-on').forEach(function (x) { x.classList.remove('col-on'); });
        });
    }
})();
