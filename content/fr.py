"""Contenu français de Atelier Nordfeld.

Règle : aucun fait inventé. Seuls les faits fournis par Erol Zor sont utilisés
(3 ans d'activité, plus de 100 clients, 7 métiers, adresse, téléphone).
Les articles du blog sont des conseils métier à la première personne, à valider
par Erol Zor avant publication définitive.
"""

LANG = "fr"
HTML_LANG = "fr"
OG_LOCALE = "fr_FR"
HREFLANG = "fr"

UI = {
    "skip": "Aller au contenu",
    "call": "Appeler",
    "call_long": "Appeler le 07 58 67 94 66",
    "quote": "Demander un devis",
    "menu": "Menu",
    "trades": "Nos métiers",
    "see_trade": "Découvrir ce métier",
    "read_more": "Lire l'article",
    "all_articles": "Tous les articles",
    "language": "Langue",
    "breadcrumb_home": "Accueil",
    "founder_role": "Fondateur de Atelier Nordfeld",
    "by": "Par",
    "updated": "Publié le",
    "min_read": "min de lecture",
    "related_trade": "Le métier concerné",
    "other_trades": "Nos autres métiers",
    "faq": "Questions fréquentes",
    "services_list": "Nos prestations",
    "process_title": "Comment se passe un chantier",
    "contact_title": "Parlons de votre projet",
    "footer_about": "Rénovation et artisanat du bâtiment à Mulhouse : menuiserie, peinture, carrelage, terrasse bois, revêtements de sol, aménagement intérieur et électricité.",
    "footer_nav": "Navigation",
    "footer_contact": "Contact",
    "footer_legal": "Informations légales",
    "rights": "Tous droits réservés.",
    "pole": "Pôle rénovation",
    "illustration": "Illustration générée par IA, non contractuelle.",
    "form": {
        "name": "Nom et prénom",
        "phone": "Téléphone",
        "email": "E-mail",
        "city": "Commune du chantier",
        "trade": "Type de travaux",
        "trade_other": "Autre / plusieurs métiers",
        "message": "Décrivez votre projet",
        "message_ph": "Surface approximative, état actuel, délais souhaités…",
        "consent": "J'accepte que mes données soient utilisées pour répondre à ma demande (voir la politique de confidentialité).",
        "send": "Envoyer ma demande",
        "required": "Ce champ est obligatoire.",
        "invalid_email": "Adresse e-mail invalide.",
        "invalid_phone": "Numéro de téléphone invalide.",
        "success": "Merci, votre demande est bien partie. Nous vous répondons rapidement.",
        "unavailable": "Le formulaire en ligne n'est pas encore activé. Appelez-nous au 07 58 67 94 66, nous vous répondons directement.",
        "error": "L'envoi a échoué. Appelez-nous au 07 58 67 94 66.",
    },
}

NAV = {"home": "Accueil", "blog": "Blog", "about": "À propos", "contact": "Contact"}

# slug de chaque page (relatif à /fr/)
SLUGS = {
    "home": "",
    "blog": "blog",
    "about": "a-propos",
    "contact": "contact",
    "legal": "mentions-legales",
    "privacy": "confidentialite",
}

PAGES = {
    "home": {
        "title": "Atelier Nordfeld | Rénovation et artisans du bâtiment à Mulhouse",
        "desc": "Menuiserie, peinture, carrelage, terrasse bois, sols, aménagement intérieur et électricité à Mulhouse. Un seul interlocuteur pour vos travaux. Appelez le 07 58 67 94 66.",
    },
    "blog": {
        "title": "Blog rénovation à Mulhouse : conseils et retours de chantier | Atelier Nordfeld",
        "desc": "Les conseils d'Erol Zor, artisan à Mulhouse : terrasse bois, peinture, carrelage, électricité, revêtements de sol. Guides pratiques avant de lancer vos travaux.",
        "h1": "Blog : conseils d'artisan et retours de chantier",
        "intro": "Je m'appelle Erol Zor et je dirige Atelier Nordfeld à Mulhouse. Ici, je partage ce que j'explique à mes clients avant un chantier : comment choisir un matériau, quelles erreurs éviter, par où commencer.",
        "notice_title": "Études de cas à venir",
        "notice": "Chaque chantier réalisé sera publié ici avec ses vraies photos, après accord du client. En attendant, voici les guides que j'aurais aimé avoir lus avant mes premiers chantiers.",
    },
    "about": {
        "title": "À propos de Atelier Nordfeld | Erol Zor, artisan à Mulhouse",
        "desc": "Atelier Nordfeld, entreprise de rénovation fondée par Erol Zor à Mulhouse. Trois ans d'activité, plus de 100 clients accompagnés, sept métiers du bâtiment.",
        "h1": "Atelier Nordfeld, une entreprise de rénovation née à Mulhouse",
        "paras": [
            "Atelier Nordfeld est une entreprise de rénovation installée au 70 rue du Nordfeld, à Mulhouse. Elle a été fondée par Erol Zor, artisan du bâtiment, avec une idée simple : un propriétaire ne devrait pas avoir à coordonner sept corps de métier pour refaire son logement.",
            "En trois ans d'activité, plus de cent clients nous ont confié leurs travaux : une pièce à repeindre, une salle de bains à carreler, une terrasse à construire, une installation électrique à remettre aux normes ou un aménagement sur mesure.",
            "Nous intervenons sur la menuiserie, la peinture, le carrelage, la terrasse bois, les revêtements de sol, l'aménagement intérieur et l'électricité. Un seul interlocuteur suit votre projet, du premier appel à la réception du chantier.",
        ],
        "values_title": "Ce qui guide notre travail",
        "values": [
            ("Un interlocuteur, un chantier", "Vous parlez à la même personne du devis jusqu'à la remise des clés. Pas de relais, pas de zones d'ombre."),
            ("Des devis lisibles", "Chaque poste est détaillé : matériaux, main-d'œuvre, délais. Vous savez ce que vous achetez avant de signer."),
            ("Le détail qui tient dans le temps", "Préparation des supports, respect des temps de séchage, pose soignée : ce que l'on ne voit pas fait la durée de vie d'un chantier."),
        ],
        "founder_title": "Le fondateur",
        "founder_text": "Erol Zor a créé Atelier Nordfeld pour proposer aux particuliers de Mulhouse et des environs un artisanat sérieux, sans intermédiaire. Il suit lui-même les projets et reste votre point de contact.",
    },
    "contact": {
        "title": "Contact et devis travaux à Mulhouse | Atelier Nordfeld",
        "desc": "Contactez Atelier Nordfeld pour votre devis de rénovation à Mulhouse : 07 58 67 94 66, 70 rue du Nordfeld, 68100 Mulhouse. Réponse rapide.",
        "h1": "Contact et demande de devis",
        "intro": "Décrivez-nous votre projet ou appelez directement. Plus vous nous donnez de détails (surface, état actuel, délais), plus notre réponse sera précise.",
        "address_label": "Adresse",
        "phone_label": "Téléphone",
        "map": "Voir l'itinéraire sur OpenStreetMap",
    },
    "legal": {
        "title": "Mentions légales | Atelier Nordfeld",
        "desc": "Mentions légales du site Atelier Nordfeld, entreprise de rénovation à Mulhouse.",
        "h1": "Mentions légales",
    },
    "privacy": {
        "title": "Politique de confidentialité | Atelier Nordfeld",
        "desc": "Comment Atelier Nordfeld traite les données personnelles collectées via le formulaire de contact.",
        "h1": "Politique de confidentialité",
    },
}

HOME = {
    "kicker": "Rénovation à Mulhouse",
    "h1": "Votre rénovation à Mulhouse, de la menuiserie à l'électricité",
    "lead": "Atelier Nordfeld réunit sept métiers du bâtiment sous un seul interlocuteur. Vous décrivez votre projet, nous nous occupons du reste.",
    "cta2": "Voir nos métiers",
    "stats": [("3 ans", "d'activité à Mulhouse"), ("100+", "clients accompagnés"), ("7", "métiers du bâtiment"), ("1", "interlocuteur du devis à la réception")],
    "trades_kicker": "Nos métiers",
    "trades_h2": "Sept métiers pour un seul projet",
    "trades_text": "Chaque métier a sa page dédiée. Vous pouvez nous confier un seul lot ou l'ensemble de vos travaux.",
    "why_kicker": "Pourquoi Atelier Nordfeld",
    "why_h2": "Rénover sans courir après cinq entreprises",
    "why": [
        ("Un seul interlocuteur", "Menuisier, peintre, carreleur, électricien : vous n'avez pas à les coordonner. Nous planifions les interventions dans le bon ordre."),
        ("Un devis détaillé", "Vous recevez un devis poste par poste, avec les matériaux et les délais. Pas de surprise en cours de route."),
        ("Une finition soignée", "Supports préparés, joints propres, lignes droites : nous soignons ce qui se voit comme ce qui ne se voit pas."),
    ],
    "area_kicker": "Zone d'intervention",
    "area_h2": "Mulhouse et son agglomération",
    "area_text": "Notre atelier est situé à Mulhouse, dans le quartier du Nordfeld. Nous intervenons à Mulhouse et dans les communes voisines.",
    "founder_kicker": "Le mot du fondateur",
    "founder_quote": "Mon rôle, c'est que vous n'ayez pas à vous demander si le chantier avance. Vous savez ce qui est fait, ce qui reste à faire et quand.",
    "blog_kicker": "Blog",
    "blog_h2": "Derniers conseils d'artisan",
    "final_h2": "Un projet de rénovation à Mulhouse ?",
    "final_text": "Appelez-nous ou décrivez votre projet en deux minutes. Nous vous répondons rapidement.",
}

AREAS = ["Mulhouse", "Rixheim", "Riedisheim", "Illzach", "Kingersheim", "Wittenheim", "Pfastatt", "Brunstatt-Didenheim", "Lutterbach", "Sausheim"]

PROCESS = [
    ("Premier contact", "Vous nous appelez ou remplissez le formulaire. Nous cernons votre besoin et fixons un rendez-vous sur place si nécessaire."),
    ("Devis détaillé", "Nous chiffrons chaque poste et proposons un calendrier réaliste. Vous validez, ou nous ajustons ensemble."),
    ("Réalisation", "Le chantier est mené poste par poste, avec un point clair sur l'avancement et sur ce qui vient ensuite."),
    ("Réception", "Nous passons ensemble en revue les travaux. Rien n'est terminé tant que vous n'êtes pas satisfait."),
]

TRADES = [
    {
        "key": "menuiserie",
        "slug": "menuiserie",
        "name": "Menuiserie",
        "short": "Portes, fenêtres, placards, escaliers et ouvrages sur mesure en bois.",
        "title": "Menuiserie à Mulhouse : sur mesure, pose et rénovation | Atelier Nordfeld",
        "desc": "Menuisier à Mulhouse : portes, fenêtres, placards, escaliers et ouvrages sur mesure. Devis détaillé, un seul interlocuteur. Appelez le 07 58 67 94 66.",
        "h1": "Menuiserie à Mulhouse",
        "intro": "De la porte d'entrée au placard sous pente, la menuiserie est ce qui donne à un logement sa fonction et son caractère. Atelier Nordfeld réalise la pose, la rénovation et la fabrication d'ouvrages sur mesure à Mulhouse et aux alentours.",
        "items": [
            "Pose et remplacement de portes intérieures et de portes d'entrée",
            "Pose de fenêtres et de volets, remplacement de menuiseries existantes",
            "Placards et rangements sur mesure, y compris sous combles",
            "Escaliers : rénovation de marches, garde-corps, rampes",
            "Plinthes, habillages, moulures et finitions",
            "Petites réparations : portes qui frottent, quincaillerie, ajustements",
        ],
        "faq": [
            ("Faut-il changer toutes les fenêtres en même temps ?", "Pas obligatoirement. On peut procéder pièce par pièce, mais remplacer l'ensemble d'une façade en une fois donne un résultat plus homogène et simplifie la gestion du chantier. Nous vous conseillons selon l'état de vos menuiseries."),
            ("Un placard sur mesure, est-ce vraiment plus intéressant qu'un meuble du commerce ?", "Dans une pièce aux dimensions atypiques (sous pente, alcôve, mur en biais), oui : un ouvrage sur mesure exploite chaque centimètre. Sur un mur droit standard, un meuble du commerce peut suffire."),
            ("Combien de temps dure la pose d'une porte intérieure ?", "En général, quelques heures par porte lorsque le dormant est sain. Le délai s'allonge si le cadre doit être refait ou si les murs sont à reprendre."),
        ],
        "article": "terrasse-bois-pin-ipe-composite",
    },
    {
        "key": "peinture",
        "slug": "peinture",
        "name": "Peinture",
        "short": "Peinture intérieure et extérieure, préparation des supports, finitions.",
        "title": "Peintre à Mulhouse : peinture intérieure et extérieure | Atelier Nordfeld",
        "desc": "Peinture intérieure et extérieure à Mulhouse : préparation des murs, enduits, finitions soignées. Devis détaillé. Appelez Atelier Nordfeld au 07 58 67 94 66.",
        "h1": "Peinture à Mulhouse",
        "intro": "Une belle peinture se joue avant la première couche : un support bien préparé change tout. Atelier Nordfeld réalise vos travaux de peinture intérieure et extérieure à Mulhouse, avec une préparation sérieuse et des finitions propres.",
        "items": [
            "Peinture de murs et de plafonds, pièce par pièce ou logement complet",
            "Préparation des supports : rebouchage, ponçage, enduit, sous-couche",
            "Peinture de boiseries, portes, plinthes et radiateurs",
            "Pose d'enduits décoratifs et de revêtements muraux",
            "Peinture extérieure : volets, portails, façades",
            "Protection du mobilier et des sols, nettoyage en fin de chantier",
        ],
        "faq": [
            ("Faut-il toujours poser une sous-couche ?", "Sur un support neuf, très absorbant ou taché, oui. Sur une ancienne peinture saine et propre, une sous-couche n'est pas toujours nécessaire, mais elle améliore souvent la couvrance et la tenue. Nous jugeons au cas par cas."),
            ("Combien de temps avant de remeubler une pièce peinte ?", "Une peinture est sèche au toucher en quelques heures, mais elle met plusieurs jours à durcir complètement. Il vaut mieux attendre avant de plaquer des meubles contre les murs. Les fabricants indiquent des délais sur leurs pots."),
            ("Peut-on peindre par-dessus du papier peint ?", "C'est possible dans certains cas, mais le résultat est rarement durable. Nous recommandons de déposer le papier peint puis de préparer le mur."),
        ],
        "article": "preparer-murs-avant-peinture",
    },
    {
        "key": "carrelage",
        "slug": "carrelage",
        "name": "Carrelage",
        "short": "Pose de carrelage, faïence, grands formats, salles de bains et cuisines.",
        "title": "Carreleur à Mulhouse : pose de carrelage et faïence | Atelier Nordfeld",
        "desc": "Pose de carrelage et de faïence à Mulhouse : salle de bains, cuisine, sols, grands formats. Préparation soignée, devis détaillé. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Carrelage à Mulhouse",
        "intro": "Un carrelage bien posé dure des décennies, mal posé il se voit tout de suite. Atelier Nordfeld réalise la pose de carrelage et de faïence à Mulhouse : sols, murs, salles de bains, cuisines, entrées et terrasses.",
        "items": [
            "Carrelage de sol et faïence murale, intérieur et extérieur",
            "Pose de grands formats avec calepinage et planéité contrôlée",
            "Salles de bains : douches à l'italienne, étanchéité, receveurs extra-plats",
            "Cuisines : crédences et sols",
            "Ragréage et préparation des supports avant pose",
            "Joints, silicone et finitions de pourtour",
        ],
        "faq": [
            ("Peut-on poser un nouveau carrelage sur l'ancien ?", "C'est parfois possible si l'ancien carrelage est sain, bien adhérent et plan, mais cela ajoute une épaisseur et pose des questions de hauteur de portes. Nous vérifions l'état du support avant de décider."),
            ("Pourquoi le ragréage est-il si important ?", "Le carrelage ne rattrape pas les défauts du sol. Un support irrégulier donne des lames de joints inégales et peut provoquer des fissures, surtout en grand format."),
            ("Quelle différence entre faïence et carrelage ?", "La faïence désigne en général le revêtement mural, plus fin, tandis que le carrelage de sol est conçu pour résister à la marche et à l'usure. Certains carreaux conviennent aux deux usages."),
        ],
        "article": "carrelage-grand-format-erreurs-pose",
    },
    {
        "key": "terrasse-bois",
        "slug": "terrasse-bois",
        "name": "Terrasse bois",
        "short": "Construction de terrasses en bois et composite, sur plots ou lambourdes.",
        "title": "Terrasse bois à Mulhouse : pose et construction | Atelier Nordfeld",
        "desc": "Construction de terrasse bois à Mulhouse : pin, douglas, ipé, composite. Structure ventilée, pose soignée. Devis détaillé, Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Terrasse bois à Mulhouse",
        "intro": "Une terrasse bois est un ouvrage extérieur exposé à la pluie, au gel et au soleil. Sa durée de vie dépend de la structure, de la ventilation et de l'essence choisie. Atelier Nordfeld construit des terrasses bois et composite à Mulhouse et dans les communes voisines.",
        "items": [
            "Terrasses sur plots réglables ou sur lambourdes",
            "Choix de l'essence : pin traité, douglas, mélèze, bois exotique, composite",
            "Structure ventilée et gestion de l'écoulement de l'eau",
            "Escaliers, marches et bordures de terrasse",
            "Garde-corps et finitions",
            "Entretien et remise en état de terrasses existantes",
        ],
        "faq": [
            ("Quelle essence choisir pour une terrasse ?", "Cela dépend du budget, de l'exposition et de l'entretien que vous acceptez. Le pin traité est économique, le douglas et le mélèze offrent une bonne résistance naturelle, les bois exotiques durent longtemps, le composite demande très peu d'entretien. Notre article détaille ces choix."),
            ("Faut-il une autorisation pour construire une terrasse ?", "Cela dépend de sa hauteur, de sa surface et de votre commune. Une terrasse de plain-pied de petite surface est souvent dispensée de formalités, mais il faut vérifier auprès de la mairie ou du plan local d'urbanisme."),
            ("Pourquoi la ventilation sous la terrasse est-elle essentielle ?", "L'humidité stagnante est le premier ennemi du bois. Une structure ventilée et des lames espacées permettent à l'eau de s'évacuer et au bois de sécher."),
        ],
        "article": "terrasse-bois-pin-ipe-composite",
    },
    {
        "key": "revetement-sol",
        "slug": "revetement-de-sol",
        "name": "Revêtement de sol",
        "short": "Parquet, stratifié, vinyle, sol souple : pose et rénovation.",
        "title": "Revêtement de sol à Mulhouse : parquet, stratifié, vinyle | Atelier Nordfeld",
        "desc": "Pose de parquet, stratifié, vinyle et sols souples à Mulhouse. Préparation du support, finitions propres. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Revêtement de sol à Mulhouse",
        "intro": "Le sol occupe la plus grande surface visible d'une pièce, et c'est lui qui encaisse le plus d'usure. Atelier Nordfeld pose et rénove parquet, stratifié, vinyle et sols souples à Mulhouse, avec une préparation rigoureuse du support.",
        "items": [
            "Pose de parquet massif, contrecollé et stratifié",
            "Sols vinyle et PVC : lames clipsables ou collées",
            "Sols souples en rouleau pour pièces humides",
            "Ragréage et mise à niveau du support",
            "Dépose de l'ancien revêtement",
            "Plinthes, barres de seuil et finitions",
        ],
        "faq": [
            ("Stratifié, vinyle ou parquet : lequel choisir ?", "Le stratifié est économique mais craint l'eau. Le vinyle est le plus tolérant à l'humidité. Le parquet est le plus noble et peut se rénover, mais il demande plus de soin. Notre article compare les trois."),
            ("Peut-on poser un sol sur un plancher chauffant ?", "Oui avec un revêtement compatible. Il faut vérifier la résistance thermique du produit et respecter la mise en chauffe progressive prévue par le fabricant."),
            ("Faut-il laisser reposer les lames avant la pose ?", "C'est recommandé pour le parquet et le stratifié : les lames s'acclimatent à la température et à l'humidité de la pièce, ce qui limite les mouvements après la pose."),
        ],
        "article": "stratifie-vinyle-parquet-choisir-son-sol",
    },
    {
        "key": "amenagement-interieur",
        "slug": "amenagement-interieur",
        "name": "Aménagement intérieur",
        "short": "Cloisons, faux plafonds, rangements, redistribution des pièces.",
        "title": "Aménagement intérieur à Mulhouse : cloisons, plafonds | Atelier Nordfeld",
        "desc": "Aménagement intérieur à Mulhouse : cloisons, faux plafonds, rangements, redistribution de pièces. Un seul interlocuteur. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Aménagement intérieur à Mulhouse",
        "intro": "Redistribuer un logement, créer une chambre, isoler un plafond ou ouvrir une cuisine : l'aménagement intérieur demande de coordonner plusieurs métiers. Atelier Nordfeld pilote l'ensemble à Mulhouse et dans les environs.",
        "items": [
            "Cloisons et redistribution des pièces",
            "Faux plafonds et habillages de plafond",
            "Doublages et isolation intérieure des murs",
            "Rangements, dressings et niches sur mesure",
            "Aménagement de combles et de sous-sols",
            "Coordination des finitions : peinture, sols, électricité",
        ],
        "faq": [
            ("Peut-on supprimer une cloison sans risque ?", "Seulement si elle n'est pas porteuse. Une cloison porteuse demande une étude et un renfort structurel. Nous identifions la nature du mur avant toute démolition."),
            ("L'aménagement intérieur est-il soumis à autorisation ?", "Les travaux strictement intérieurs sont souvent libres, mais ils peuvent dépendre du règlement de copropriété ou d'un changement de surface habitable. Renseignez-vous auprès de la mairie ou du syndic."),
            ("Combien de temps pour aménager des combles ?", "Cela varie fortement selon la surface, l'isolation et l'accès. Nous donnons un calendrier précis après visite."),
        ],
        "article": "preparer-murs-avant-peinture",
    },
    {
        "key": "electricite",
        "slug": "electricite",
        "name": "Électricité",
        "short": "Installation, mise aux normes, tableau électrique, éclairage, prises.",
        "title": "Électricien à Mulhouse : installation et mise aux normes | Atelier Nordfeld",
        "desc": "Électricité à Mulhouse : installation neuve, mise aux normes, tableau électrique, éclairage et prises. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Électricité à Mulhouse",
        "intro": "Une installation électrique doit d'abord être sûre, ensuite pratique. Atelier Nordfeld réalise vos installations neuves et rénovations électriques à Mulhouse, en respectant la norme française en vigueur.",
        "items": [
            "Rénovation complète ou partielle d'installations anciennes",
            "Remplacement et mise aux normes du tableau électrique",
            "Création de circuits : prises, éclairage, plaques de cuisson",
            "Éclairage intérieur et extérieur, spots encastrés",
            "Prises réseau, antenne, interphone",
            "Remise en état après diagnostic",
        ],
        "faq": [
            ("Mon installation date de plus de 30 ans, faut-il tout refaire ?", "Pas forcément. Un diagnostic permet de savoir ce qui est conforme, ce qui est dangereux et ce qui peut rester. Nous proposons une remise à niveau adaptée à l'état réel."),
            ("Qu'est-ce que la norme NF C 15-100 ?", "C'est la norme qui encadre les installations électriques des logements en France : nombre de prises par pièce, protections, sections de câbles, dispositifs différentiels. Elle vise la sécurité des personnes et des biens."),
            ("Faut-il couper le courant pour changer une prise ?", "Toujours. Coupez le disjoncteur correspondant et vérifiez l'absence de tension avant d'intervenir. En cas de doute, faites appel à un professionnel."),
        ],
        "article": "renovation-electrique-logement-ancien",
    },
]

ARTICLES = [
    {
        "key": "terrasse-bois-pin-ipe-composite",
        "slug": "terrasse-bois-pin-ipe-composite",
        "trade": "terrasse-bois",
        "title": "Terrasse bois : pin, douglas, ipé ou composite, comment choisir ?",
        "desc": "Pin traité, douglas, ipé ou composite : durée de vie, entretien, budget. Le guide d'Erol Zor, artisan à Mulhouse, pour choisir sa terrasse.",
        "date": "2026-10-17",
        "read": 6,
        "intro": "Quand un client me demande une terrasse, la première question est toujours la même : quelle essence ? Il n'y a pas de bonne réponse universelle, seulement la bonne réponse pour votre budget, votre exposition et votre tolérance à l'entretien. Voici comment je raisonne.",
        "sections": [
            ("Le pin traité : le plus accessible", [
                "Le pin traité en classe 4 est le choix économique. Il convient bien aux terrasses de taille modeste et aux budgets serrés. En contrepartie, il demande un entretien régulier (saturateur, nettoyage) et peut se fendiller ou se déformer avec le temps.",
                "C'est un bon point d'entrée à condition d'accepter de s'en occuper chaque année ou tous les deux ans.",
            ]),
            ("Douglas et mélèze : le compromis", [
                "Ces résineux sont naturellement plus durables que le pin standard, sans traitement chimique lourd. Ils grisent avec le temps si on les laisse faire, ce que beaucoup de clients apprécient, ou se conservent avec un saturateur.",
                "Pour une terrasse familiale à Mulhouse, soumise au gel et à l'humidité de nos hivers, c'est souvent l'option que je conseille en premier.",
            ]),
            ("Les bois exotiques : la durée", [
                "L'ipé et d'autres bois exotiques sont très denses et très résistants. Ils durent longtemps, mais ils sont chers, lourds, difficiles à percer et leur provenance doit être vérifiée (certification de gestion durable).",
            ]),
            ("Le composite : le moins d'entretien", [
                "Le composite mélange fibres de bois et polymère. Il ne demande ni saturateur ni ponçage, résiste bien à l'humidité et reste stable. Il chauffe davantage au soleil et son aspect, très uniforme, ne plaît pas à tout le monde.",
                "Je le recommande aux clients qui veulent une terrasse sans corvée d'entretien.",
            ]),
            ("Ce qui compte plus que l'essence : la structure", [
                "Une terrasse pourrit rarement par le haut, elle pourrit par le bas. L'essentiel est une structure ventilée : lambourdes ou plots réglables posés sur un support stable, vide d'air sous les lames, lames légèrement espacées pour évacuer l'eau, légère pente pour que l'eau ne stagne pas.",
                "Une terrasse en bois noble posée sans ventilation vieillira plus mal qu'une terrasse en pin bien construite.",
            ]),
        ],
        "outro": "Si vous hésitez, appelez-moi : je me déplace, je regarde l'exposition et le support, et je vous conseille selon votre situation.",
    },
    {
        "key": "preparer-murs-avant-peinture",
        "slug": "preparer-murs-avant-peinture",
        "trade": "peinture",
        "title": "Peinture : les 5 étapes de préparation que je ne saute jamais",
        "desc": "Rebouchage, ponçage, lessivage, sous-couche : les étapes de préparation d'un mur avant peinture selon Erol Zor, artisan à Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "On remarque une belle peinture quand elle est bien préparée, et on remarque une peinture ratée quand elle ne l'est pas. Les défauts apparaissent dès que la lumière rase le mur. Voici les cinq étapes que je respecte à chaque chantier.",
        "sections": [
            ("1. Protéger", [
                "Sols, plinthes, prises, mobilier : tout ce qui ne doit pas être peint est couvert ou déposé. C'est une étape qui paraît longue et qui évite des heures de nettoyage.",
            ]),
            ("2. Lessiver et dépoussiérer", [
                "Une peinture accroche mal sur un support gras ou poussiéreux. Les cuisines et les entrées demandent un vrai lessivage. Sur un support très abîmé, on retire d'abord ce qui ne tient pas : peinture écaillée, papier peint, enduit friable.",
            ]),
            ("3. Reboucher et enduire", [
                "Fissures, trous de chevilles, impacts : on les rebouche à l'enduit, puis on laisse sécher le temps indiqué par le fabricant. Sur un mur très irrégulier, un enduit de lissage donne une surface uniforme.",
            ]),
            ("4. Poncer", [
                "Le ponçage rend la surface lisse et fait disparaître les surépaisseurs d'enduit. Il se fait à sec, avec un dépoussiérage soigné ensuite, car la poussière marque la peinture.",
            ]),
            ("5. Appliquer la sous-couche", [
                "La sous-couche uniformise l'absorption du support. Sans elle, un mur rebouché peut « boire » la peinture par endroits et laisser des différences de teinte. Je l'applique systématiquement sur support neuf, taché ou fortement réparé.",
            ]),
            ("Les deux couches de finition", [
                "Deux couches fines valent mieux qu'une couche épaisse. On respecte le temps de séchage entre les deux, et on travaille « frais sur frais » sur les angles et les raccords pour éviter les traces.",
            ]),
        ],
        "outro": "Préparer demande du temps, et c'est justement ce temps qui fait la différence entre une peinture qui tient et une peinture à refaire.",
    },
    {
        "key": "carrelage-grand-format-erreurs-pose",
        "slug": "carrelage-grand-format-erreurs-pose",
        "trade": "carrelage",
        "title": "Carrelage grand format : les erreurs de pose à éviter",
        "desc": "Ragréage, double encollage, joints, calepinage : les erreurs fréquentes à la pose de carrelage grand format, expliquées par un artisan de Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Le grand format est très tendance : moins de joints, des pièces plus lumineuses, un rendu plus continu. Mais il ne pardonne rien. Voici les erreurs de pose qui reviennent le plus souvent et comment les éviter.",
        "sections": [
            ("Un support qui n'est pas plan", [
                "Sur un carreau de 60 x 120 cm, un creux de quelques millimètres devient un défaut visible, voire une cause de rupture. Le ragréage n'est pas une option : il faut un support plan, propre et sec.",
            ]),
            ("Pas assez de colle sous le carreau", [
                "Sur un grand format, on encolle le support et le dos du carreau (double encollage) avec une colle adaptée. Il ne doit pas rester de vide sous la plaque. Un carreau mal collé sonne creux et finit par fissurer.",
            ]),
            ("Pas de calepinage", [
                "Avant de coller le premier carreau, il faut savoir où tombent les coupes. On évite les petites coupes en bord de pièce et on place les joints de façon cohérente avec les ouvertures et les meubles.",
            ]),
            ("Des joints trop fins ou oubliés", [
                "Les joints absorbent les dilatations. Même en grand format dit « rectifié », il faut un joint, dont la largeur dépend des préconisations du fabricant. Au pourtour de la pièce et au changement de plan, on laisse un joint de fractionnement souple.",
            ]),
            ("L'étanchéité en pièce humide", [
                "Dans une douche à l'italienne, on ne carrelle pas directement sur le support. Un système d'étanchéité sous carrelage est indispensable, et les angles et traversées de tuyaux doivent être traités avec soin.",
            ]),
            ("Marcher dessus trop tôt", [
                "La colle a besoin de temps pour durcir. Marcher, jointoyer ou remeubler trop tôt fragilise la pose. On respecte les délais indiqués par le fabricant.",
            ]),
        ],
        "outro": "Un carrelage bien posé, c'est surtout 80 % de préparation. Si vous avez un projet de salle de bains ou de grand format, je viens voir le support avant de chiffrer.",
    },
    {
        "key": "renovation-electrique-logement-ancien",
        "slug": "renovation-electrique-logement-ancien",
        "trade": "electricite",
        "title": "Rénover l'électricité d'un logement ancien : par où commencer ?",
        "desc": "Tableau, protections, circuits, norme NF C 15-100 : par où commencer pour rénover l'électricité d'un logement ancien. Conseils d'Erol Zor, Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Dans un logement ancien, l'installation électrique est souvent un empilement de modifications successives. Avant de parler de prises design ou de spots, il faut commencer par le plus important : la sécurité.",
        "sections": [
            ("Faire le point sur l'existant", [
                "Je commence toujours par regarder le tableau électrique : âge, type de protections, présence d'un dispositif différentiel, état des câbles. Un diagnostic permet de distinguer ce qui est dangereux, ce qui est obsolète et ce qui peut rester.",
            ]),
            ("Le tableau électrique, cœur de l'installation", [
                "Un tableau ancien, sans protection différentielle adaptée, est la première chose à remplacer. Un tableau moderne répartit les circuits par groupes (éclairage, prises, cuisine, chauffage) avec des protections dimensionnées.",
            ]),
            ("Les circuits spécialisés", [
                "Plaques de cuisson, four, lave-linge, chauffe-eau : chaque gros consommateur a besoin de son propre circuit, avec la bonne section de câble. C'est un point essentiel pour éviter les surchauffes.",
            ]),
            ("La terre et les pièces d'eau", [
                "La mise à la terre et la liaison équipotentielle sont indispensables, surtout en salle de bains. Les règles de protection dépendent du volume où l'on se trouve par rapport à la baignoire ou à la douche.",
            ]),
            ("Prises et éclairage : penser les usages", [
                "Une fois la sécurité traitée, on pense aux usages : combien de prises par pièce, où placer les interrupteurs, quel éclairage pour quel usage. La norme NF C 15-100 fixe des minima, mais un projet bien pensé va souvent au-delà.",
            ]),
        ],
        "outro": "L'électricité n'est pas un domaine à improviser. Si vous avez un doute sur votre installation, un diagnostic est le meilleur point de départ.",
    },
    {
        "key": "stratifie-vinyle-parquet-choisir-son-sol",
        "slug": "stratifie-vinyle-parquet-choisir-son-sol",
        "trade": "revetement-sol",
        "title": "Stratifié, vinyle ou parquet : quel revêtement de sol choisir ?",
        "desc": "Comparatif honnête stratifié, vinyle et parquet : résistance à l'eau, durabilité, rénovation, confort. Le point de vue d'un artisan de Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Choisir un sol, c'est arbitrer entre budget, résistance à l'usage et aspect. Voici comment je compare les trois grandes familles quand un client me demande conseil.",
        "sections": [
            ("Le stratifié : économique et facile à poser", [
                "Le stratifié est composé de panneaux de fibres revêtus d'un décor. Il est abordable, résiste bien aux rayures et se pose en lames clipsables. Son point faible : l'eau. Il gonfle si elle s'infiltre, ce qui le rend peu adapté aux pièces humides.",
            ]),
            ("Le vinyle : le plus tolérant à l'humidité", [
                "Le vinyle (lames ou dalles PVC) résiste à l'eau, reste confortable sous le pied et imite bien le bois ou la pierre. Il convient à la cuisine et à la salle de bains. Choisissez un produit épais, avec une bonne couche d'usure, car les entrées de gamme se marquent.",
            ]),
            ("Le parquet : le plus noble", [
                "Le parquet massif ou contrecollé apporte chaleur et valeur au logement. Il peut être poncé et rénové plusieurs fois selon l'épaisseur de la couche de bois. En contrepartie, il demande plus de soin et un budget plus élevé.",
            ]),
            ("Le support compte autant que le revêtement", [
                "Quel que soit le choix, le sol doit être plan, propre et sec. Une mauvaise préparation donne des lames qui grincent, des joints qui s'ouvrent ou des creux. Je prévois systématiquement la vérification du support.",
            ]),
            ("Mon conseil", [
                "Pièces à vivre sèches et budget serré : stratifié ou vinyle. Pièces d'eau : vinyle. Logement dans lequel vous voulez investir : parquet. Mais ces règles dépendent de votre usage : parlez-m'en.",
            ]),
        ],
        "outro": "Si vous hésitez entre deux produits, demandez-moi un avis sur échantillon : voir et toucher change souvent la décision.",
    },
]

LEGAL = {
    "fr": [
        ("Éditeur du site", "Atelier Nordfeld, 70 rue du Nordfeld, 68100 Mulhouse. Téléphone : 07 58 67 94 66. Directeur de la publication : Erol Zor."),
        ("Informations d'immatriculation", "Forme juridique : [À COMPLÉTER]. SIRET : [À COMPLÉTER]. Numéro de TVA intracommunautaire : [À COMPLÉTER]. Adresse e-mail : [À COMPLÉTER]."),
        ("Hébergement", "Le site est actuellement hébergé par GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis). Cette mention sera mise à jour lors du changement d'hébergeur."),
        ("Propriété intellectuelle", "Les textes, images et éléments graphiques de ce site sont la propriété de Atelier Nordfeld, sauf mention contraire. Les visuels signalés comme illustrations ont été générés par intelligence artificielle et n'ont pas valeur contractuelle."),
        ("Responsabilité", "Les informations de ce site sont données à titre indicatif. Les conseils techniques ne remplacent pas un devis ni une visite sur place."),
    ],
}

PRIVACY = [
    ("Responsable du traitement", "Atelier Nordfeld, 70 rue du Nordfeld, 68100 Mulhouse, représenté par Erol Zor."),
    ("Données collectées", "Via le formulaire de contact : nom, téléphone, adresse e-mail, commune du chantier, description du projet. Ces données sont fournies volontairement par le visiteur."),
    ("Finalité", "Répondre à votre demande de contact ou de devis. Elles ne sont ni vendues ni utilisées à d'autres fins."),
    ("Base légale", "Votre consentement (case à cocher du formulaire) et, le cas échéant, l'exécution de mesures précontractuelles à votre demande."),
    ("Durée de conservation", "Les données sont conservées pendant la durée nécessaire au traitement de votre demande, puis supprimées ou archivées selon les obligations légales applicables."),
    ("Cookies et traceurs", "Ce site n'utilise ni cookie publicitaire, ni outil de mesure d'audience, ni service tiers de police de caractères ou de cartographie intégré. Aucun bandeau de consentement n'est donc nécessaire."),
    ("Vos droits", "Vous disposez d'un droit d'accès, de rectification, d'effacement, d'opposition et de limitation du traitement. Pour l'exercer, contactez-nous par téléphone au 07 58 67 94 66 ou par courrier à l'adresse ci-dessus. Vous pouvez également saisir la CNIL (www.cnil.fr)."),
]
