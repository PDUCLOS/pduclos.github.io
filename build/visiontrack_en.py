"""English version of visiontrack.VISIONTRACK (same slug, structure and figures)."""

from visiontrack import VISIONTRACK as _FR

GH = "https://github.com/PDUCLOS/"
MEDIA = "/media/visiontrack"

_VID = 'controls preload="none" style="width:100%;border-radius:12px;border:1px solid var(--border);background:#0f1830"'

_VIDEO = f"""
<video {_VID} poster="{MEDIA}/reel-poster.webp">
    <source src="{MEDIA}/reel.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem"><strong>Demo reel, 69 s</strong> (v0.3.1, on-screen text in French) · a hook, then 16 examples of 3.4 s in 4 chapters:
speed, speeding, flow, people. The overlaid figures (top speed, alerts, vehicles or people in frame) are computed from the pipeline's JSON
by <code>demo/make_reel.py</code>. No sound.</p>

<h3 style="margin-top:2.2rem">Road traffic · 1 min 37</h3>
<video {_VID} poster="{MEDIA}/trafic-poster.webp">
    <source src="{MEDIA}/trafic.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">Vehicle demo (v0.3.0) · <code>make_demo.py --profile trafic</code>: speed calibrated on road markings,
speeding, intersection and roundabout seen from above, highway without calibration. Speeds are estimates, not certified measurements;
on overhead views they are shown without speeding alerts. The demo shows no wrong-way case: no real royalty-free footage was available.</p>

<h3 style="margin-top:2.2rem">People · 2 min 24</h3>
<video {_VID} poster="{MEDIA}/poster.webp">
    <source src="{MEDIA}/demo.mp4" type="video/mp4">
</video>
<p class="code-caption" style="margin-top:.8rem">People demo (v0.2.0) · edited by <code>demo/make_demo.py</code>, which runs the real pipeline on every scene:
pipeline diagram, tracking, distance, dense crowd, night, counting, restricted zone, heatmap, settings, then a fast vs. accurate settings comparison.</p>
<div class="pipeline-figure" style="margin-top:1.5rem;padding:.6rem"><img src="{MEDIA}/chelmsford.webp" alt="VisionTrack on a pedestrian street: boxes, IDs, distances and depth map inset" loading="lazy" draggable="false" style="min-width:0"></div>
<p class="code-caption">Chelmsford pedestrian street (CC BY): stable IDs, each person's distance in meters (red &lt; 3 m, orange &lt; 8 m),
depth map inset, counting line.</p>
<p class="code-caption" style="margin-top:1rem">Source videos under CC BY license, credited on screen: Karol Majek, StockVid, Copyright Free Videos, Culture Snap,
Free Footage, Montreal Walking Tours, MOAH CLUB.</p>"""

VISIONTRACK_EN = dict(
    slug="visiontrack",
    short="VisionTrack — on-premise computer vision",
    kicker="Computer vision · People and road traffic · 100% on-premise",
    title="VisionTrack — real-time people and road traffic: tracking, distance, speed, 100% on-premise",
    title_html='Count, track and measure people and vehicles <span class="highlight">without a single image leaving the site</span>',
    lead="Real-time computer vision pipeline on a PC with a consumer NVIDIA GPU: RF-DETR detection, ByteTrack tracking, "
         "distance from a fusion of geometry and Depth Anything V2 depth, counting lines, restricted zones and heatmap. "
         "A road-traffic profile adds each vehicle's speed in km/h, speeding and wrong-way alerts, counts by type and flow. "
         "Everything is configured in one YAML file; outputs are an annotated video and JSON Lines.",
    kpis=[("29", "frames/s, full pipeline at 1280×720"), ("26", "frames/s on CPU only, without depth"),
          ("100%", "on-premise, works offline"), ("5", "vehicle types counted"), ("16", "examples in the demo reel")],
    links=[("Source code", GH + "visiontrack", True), ("Demo videos", "#video", False)],
    context=[
        "Counting store entries, detecting a person in a hazardous area or measuring crowd density: market offerings usually "
        "send images to the cloud and charge <strong>per camera</strong>. For many sites, that is a GDPR blocker as much as a "
        "cost that grows with volume.",
        "VisionTrack does everything <strong>on site</strong>, on a single GPU PC: detection, tracking, distance in meters, "
        "counting and zone alerts. Only metrics (counts, JSON) leave the site, and only if wanted. Adapting it to a new site "
        "happens in <code>config.yaml</code>, without touching the code.",
    ],
    rh=[
        "<strong>Compliance by design</strong>: no image leaves the local network, no per-camera subscription.",
        "<strong>Built as an offering</strong>: site audit, 2-week POC on the client's videos, then deployment and training.",
        "<strong>Concrete use cases</strong>: retail (footfall, heatmap), safety (restricted zone), events, smart city, warehouses, sports, "
        "and road traffic (speed, speeding, wrong way, flow by vehicle type).",
        "<strong>Technical honesty</strong>: distance is presented as an estimate (±15–20% without calibration), with how to make it reliable.",
    ],
    tech=[
        "<strong>RF-DETR</strong> detection (Apache 2.0) or optional YOLO; <strong>ByteTrack</strong> tracking with stable IDs and trails.",
        "Tracker thresholds automatically aligned with the detector confidence, so detections deliberately kept are not rejected.",
        "Distance: geometry (focal length × height / box height), <strong>Depth Anything V2</strong> depth in fp16 on GPU, "
        "or a fusion that rescales relative depth to meters; exponential smoothing per track.",
        "Counting lines and restricted zones, heatmap; outputs annotated MP4 + JSON Lines (one line per frame: tracks, distances, zones).",
        "<strong>Road-traffic</strong> profile (<code>config_trafic.yaml</code>): cars, trucks, buses, motorcycles, bicycles; speed in km/h, "
        "calibrated (4 ground points and their real dimensions) or automatic; speeding confirmed after 0.7 s; direction of travel per lane "
        "(polygon + arrow) and wrong-way alert; counts by type and flow in vehicles/min.",
        "Live local <strong>Gradio</strong> interface (15 test videos, webcam, YouTube URL streamed, real-time mode); "
        "demo videos and reel generated by script from the real pipeline.",
    ],
    stages=[
        ("Sources", "source", ["YouTube (yt-dlp)", "File or webcam", "IP camera (RTSP)"]),
        ("Detection", "ml", ["RF-DETR (Apache 2.0)", "YOLO (optional, AGPL)"]),
        ("Tracking", "process", ["ByteTrack", "Stable IDs + trails"]),
        ("Distance", "ml", ["Geometry (pinhole)", "Depth Anything V2", "Fusion + smoothing"]),
        ("Zones", "process", ["Counting lines", "Restricted zones", "Heatmap", "Speed, speeding, wrong way"]),
        ("Outputs", "serve", ["Annotated MP4", "JSON Lines", "Gradio interface"]),
    ],
    edges=[(a, b, {"boîtes": "boxes", "recalage": "rescaling"}.get(l, l), d) for a, b, l, d in _FR["edges"]],
    band=("config.yaml: source, model, classes, zones, thresholds · PyTorch CUDA (fp16) · everything stays on the local network", "infra"),
    steps=[
        "<strong>Source</strong> — YouTube video (cached), file, webcam or RTSP stream; excerpt and resolution configurable.",
        "<strong>Detection</strong> — RF-DETR (nano to large) keeps the requested classes (people by default) above the chosen confidence threshold.",
        "<strong>Tracking</strong> — ByteTrack gives each person a stable ID and keeps lost tracks for a few moments (occlusions).",
        "<strong>Distance</strong> — fusion of the geometric method and the depth map, computed every other frame to stay real time, then smoothed per track.",
        "<strong>Zones and rendering</strong> — in / out counting, restricted-zone alerts, heatmap; annotated video, JSON Lines and statistics in the Gradio interface.",
        "<strong>Traffic profile</strong> — from the tracks, each vehicle's speed in km/h, speeding and wrong-way alerts per lane, counts by type and flow.",
    ],
    extra_diagrams=[("visiontrack-architecture", "Pipeline architecture (in French)"),
                    ("visiontrack-local-vs-cloud", "On-premise vs. cloud: what leaves the site (in French)"),
                    ("visiontrack-use-cases", "Use cases (in French)")],
    langs=[("Python", 100)],
    langs_note="≈ 2,780 lines of Python: pipeline, traffic profile, Gradio interface, demo, reel and benchmark scripts.",
    tags=["Computer vision", "RF-DETR", "ByteTrack", "Depth Anything V2", "PyTorch", "CUDA", "OpenCV", "supervision",
          "Gradio", "YAML", "GDPR", "Road traffic"],
    stack=[
        ("RF-DETR", "People and vehicle detection (nano → large)", "Choosing a recent model under a permissive license"),
        ("ByteTrack (trackers / supervision)", "Multi-object tracking, stable IDs", "Handling occlusions and ghost IDs"),
        ("Depth Anything V2", "Monocular depth map in fp16", "Integrating a Hugging Face model on GPU"),
        ("PyTorch CUDA", "End-to-end GPU inference", "Staying real time on consumer hardware"),
        ("OpenCV", "Reading sources, rendering and writing MP4", "Video processing"),
        ("supervision", "Counting lines, polygon zones, annotations", "Business logic on top of detections"),
        ("Gradio", "Local demo interface, feedback stored locally", "A tool ready to show in client meetings"),
        ("YAML", "All site-specific tuning in one file (people or traffic)", "Separating configuration from code"),
    ],
    matrix=dict(_FR["matrix"]),
    matrix_notes=dict(serving="Local Gradio interface (no API)", deploy="Documented installation on a Windows / Linux GPU PC"),
    metrics=dict(head=["Measure", "Result", "Conditions"], rows=[
        ["Whole-pipeline throughput", "29 frames/s", "RTX 4070 Ti SUPER, Ryzen 9 3900X, 1280×720, RF-DETR medium + tracking + depth + zones + rendering"],
        ["Light configuration", "40 frames/s", "same PC, 1280×720"],
        ["CPU only", "26 frames/s", "without depth (counting, zones, geometric distance)"],
        ["Distance accuracy", "estimate within ±15–20%", "without camera calibration; better with the real field of view"],
        ["Vehicle speed", "estimate", "calibrated on 4 ground points, or approximate without calibration; not a certified measurement"],
    ], note="The demo video compares, on the same scene, a fast setting (medium, threshold 0.45, 1280 px) and an accurate setting "
            "(large, threshold 0.30, 1920 px), with the average number of people detected and the speed achieved."),
    snippets=[
        ("visiontrack/pipeline.py — the tracker does not reject what the detector kept", _FR["snippets"][0][1]),
        ("config.yaml — adapting to a site without touching the code", _FR["snippets"][1][1]),
    ],
    limits=[
        "No automated tests or continuous integration yet: the demo came first; to add before a client engagement.",
        "Distance estimated without calibration (±15–20%): on a real engagement, set the actual field of view or calibrate the camera.",
        "Full pipeline (with depth) on an x86 PC with an NVIDIA GPU (CUDA); on CPU only, 26 frames/s but without the depth map.",
        "Vehicle speeds are estimated, not certified; on overhead views they are shown without speeding alerts.",
        "Wrong-way alert built but not shown in the demo: no real royalty-free footage was available.",
        "YOLO backend under AGPL-3.0, and Depth Anything Base / Large or “Metric” models: check the license before commercial use.",
    ],
    custom_sections=[("video", "Demo", "VisionTrack on video: reel, traffic, people", _VIDEO)],
    strengths=[
        "<strong>100% on-premise</strong>: no image leaves the site, no cloud or per-camera subscription, works offline.",
        "<strong>Real time on consumer hardware</strong>: 29 frames/s at 1280×720 for the whole pipeline on an RTX 4070 Ti SUPER, 40 in a light configuration.",
        "<strong>People and vehicles</strong>: the same tool counts passers-by or measures a road's speed and flow, depending on the profile.",
        "<strong>Reliable distance in crowded scenes</strong>: geometry + depth fusion takes over when a person is sitting or occluded.",
        "<strong>Configurable</strong>: source, model, classes, zones and thresholds in a single YAML file.",
    ],
)
