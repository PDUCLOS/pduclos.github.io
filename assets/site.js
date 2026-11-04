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

// Animations Carrier : parcours commande, collecte, colonnes, devises, glissement de mois ([data-ca])
(function () {
    var roots = document.querySelectorAll('[data-ca]');
    if (!roots.length) return;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function h(tag, cls, txt) { var el = document.createElement(tag); if (cls) el.className = cls; if (txt != null) el.textContent = txt; return el; }
    function flip(el, parent) {
        var a = el.getBoundingClientRect(); parent.appendChild(el);
        if (reduce) return;
        var b = el.getBoundingClientRect();
        el.style.transition = 'none';
        el.style.transform = 'translate(' + (a.left - b.left) + 'px,' + (a.top - b.top) + 'px)';
        void el.offsetWidth; el.style.transition = ''; el.style.transform = '';
    }
    var R = {};

    R.journey = function (c) {
        var d = c.d, sc = d.scenarios[c.scen || 0], st = c.stage;
        var top = h('div', 'cj-top'), day = h('div', 'cj-day'); day.appendChild(h('span', '', d.ui.day)); var dv = h('b', '', '0'); day.appendChild(dv); top.appendChild(day);
        st.appendChild(top);
        var track = h('ol', 'cj-track'), lis = d.stations.map(function (s) {
            var li = h('li', 'cj-st'); li.appendChild(h('i')); li.appendChild(h('strong', '', s[0])); li.appendChild(h('small', '', s[1])); track.appendChild(li); return li;
        });
        st.appendChild(track);
        var tl = h('div', 'cj-tl'), cur = h('span', 'cj-cur'); tl.appendChild(cur); st.appendChild(tl);
        var ev = h('ul', 'cj-ev'); st.appendChild(ev);
        var res = h('div', 'cj-res'); st.appendChild(res);
        function pct(x) { return (x / d.max * 100) + '%'; }
        return sc.events.map(function (e) {
            return function () {
                dv.textContent = e.day; cur.style.left = pct(e.day);
                lis.forEach(function (li, i) { li.classList.toggle('done', i < e.st); li.classList.toggle('on', i === e.st); li.classList.toggle('bad', i === e.st && !!e.bad); });
                Object.keys(e.set || {}).forEach(function (k) {
                    var f = h('span', 'cj-flag f-' + k, d.flags[k] + ' · ' + e.set[k]); f.style.left = pct(e.set[k]);
                    if (k === 'd2' || k === 'd3') tl.querySelectorAll('.f-d1,.f-d2').forEach(function (x) { x.classList.add('old'); });
                    tl.appendChild(f);
                });
                var li = h('li', e.bad ? 'bad' : ''); li.appendChild(h('b', '', d.ui.day + ' ' + e.day)); li.appendChild(document.createTextNode(' ' + e.txt));
                ev.insertBefore(li, ev.firstChild);
                c.log(e.txt);
            };
        }).concat([function () {
            lis.forEach(function (li) { li.classList.remove('on'); li.classList.add('done'); });
            sc.result.forEach(function (r, i) {
                var k = h('div', 'cj-kpi ' + (r[2] ? 'ok' : 'ko')); k.style.transitionDelay = (reduce ? 0 : i * 120) + 'ms';
                k.appendChild(h('small', '', r[0])); k.appendChild(h('strong', '', r[1])); res.appendChild(k);
                requestAnimationFrame(function () { k.classList.add('in'); });
            });
        }]);
    };

    R.collect = function (c) {
        var d = c.d, st = c.stage, wrap = h('div', 'cc');
        var src = h('div', 'cc-src'), hub = h('div', 'cc-hub'), out = h('div', 'cc-out');
        var chips = []; for (var i = 1; i <= 12; i++) { var ch = h('span', 'cc-chip', d.src + ' ' + i); src.appendChild(ch); chips.push(ch); }
        hub.appendChild(h('strong', '', d.hub)); var clock = h('span', 'cc-clock', d.clock[0]); hub.appendChild(clock); var files = h('div', 'cc-files'); hub.appendChild(files);
        var tiles = d.out.map(function (t) { var x = h('span', 'cc-tile', t); out.appendChild(x); return x; });
        wrap.appendChild(src); wrap.appendChild(hub); wrap.appendChild(out); st.appendChild(wrap);
        return [
            function () { c.log(d.txt[0]); chips.forEach(function (x) { x.classList.add('in'); }); },
            function () { c.log(d.txt[1]); chips.forEach(function (x, i) { setTimeout(function () { flip(x, files); x.classList.add('moved'); }, reduce ? 0 : i * 110); }); },
            function () {
                c.log(d.txt[2]); hub.classList.add('run'); var m = 6 * 60, end = 8 * 60;
                (function tick() { clock.textContent = ('0' + Math.floor(m / 60)).slice(-2) + ':' + ('0' + m % 60).slice(-2); if (m < end) { m += 15; setTimeout(tick, reduce ? 0 : 140); } })();
            },
            function () { c.log(d.txt[3]); hub.classList.remove('run'); tiles.forEach(function (t, i) { setTimeout(function () { t.classList.add('on'); }, reduce ? 0 : i * 200); }); }
        ];
    };

    R.columns = function (c) {
        var d = c.d, st = c.stage;
        var head = h('div', 'ck-head'), n = h('b', '', d.total); head.appendChild(n); head.appendChild(h('span', '', ' ' + d.unit)); st.appendChild(head);
        var grid = h('div', 'ck-grid'), cells = [];
        for (var i = 0; i < d.total; i++) { var x = h('i'); x.dataset.keep = ((i * 37) % d.total) < d.kept ? '1' : ''; grid.appendChild(x); cells.push(x); }
        st.appendChild(grid);
        var legend = h('div', 'ck-legend'); st.appendChild(legend);
        var list = h('ul', 'ck-anom'); st.appendChild(list);
        var kept = cells.filter(function (x) { return x.dataset.keep; }), bad = [3, 21, 40, 66], items = [];
        function count(a, b) { var v = a, s = (b - a) / 20; (function t() { v += s; if ((s < 0 && v <= b) || reduce) v = b; n.textContent = Math.round(v); if (v !== b) setTimeout(t, 30); })(); }
        return [
            function () { c.log(d.txt[0]); grid.classList.add('in'); },
            function () { c.log(d.txt[1]); cells.forEach(function (x) { if (!x.dataset.keep) x.classList.add('drop'); }); count(d.total, d.kept); },
            function () {
                c.log(d.txt[2]); grid.classList.add('slim'); var k = 0;
                d.types.forEach(function (t) {
                    for (var j = 0; j < t[1]; j++) kept[k++].className = t[2];
                    var l = h('span', 'ck-lg ' + t[2], t[0] + ' · ' + t[1]); legend.appendChild(l);
                });
            },
            function () {
                c.log(d.txt[3]);
                bad.forEach(function (b, i) { kept[b].classList.add('bad'); var li = h('li', 'bad', d.anomalies[i]); list.appendChild(li); items.push(li); });
            },
            function () {
                c.log(d.txt[4]);
                bad.forEach(function (b, i) { kept[b].classList.remove('bad'); kept[b].classList.add('fixed'); items[i].className = 'ok'; items[i].appendChild(h('small', '', ' — ' + d.fixed)); });
            }
        ];
    };

    R.currency = function (c) {
        var d = c.d, st = c.stage, row = h('div', 'cx');
        var cards = d.cards.map(function (k, i) {
            var el = h('div', 'cx-card'); el.appendChild(h('small', '', k[0]));
            var v = h('strong'); v.appendChild(h('span', 'cx-v', k[1])); v.appendChild(h('em', '', ' ' + k[2])); el.appendChild(v);
            el.appendChild(h('span', 'cx-bar')); row.appendChild(el); return el;
        });
        st.appendChild(row);
        return d.steps.map(function (s) {
            return function () {
                c.log(s.txt);
                cards.forEach(function (x) { x.classList.remove('warn'); });
                (s.show || []).forEach(function (i) { cards[i].classList.add('in'); });
                (s.set || []).forEach(function (p) { cards[p[0]].querySelector('.cx-v').textContent = p[1]; });
                (s.warn || []).forEach(function (i) { cards[i].classList.add('warn'); });
                if (s.bar) { var b = cards[s.bar[0]]; b.classList.add('has-bar'); b.querySelector('.cx-bar').style.setProperty('--w', s.bar[1] + '%'); }
            };
        });
    };

    R.slip = function (c) {
        var d = c.d, st = c.stage, wrap = h('div', 'cs'), cols = d.months.map(function (m) {
            var col = h('div', 'cs-col'); col.appendChild(h('h5', '', m)); var box = h('div', 'cs-box'); col.appendChild(box);
            var f = h('small', 'cs-foot'); col.appendChild(f); wrap.appendChild(col); return { box: box, foot: f };
        });
        st.appendChild(wrap);
        var orders = []; for (var i = 1; i <= d.orders; i++) { var o = h('span', 'cs-o', d.prefix + i); cols[0].box.appendChild(o); orders.push(o); }
        function foot() {
            cols.forEach(function (c2, i) { var n2 = c2.box.children.length; c2.foot.textContent = i === 0 ? n2 + ' / ' + d.orders + ' ' + d.delivered : (n2 ? '+' + n2 : ''); });
        }
        foot(); cols[0].foot.textContent = d.orders + ' ' + d.planned;
        return [
            function () { c.log(d.txt[0]); orders.forEach(function (o) { o.classList.add('in'); }); },
            function () {
                c.log(d.txt[1]);
                d.moves.forEach(function (m, i) { setTimeout(function () { var o = orders[m[0]]; o.classList.add('late'); flip(o, cols[m[1]].box); foot(); }, reduce ? 0 : i * 450); });
            },
            function () { c.log(d.txt[2]); wrap.classList.add('done'); }
        ];
    };

    R.tickets = function (c) {
        var d = c.d, st = c.stage, wrap = h('div', 'ct'), head = h('div', 'ct-head');
        d.months.forEach(function (m) { head.appendChild(h('span', '', m)); });
        wrap.appendChild(head);
        var body = h('div', 'ct-body');
        function pct(x) { return (x / d.max * 100) + '%'; }
        function month(x) { return Math.min(d.months.length - 1, Math.floor(x / (d.max / d.months.length))); }
        var rows = d.tickets.map(function (t) {
            var r = h('div', 'ct-row'), bar = h('span', 'ct-bar ' + t[3]), mk = h('i', 'ct-mk'), lab = h('b', '', t[0]);
            bar.style.left = pct(t[1]); bar.style.width = pct((t[2] == null ? d.max : t[2]) - t[1]);
            bar.appendChild(lab); r.appendChild(bar); r.appendChild(mk); body.appendChild(r);
            return { t: t, r: r, bar: bar, mk: mk, lab: lab };
        });
        wrap.appendChild(body);
        var legend = h('div', 'ct-legend');
        Object.keys(d.types).forEach(function (k) { legend.appendChild(h('span', 'ct-lg ' + k, d.types[k])); });
        wrap.appendChild(legend);
        var tab = h('div', 'ct-tab'), cells = d.rows.map(function (lbl) {
            var row = h('div', 'ct-trow'); row.appendChild(h('span', 'ct-tl', lbl));
            var cs = d.months.map(function () { var x = h('b', '', '·'); row.appendChild(x); return x; });
            tab.appendChild(row); return { row: row, cs: cs };
        });
        wrap.appendChild(tab); st.appendChild(wrap);
        function fill(k, key) {
            var n = d.months.map(function () { return 0; });
            rows.forEach(function (x) { var v = key(x.t); if (v != null) n[month(v)]++; });
            cells[k].cs.forEach(function (x, i) { x.textContent = n[i]; });
            cells[k].row.classList.add('on');
            return n;
        }
        return [
            function () { c.log(d.txt[0]); wrap.classList.add('in'); },
            function () {
                c.log(d.txt[1]); wrap.classList.add('closed');
                rows.forEach(function (x) {
                    if (x.t[2] == null) { x.r.classList.add('gone'); x.lab.textContent = x.t[0] + ' · ' + d.hidden; }
                    else { x.mk.style.left = pct(x.t[2]); x.mk.classList.add('on'); }
                });
                fill(0, function (t) { return t[2]; });
            },
            function () {
                c.log(d.txt[2]);
                rows.forEach(function (x) { if (x.t[2] != null && month(x.t[1]) !== month(x.t[2])) x.r.classList.add('warn'); });
            },
            function () {
                c.log(d.txt[3]); wrap.classList.remove('closed'); wrap.classList.add('created');
                rows.forEach(function (x) {
                    x.r.classList.remove('warn', 'gone'); x.mk.style.left = pct(x.t[1]); x.mk.classList.add('on');
                    if (x.t[2] == null) x.lab.textContent = x.t[0] + ' · ' + d.running;
                });
                var a = cells[0].cs.map(function (x) { return +x.textContent; }), b = fill(1, function (t) { return t[1]; });
                b.forEach(function (v, i) { if (v !== a[i]) { cells[0].cs[i].classList.add('diff'); cells[1].cs[i].classList.add('diff'); } });
            },
            function () { c.log(d.txt[4]); }
        ];
    };

    R.pareto = function (c) {
        var d = c.d, st = c.stage, wrap = h('div', 'cp2'), plot = h('div', 'cp2-plot'), labels = h('div', 'cp2-lab');
        var NS = 'http://www.w3.org/2000/svg', svg = document.createElementNS(NS, 'svg'), line = document.createElementNS(NS, 'polyline'), rule = h('span', 'cp2-rule', d.rule);
        svg.setAttribute('viewBox', '0 0 100 100'); svg.setAttribute('preserveAspectRatio', 'none'); line.setAttribute('vector-effect', 'non-scaling-stroke'); svg.appendChild(line);
        var cats = d.cats.map(function (k, i) {
            var b = h('div', 'cp2-b'), bar = h('i'), v = h('small', '', k[1]); b.appendChild(v); b.appendChild(bar);
            var lab = h('span', '', k[0]); plot.appendChild(b); labels.appendChild(lab);
            return { n: k[1], el: b, bar: bar, v: v, lab: lab, i: i };
        });
        // ordre de départ mélangé
        [3, 0, 5, 1, 6, 2, 4].forEach(function (i) { plot.appendChild(cats[i].el); labels.appendChild(cats[i].lab); });
        plot.appendChild(svg); plot.appendChild(rule); wrap.appendChild(plot); wrap.appendChild(labels); st.appendChild(wrap);
        function size() { var mx = Math.max.apply(null, cats.map(function (x) { return x.n; })); cats.forEach(function (x) { x.bar.style.height = (x.n / mx * 100) + '%'; x.v.textContent = x.n; }); }
        function sort() {
            cats.slice().sort(function (a, b) { return b.n - a.n; }).forEach(function (x) { flip(x.el, plot); labels.appendChild(x.lab); });
            plot.appendChild(svg); plot.appendChild(rule);
            var tot = 0, sum = 0, ord = cats.slice().sort(function (a, b) { return b.n - a.n; });
            ord.forEach(function (x) { tot += x.n; });
            line.setAttribute('points', ord.map(function (x, i) { sum += x.n; return ((i + .5) / ord.length * 100) + ',' + (100 - sum / tot * 100); }).join(' '));
            wrap.classList.add('cum');
        }
        return [
            function () { c.log(d.txt[0]); size(); plot.classList.add('in'); },
            function () { c.log(d.txt[1]); sort(); },
            function () { c.log(d.txt[2]); var x = cats[d.add[0]]; x.el.classList.add('new'); x.lab.classList.add('new'); x.n += d.add[1]; size(); },
            function () { c.log(d.txt[3]); sort(); }
        ];
    };

    roots.forEach(function (root) {
        var d = JSON.parse(root.getAttribute('data-json')), play = root.querySelector('.ca-play');
        var c = { d: d, stage: root.querySelector('.ca-stage'), scen: 0, run: 0 };
        var logEl = root.querySelector('.ca-log');
        c.log = function (t) { logEl.textContent = t; };
        root.classList.add('ready');
        function start() {
            var run = ++c.run; c.stage.innerHTML = ''; logEl.textContent = '';
            var steps = R[root.dataset.ca](c), i = 0;
            play.textContent = d.ui.replay;
            (function next() {
                if (run !== c.run || i >= steps.length) return;
                steps[i++](); setTimeout(next, reduce ? 0 : (root.dataset.ca === 'journey' ? 1700 : 2100));
            })();
        }
        play.addEventListener('click', start);
        root.querySelectorAll('.ca-scen').forEach(function (b) {
            b.addEventListener('click', function () {
                c.scen = +b.dataset.s;
                root.querySelectorAll('.ca-scen').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
                start();
            });
        });
        // lancement automatique à la première apparition (sauf mouvement réduit)
        if (reduce) start();
        else if ('IntersectionObserver' in window) {
            var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); start(); } }, { threshold: 0.35 });
            io.observe(root);
        }
    });
})();
