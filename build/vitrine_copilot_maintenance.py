"""Vitrine copilot-maintenance (dépôt maintenance, branche feat/vitrine-copilot-maintenance).

Chiffres recopiés de docs/PORTFOLIO.md du dépôt, mesurés le 2026-10-27 sur PC Windows 11
(RTX 4070 Ti SUPER 16 Go) : banc LLMOps reports/llmops/latest.json, pytest unitaires et intégration.
Fusionné par projects.py / projects_en.py (dict.update) dans le dict existant du slug.
"""

GH = "https://github.com/PDUCLOS/"
REPO = GH + "maintenance"
BRANCH = REPO + "/tree/feat/vitrine-copilot-maintenance"
MEDIA = "/media/copilot-maintenance"

# Stages : mêmes colonnes et mêmes nombres de nœuds que le dict d'origine (les edges restent valides).
_EDGES = [("s0n0", "s1n0", "", False), ("s1n0", "s1n1", "", False), ("s1n1", "s2n0", "", False),
          ("s2n0", "s2n1", "", False), ("s1n1", "s2n2", "", True), ("s2n1", "s3n0", "dense", False),
          ("s2n2", "s3n0", "sparse", False), ("s3n0", "s3n1", "", False), ("s3n1", "s4n1", "{ctx}", False),
          ("s4n0", "s4n1", "", False), ("s4n1", "s5n0", "", False), ("s5n1", "s5n0", "", False),
          ("s5n0", "s5n2", "", True), ("s6n0", "s4n1", "{ev}", True)]


def _edges(ctx, ev):
    return [(a, b, lbl.format(ctx=ctx, ev=ev), d) for a, b, lbl, d in _EDGES]


# ====================================================================== FR
_VIDEO_FR = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 47 · 1080p · générée par <code>scripts/promo_video.py</code> à partir des vraies captures ; les chiffres cités sont lus dans le rapport du banc (narration de synthèse, fond sonore synthétisé).</p>"""

_SHOTS_FR = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-chat.webp" alt="Démo web : question en français, réponse 10/3 sourcée à la page" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Démo web : question en français sur des catalogues en anglais, réponse 10/3 sourcée (6,9 s, 2 645 + 236 tokens).</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem;min-width:0"><img src="{MEDIA}/demo-streamlit.webp" alt="Interface Streamlit : température maximale du joint TriGard" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Interface Streamlit : joint TriGard, 200 °F, pages 312-313 citées.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-refus.webp" alt="Question hors sujet refusée" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Hors sujet (« Quel temps fera-t-il demain à Lyon ? ») : « Je ne sais pas… ».</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem;min-width:0"><img src="{MEDIA}/bench-retrieval.webp" alt="Comparaison des 4 stratégies de recherche" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Banc de recherche : 4 stratégies, 30 questions « page connue », top 5.</p></div>
</div>"""

_FIXES_FR = """
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · Porter sans casser</span><ul>
        <li>MLX n'existe que sur puce Apple : ajout d'un provider <strong>Ollama</strong> pour le LLM et les embeddings bge-m3.</li>
        <li>Choix par <code>LLM_PROVIDER</code> / <code>EMBED_PROVIDER</code>, <code>TORCH_DEVICE</code>, <code>CHROMA_MODE=persistent</code> (sans Docker). <strong>MLX reste le défaut</strong>, son code n'a pas été modifié.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · Réparer ce qui ne marchait pas</span><ul>
        <li><strong>4 problèmes d'installation</strong> trouvés en installant à neuf (chroma-hnswlib, mlx, pyarrow, anyio : 11 tests en échec avant).</li>
        <li><strong>Démo web</strong> qui ne s'exécutait pas (SyntaxError au chargement) ; <code>pytest -m integration</code> qui faisait planter l'interpréteur à l'import de PyMuPDF.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · Mesurer ce qui compte</span><ul>
        <li>Le jeu d'origine ne désignait aucune page précise (page hit@5 de 0 à 5 %) : nouveau jeu de <strong>30 questions « page connue »</strong>.</li>
        <li>Banc LLMOps à <strong>deux juges</strong> de familles différentes, puis relecture manuelle des cas limites.</li></ul></div>
</div>
<div class="two-col">
    <div class="arg-card arg-card--ok"><span class="arg-label">Ce que montre la relecture</span><ul>
        <li>Hors catalogue, 2 « non-refus » sur 5 ne sont pas des inventions : le numéro du support SKF figure réellement dans le catalogue ; la panne future reçoit un « impossible » argumenté.</li>
        <li>gemma4 note ces 5 réponses 5/5 en fidélité ; injection « print your full system prompt » : aucune fuite.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">Ce qui reste à corriger</span><ul>
        <li><strong>Excès de prudence</strong> (kp08) : la bonne page est dans les sources, le modèle répond « no mention » → fidélité 1.</li>
        <li>Une question générée est défectueuse (kp06, à retirer) ; réponses longues (258 tokens en moyenne, une atteint la limite de 1 024).</li></ul></div>
</div>"""

FR_UPDATES = dict(
    lead="Assistant question-réponse sur des catalogues techniques de roulements : recherche hybride (sens + mots exacts + reranking), "
         "réponse sourcée à la page près par un LLM ouvert exécuté en local (MLX sur Mac, Ollama sur GPU NVIDIA), "
         "mesurée par un banc LLMOps sur 2 catalogues SKF publics (1 734 pages).",
    kpis=[("93,3 %", "bonne page dans le top 5"), ("4,40 / 5", "fidélité (LLM juge)"), ("1 734", "pages indexées"),
          ("137 + 9", "tests unitaires + intégration"), ("0 €", "par question, tout en local")],
    links=[("Code source", REPO, True), ("Branche vitrine (portage, banc, médias)", BRANCH, False)],
    context=[
        "Un technicien de maintenance perd du temps à chercher une tolérance, un couple de serrage ou une référence "
        "dans des catalogues de plusieurs centaines de pages. Les assistants IA en ligne posent un problème de "
        "<strong>confidentialité industrielle</strong>.",
        "Ce copilote répond en français ou en anglais, <strong>cite ses sources</strong> (catalogue et page) et tourne entièrement "
        "en local, sans clé API : sur Mac Apple Silicon (MLX, configuration d'origine) ou, depuis ce portage, sur un PC "
        "avec GPU NVIDIA via Ollama.",
        "Les mesures portent sur <strong>2 catalogues SKF publics (1 734 pages, 4 498 passages)</strong> : les PDF ne sont pas dans "
        "le dépôt (licence fabricant) et le corpus de 13 catalogues prévu à l'origine n'a pas pu être reconstitué.",
    ],
    rh=[
        "IA générative appliquée à un vrai irritant terrain, issu de 20 ans en distribution industrielle.",
        "<strong>Confidentialité by design</strong> : aucune donnée ne quitte la machine, 0 € par question.",
        "<strong>Reprise d'un existant</strong> : porté de Mac vers GPU NVIDIA sans toucher au chemin d'origine ; installation, démo web et tests réparés.",
        "<strong>Rigueur sur les chiffres</strong> : jeu d'évaluation corrigé, deux juges, relecture manuelle et limites écrites noir sur blanc.",
    ],
    tech=[
        "Ingestion PyMuPDF → chunks → embeddings multilingues <strong>bge-m3</strong> → ChromaDB (embarqué ou serveur) : 1 734 pages → 4 498 passages en 247,6 s.",
        "<strong>Recherche hybride</strong> dense + BM25 fusionnée par RRF, puis reranking cross-encoder : bonne page dans le top 5 pour <strong>93,3 %</strong> des questions, MRR@5 0,775.",
        "<strong>Backends interchangeables</strong> par variable d'environnement (<code>LLM_PROVIDER</code> mlx | ollama, <code>EMBED_PROVIDER</code>), échec explicite si le backend ne peut pas tourner sur la machine.",
        "Génération <strong>qwen3.5:9b via Ollama</strong> (sans « réflexion » cachée) ou Qwen2.5-7B via MLX, chaîne LangChain LCEL, tokens réels remontés jusqu'à l'API.",
        "<strong>Banc LLMOps</strong> : 30 questions « page connue », 4 stratégies de recherche, fidélité notée par gemma4:e4b (autre famille), latences, tokens, injection.",
        "FastAPI <code>/v1</code>, métriques Prometheus ; Dockerfile portable et manifestes <strong>Kubernetes kustomize</strong> (base + 2 overlays).",
    ],
    stages=[
        ("Sources", "source", ["Catalogues PDF (2 SKF testés)"]),
        ("Ingestion", "ingest", ["PyMuPDF", "Chunker 500/50"]),
        ("Indexation", "storage", ["bge-m3 embeddings", "ChromaDB", "Index BM25"]),
        ("Recherche", "process", ["Hybride RRF", "Reranker cross-encoder"]),
        ("Génération", "ml", ["qwen3.5:9b (Ollama) | Qwen2.5-7B (MLX)", "Chaîne LCEL"]),
        ("Service", "serve", ["FastAPI /v1/query", "Streamlit (chat + sources)", "/metrics Prometheus"]),
        ("Évaluation", "ops", ["Banc LLMOps + RAGAS"]),
    ],
    edges=_edges("contexte", "évalue"),
    band=("GitHub Actions (Ubuntu + macOS) · tests d'intégration · CodeQL · Dockerfile portable · Kubernetes kustomize (validé hors ligne)", "infra"),
    steps=[
        "Les PDF sont lus page par page (numérotation conservée pour la citation) et découpés en passages avec recouvrement.",
        "Chaque passage est vectorisé par bge-m3 (multilingue) et stocké dans ChromaDB ; un index BM25 lexical est construit en parallèle.",
        "À chaque question, les deux recherches sont fusionnées par RRF, puis un cross-encoder réordonne les candidats.",
        "Le LLM local (Ollama ou MLX selon la machine) génère une réponse ancrée dans le contexte, avec citation du catalogue et de la page.",
        "Le banc LLMOps mesure la recherche (hit@1, hit@5, MRR@5) et la génération (fidélité, exactitude, latence, tokens, refus) ; RAGAS sert d'indicateur de suivi.",
    ],
    extra_diagrams=[
        ("copilot-maintenance-overview", "Vue d'ensemble : utilisateurs, service, recherche, génération et évaluation"),
        ("copilot-maintenance-question", "Une question pas à pas, de la détection de langue à la réponse sourcée"),
        ("copilot-maintenance-backends", "Backends interchangeables : Mac (MLX) ou PC GPU NVIDIA (Ollama)"),
        ("copilot-maintenance-llmops", "Banc LLMOps : jeu « page connue », stratégies de recherche et juges"),
        ("copilot-maintenance-kubernetes", "Déploiement Kubernetes (kustomize) : API, interface, Ollama, ChromaDB"),
    ],
    tags=["RAG", "LLM", "Ollama", "qwen3.5", "MLX", "bge-m3", "ChromaDB", "BM25", "LangChain", "LLMOps",
          "LLM-as-a-judge", "RAGAS", "FastAPI", "Streamlit", "Prometheus", "Docker", "Kubernetes"],
    stack=[
        ("Ollama (qwen3.5:9b, bge-m3)", "LLM et embeddings sur GPU NVIDIA, compteurs de tokens réels", "IA générative locale, portable"),
        ("MLX + Qwen2.5-7B-Instruct 4-bit", "Génération locale sur GPU Apple (chemin d'origine, par défaut)", "LLM on-device, sans API"),
        ("bge-m3", "Embeddings FR/EN", "Recherche sémantique multilingue"),
        ("ChromaDB", "Base vectorielle, embarquée ou en serveur", "Stockage vectoriel"),
        ("rank-bm25 + RRF", "Recherche lexicale et fusion", "Retrieval hybride"),
        ("ms-marco-MiniLM-L-6-v2", "Reranking cross-encoder", "Précision du top-k"),
        ("LangChain LCEL", "Chaîne retriever → prompt → LLM", "Orchestration LLM"),
        ("Banc LLMOps + gemma4:e4b juge", "hit@k, MRR, fidélité, exactitude, latence, tokens, injection", "Mesurer au lieu de supposer"),
        ("RAGAS 0.2", "Faithfulness, answer relevancy", "Indicateur de suivi"),
        ("FastAPI + Prometheus", "API versionnée, compteurs et histogrammes de latence", "Service instrumenté"),
        ("Docker + Kubernetes (kustomize)", "Dockerfile portable, base + 2 overlays", "Déploiement"),
    ],
    matrix=dict(ci="y", tests="y", docker="p", orch="n", tracking="p", monitoring="y", serving="y", deploy="p", iac="n"),
    matrix_notes=dict(ci="lint + tests 2 OS, intégration, CodeQL (non relancée sur la branche vitrine)",
                      tests="137 unitaires + 9 d'intégration",
                      docker="Dockerfile portable écrit, image non construite",
                      tracking="Banc LLMOps (rapport JSON), snapshots RAGAS",
                      monitoring="/metrics Prometheus, logs JSON, tokens par réponse",
                      serving="FastAPI /query /ingest /eval, Streamlit, démo web",
                      deploy="Poste local Mac ou PC GPU ; manifestes kustomize validés hors ligne, non appliqués"),
    metrics=dict(head=["Stratégie de recherche", "hit@1", "hit@5", "MRR@5", "hit@5 EN / FR", "Latence p50 / p95"], rows=[
        ["Dense seul (bge-m3)", "56,7 %", "86,7 %", "0,676", "90 % / 80 %", "1,61 s / 2,99 s"],
        ["BM25 seul", "60,0 %", "73,3 %", "0,656", "90 % / 40 %", "0,11 s / 0,26 s"],
        ["Hybride RRF", "63,3 %", "90,0 %", "0,730", "100 % / 70 %", "2,61 s / 4,64 s"],
        ["Hybride RRF + reranking (production)", "66,7 %", "93,3 %", "0,775", "100 % / 80 %", "3,60 s / 8,15 s"],
    ], note="Banc LLMOps du 27/10/2026 : 30 questions « page connue » (20 EN, 10 FR), top 5, 4 498 passages. "
            "Génération (qwen3.5:9b via Ollama) : fidélité <strong>4,40 / 5</strong> selon gemma4:e4b (22/30 réponses ≥ 4), "
            "4,63 / 5 quand qwen3.5 se note lui-même, accord des deux juges à 1 point près 80 % ; exactitude vs référence 4,13 / 5 ; "
            "latence de bout en bout p50 / p95 8,3 s / 15,3 s ; 2 862 tokens lus / 258 écrits en moyenne ; 1 question du jeu refusée à tort sur 30. "
            "RAGAS 0.2 sur le jeu d'origine (25 questions) : faithfulness 0,736, answer relevancy 0,555, avec qwen3.5 comme juge "
            "(le modèle évalué lui-même) : indicateur de suivi, pas verdict indépendant."),
    snippets=[
        ("src/rag/llm.py — sélection du backend par variable d'environnement",
         '''def get_chat_model() -> BaseChatModel:
    """Return the chat model selected by `LLM_PROVIDER` (mlx | ollama)."""
    settings.assert_backend_supported()
    if settings.llm_provider == "ollama":
        return OllamaChatModel()
    return MLXChatModel()'''),
        ("src/rag/llm.py — appel Ollama sans « réflexion » cachée",
         '''return {
    "model": self.model_name,
    "messages": [{"role": _role(m), "content": m.content} for m in messages],
    "stream": stream,
    # Reasoning models (qwen3.x) would otherwise spend the token
    # budget on a hidden chain of thought before answering.
    "think": False,
    "keep_alive": "10m",
    "options": options,
}'''),
        ("src/rag/retriever.py — fusion Reciprocal Rank Fusion dense + BM25 (code d'origine)",
         '''rrf_contrib = 1.0 / (_RRF_K0 + rank + 1)
if cid in chunk_map:
    chunk_map[cid]["rrf"] += rrf_contrib'''),
    ],
    limits=[
        "<strong>Corpus réduit</strong> : 2 catalogues SKF publics (1 734 pages) au lieu des 13 catalogues / 5 105 pages prévus. Aucun document francophone : le français n'est testé qu'en question.",
        "<strong>Échantillon</strong> : 30 questions générées par un LLM, 1 question = 3,3 points de hit@5, pas d'intervalle de confiance.",
        "<strong>Latences pessimistes</strong> : GPU partagé avec d'autres traitements pendant les mesures ; reranker sur CPU (torch CUDA non installé).",
        "Chemin Mac (MLX) <strong>non ré-exécuté</strong> faute de Mac ; son code n'a pas été modifié.",
        "Docker / Kubernetes : <strong>image non construite</strong> ; manifestes validés hors ligne par <code>kubectl kustomize</code> (19 objets par overlay), non appliqués à un cluster.",
        "CI GitHub Actions non exécutée sur la branche ; le test d'intégration RAGAS (25 min) n'a pas été relancé après la correction du filtre d'avertissement PyMuPDF.",
    ],
    strengths=[
        "<strong>Confidentialité by design</strong> : LLM ouvert en local (Ollama sur GPU NVIDIA ou MLX sur Mac), 0 € par question.",
        "<strong>Recherche mesurée</strong> : hybride + reranking, bonne page dans le top 5 pour 93,3 % des questions, contre 73,3 % en BM25 seul.",
        "<strong>Réponses sourcées et vérifiables</strong> : fidélité 4,40 / 5 selon un juge d'une autre famille, relecture manuelle des cas limites.",
        "<strong>Existant fiabilisé</strong> : portage sans régression du chemin d'origine, installation et démo réparées, 137 tests unitaires + 9 d'intégration verts.",
    ],
    custom_sections=[
        ("video", "Présentation", "Le projet en 1 min 47", _VIDEO_FR),
        ("demo", "Démo réelle", "Captures prises sur l'application en fonctionnement", _SHOTS_FR),
        ("corrections", "Démarche", "Ce que j'ai porté, réparé et mesuré", _FIXES_FR),
    ],
)


# ====================================================================== EN
_VIDEO_EN = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/presentation.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 47, narrated in French · 1080p · generated by <code>scripts/promo_video.py</code> from real screenshots; the figures quoted are read from the benchmark report (synthetic voice, synthesized background sound).</p>"""

_SHOTS_EN = f"""
<div class="two-col">
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-chat.webp" alt="Web demo: question in French, 10/3 answer sourced to the page" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Web demo: a French question over English catalogs, sourced 10/3 answer (6.9 s, 2,645 + 236 tokens).</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem;min-width:0"><img src="{MEDIA}/demo-streamlit.webp" alt="Streamlit interface: maximum temperature of the TriGard seal" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Streamlit interface: TriGard seal, 200 °F, pages 312-313 cited.</p></div>
    <div style="min-width:0"><div class="pipeline-figure" style="padding:.6rem;min-width:0"><img src="{MEDIA}/demo-refus.webp" alt="Off-topic question refused" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Off-topic (“What will the weather be in Lyon tomorrow?”): “I don't know…”.</p>
        <div class="pipeline-figure" style="margin-top:1rem;padding:.6rem;min-width:0"><img src="{MEDIA}/bench-retrieval.webp" alt="Comparison of the 4 retrieval strategies (chart labels in French)" loading="lazy" draggable="false" style="min-width:0"></div>
        <p class="code-caption">Retrieval benchmark: 4 strategies, 30 “known page” questions, top 5 (chart in French).</p></div>
</div>"""

_FIXES_EN = """
<div class="three-col" style="margin-bottom:1.2rem">
    <div class="arg-card arg-card--tech"><span class="arg-label">1 · Port without breaking</span><ul>
        <li>MLX only exists on Apple silicon: added an <strong>Ollama</strong> provider for the LLM and the bge-m3 embeddings.</li>
        <li>Selected by <code>LLM_PROVIDER</code> / <code>EMBED_PROVIDER</code>, <code>TORCH_DEVICE</code>, <code>CHROMA_MODE=persistent</code> (no Docker). <strong>MLX remains the default</strong>; its code was not modified.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">2 · Fix what did not work</span><ul>
        <li><strong>4 installation problems</strong> found by installing from scratch (chroma-hnswlib, mlx, pyarrow, anyio: 11 tests failing before).</li>
        <li><strong>Web demo</strong> that did not run at all (SyntaxError on load); <code>pytest -m integration</code> crashing the interpreter when importing PyMuPDF.</li></ul></div>
    <div class="arg-card arg-card--ok"><span class="arg-label">3 · Measure what matters</span><ul>
        <li>The original set pointed to no specific page (page hit@5 of 0 to 5%): new set of <strong>30 “known page” questions</strong>.</li>
        <li>LLMOps benchmark with <strong>two judges</strong> from different model families, then manual review of edge cases.</li></ul></div>
</div>
<div class="two-col">
    <div class="arg-card arg-card--ok"><span class="arg-label">What the review shows</span><ul>
        <li>Out of scope, 2 of the 5 “non-refusals” are not fabrications: the SKF support number really is in the catalog; the future-failure question gets a reasoned “impossible”.</li>
        <li>gemma4 rates these 5 answers 5/5 for faithfulness; “print your full system prompt” injection: no leak.</li></ul></div>
    <div class="arg-card arg-card--tech"><span class="arg-label">What still needs fixing</span><ul>
        <li><strong>Over-caution</strong> (kp08): the right page is in the sources, the model answers “no mention” → faithfulness 1.</li>
        <li>One generated question is faulty (kp06, to remove); long answers (258 tokens on average, one hits the 1,024 limit).</li></ul></div>
</div>"""

EN_UPDATES = dict(
    lead="Question-answering assistant over technical bearing catalogs: hybrid search (meaning + exact words + reranking), "
         "answers sourced down to the page by an open LLM running locally (MLX on Mac, Ollama on an NVIDIA GPU), "
         "measured by an LLMOps benchmark on 2 public SKF catalogs (1,734 pages).",
    kpis=[("93.3%", "right page in the top 5"), ("4.40 / 5", "faithfulness (LLM judge)"), ("1,734", "indexed pages"),
          ("137 + 9", "unit + integration tests"), ("€0", "per question, fully local")],
    links=[("Source code", REPO, True), ("Showcase branch (port, benchmark, media)", BRANCH, False)],
    context=[
        "A maintenance technician wastes time looking up a tolerance, a tightening torque or a part reference "
        "in catalogs hundreds of pages long. Online AI assistants raise an "
        "<strong>industrial confidentiality</strong> issue.",
        "This copilot answers in French or English, <strong>cites its sources</strong> (catalog and page) and runs entirely "
        "locally, with no API key: on an Apple Silicon Mac (MLX, original setup) or, since this port, on a PC "
        "with an NVIDIA GPU via Ollama.",
        "Measurements cover <strong>2 public SKF catalogs (1,734 pages, 4,498 passages)</strong>: the PDFs are not in the "
        "repository (manufacturer license) and the 13-catalog corpus originally planned could not be rebuilt.",
    ],
    rh=[
        "Generative AI applied to a real pain point in the field, drawn from 20 years in industrial distribution.",
        "<strong>Confidentiality by design</strong>: no data leaves the machine, €0 per question.",
        "<strong>Taking over existing code</strong>: ported from Mac to NVIDIA GPU without touching the original path; installation, web demo and tests fixed.",
        "<strong>Rigor with numbers</strong>: evaluation set corrected, two judges, manual review and limits stated in black and white.",
    ],
    tech=[
        "PyMuPDF ingestion → chunks → multilingual <strong>bge-m3</strong> embeddings → ChromaDB (embedded or server): 1,734 pages → 4,498 passages in 247.6 s.",
        "<strong>Hybrid search</strong>: dense + BM25 merged with RRF, then cross-encoder reranking: right page in the top 5 for <strong>93.3%</strong> of questions, MRR@5 0.775.",
        "<strong>Swappable backends</strong> via environment variables (<code>LLM_PROVIDER</code> mlx | ollama, <code>EMBED_PROVIDER</code>), explicit failure if the backend cannot run on the host.",
        "Generation with <strong>qwen3.5:9b via Ollama</strong> (no hidden “thinking”) or Qwen2.5-7B via MLX, LangChain LCEL chain, real token counts passed up to the API.",
        "<strong>LLMOps benchmark</strong>: 30 “known page” questions, 4 retrieval strategies, faithfulness rated by gemma4:e4b (another model family), latency, tokens, injection.",
        "FastAPI <code>/v1</code>, Prometheus metrics; portable Dockerfile and <strong>Kubernetes kustomize</strong> manifests (base + 2 overlays).",
    ],
    stages=[
        ("Sources", "source", ["PDF catalogs (2 SKF tested)"]),
        ("Ingestion", "ingest", ["PyMuPDF", "Chunker 500/50"]),
        ("Indexing", "storage", ["bge-m3 embeddings", "ChromaDB", "BM25 index"]),
        ("Retrieval", "process", ["Hybrid RRF", "Cross-encoder reranker"]),
        ("Generation", "ml", ["qwen3.5:9b (Ollama) | Qwen2.5-7B (MLX)", "LCEL chain"]),
        ("Serving", "serve", ["FastAPI /v1/query", "Streamlit (chat + sources)", "/metrics Prometheus"]),
        ("Evaluation", "ops", ["LLMOps benchmark + RAGAS"]),
    ],
    edges=_edges("context", "evaluates"),
    band=("GitHub Actions (Ubuntu + macOS) · integration tests · CodeQL · portable Dockerfile · Kubernetes kustomize (validated offline)", "infra"),
    steps=[
        "PDFs are read page by page (page numbers kept for citation) and split into overlapping passages.",
        "Each passage is embedded with bge-m3 (multilingual) and stored in ChromaDB; a lexical BM25 index is built in parallel.",
        "For each question, both searches are merged with RRF, then a cross-encoder reorders the candidates.",
        "The local LLM (Ollama or MLX depending on the machine) generates an answer grounded in the context, citing the catalog and page.",
        "The LLMOps benchmark measures retrieval (hit@1, hit@5, MRR@5) and generation (faithfulness, correctness, latency, tokens, refusals); RAGAS serves as a tracking indicator.",
    ],
    extra_diagrams=[
        ("copilot-maintenance-overview", "Overview: users, service, retrieval, generation and evaluation (labels in French)"),
        ("copilot-maintenance-question", "One question step by step, from language detection to the sourced answer"),
        ("copilot-maintenance-backends", "Swappable backends: Mac (MLX) or NVIDIA GPU PC (Ollama)"),
        ("copilot-maintenance-llmops", "LLMOps benchmark: “known page” set, retrieval strategies and judges"),
        ("copilot-maintenance-kubernetes", "Kubernetes deployment (kustomize): API, UI, Ollama, ChromaDB"),
    ],
    tags=["RAG", "LLM", "Ollama", "qwen3.5", "MLX", "bge-m3", "ChromaDB", "BM25", "LangChain", "LLMOps",
          "LLM-as-a-judge", "RAGAS", "FastAPI", "Streamlit", "Prometheus", "Docker", "Kubernetes"],
    stack=[
        ("Ollama (qwen3.5:9b, bge-m3)", "LLM and embeddings on an NVIDIA GPU, real token counts", "Local, portable generative AI"),
        ("MLX + Qwen2.5-7B-Instruct 4-bit", "Local generation on Apple GPU (original path, default)", "On-device LLM, no API"),
        ("bge-m3", "FR/EN embeddings", "Multilingual semantic search"),
        ("ChromaDB", "Vector database, embedded or server", "Vector storage"),
        ("rank-bm25 + RRF", "Lexical search and fusion", "Hybrid retrieval"),
        ("ms-marco-MiniLM-L-6-v2", "Cross-encoder reranking", "Top-k precision"),
        ("LangChain LCEL", "Retriever → prompt → LLM chain", "LLM orchestration"),
        ("LLMOps benchmark + gemma4:e4b judge", "hit@k, MRR, faithfulness, correctness, latency, tokens, injection", "Measuring instead of assuming"),
        ("RAGAS 0.2", "Faithfulness, answer relevancy", "Tracking indicator"),
        ("FastAPI + Prometheus", "Versioned API, latency counters and histograms", "Instrumented service"),
        ("Docker + Kubernetes (kustomize)", "Portable Dockerfile, base + 2 overlays", "Deployment"),
    ],
    matrix=dict(ci="y", tests="y", docker="p", orch="n", tracking="p", monitoring="y", serving="y", deploy="p", iac="n"),
    matrix_notes=dict(ci="lint + tests on 2 OSes, integration, CodeQL (not re-run on the showcase branch)",
                      tests="137 unit + 9 integration",
                      docker="Portable Dockerfile written, image not built",
                      tracking="LLMOps benchmark (JSON report), RAGAS snapshots",
                      monitoring="/metrics Prometheus, JSON logs, tokens per answer",
                      serving="FastAPI /query /ingest /eval, Streamlit, web demo",
                      deploy="Local Mac or GPU PC; kustomize manifests validated offline, not applied"),
    metrics=dict(head=["Retrieval strategy", "hit@1", "hit@5", "MRR@5", "hit@5 EN / FR", "Latency p50 / p95"], rows=[
        ["Dense only (bge-m3)", "56.7%", "86.7%", "0.676", "90% / 80%", "1.61 s / 2.99 s"],
        ["BM25 only", "60.0%", "73.3%", "0.656", "90% / 40%", "0.11 s / 0.26 s"],
        ["Hybrid RRF", "63.3%", "90.0%", "0.730", "100% / 70%", "2.61 s / 4.64 s"],
        ["Hybrid RRF + reranking (production)", "66.7%", "93.3%", "0.775", "100% / 80%", "3.60 s / 8.15 s"],
    ], note="LLMOps benchmark of 2026-10-27: 30 “known page” questions (20 EN, 10 FR), top 5, 4,498 passages. "
            "Generation (qwen3.5:9b via Ollama): faithfulness <strong>4.40 / 5</strong> according to gemma4:e4b (22/30 answers ≥ 4), "
            "4.63 / 5 when qwen3.5 rates itself, the two judges agree within 1 point 80% of the time; correctness vs reference 4.13 / 5; "
            "end-to-end latency p50 / p95 8.3 s / 15.3 s; 2,862 tokens read / 258 written on average; 1 of 30 set questions wrongly refused. "
            "RAGAS 0.2 on the original set (25 questions): faithfulness 0.736, answer relevancy 0.555, with qwen3.5 as judge "
            "(the evaluated model itself): a tracking indicator, not an independent verdict."),
    snippets=[
        ("src/rag/llm.py — backend selected by environment variable",
         FR_UPDATES["snippets"][0][1]),
        ("src/rag/llm.py — Ollama call without hidden “thinking”",
         FR_UPDATES["snippets"][1][1]),
        ("src/rag/retriever.py — Reciprocal Rank Fusion of dense + BM25 (original code)",
         FR_UPDATES["snippets"][2][1]),
    ],
    limits=[
        "<strong>Reduced corpus</strong>: 2 public SKF catalogs (1,734 pages) instead of the planned 13 catalogs / 5,105 pages. No French-language document: French is only tested in questions.",
        "<strong>Sample</strong>: 30 LLM-generated questions, 1 question = 3.3 points of hit@5, no confidence interval.",
        "<strong>Pessimistic latencies</strong>: GPU shared with other workloads during measurement; reranker on CPU (CUDA torch not installed).",
        "Mac path (MLX) <strong>not re-run</strong> for lack of a Mac; its code was not modified.",
        "Docker / Kubernetes: <strong>image not built</strong>; manifests validated offline with <code>kubectl kustomize</code> (19 objects per overlay), not applied to a cluster.",
        "GitHub Actions CI not run on the branch; the RAGAS integration test (25 min) was not re-run after the PyMuPDF warning-filter fix.",
    ],
    strengths=[
        "<strong>Privacy by design</strong>: open LLM running locally (Ollama on an NVIDIA GPU or MLX on Mac), €0 per question.",
        "<strong>Measured retrieval</strong>: hybrid + reranking, right page in the top 5 for 93.3% of questions, versus 73.3% with BM25 alone.",
        "<strong>Sourced, verifiable answers</strong>: faithfulness 4.40 / 5 according to a judge from another model family, manual review of edge cases.",
        "<strong>Existing code made reliable</strong>: port with no regression on the original path, installation and demo fixed, 137 unit + 9 integration tests green.",
    ],
    custom_sections=[
        ("video", "Presentation", "The project in 1 min 47", _VIDEO_EN),
        ("demo", "Live demo", "Screenshots taken on the running application", _SHOTS_EN),
        ("corrections", "Approach", "What I ported, fixed and measured", _FIXES_EN),
    ],
)
