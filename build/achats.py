"""Purchasing analytics project, written from a business-analyst angle (anonymised: no company, supplier, site or amount)."""

LEVERS = [
    ("G1", "Négocier sur la hausse <strong>pondérée par les volumes</strong>, pas sur la moyenne affichée", "0,3 à 0,8 pt de hausse évité sur la dépense en révision", "Argument chiffré, référence par référence"),
    ("G2", "Faire payer le <strong>prix convenu</strong> : écart entre prix payé dans l'ERP et prix dû", "0,10 à 0,50 % de la dépense", "Sépare le simple retard d'application de l'écart réellement inexpliqué"),
    ("G3", "Aligner les entités sur le <strong>meilleur prix du groupe</strong>", "30 à 50 % de l'écart entre sites", "Jamais de prix à 0 € quand une donnée manque"),
    ("G4", "Faire respecter les <strong>prix spéciaux</strong> : plafonds de hausse, engagements de volume, accords non déclarés", "0,5 à 1,5 % de la dépense concernée", "Phrase de négociation rédigée avec sa source"),
    ("G5", "Rendre du <strong>temps à l'acheteur</strong>", "1,5 à 3 jours par révision tarifaire", "Temps réinvesti dans la négociation, pas dans la recopie"),
    ("G6", "<strong>Acheter avant la hausse</strong> jusqu'au point où le stock coûte plus qu'il ne rapporte", "bénéfice ∝ hausse² / coût de possession", "Plafonné par la péremption et les règles de provision"),
]
lever_rows = "".join(f"<tr><td>{c}</td><td>{l}</td><td>{o}</td><td>{n}</td></tr>" for c, l, o, n in LEVERS)

STAKEHOLDERS = [
    ("Acheteur", "Négocier vite, avec des chiffres incontestables", "Dossier de négociation, mémo d'une page, file d'arbitrage triée par enjeu"),
    ("Référent achats / responsable produit", "Arbitrer seuils, règles et priorités", "Règles en configuration, journal des décisions"),
    ("Direction achats", "Piloter la performance fournisseurs et les économies", "Scorecards trimestrielles, Board consolidé, économies constatées"),
    ("Contrôle de gestion", "Fiabilité des chiffres", "Chaque montant traçable jusqu'à sa source ; aucune valeur devinée"),
    ("DSI", "Sécurité, exploitation, coût", "Lecture seule sur les ERP, habilitations par profil, sauvegardes, mises à jour sans perte"),
]
stake_rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in STAKEHOLDERS)

ACHATS = dict(
    slug="achats-negociation",
    short="Achats — tarifs & scorecards",
    kicker="Projet en cours · Business Analyst · Achats",
    badge="PROJET EN COURS · BUSINESS ANALYST",
    title="Plateforme d'aide à la négociation achats",
    title_html='Business Analyst achats : transformer chaque hausse tarifaire en <span class="highlight">argument chiffré</span>',
    lead="Projet réel, en cours dans une direction Achats industrielle. J'y interviens comme <strong>Business Analyst</strong> "
         "et j'assure le <strong>suivi du projet</strong> : recueil des besoins, règles de gestion, business case, cahier des charges, "
         "backlog, recette avec les acheteurs et pilotage des lots — jusqu'à la livraison d'un moteur Python / DuckDB et d'une interface R/Shiny.",
    kpis=[("≈ 1 %", "de la dépense suivie (gain central)"), ("105", "éléments de backlog suivis"), ("24", "règles de gestion formalisées"),
          ("6", "leviers de gain chiffrés"), ("≈ 3 000", "tests automatisés")],
    links=[],
    context=[
        "<strong>Ce projet existe et il est en cours.</strong> Je l'accompagne en tant que Business Analyst, de l'expression du besoin "
        "au suivi de la mise en œuvre. <em>Présentation anonymisée : aucune entreprise, aucun fournisseur, aucun site ni aucun montant réel ; "
        "les exemples chiffrés viennent du jeu de démonstration, entièrement fictif. Code non public.</em>",
        "Une direction Achats reçoit chaque année des dizaines de révisions tarifaires, dans tous les formats (Excel, CSV, PDF). "
        "Aujourd'hui, l'acheteur passe <strong>1 à 3 jours par révision</strong> à remettre le fichier au format, rapprocher les références "
        "de l'ERP et chiffrer l'impact — et négocie souvent sur la hausse <em>affichée</em> par le fournisseur.",
        "Le projet outille deux processus : l'analyse des <strong>tarifs fournisseurs</strong> (de la réception au dossier de négociation) "
        "et les <strong>scorecards fournisseurs</strong> trimestrielles (fin de la ressaisie, l'acheteur ne garde que le jugement).",
    ],
    rh=[
        "<strong>Rôle actuel de Business Analyst</strong> sur un projet réel : besoins, règles de gestion, cahier des charges, backlog, recette, suivi.",
        "<strong>Business case chiffré</strong> en trois scénarios (bas / central / haut) : de 0,5 % à 2,3 % de la dépense suivie, retour dès le premier trimestre.",
        "Conditions d'échec écrites noir sur blanc : volumes non fiables, référentiel non rattaché, rapport de force défavorable, alertes non suivies.",
        "Organisation proposée : équipe de 8 personnes, dont <strong>deux profils métier</strong> jugés indispensables au succès.",
    ],
    tech=[
        "Moteur Python 3.12 piloté par configuration YAML : ajouter un fournisseur relève de la <strong>configuration, pas du code</strong>.",
        "<strong>Cascade de rattachement</strong> L0 exact → L1 règles → L2 approché (rapidfuzz) → L3 arbitrage humain, référentiel versionné et annulable.",
        "Entrepôt DuckDB (68 tables, 42 vues d'interface sous contrat versionné), interface R/Shiny en lecture seule, 5 profils d'habilitation.",
        "Qualité : ≈ 2 500 tests Python (pytest-xdist), 445 tests R (testthat), CI GitHub Actions Python 3.12 / 3.13 + ruff.",
        "Principe directeur : ce que le moteur ne sait pas lire reste <strong>vide avec son motif</strong> — jamais zéro, jamais deviné.",
    ],
    custom_sections=[
        ("mon-role", "Mon rôle", "Business Analyst et suivi du projet",
         '<div class="two-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Analyse métier</span><ul>'
         "<li><strong>Recueil des besoins</strong> auprès des acheteurs et de la direction Achats ; cartographie du processus actuel et cible.</li>"
         "<li><strong>24 règles de gestion</strong> formalisées (RG-xx), avec leurs cas limites, puis une revue critique complète des règles.</li>"
         "<li><strong>Cahier des charges</strong> versionné (v3) et <strong>traçabilité des exigences</strong> jusqu'aux tests.</li>"
         "<li><strong>Business case</strong> : 6 leviers chiffrés en 3 scénarios, conditions d'échec explicites.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Suivi du projet</span><ul>'
         "<li><strong>Backlog de 105 éléments</strong> décrits assez précisément pour être chiffrés, priorisés avec le référent métier.</li>"
         "<li><strong>Décisions datées</strong> et tracées (périmètre gelé, arbitrages, choix d'architecture).</li>"
         "<li><strong>Contrôles réguliers</strong> de l'avancement et revues de code datées : ce qui est réellement livré, pas ce qui est annoncé.</li>"
         "<li><strong>Recette</strong> sur fichiers réels rejoués, rapport remis à l'acheteur pour validation ; jalons go / no-go.</li>"
         "<li><strong>Pilotage de lots délégués</strong> : chaque lot a sa demande écrite, ses critères d'acceptation et sa grille de contrôle.</li></ul></div></div>"),
        ("parties-prenantes", "Parties prenantes", "Qui a besoin de quoi",
         '<div class="table-wrap"><table class="stack-table"><thead><tr><th>Acteur</th><th>Besoin</th><th>Réponse apportée</th></tr></thead>'
         f"<tbody>{stake_rows}</tbody></table></div>"),
        ("processus", "Processus as-is / to-be", "Du fichier fournisseur au mémo de négociation",
         '<div class="two-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Aujourd\'hui (as-is)</span><ul>'
         "<li>Mise au format et rapprochement des références à la main : 1 à 2 jours.</li>"
         "<li>Comparaison N-1 / N et chiffrage de l'impact : 0,5 à 1 jour.</li>"
         "<li>Arguments et mémo : 0,5 jour.</li>"
         "<li>Vérification de l'application du prix dans l'ERP : rarement faite.</li>"
         "<li>Négociation sur la hausse moyenne annoncée par le fournisseur.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Cible (to-be)</span><ul>'
         "<li>Dépôt du fichier tel quel ; gabarit reconnu et mémorisé : 30 min.</li>"
         "<li>Rattachement automatique, l'acheteur n'arbitre que les cas douteux.</li>"
         "<li>Hausse pondérée par les volumes, impact annualisé, Pareto : automatique.</li>"
         "<li>Mémo d'une page et support Excel produits : 15 min.</li>"
         "<li>Écarts d'application ERP détectés et chiffrés chaque mois.</li></ul></div></div>"
         '<p style="margin-top:1.5rem">Exemple sur la démonstration (données fictives) : un tarif annoncé à <strong>+4,80 %</strong> '
         "ne pèse que <strong>+2,08 %</strong> une fois pondéré par les volumes et la grille de remise — et l'impact tient dans quelques références.</p>"),
        ("business-case", "Business case", "Six leviers de gain, chiffrés et bornés",
         '<div class="table-wrap"><table class="stack-table"><thead><tr><th>#</th><th>Levier</th><th>Ordre de grandeur</th><th>Ce qui le rend crédible</th></tr></thead>'
         f"<tbody>{lever_rows}</tbody></table></div>"
         '<div class="kpi-row" style="margin-top:1.5rem">'
         '<div class="kpi"><b>0,47 %</b><span>scénario bas</span></div>'
         '<div class="kpi"><b>1,15 %</b><span>scénario central</span></div>'
         '<div class="kpi"><b>2,29 %</b><span>scénario haut</span></div>'
         '<div class="kpi"><b>T1</b><span>retour sur investissement</span></div></div>'
         "<p>Gains exprimés en part de la dépense suivie. Ils séparent toujours le <strong>mesuré</strong> (sur la démonstration) de "
         "l'<strong>estimé</strong> (hypothèses à confirmer sur les données réelles), et la méthode pour remplacer les estimations par les "
         "vrais chiffres dès la première campagne est documentée.</p>"
         '<p>Condition de tous les autres gains : <strong>lire les prix sans erreur</strong>. Le rejeu d\'un corpus de tarifs a révélé dix erreurs '
         "de lecture silencieuses (une base « prix pour 1000 » ignorée = prix mille fois trop bas ; une date américaine = trois mois d'écart). "
         "Chacune a aujourd'hui son test de non-régression.</p>"),
        ("risques", "Risques & conditions de succès", "Ce qui rendrait ces chiffres faux",
         '<div class="two-col">'
         '<div class="arg-card arg-card--rh"><span class="arg-label">Conditions d\'échec identifiées</span><ul>'
         "<li><strong>Volumes ERP non fiables</strong> : la pondération s'effondre (l'outil refuse alors de chiffrer).</li>"
         "<li><strong>Référentiel non rattaché</strong> : pas de comparaison possible — premier chantier, en temps d'acheteur.</li>"
         "<li><strong>Rapport de force défavorable</strong> : l'outil donne l'argument, pas le pouvoir.</li>"
         "<li><strong>Alertes non traitées</strong> : un écart détecté et jamais corrigé ne rapporte rien.</li></ul></div>"
         '<div class="arg-card arg-card--ok"><span class="arg-label">Plan de déploiement (6 mois, 8 lots)</span><ul>'
         "<li>L0 cadrage et accès → L1 raccordement ERP → L2 reprise du référentiel → L3 recette sur données réelles.</li>"
         "<li>L4 interface et habilitations → L5 économies et négociation → L6 industrialisation → L7 déploiement et formation.</li>"
         "<li>Jalons go / no-go : une entité raccordée (M2), un fournisseur de bout en bout validé par l'acheteur (M3).</li>"
         "<li>Périmètre fonctionnel gelé, documentation livrée avec chaque lot.</li></ul></div></div>"),
    ],
    stages=[
        ("Sources", "source", ["Tarifs fournisseurs (xlsx, csv, pdf)", "ERP des entités", "Taux de change BCE"]),
        ("Ingestion", "ingest", ["Gabarit + clé unique", "Compte rendu préalable"]),
        ("Normalisation", "process", ["Devises, unités", "Masques de référence"]),
        ("Rattachement", "ml", ["Cascade L0 → L2", "Arbitrage humain (L3)"]),
        ("Analyse", "process", ["Hausse pondérée volumes", "Prix spéciaux, écarts ERP"]),
        ("Entrepôt", "storage", ["DuckDB + journal"]),
        ("Restitution", "ui", ["Interface R/Shiny", "Mémo + dossier Excel", "Scorecards + Board"]),
    ],
    edges=[("s0n0", "s1n0", "", False), ("s0n1", "s1n0", "", False), ("s1n0", "s1n1", "", False),
           ("s1n1", "s2n0", "", False), ("s2n0", "s2n1", "", False), ("s2n1", "s3n0", "", False),
           ("s3n0", "s3n1", "doute", True), ("s3n0", "s4n0", "", False), ("s3n1", "s4n0", "", False),
           ("s4n0", "s4n1", "", False), ("s4n1", "s5n0", "", False), ("s5n0", "s6n0", "lecture seule", False),
           ("s6n0", "s6n1", "", False), ("s6n1", "s6n2", "", False)],
    band=("Configuration YAML par fournisseur · pytest (≈ 2 500) · testthat (445) · GitHub Actions · ERP en lecture seule", "infra"),
    steps=[
        "<strong>Déposer</strong> — le fichier est reçu tel quel, empreinté et archivé ; un doublon est refusé.",
        "<strong>Comprendre</strong> — gabarit reconnu, clé unique détectée, compte rendu de lecture présenté avant tout calcul.",
        "<strong>Rattacher</strong> — chaque référence fournisseur est reliée à l'article ERP par la cascade ; l'acheteur n'arbitre que les doutes, une seule fois.",
        "<strong>Analyser</strong> — hausse pondérée, impact annualisé, Pareto, remises, plafonds de prix spéciaux, écarts d'application ERP ; les aberrants partent en quarantaine.",
        "<strong>Négocier</strong> — mémo d'une page, support Excel et demande de reprise ; chaque chiffre renvoie à sa source.",
    ],
    extra_diagrams=[("achats-parcours", "Parcours d'un tarif — et ce que l'outil refuse de faire"),
                    ("achats-cascade", "Cascade de rattachement aux références ERP"),
                    ("achats-architecture", "Architecture et flux de données")],
    langs=[("Python", 78), ("R", 18), ("YAML", 3), ("JavaScript", 1)],
    tags=["Business Analysis", "Achats", "Business case", "Règles de gestion", "Cahier des charges", "Python", "DuckDB",
          "R / Shiny", "rapidfuzz", "pandas", "YAML", "pytest", "GitHub Actions"],
    stack=[
        ("Analyse métier", "Règles de gestion, cas limites, revue critique des règles (défauts critiques, lacunes)", "Formaliser ce que l'acheteur fait implicitement"),
        ("Business case", "6 leviers chiffrés en 3 scénarios, conditions d'échec", "Décision d'investissement argumentée"),
        ("Cahier des charges + backlog", "Exigences tracées, lots chiffrables, jalons go / no-go", "Pilotage de projet"),
        ("Python + pandas", "Moteur de lecture, normalisation et analyse", "Industrialiser des règles métier"),
        ("rapidfuzz", "Rapprochement approché des références", "Matching robuste avec garde-fous"),
        ("DuckDB", "Entrepôt analytique en fichier, vues sous contrat", "Analytique embarquée sans serveur"),
        ("R / Shiny", "Poste de travail acheteur, 5 profils", "Interface métier"),
        ("YAML", "Un fichier de configuration par fournisseur", "Évolutivité sans développement"),
        ("pytest · testthat · GitHub Actions", "≈ 2 500 tests Python + 445 tests R, CI multi-versions", "Fiabilité des chiffres"),
    ],
    matrix=dict(ci="y", tests="y", docker="p", orch="p", tracking="n", monitoring="p", serving="y", deploy="p", iac="n"),
    matrix_notes=dict(ci="Python 3.12 / 3.13, ruff ; R testthat", tests="≈ 2 500 tests Python + 445 tests R",
                      docker="Déploiement conteneurisé multi-utilisateurs planifié", orch="Campagnes planifiables, rejouables",
                      monitoring="Journal de toutes les opérations, registre des injections", serving="Interface R/Shiny",
                      deploy="Démonstration complète rejouable ; mise en service par lots"),
    snippets=[
        ("tarifs/rattachement.py — niveau L3 de la cascade : rapprochement approché motivé",
         '''# L3 — rapprochement approché (RG-07). `score_cutoff` : rapidfuzz abandonne tôt les candidats
# sous le seuil de présentation ; même résultat que le filtre a posteriori, bien moins de travail.
choix = process.extract(refnorm, idx["cles"], scorer=fuzz.ratio, limit=int(s["nb_candidats"]) + 1,
                        score_cutoff=float(s.get("seuil_candidat_min", 0)))
cands = [{"reference_erp": par_norm[c], "score": round(sc, 1),
          "rapproche": f"similarité {sc:.0f} % sur la référence normalisée",
          "separe": f"{refnorm} ≠ {c}"} for c, sc, _ in choix if sc >= s.get("seuil_candidat_min", 0)]'''),
    ],
    limits=[
        "Déploiement conteneurisé multi-utilisateurs et connexion à l'annuaire d'entreprise encore au backlog.",
        "Un seul profil sectoriel riche (industriel) en plus du profil générique ; interface en français.",
        "Gains estimés tant que la première campagne sur données réelles n'a pas eu lieu — la méthode de mesure est prête.",
        "Revue critique des règles métier menée : défauts critiques identifiés (paliers, remises, encodages) et corrigés un par un, avec test dédié.",
    ],
)
