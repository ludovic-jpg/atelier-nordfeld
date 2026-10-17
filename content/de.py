"""Deutscher Inhalt von Atelier Nordfeld (Entsprechung zu fr.py).

Regel: keine erfundenen Fakten. Verwendet werden nur die von Erol Zor genannten
Angaben (3 Jahre Tätigkeit, über 100 Kunden, 7 Gewerke, Adresse, Telefon).
Die Blogartikel sind Fachratschläge in der Ich-Form und müssen von Erol Zor
vor der endgültigen Veröffentlichung freigegeben werden.
"""

LANG = "de"
HTML_LANG = "de"
OG_LOCALE = "de_DE"
HREFLANG = "de"

UI = {
    "skip": "Zum Inhalt springen",
    "call": "Anrufen",
    "call_long": "Anrufen: 07 58 67 94 66",
    "quote": "Angebot anfragen",
    "menu": "Menü",
    "trades": "Unsere Gewerke",
    "see_trade": "Gewerk ansehen",
    "read_more": "Artikel lesen",
    "all_articles": "Alle Artikel",
    "language": "Sprache",
    "breadcrumb_home": "Startseite",
    "founder_role": "Gründer von Atelier Nordfeld",
    "by": "Von",
    "updated": "Veröffentlicht am",
    "min_read": "Min. Lesezeit",
    "related_trade": "Das passende Gewerk",
    "other_trades": "Unsere weiteren Gewerke",
    "faq": "Häufige Fragen",
    "services_list": "Unsere Leistungen",
    "process_title": "So läuft eine Baustelle ab",
    "contact_title": "Sprechen wir über Ihr Projekt",
    "footer_about": "Renovierung und Handwerk rund ums Gebäude in Mülhausen (Mulhouse): Schreinerei, Malerarbeiten, Fliesen, Holzterrassen, Bodenbeläge, Innenausbau und Elektroinstallation.",
    "footer_nav": "Navigation",
    "footer_contact": "Kontakt",
    "footer_legal": "Rechtliches",
    "rights": "Alle Rechte vorbehalten.",
    "pole": "Renovierungs-Verbund",
    "illustration": "KI-generierte Illustration, unverbindlich.",
    "form": {
        "name": "Vor- und Nachname",
        "phone": "Telefon",
        "email": "E-Mail",
        "city": "Ort der Baustelle",
        "trade": "Art der Arbeiten",
        "trade_other": "Anderes / mehrere Gewerke",
        "message": "Beschreiben Sie Ihr Projekt",
        "message_ph": "Ungefähre Fläche, aktueller Zustand, gewünschter Zeitrahmen …",
        "consent": "Ich bin damit einverstanden, dass meine Daten zur Bearbeitung meiner Anfrage verwendet werden (siehe Datenschutzerklärung).",
        "send": "Anfrage senden",
        "required": "Dieses Feld ist erforderlich.",
        "invalid_email": "Ungültige E-Mail-Adresse.",
        "invalid_phone": "Ungültige Telefonnummer.",
        "success": "Vielen Dank, Ihre Anfrage wurde gesendet. Wir melden uns zeitnah.",
        "unavailable": "Das Online-Formular ist noch nicht aktiviert. Rufen Sie uns an: 07 58 67 94 66.",
        "error": "Das Senden ist fehlgeschlagen. Rufen Sie uns an: 07 58 67 94 66.",
    },
}

NAV = {"home": "Startseite", "blog": "Ratgeber", "about": "Über uns", "contact": "Kontakt"}

SLUGS = {
    "home": "",
    "blog": "ratgeber",
    "about": "ueber-uns",
    "contact": "kontakt",
    "legal": "impressum",
    "privacy": "datenschutz",
}

PAGES = {
    "home": {
        "title": "Atelier Nordfeld | Renovierung und Handwerk in Mülhausen",
        "desc": "Schreinerei, Malerarbeiten, Fliesen, Holzterrasse, Bodenbeläge, Innenausbau und Elektrik in Mülhausen (Mulhouse). Ein Ansprechpartner für Ihr Projekt. Tel. 07 58 67 94 66.",
    },
    "blog": {
        "title": "Renovierungs-Ratgeber Mulhouse: Tipps vom Handwerker | Atelier Nordfeld",
        "desc": "Die Tipps von Erol Zor, Handwerker in Mülhausen: Holzterrasse, Malerarbeiten, Fliesen, Elektrik, Bodenbeläge. Praktische Ratgeber vor dem Baustart.",
        "h1": "Ratgeber: Handwerkertipps und Baustellenberichte",
        "intro": "Ich bin Erol Zor und leite das Atelier Nordfeld in Mulhouse. Hier teile ich, was ich meinen Kunden vor einer Baustelle erkläre: wie man ein Material auswählt, welche Fehler man vermeidet und wo man anfängt.",
        "notice_title": "Projektberichte folgen",
        "notice": "Jede abgeschlossene Baustelle wird hier mit echten Fotos veröffentlicht, nach Zustimmung des Kunden. Bis dahin finden Sie hier die Ratgeber, die ich mir vor meinen ersten Baustellen gewünscht hätte.",
    },
    "about": {
        "title": "Über uns | Atelier Nordfeld, Handwerk in Mulhouse",
        "desc": "Atelier Nordfeld, Renovierungsbetrieb von Erol Zor in Mulhouse. Drei Jahre Tätigkeit, über 100 betreute Kunden, sieben Gewerke rund ums Gebäude.",
        "h1": "Atelier Nordfeld, ein Renovierungsbetrieb aus Mulhouse",
        "paras": [
            "Atelier Nordfeld ist ein Renovierungsbetrieb in der 70 rue du Nordfeld in Mulhouse. Gegründet wurde er von Erol Zor, Handwerker im Baugewerbe, mit einer einfachen Idee: Ein Eigentümer sollte nicht sieben Gewerke koordinieren müssen, um seine Wohnung zu renovieren.",
            "In drei Jahren Tätigkeit haben uns mehr als hundert Kunden ihre Arbeiten anvertraut: ein Zimmer zum Streichen, ein Bad zum Fliesen, eine Terrasse zum Bauen, eine Elektroinstallation zur Modernisierung oder ein Einbau nach Maß.",
            "Wir arbeiten in den Bereichen Schreinerei, Malerarbeiten, Fliesen, Holzterrasse, Bodenbeläge, Innenausbau und Elektroinstallation. Ein einziger Ansprechpartner begleitet Ihr Projekt vom ersten Anruf bis zur Abnahme.",
        ],
        "values_title": "Was unsere Arbeit leitet",
        "values": [
            ("Ein Ansprechpartner, eine Baustelle", "Sie sprechen vom Angebot bis zur Übergabe mit derselben Person. Keine Zwischenstationen, keine Grauzonen."),
            ("Verständliche Angebote", "Jede Position ist aufgeführt: Material, Arbeitszeit, Fristen. Sie wissen, was Sie kaufen, bevor Sie unterschreiben."),
            ("Details, die lange halten", "Untergründe vorbereiten, Trocknungszeiten einhalten, sauber verlegen: Was man nicht sieht, bestimmt die Lebensdauer einer Baustelle."),
        ],
        "founder_title": "Der Gründer",
        "founder_text": "Erol Zor hat das Atelier Nordfeld gegründet, um Privatkunden in Mulhouse und Umgebung seriöses Handwerk ohne Zwischenhändler zu bieten. Er betreut die Projekte selbst und bleibt Ihr Ansprechpartner.",
    },
    "contact": {
        "title": "Kontakt und Angebot für Renovierung in Mulhouse | Atelier Nordfeld",
        "desc": "Kontaktieren Sie das Atelier Nordfeld für Ihr Renovierungsangebot in Mulhouse: 07 58 67 94 66, 70 rue du Nordfeld, 68100 Mulhouse.",
        "h1": "Kontakt und Angebotsanfrage",
        "intro": "Beschreiben Sie uns Ihr Projekt oder rufen Sie direkt an. Je mehr Details Sie nennen (Fläche, Zustand, Zeitrahmen), desto genauer unsere Antwort.",
        "address_label": "Adresse",
        "phone_label": "Telefon",
        "map": "Anfahrt auf OpenStreetMap ansehen",
    },
    "legal": {
        "title": "Impressum | Atelier Nordfeld",
        "desc": "Impressum der Website Atelier Nordfeld, Renovierungsbetrieb in Mulhouse.",
        "h1": "Impressum",
    },
    "privacy": {
        "title": "Datenschutzerklärung | Atelier Nordfeld",
        "desc": "Wie das Atelier Nordfeld die über das Kontaktformular erhobenen personenbezogenen Daten verarbeitet.",
        "h1": "Datenschutzerklärung",
    },
}

HOME = {
    "kicker": "Renovierung in Mulhouse",
    "h1": "Ihre Renovierung in Mulhouse, von der Schreinerei bis zur Elektrik",
    "lead": "Das Atelier Nordfeld vereint sieben Gewerke unter einem Ansprechpartner. Sie beschreiben Ihr Projekt, wir kümmern uns um den Rest.",
    "cta2": "Unsere Gewerke ansehen",
    "stats": [("3 Jahre", "Tätigkeit in Mulhouse"), ("100+", "betreute Kunden"), ("7", "Gewerke rund ums Gebäude"), ("1", "Ansprechpartner vom Angebot bis zur Abnahme")],
    "trades_kicker": "Unsere Gewerke",
    "trades_h2": "Sieben Gewerke für ein Projekt",
    "trades_text": "Jedes Gewerk hat seine eigene Seite. Sie können uns ein einzelnes Los oder die gesamten Arbeiten anvertrauen.",
    "why_kicker": "Warum Atelier Nordfeld",
    "why_h2": "Renovieren, ohne fünf Firmen hinterherzulaufen",
    "why": [
        ("Ein einziger Ansprechpartner", "Schreiner, Maler, Fliesenleger, Elektriker: Sie müssen sie nicht koordinieren. Wir planen die Einsätze in der richtigen Reihenfolge."),
        ("Ein detailliertes Angebot", "Sie erhalten ein Angebot Position für Position, mit Material und Fristen. Keine Überraschungen unterwegs."),
        ("Saubere Ausführung", "Vorbereitete Untergründe, saubere Fugen, gerade Linien: Wir achten auf das, was man sieht, und auf das, was man nicht sieht."),
    ],
    "area_kicker": "Einsatzgebiet",
    "area_h2": "Mulhouse und Umgebung",
    "area_text": "Unser Betrieb sitzt in Mulhouse im Stadtteil Nordfeld, im Südelsass. Wir arbeiten in Mulhouse und den Nachbargemeinden.",
    "founder_kicker": "Ein Wort des Gründers",
    "founder_quote": "Meine Aufgabe ist, dass Sie sich nicht fragen müssen, ob die Baustelle vorankommt. Sie wissen, was erledigt ist, was noch aussteht und wann.",
    "blog_kicker": "Ratgeber",
    "blog_h2": "Die neuesten Handwerkertipps",
    "final_h2": "Ein Renovierungsprojekt in Mulhouse?",
    "final_text": "Rufen Sie uns an oder beschreiben Sie Ihr Projekt in zwei Minuten. Wir antworten zeitnah.",
}

AREAS = ["Mulhouse", "Rixheim", "Riedisheim", "Illzach", "Kingersheim", "Wittenheim", "Pfastatt", "Brunstatt-Didenheim", "Lutterbach", "Sausheim"]

PROCESS = [
    ("Erster Kontakt", "Sie rufen an oder füllen das Formular aus. Wir erfassen Ihren Bedarf und vereinbaren bei Bedarf einen Termin vor Ort."),
    ("Detailliertes Angebot", "Wir kalkulieren jede Position und schlagen einen realistischen Zeitplan vor. Sie stimmen zu, oder wir passen gemeinsam an."),
    ("Ausführung", "Die Baustelle wird Gewerk für Gewerk abgewickelt, mit klarem Stand zum Fortschritt und zum nächsten Schritt."),
    ("Abnahme", "Wir gehen die Arbeiten gemeinsam durch. Erst wenn Sie zufrieden sind, ist die Baustelle abgeschlossen."),
]

TRADES = [
    {
        "key": "menuiserie",
        "slug": "schreinerei",
        "name": "Schreinerei",
        "short": "Türen, Fenster, Schränke, Treppen und Einbauten nach Maß aus Holz.",
        "title": "Schreinerei in Mulhouse: Maßanfertigung und Montage | Atelier Nordfeld",
        "desc": "Schreiner in Mulhouse: Türen, Fenster, Einbauschränke, Treppen und Maßanfertigungen. Detailliertes Angebot, ein Ansprechpartner. Tel. 07 58 67 94 66.",
        "h1": "Schreinerei in Mulhouse",
        "intro": "Von der Haustür bis zum Einbauschrank unter der Dachschräge: Die Schreinerei gibt einer Wohnung Funktion und Charakter. Das Atelier Nordfeld übernimmt Montage, Renovierung und Maßanfertigung in Mulhouse und Umgebung.",
        "items": [
            "Einbau und Austausch von Innentüren und Haustüren",
            "Einbau von Fenstern und Fensterläden, Austausch bestehender Elemente",
            "Einbauschränke und Stauraum nach Maß, auch unter Dachschrägen",
            "Treppen: Stufen renovieren, Geländer, Handläufe",
            "Sockelleisten, Verkleidungen, Zierleisten und Abschlüsse",
            "Kleinreparaturen: klemmende Türen, Beschläge, Anpassungen",
        ],
        "faq": [
            ("Müssen alle Fenster gleichzeitig getauscht werden?", "Nicht unbedingt. Man kann Raum für Raum vorgehen, aber der Austausch einer ganzen Fassade auf einmal wirkt einheitlicher und vereinfacht die Organisation. Wir beraten Sie je nach Zustand Ihrer Fenster."),
            ("Lohnt sich ein Einbauschrank nach Maß wirklich?", "In Räumen mit besonderen Maßen (Dachschräge, Nische, schiefe Wand) ja: Er nutzt jeden Zentimeter. An einer geraden Standardwand kann ein fertiges Möbel genügen."),
            ("Wie lange dauert der Einbau einer Innentür?", "In der Regel einige Stunden pro Tür, wenn die Zarge intakt ist. Es dauert länger, wenn der Rahmen erneuert oder die Wände ausgebessert werden müssen."),
        ],
        "article": "terrasse-bois-pin-ipe-composite",
    },
    {
        "key": "peinture",
        "slug": "malerarbeiten",
        "name": "Malerarbeiten",
        "short": "Innen- und Außenanstriche, Untergrundvorbereitung, saubere Oberflächen.",
        "title": "Maler in Mulhouse: Innen- und Außenanstriche | Atelier Nordfeld",
        "desc": "Malerarbeiten in Mulhouse: Innen und außen, Untergrundvorbereitung, Spachtelarbeiten, saubere Oberflächen. Angebot unter 07 58 67 94 66.",
        "h1": "Malerarbeiten in Mulhouse",
        "intro": "Ein schöner Anstrich entscheidet sich vor dem ersten Auftrag: Ein gut vorbereiteter Untergrund macht den Unterschied. Das Atelier Nordfeld führt Ihre Innen- und Außenmalerarbeiten in Mulhouse mit sorgfältiger Vorbereitung und sauberem Finish aus.",
        "items": [
            "Wände und Decken streichen, Raum für Raum oder die ganze Wohnung",
            "Untergrundvorbereitung: Spachteln, Schleifen, Grundierung",
            "Streichen von Holzteilen, Türen, Sockelleisten und Heizkörpern",
            "Dekorputz und Wandbeläge",
            "Außenanstriche: Fensterläden, Tore, Fassaden",
            "Schutz von Möbeln und Böden, Reinigung nach der Baustelle",
        ],
        "faq": [
            ("Braucht man immer eine Grundierung?", "Auf neuem, stark saugendem oder fleckigem Untergrund ja. Auf einem intakten, sauberen Altanstrich nicht immer, aber sie verbessert oft Deckkraft und Haltbarkeit. Wir entscheiden im Einzelfall."),
            ("Wie lange sollte man warten, bevor man Möbel zurückstellt?", "Farbe ist nach wenigen Stunden grifffest, braucht aber mehrere Tage, um vollständig auszuhärten. Möbel sollten nicht sofort an die Wand gestellt werden. Die Hersteller geben Fristen auf dem Gebinde an."),
            ("Kann man über Tapete streichen?", "In manchen Fällen ist das möglich, das Ergebnis ist aber selten dauerhaft. Wir empfehlen, die Tapete zu entfernen und die Wand vorzubereiten."),
        ],
        "article": "preparer-murs-avant-peinture",
    },
    {
        "key": "carrelage",
        "slug": "fliesenarbeiten",
        "name": "Fliesen",
        "short": "Fliesenverlegung, Wandfliesen, Großformate, Bäder und Küchen.",
        "title": "Fliesenleger in Mulhouse: Fliesen und Wandfliesen | Atelier Nordfeld",
        "desc": "Fliesenverlegung in Mulhouse: Bad, Küche, Boden, Großformate. Sorgfältige Vorbereitung, detailliertes Angebot. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Fliesenarbeiten in Mulhouse",
        "intro": "Gut verlegte Fliesen halten Jahrzehnte, schlecht verlegte fallen sofort auf. Das Atelier Nordfeld verlegt Boden- und Wandfliesen in Mulhouse: Bäder, Küchen, Eingänge und Terrassen.",
        "items": [
            "Bodenfliesen und Wandfliesen, innen und außen",
            "Verlegung von Großformaten mit Verlegeplan und geprüfter Ebenheit",
            "Bäder: bodengleiche Duschen, Abdichtung, extraflache Duschwannen",
            "Küchen: Fliesenspiegel und Böden",
            "Ausgleichsmasse und Vorbereitung der Untergründe",
            "Fugen, Silikon und Anschlussarbeiten",
        ],
        "faq": [
            ("Kann man neue Fliesen auf alte verlegen?", "Manchmal ja, wenn die alten Fliesen intakt, fest haftend und eben sind. Das erhöht aber den Bodenaufbau und kann Türhöhen betreffen. Wir prüfen den Untergrund, bevor wir entscheiden."),
            ("Warum ist der Ausgleich des Untergrunds so wichtig?", "Fliesen gleichen Unebenheiten nicht aus. Ein unebener Untergrund führt zu ungleichen Fugen und kann Risse verursachen, besonders bei Großformaten."),
            ("Was ist der Unterschied zwischen Wandfliesen und Bodenfliesen?", "Wandfliesen sind meist dünner, Bodenfliesen sind auf Begehung und Abrieb ausgelegt. Manche Fliesen eignen sich für beides."),
        ],
        "article": "carrelage-grand-format-erreurs-pose",
    },
    {
        "key": "terrasse-bois",
        "slug": "holzterrasse",
        "name": "Holzterrasse",
        "short": "Bau von Terrassen aus Holz und Verbundwerkstoff, auf Stelzlagern oder Unterkonstruktion.",
        "title": "Holzterrasse in Mulhouse: Bau und Verlegung | Atelier Nordfeld",
        "desc": "Holzterrasse in Mulhouse: Kiefer, Douglasie, Ipé, WPC. Belüftete Unterkonstruktion, saubere Verlegung. Angebot: Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Holzterrasse in Mulhouse",
        "intro": "Eine Holzterrasse ist ein Außenbauwerk, das Regen, Frost und Sonne ausgesetzt ist. Ihre Lebensdauer hängt von der Unterkonstruktion, der Belüftung und der Holzart ab. Das Atelier Nordfeld baut Holz- und WPC-Terrassen in Mulhouse und den Nachbargemeinden.",
        "items": [
            "Terrassen auf höhenverstellbaren Stelzlagern oder auf Unterkonstruktion",
            "Wahl der Holzart: Kiefer kesseldruckimprägniert, Douglasie, Lärche, Tropenholz, WPC",
            "Belüftete Unterkonstruktion und Wasserableitung",
            "Treppen, Stufen und Terrassenkanten",
            "Geländer und Abschlüsse",
            "Pflege und Instandsetzung bestehender Terrassen",
        ],
        "faq": [
            ("Welche Holzart ist für eine Terrasse die richtige?", "Das hängt von Budget, Lage und Pflegebereitschaft ab. Imprägnierte Kiefer ist günstig, Douglasie und Lärche sind von Natur aus recht widerstandsfähig, Tropenhölzer halten lange, WPC braucht kaum Pflege. Unser Artikel erklärt die Unterschiede."),
            ("Braucht man eine Genehmigung für eine Terrasse?", "Das hängt von Höhe, Fläche und Gemeinde ab. Eine kleine ebenerdige Terrasse ist oft genehmigungsfrei, man sollte sich aber bei der Gemeinde oder im örtlichen Bebauungsplan informieren."),
            ("Warum ist die Belüftung unter der Terrasse so wichtig?", "Stehende Feuchtigkeit ist der größte Feind von Holz. Eine belüftete Unterkonstruktion und Dielen mit Fugen lassen Wasser abfließen und das Holz trocknen."),
        ],
        "article": "terrasse-bois-pin-ipe-composite",
    },
    {
        "key": "revetement-sol",
        "slug": "bodenbelaege",
        "name": "Bodenbeläge",
        "short": "Parkett, Laminat, Vinyl, elastische Beläge: Verlegung und Renovierung.",
        "title": "Bodenbeläge in Mulhouse: Parkett, Laminat, Vinyl | Atelier Nordfeld",
        "desc": "Verlegung von Parkett, Laminat, Vinyl und elastischen Bodenbelägen in Mulhouse. Untergrundvorbereitung, saubere Anschlüsse. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Bodenbeläge in Mulhouse",
        "intro": "Der Boden nimmt die größte sichtbare Fläche eines Raums ein und wird am stärksten beansprucht. Das Atelier Nordfeld verlegt und renoviert Parkett, Laminat, Vinyl und elastische Beläge in Mulhouse, mit sorgfältiger Untergrundvorbereitung.",
        "items": [
            "Verlegung von Massivparkett, Fertigparkett und Laminat",
            "Vinyl- und PVC-Böden: Klick- oder Klebesystem",
            "Elastische Beläge in Rollen für Feuchträume",
            "Ausgleichsmasse und Nivellierung des Untergrunds",
            "Entfernung des alten Belags",
            "Sockelleisten, Übergangsprofile und Abschlüsse",
        ],
        "faq": [
            ("Laminat, Vinyl oder Parkett: was wählen?", "Laminat ist günstig, fürchtet aber Wasser. Vinyl verträgt Feuchtigkeit am besten. Parkett ist am hochwertigsten und kann renoviert werden, braucht aber mehr Pflege. Unser Artikel vergleicht die drei."),
            ("Kann man auf einer Fußbodenheizung verlegen?", "Ja, mit einem geeigneten Belag. Der Wärmedurchlasswiderstand des Produkts muss geprüft und das vom Hersteller vorgesehene schrittweise Aufheizen eingehalten werden."),
            ("Müssen die Dielen vor dem Verlegen ruhen?", "Bei Parkett und Laminat wird das empfohlen: Die Dielen passen sich Temperatur und Feuchtigkeit des Raums an, das begrenzt Bewegungen nach der Verlegung."),
        ],
        "article": "stratifie-vinyle-parquet-choisir-son-sol",
    },
    {
        "key": "amenagement-interieur",
        "slug": "innenausbau",
        "name": "Innenausbau",
        "short": "Trennwände, abgehängte Decken, Stauraum, neue Raumaufteilung.",
        "title": "Innenausbau in Mulhouse: Trennwände, Decken | Atelier Nordfeld",
        "desc": "Innenausbau in Mulhouse: Trennwände, abgehängte Decken, Stauraum, neue Raumaufteilung. Ein Ansprechpartner. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Innenausbau in Mulhouse",
        "intro": "Eine Wohnung neu aufteilen, ein Zimmer schaffen, eine Decke dämmen oder eine Küche öffnen: Der Innenausbau erfordert die Koordination mehrerer Gewerke. Das Atelier Nordfeld steuert alles in Mulhouse und Umgebung.",
        "items": [
            "Trennwände und neue Raumaufteilung",
            "Abgehängte Decken und Deckenverkleidungen",
            "Vorsatzschalen und Innendämmung der Wände",
            "Einbauschränke, Ankleiden und Nischen nach Maß",
            "Dachboden- und Kellerausbau",
            "Koordination der Abschlussarbeiten: Malerarbeiten, Böden, Elektrik",
        ],
        "faq": [
            ("Kann man eine Wand ohne Risiko entfernen?", "Nur, wenn sie nicht tragend ist. Eine tragende Wand erfordert eine Berechnung und eine Verstärkung. Wir klären die Art der Wand vor jedem Abriss."),
            ("Muss man den Innenausbau genehmigen lassen?", "Rein innere Arbeiten sind oft frei, können aber von der Hausordnung oder einer Änderung der Wohnfläche abhängen. Informieren Sie sich bei der Gemeinde oder der Hausverwaltung."),
            ("Wie lange dauert ein Dachbodenausbau?", "Das schwankt stark je nach Fläche, Dämmung und Zugang. Nach einer Besichtigung nennen wir einen genauen Zeitplan."),
        ],
        "article": "preparer-murs-avant-peinture",
    },
    {
        "key": "electricite",
        "slug": "elektroinstallation",
        "name": "Elektroinstallation",
        "short": "Neuinstallation, Modernisierung, Zählerschrank, Beleuchtung, Steckdosen.",
        "title": "Elektriker in Mulhouse: Installation und Modernisierung | Atelier Nordfeld",
        "desc": "Elektroinstallation in Mulhouse: Neuinstallation, Modernisierung, Zählerschrank, Beleuchtung und Steckdosen. Atelier Nordfeld, 07 58 67 94 66.",
        "h1": "Elektroinstallation in Mulhouse",
        "intro": "Eine Elektroinstallation muss zuerst sicher und dann praktisch sein. Das Atelier Nordfeld führt Neuinstallationen und Elektrorenovierungen in Mulhouse unter Beachtung der geltenden französischen Norm aus.",
        "items": [
            "Komplette oder teilweise Erneuerung alter Installationen",
            "Austausch und Modernisierung des Zählerschranks",
            "Neue Stromkreise: Steckdosen, Beleuchtung, Kochfeld",
            "Innen- und Außenbeleuchtung, Einbaustrahler",
            "Netzwerk-, Antennen- und Türsprechanlagen",
            "Instandsetzung nach einer Prüfung",
        ],
        "faq": [
            ("Meine Installation ist über 30 Jahre alt, muss alles erneuert werden?", "Nicht unbedingt. Eine Prüfung zeigt, was konform ist, was gefährlich ist und was bleiben kann. Wir schlagen eine Anpassung vor, die dem tatsächlichen Zustand entspricht."),
            ("Was ist die Norm NF C 15-100?", "Sie ist die französische Norm für Elektroinstallationen in Wohnungen: Anzahl der Steckdosen pro Raum, Schutzeinrichtungen, Leitungsquerschnitte, Fehlerstromschutz. Sie dient der Sicherheit von Menschen und Sachen."),
            ("Muss man den Strom abschalten, um eine Steckdose zu tauschen?", "Immer. Schalten Sie den zugehörigen Sicherungsautomaten aus und prüfen Sie die Spannungsfreiheit, bevor Sie arbeiten. Im Zweifel einen Fachmann beauftragen."),
        ],
        "article": "renovation-electrique-logement-ancien",
    },
]

ARTICLES = [
    {
        "key": "terrasse-bois-pin-ipe-composite",
        "slug": "holzterrasse-kiefer-douglasie-ipe-wpc",
        "trade": "terrasse-bois",
        "title": "Holzterrasse: Kiefer, Douglasie, Ipé oder WPC – wie wählt man?",
        "desc": "Kiefer, Douglasie, Ipé oder WPC: Lebensdauer, Pflege, Budget. Der Ratgeber von Erol Zor, Handwerker in Mulhouse, zur Wahl der Terrasse.",
        "date": "2026-10-17",
        "read": 6,
        "intro": "Wenn ein Kunde eine Terrasse möchte, ist die erste Frage immer dieselbe: welche Holzart? Eine allgemeingültige Antwort gibt es nicht, nur die richtige für Ihr Budget, Ihre Lage und Ihre Bereitschaft zur Pflege. So denke ich darüber nach.",
        "sections": [
            ("Kesseldruckimprägnierte Kiefer: die günstige Wahl", [
                "Kiefer in Nutzungsklasse 4 ist die wirtschaftliche Wahl. Sie eignet sich für kleine Terrassen und knappe Budgets. Dafür braucht sie regelmäßige Pflege (Öl, Reinigung) und kann mit der Zeit Risse bekommen oder sich verziehen.",
                "Sie ist ein guter Einstieg, wenn Sie bereit sind, sich jährlich oder alle zwei Jahre darum zu kümmern.",
            ]),
            ("Douglasie und Lärche: der Kompromiss", [
                "Diese Nadelhölzer sind von Natur aus haltbarer als normale Kiefer, ohne starke chemische Behandlung. Sie vergrauen mit der Zeit, wenn man sie lässt, was viele Kunden schätzen, oder bleiben mit Öl farbig.",
                "Für eine Familienterrasse in Mulhouse, mit Frost und Feuchtigkeit in unseren Wintern, empfehle ich oft zuerst diese Option.",
            ]),
            ("Tropenhölzer: die Haltbarkeit", [
                "Ipé und andere Tropenhölzer sind sehr dicht und widerstandsfähig. Sie halten lange, sind aber teuer, schwer, schwer zu bohren, und ihre Herkunft muss geprüft werden (Zertifikat für nachhaltige Forstwirtschaft).",
            ]),
            ("WPC: am wenigsten Pflege", [
                "WPC mischt Holzfasern und Kunststoff. Es braucht kein Öl und kein Schleifen, verträgt Feuchtigkeit gut und bleibt formstabil. Es erwärmt sich in der Sonne stärker, und das sehr gleichmäßige Aussehen gefällt nicht jedem.",
                "Ich empfehle es Kunden, die eine Terrasse ohne Pflegeaufwand möchten.",
            ]),
            ("Wichtiger als die Holzart: die Unterkonstruktion", [
                "Eine Terrasse fault selten von oben, sie fault von unten. Entscheidend ist eine belüftete Unterkonstruktion: Unterkonstruktionshölzer oder verstellbare Stelzlager auf stabilem Untergrund, Luftraum unter den Dielen, Dielen mit leichtem Fugenabstand, ein leichtes Gefälle, damit Wasser nicht steht.",
                "Eine Terrasse aus edlem Holz ohne Belüftung altert schlechter als eine gut gebaute Kiefernterrasse.",
            ]),
        ],
        "outro": "Wenn Sie unsicher sind, rufen Sie mich an: Ich komme vorbei, sehe mir Lage und Untergrund an und berate Sie entsprechend Ihrer Situation.",
    },
    {
        "key": "preparer-murs-avant-peinture",
        "slug": "wande-vor-dem-streichen-vorbereiten",
        "trade": "peinture",
        "title": "Malerarbeiten: die 5 Vorbereitungsschritte, die ich nie auslasse",
        "desc": "Spachteln, Schleifen, Reinigen, Grundieren: die Vorbereitungsschritte vor dem Streichen, erklärt von Erol Zor, Handwerker in Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Einen schönen Anstrich erkennt man an der guten Vorbereitung, einen misslungenen daran, dass sie fehlt. Die Fehler zeigen sich, sobald Streiflicht auf die Wand fällt. Das sind die fünf Schritte, die ich auf jeder Baustelle einhalte.",
        "sections": [
            ("1. Abdecken", [
                "Böden, Sockelleisten, Steckdosen, Möbel: Alles, was nicht gestrichen werden soll, wird abgedeckt oder abgenommen. Das wirkt aufwendig und erspart stundenlanges Putzen.",
            ]),
            ("2. Reinigen und entstauben", [
                "Farbe haftet schlecht auf fettigem oder staubigem Untergrund. Küchen und Eingänge brauchen eine echte Reinigung. Auf stark beschädigtem Untergrund wird zuerst entfernt, was nicht hält: abblätternde Farbe, Tapete, bröckelnder Putz.",
            ]),
            ("3. Spachteln und ausbessern", [
                "Risse, Dübellöcher, Schlagstellen werden mit Spachtelmasse gefüllt und dann so lange getrocknet, wie der Hersteller angibt. Bei sehr unebenen Wänden sorgt eine Glättspachtelung für eine gleichmäßige Fläche.",
            ]),
            ("4. Schleifen", [
                "Das Schleifen macht die Oberfläche glatt und entfernt Spachtelkanten. Es geschieht trocken, danach wird sorgfältig entstaubt, denn Staub zeichnet sich in der Farbe ab.",
            ]),
            ("5. Grundierung auftragen", [
                "Die Grundierung vereinheitlicht die Saugfähigkeit des Untergrunds. Ohne sie kann eine ausgebesserte Wand die Farbe stellenweise „schlucken“ und Farbunterschiede hinterlassen. Ich trage sie immer auf neuem, fleckigem oder stark repariertem Untergrund auf.",
            ]),
            ("Die zwei Schlichtanstriche", [
                "Zwei dünne Schichten sind besser als eine dicke. Die Trocknungszeit zwischen beiden wird eingehalten, und an Ecken und Anschlüssen arbeitet man „nass in nass“, um Ansätze zu vermeiden.",
            ]),
        ],
        "outro": "Vorbereiten braucht Zeit, und genau diese Zeit macht den Unterschied zwischen einem Anstrich, der hält, und einem, den man neu machen muss.",
    },
    {
        "key": "carrelage-grand-format-erreurs-pose",
        "slug": "grossformatfliesen-verlegefehler",
        "trade": "carrelage",
        "title": "Großformatfliesen: diese Verlegefehler sollten Sie vermeiden",
        "desc": "Untergrundausgleich, Buttering-Floating, Fugen, Verlegeplan: häufige Fehler bei Großformatfliesen, erklärt von einem Handwerker aus Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Großformate liegen im Trend: weniger Fugen, hellere Räume, ein durchgehenderes Bild. Aber sie verzeihen nichts. Das sind die Verlegefehler, die am häufigsten vorkommen, und wie man sie vermeidet.",
        "sections": [
            ("Ein Untergrund, der nicht eben ist", [
                "Bei einer Fliese von 60 x 120 cm wird eine Vertiefung von wenigen Millimetern zum sichtbaren Mangel oder sogar zur Bruchursache. Der Ausgleich ist keine Option: Der Untergrund muss eben, sauber und trocken sein.",
            ]),
            ("Zu wenig Kleber unter der Fliese", [
                "Bei Großformaten trägt man Kleber auf den Untergrund und auf die Rückseite der Fliese auf (Buttering-Floating-Verfahren), mit einem geeigneten Kleber. Unter der Platte darf kein Hohlraum bleiben. Eine schlecht verklebte Fliese klingt hohl und reißt irgendwann.",
            ]),
            ("Kein Verlegeplan", [
                "Bevor man die erste Fliese klebt, muss man wissen, wo die Schnitte liegen. Man vermeidet schmale Randstreifen und legt die Fugen stimmig zu Öffnungen und Möbeln.",
            ]),
            ("Zu schmale oder vergessene Fugen", [
                "Fugen nehmen Bewegungen auf. Auch bei sogenannten rektifizierten Großformaten braucht es eine Fuge, deren Breite sich nach den Herstellerangaben richtet. Am Raumrand und bei Ebenenwechseln lässt man eine elastische Bewegungsfuge.",
            ]),
            ("Die Abdichtung im Feuchtraum", [
                "In einer bodengleichen Dusche wird nicht direkt auf den Untergrund gefliest. Ein Verbundabdichtungssystem unter den Fliesen ist unverzichtbar, und Ecken sowie Rohrdurchführungen müssen sorgfältig behandelt werden.",
            ]),
            ("Zu früh betreten", [
                "Der Kleber braucht Zeit zum Aushärten. Zu frühes Betreten, Verfugen oder Möblieren schwächt die Verlegung. Wir halten die vom Hersteller angegebenen Fristen ein.",
            ]),
        ],
        "outro": "Gut verlegte Fliesen sind vor allem 80 % Vorbereitung. Wenn Sie ein Badprojekt oder Großformate planen, sehe ich mir den Untergrund an, bevor ich kalkuliere.",
    },
    {
        "key": "renovation-electrique-logement-ancien",
        "slug": "elektrik-altbau-renovieren",
        "trade": "electricite",
        "title": "Elektrik im Altbau erneuern: wo fängt man an?",
        "desc": "Zählerschrank, Schutzeinrichtungen, Stromkreise, Norm NF C 15-100: wo man bei der Elektrorenovierung im Altbau anfängt. Tipps von Erol Zor, Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "In einer älteren Wohnung ist die Elektroinstallation oft eine Abfolge von Änderungen. Bevor man über Designer-Steckdosen oder Spots spricht, beginnt man mit dem Wichtigsten: der Sicherheit.",
        "sections": [
            ("Den Bestand erfassen", [
                "Ich schaue immer zuerst auf den Zählerschrank: Alter, Art der Schutzeinrichtungen, Vorhandensein eines Fehlerstromschutzschalters, Zustand der Leitungen. Eine Prüfung trennt, was gefährlich ist, was veraltet ist und was bleiben kann.",
            ]),
            ("Der Zählerschrank, das Herz der Installation", [
                "Ein alter Schrank ohne passenden Fehlerstromschutz ist das Erste, was ersetzt werden sollte. Ein moderner Schrank teilt die Stromkreise in Gruppen (Beleuchtung, Steckdosen, Küche, Heizung) mit passend dimensionierten Schutzeinrichtungen.",
            ]),
            ("Spezialisierte Stromkreise", [
                "Kochfeld, Backofen, Waschmaschine, Boiler: Jeder große Verbraucher braucht einen eigenen Stromkreis mit dem richtigen Leitungsquerschnitt. Das ist wichtig, um Überhitzung zu vermeiden.",
            ]),
            ("Erdung und Feuchträume", [
                "Erdung und Potentialausgleich sind unverzichtbar, besonders im Bad. Die Schutzvorschriften hängen davon ab, in welchem Bereich man sich im Verhältnis zu Badewanne oder Dusche befindet.",
            ]),
            ("Steckdosen und Beleuchtung: Nutzung durchdenken", [
                "Ist die Sicherheit geklärt, denkt man an die Nutzung: wie viele Steckdosen pro Raum, wo die Schalter sitzen, welches Licht wofür. Die französische Norm NF C 15-100 legt Mindestwerte fest, ein gut durchdachtes Projekt geht oft darüber hinaus.",
            ]),
        ],
        "outro": "Elektrik ist kein Bereich zum Improvisieren. Wenn Sie an Ihrer Installation zweifeln, ist eine Prüfung der beste Ausgangspunkt.",
    },
    {
        "key": "stratifie-vinyle-parquet-choisir-son-sol",
        "slug": "laminat-vinyl-parkett-bodenbelag-waehlen",
        "trade": "revetement-sol",
        "title": "Laminat, Vinyl oder Parkett: welchen Bodenbelag wählen?",
        "desc": "Ehrlicher Vergleich von Laminat, Vinyl und Parkett: Wasserbeständigkeit, Haltbarkeit, Renovierbarkeit, Komfort. Die Sicht eines Handwerkers aus Mulhouse.",
        "date": "2026-10-17",
        "read": 5,
        "intro": "Einen Boden zu wählen heißt, zwischen Budget, Belastbarkeit und Optik abzuwägen. So vergleiche ich die drei großen Familien, wenn mich ein Kunde um Rat fragt.",
        "sections": [
            ("Laminat: günstig und leicht zu verlegen", [
                "Laminat besteht aus Faserplatten mit Dekorschicht. Es ist erschwinglich, kratzfest und wird als Klickpaneel verlegt. Sein Schwachpunkt ist Wasser: Es quillt, wenn Feuchtigkeit eindringt, und ist für Feuchträume wenig geeignet.",
            ]),
            ("Vinyl: am verträglichsten bei Feuchtigkeit", [
                "Vinyl (Planken oder Fliesen aus PVC) widersteht Wasser, ist unter dem Fuß angenehm und imitiert Holz oder Stein gut. Es passt in Küche und Bad. Wählen Sie ein dickes Produkt mit guter Nutzschicht, denn günstige Varianten zeichnen sich ab.",
            ]),
            ("Parkett: das Edelste", [
                "Massiv- oder Fertigparkett bringt Wärme und Wert in die Wohnung. Je nach Dicke der Nutzschicht kann es mehrfach abgeschliffen und renoviert werden. Dafür braucht es mehr Pflege und ein höheres Budget.",
            ]),
            ("Der Untergrund zählt so viel wie der Belag", [
                "Welche Wahl auch fällt: Der Boden muss eben, sauber und trocken sein. Schlechte Vorbereitung führt zu knarrenden Dielen, sich öffnenden Fugen oder Dellen. Ich plane die Prüfung des Untergrunds immer ein.",
            ]),
            ("Mein Rat", [
                "Trockene Wohnräume und knappes Budget: Laminat oder Vinyl. Feuchträume: Vinyl. Wohnung, in die Sie investieren möchten: Parkett. Diese Regeln hängen aber von Ihrer Nutzung ab: Sprechen Sie mich darauf an.",
            ]),
        ],
        "outro": "Wenn Sie zwischen zwei Produkten schwanken, bitten Sie mich um eine Einschätzung am Muster: Sehen und Anfassen ändert oft die Entscheidung.",
    },
]

LEGAL = {
    "de": [
        ("Anbieter dieser Website", "Atelier Nordfeld, 70 rue du Nordfeld, 68100 Mulhouse, Frankreich. Telefon: 07 58 67 94 66 (aus Deutschland: +33 7 58 67 94 66). Vertretungsberechtigt: Erol Zor."),
        ("Registerangaben", "Rechtsform: [BITTE ERGÄNZEN]. SIRET: [BITTE ERGÄNZEN]. Umsatzsteuer-Identifikationsnummer: [BITTE ERGÄNZEN]. E-Mail-Adresse: [BITTE ERGÄNZEN]."),
        ("Hosting", "Die Website wird derzeit über GitHub Pages gehostet (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Diese Angabe wird bei einem Wechsel des Hosters aktualisiert."),
        ("Urheberrecht", "Texte, Bilder und Grafiken dieser Website sind Eigentum des Atelier Nordfeld, sofern nicht anders angegeben. Als Illustration gekennzeichnete Bilder wurden mit künstlicher Intelligenz erzeugt und sind nicht verbindlich."),
        ("Haftung", "Die Informationen dieser Website sind unverbindlich. Fachliche Hinweise ersetzen weder ein Angebot noch eine Besichtigung vor Ort."),
    ],
}

PRIVACY = [
    ("Verantwortlicher", "Atelier Nordfeld, 70 rue du Nordfeld, 68100 Mulhouse, Frankreich, vertreten durch Erol Zor."),
    ("Erhobene Daten", "Über das Kontaktformular: Name, Telefon, E-Mail-Adresse, Ort der Baustelle, Projektbeschreibung. Diese Daten werden freiwillig vom Besucher angegeben."),
    ("Zweck", "Bearbeitung Ihrer Kontakt- oder Angebotsanfrage. Die Daten werden weder verkauft noch für andere Zwecke verwendet."),
    ("Rechtsgrundlage", "Ihre Einwilligung (Kontrollkästchen im Formular) gemäß Art. 6 Abs. 1 lit. a DSGVO und gegebenenfalls die Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage gemäß Art. 6 Abs. 1 lit. b DSGVO."),
    ("Speicherdauer", "Die Daten werden so lange gespeichert, wie es zur Bearbeitung Ihrer Anfrage erforderlich ist, und danach gelöscht oder nach den geltenden gesetzlichen Pflichten archiviert."),
    ("Cookies und Tracker", "Diese Website verwendet keine Werbe-Cookies, kein Analysetool und keine extern eingebundenen Schriftarten oder Karten. Ein Einwilligungsbanner ist daher nicht erforderlich."),
    ("Ihre Rechte", "Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Widerspruch und Einschränkung der Verarbeitung. Wenden Sie sich dazu telefonisch an 07 58 67 94 66 oder schriftlich an die oben genannte Adresse. Sie können sich außerdem bei einer Datenschutzaufsichtsbehörde beschweren."),
]
