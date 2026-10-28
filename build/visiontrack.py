"""VisionTrack (dépôt visiontrack) : détection, tracking et distance de personnes en temps réel, 100 % local sur GPU NVIDIA.

Chiffres issus du README et de la release v0.1.0 (2026-10-28), mesurés sur RTX 4070 Ti SUPER.
"""

GH = "https://github.com/PDUCLOS/"
MEDIA = "/media/visiontrack"

_VIDEO = f"""
<video controls preload="none" poster="{MEDIA}/poster.webp" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830">
    <source src="{MEDIA}/demo.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">1 min 57 · montée par <code>demo/make_demo.py</code>, qui fait tourner le vrai pipeline sur chaque scène :
suivi, distance, foule dense, nuit, comptage, zone interdite, heatmap, puis comparatif réglage rapide / réglage précision.
Vidéos sources sous licence CC BY, créditées à l'écran.</p>
<div class="pipeline-figure" style="margin-top:1.5rem;padding:.6rem"><img src="{MEDIA}/chelmsford.webp" alt="VisionTrack sur une rue piétonne : boîtes, identifiants, distances et carte de profondeur en incrustation" loading="lazy" draggable="false" style="min-width:0"></div>
<p class="code-caption">Rue piétonne de Chelmsford (CC BY) : identifiants stables, distance de chaque personne en mètres (rouge &lt; 3 m, orange &lt; 8 m),
carte de profondeur en incrustation, ligne de comptage.</p>"""

VISIONTRACK = dict(
    slug="visiontrack",
    short="VisionTrack — vision par ordinateur locale",
    kicker="Computer vision · Temps réel · 100 % local",
    title="VisionTrack — détection, tracking et distance de personnes en temps réel, 100 % local",
    title_html='Compter, suivre et mesurer les personnes <span class="highlight">sans qu\'une image ne quitte le site</span>',
    lead="Pipeline de vision par ordinateur en temps réel sur un PC équipé d'une carte NVIDIA grand public : détection RF-DETR, "
         "tracking ByteTrack, distance par fusion géométrie + profondeur Depth Anything V2, lignes de comptage, zones interdites "
         "et heatmap. Tout se règle dans un fichier YAML ; sorties en vidéo annotée et en JSON Lines.",
    kpis=[("≈ 28–30", "images/s en 1280×720"), ("100 %", "local, fonctionne hors ligne"), ("3", "méthodes de distance"),
          ("8", "scénarios dans la vidéo de démo"), ("Apache 2.0", "modèles par défaut")],
    links=[("Code source", GH + "visiontrack", True), ("Vidéo de démo", "#video", False)],
    context=[
        "Compter les entrées d'un magasin, détecter une personne dans une zone dangereuse ou mesurer la densité d'une foule : "
        "les offres du marché envoient en général les images dans le cloud et facturent <strong>à la caméra</strong>. "
        "Pour beaucoup de sites, c'est un frein RGPD autant qu'un coût qui grandit avec le volume.",
        "VisionTrack fait tout <strong>sur place</strong>, sur un seul PC GPU : détection, suivi, distance en mètres, comptage "
        "et alertes de zone. Seules des métriques (comptages, JSON) peuvent sortir du site si on le souhaite. "
        "L'adaptation à un nouveau site se fait dans <code>config.yaml</code>, sans toucher au code.",
    ],
    rh=[
        "<strong>Conformité par conception</strong> : aucune image ne quitte le réseau local, pas d'abonnement par caméra.",
        "<strong>Pensé comme une offre</strong> : audit du site, POC de 2 semaines sur les vidéos du client, puis déploiement et formation.",
        "<strong>Cas d'usage concrets</strong> : commerce (fréquentation, heatmap), sécurité (zone interdite), événementiel, smart city, entrepôt, sport.",
        "<strong>Honnêteté technique</strong> : la distance est annoncée comme une estimation (±15–20 % sans calibration), avec la façon de la fiabiliser.",
    ],
    tech=[
        "Détection <strong>RF-DETR</strong> (Apache 2.0) ou YOLO en option ; tracking <strong>ByteTrack</strong> avec identifiants stables et traînées.",
        "Seuils du tracker alignés automatiquement sur la confiance du détecteur, pour ne pas rejeter des détections volontairement gardées.",
        "Distance : géométrie (focale × taille / hauteur de boîte), profondeur <strong>Depth Anything V2</strong> en fp16 sur GPU, "
        "ou fusion qui recale la profondeur relative en mètres ; lissage exponentiel par piste.",
        "Zones de comptage et zones interdites, heatmap ; sorties MP4 annoté + JSON Lines (une ligne par image : pistes, distances, zones).",
        "Interface <strong>Gradio</strong> locale pour les rendez-vous client ; vidéo de démo générée par script à partir du vrai pipeline.",
    ],
    stages=[
        ("Sources", "source", ["YouTube (yt-dlp)", "Fichier ou webcam", "Caméra IP (RTSP)"]),
        ("Détection", "ml", ["RF-DETR (Apache 2.0)", "YOLO (option, AGPL)"]),
        ("Tracking", "process", ["ByteTrack", "ID stables + traînées"]),
        ("Distance", "ml", ["Géométrie (pinhole)", "Depth Anything V2", "Fusion + lissage"]),
        ("Zones", "process", ["Lignes de comptage", "Zones interdites", "Heatmap"]),
        ("Sorties", "serve", ["MP4 annoté", "JSON Lines", "Interface Gradio"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s0n2", "s1n0", "", False),
           ("s0n1", "s1n1", "", False), ("s1n0", "s2n0", "boîtes", False), ("s1n1", "s2n0", "", False),
           ("s2n0", "s2n1", "", False), ("s2n1", "s3n0", "", False), ("s2n1", "s3n1", "", False),
           ("s3n0", "s3n2", "recalage", False), ("s3n1", "s3n2", "", False),
           ("s3n2", "s4n0", "", False), ("s3n2", "s4n1", "", False), ("s2n1", "s4n2", "", False),
           ("s4n0", "s5n0", "", False), ("s4n1", "s5n1", "", False), ("s4n2", "s5n0", "", False), ("s5n0", "s5n2", "", False)],
    band=("config.yaml : source, modèle, classes, zones, seuils · PyTorch CUDA (fp16) · tout reste sur le réseau local", "infra"),
    steps=[
        "<strong>Source</strong> — vidéo YouTube (mise en cache), fichier, webcam ou flux RTSP ; extrait et résolution réglables.",
        "<strong>Détection</strong> — RF-DETR (nano à large) filtre les classes demandées (personnes par défaut) au seuil de confiance choisi.",
        "<strong>Tracking</strong> — ByteTrack attribue un identifiant stable à chaque personne et conserve les pistes perdues quelques instants (occultations).",
        "<strong>Distance</strong> — fusion de la méthode géométrique et de la carte de profondeur, calculée une image sur deux pour tenir le temps réel, puis lissée par piste.",
        "<strong>Zones et rendu</strong> — comptage entrées / sorties, alertes de zone interdite, heatmap ; vidéo annotée, JSON Lines et statistiques dans l'interface Gradio.",
    ],
    extra_diagrams=[("visiontrack-architecture", "Architecture du pipeline"),
                    ("visiontrack-local-vs-cloud", "Local ou cloud : ce qui sort du site"),
                    ("visiontrack-use-cases", "Cas d'usage")],
    langs=[("Python", 100)],
    langs_note="≈ 1 270 lignes de Python : pipeline, interface Gradio et script de la vidéo de démo.",
    tags=["Computer vision", "RF-DETR", "ByteTrack", "Depth Anything V2", "PyTorch", "CUDA", "OpenCV", "supervision",
          "Gradio", "YAML", "RGPD"],
    stack=[
        ("RF-DETR", "Détection des personnes (nano → large)", "Choix d'un modèle récent sous licence permissive"),
        ("ByteTrack (trackers / supervision)", "Suivi multi-objets, identifiants stables", "Gestion des occultations et des ID fantômes"),
        ("Depth Anything V2", "Carte de profondeur monoculaire en fp16", "Intégration d'un modèle Hugging Face sur GPU"),
        ("PyTorch CUDA", "Inférence GPU de bout en bout", "Tenir le temps réel sur du matériel grand public"),
        ("OpenCV", "Lecture des sources, rendu et écriture MP4", "Traitement vidéo"),
        ("supervision", "Lignes de comptage, zones polygonales, annotations", "Logique métier au-dessus des détections"),
        ("Gradio", "Interface de démonstration locale, retours enregistrés en local", "Outil présentable en rendez-vous client"),
        ("YAML", "Toute l'adaptation à un site dans un seul fichier", "Séparer configuration et code"),
    ],
    matrix=dict(ci="n", tests="n", docker="n", orch="n", tracking="n", monitoring="n", serving="p", deploy="p", iac="n"),
    matrix_notes=dict(serving="Interface Gradio locale (pas d'API)", deploy="Installation documentée sur PC GPU Windows / Linux"),
    metrics=dict(head=["Mesure", "Résultat", "Conditions"], rows=[
        ["Débit de tout le pipeline", "≈ 28 à 30 images/s", "RTX 4070 Ti SUPER, 1280×720, RF-DETR medium + tracking + profondeur + zones + rendu"],
        ["Précision de la distance", "estimation à ±15–20 %", "sans calibration de la caméra ; meilleure avec le vrai champ de vision"],
    ], note="La vidéo de démo compare sur la même scène un réglage rapide (medium, seuil 0,45, 1280 px) et un réglage précision "
            "(large, seuil 0,30, 1920 px), avec le nombre moyen de personnes détectées et la vitesse obtenue."),
    snippets=[
        ("visiontrack/pipeline.py — le tracker ne rejette pas ce que le détecteur a gardé",
         '''conf = cfg["detector"]["confidence"]
tracker_cfg["track_activation_threshold"] = min(tracker_cfg["track_activation_threshold"], conf)
tracker_cfg["high_conf_det_threshold"] = min(tracker_cfg.get("high_conf_det_threshold", 0.6), conf + 0.15)
tracker = ByteTrackTracker(frame_rate=src_fps, **tracker_cfg)'''),
        ("config.yaml — adapter à un site sans toucher au code",
         '''detector:
  backend: rfdetr       # rfdetr (Apache 2.0) | yolo (Ultralytics, AGPL-3.0)
  model: medium
  confidence: 0.45
distance:
  method: fusion        # pinhole | depth | fusion | none
  horizontal_fov_deg: 65
zones:
  lines:
    - name: passage
      start: [0.05, 0.75]
      end: [0.95, 0.75]'''),
    ],
    limits=[
        "Pas encore de tests automatisés ni d'intégration continue : priorité à la démonstration, à ajouter avant une mission.",
        "Distance estimée sans calibration (±15–20 %) : en mission, renseigner le vrai champ de vision ou calibrer la caméra.",
        "Nécessite un PC x86 avec carte NVIDIA (CUDA) ; pas de version CPU temps réel.",
        "Backend YOLO sous AGPL-3.0 et modèles Depth Anything Base / Large ou « Metric » : licence à vérifier avant un usage commercial.",
    ],
    custom_sections=[("video", "Démonstration", "VisionTrack en 1 min 57", _VIDEO)],
    strengths=[
        "<strong>100 % local</strong> : aucune image ne quitte le site, pas de cloud ni d'abonnement par caméra, fonctionne hors ligne.",
        "<strong>Temps réel sur matériel grand public</strong> : ≈ 28–30 images/s en 1280×720 pour tout le pipeline sur une RTX 4070 Ti SUPER.",
        "<strong>Distance fiable dans les scènes encombrées</strong> : fusion géométrie + profondeur, qui prend le relais quand une personne est assise ou masquée.",
        "<strong>Adaptable par configuration</strong> : source, modèle, classes, zones et seuils dans un seul fichier YAML.",
    ],
)
