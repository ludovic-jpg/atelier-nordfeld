#!/usr/bin/env python3
"""Générateur du site Atelier Nordfeld (HTML statique bilingue FR/DE).

Usage :
    python3 build.py                      # build pour GitHub Pages (docs/)
    ZR_ORIGIN=https://exemple.fr ZR_BASE= python3 build.py   # build pour un nom de domaine

Variables d'environnement :
    ZR_ORIGIN         origine absolue du site (défaut : GitHub Pages)
    ZR_BASE           sous-chemin (défaut : /ze-renov ; vide avec un domaine propre)
    ZR_FORM_ENDPOINT  URL d'un service de formulaire (ex. Formspree). Vide = formulaire désactivé.
"""
import datetime
import html
import importlib.util
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "docs")

ORIGIN = os.environ.get("ZR_ORIGIN", "https://ludovic-jpg.github.io").rstrip("/")
BASE = os.environ.get("ZR_BASE", "/ze-renov").rstrip("/")
FORM_ENDPOINT = os.environ.get("ZR_FORM_ENDPOINT", "")
BUILD_DATE = datetime.date.today().isoformat()

BRAND = "Atelier Nordfeld"
PHONE_DISPLAY = "07 58 67 94 66"
PHONE_TEL = "+33758679466"
STREET = "70 rue du Nordfeld"
ZIP = "68100"
CITY = "Mulhouse"
FOUNDER = "Erol Zor"
LANGS = ["fr", "de"]

# Liens du pôle rénovation (sites frères). Ajouter ici uniquement des sites vérifiés.
POLE_LINKS = [
    ("DM Reformas", "Torrevieja (ES)", "https://reformasorihuelacosta.com"),
]

# ------------------------------------------------------------------ contenu


def smart(value, lang):
    """Typographie : apostrophes courbes, espaces insécables en français."""
    if isinstance(value, str):
        s = value.replace("'", "’")
        if lang == "fr":
            s = re.sub(r" ([?!:;»])", " \\1", s)
            s = s.replace("« ", "« ")
        return s
    if isinstance(value, dict):
        return {k: smart(v, lang) for k, v in value.items()}
    if isinstance(value, list):
        return [smart(v, lang) for v in value]
    if isinstance(value, tuple):
        return tuple(smart(v, lang) for v in value)
    return value


def load_content(lang):
    path = os.path.join(ROOT, "content", f"{lang}.py")
    spec = importlib.util.spec_from_file_location(f"content_{lang}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    keys = ["UI", "NAV", "PAGES", "HOME", "AREAS", "PROCESS", "TRADES", "ARTICLES", "LEGAL", "PRIVACY"]
    data = {k: smart(getattr(mod, k), lang) for k in keys}
    data["SLUGS"] = mod.SLUGS
    data["OG_LOCALE"] = mod.OG_LOCALE
    return data


C = {lang: load_content(lang) for lang in LANGS}

MONTHS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
}


def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split("-"))
    if lang == "fr":
        return f"{d} {MONTHS['fr'][m - 1]} {y}"
    return f"{d}. {MONTHS['de'][m - 1]} {y}"


# ------------------------------------------------------------------ images

IMG_KEYS = ["hero", "menuiserie", "peinture", "carrelage", "terrasse-bois", "revetement-sol", "amenagement-interieur", "electricite", "og"]
ALT = {
    "fr": {
        "hero": "Illustration d'un intérieur rénové : parquet, mur peint et menuiseries sur mesure",
        "menuiserie": "Illustration de menuiserie : escalier et placard en bois sur mesure",
        "peinture": "Illustration de peinture intérieure : mur fraîchement peint et outils de peintre",
        "carrelage": "Illustration d'une salle de bains carrelée avec douche à l'italienne",
        "terrasse-bois": "Illustration d'une terrasse en bois devant une maison alsacienne",
        "revetement-sol": "Illustration d'un sol en parquet clair dans un salon lumineux",
        "amenagement-interieur": "Illustration d'un aménagement intérieur avec cloison et rangements sur mesure",
        "electricite": "Illustration d'un tableau électrique moderne et de son câblage",
        "og": "Atelier Nordfeld, rénovation à Mulhouse",
    },
    "de": {
        "hero": "Illustration eines renovierten Innenraums: Parkett, gestrichene Wand und maßgefertigte Schreinerarbeiten",
        "menuiserie": "Illustration Schreinerei: Treppe und Einbauschrank aus Holz nach Maß",
        "peinture": "Illustration Malerarbeiten: frisch gestrichene Wand und Malerwerkzeug",
        "carrelage": "Illustration eines gefliesten Bads mit bodengleicher Dusche",
        "terrasse-bois": "Illustration einer Holzterrasse vor einem elsässischen Haus",
        "revetement-sol": "Illustration eines hellen Parkettbodens in einem lichtdurchfluteten Wohnzimmer",
        "amenagement-interieur": "Illustration eines Innenausbaus mit Trennwand und Einbauschränken",
        "electricite": "Illustration eines modernen Zählerschranks mit Verkabelung",
        "og": "Atelier Nordfeld, Renovierung in Mulhouse",
    },
}
IMAGES = {}  # key -> (url, width, height)


def process_images():
    """Convertit src/img/*.(png|jpg|jpeg|webp) en WebP optimisé dans docs/assets/img."""
    try:
        from PIL import Image
    except ImportError:
        return
    src_dir = os.path.join(SRC, "img")
    out_dir = os.path.join(OUT, "assets", "img")
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.isdir(src_dir):
        return
    for key in IMG_KEYS:
        for ext in (".webp", ".png", ".jpg", ".jpeg"):
            p = os.path.join(src_dir, key + ext)
            if os.path.exists(p):
                im = Image.open(p).convert("RGB")
                maxw = 1600 if key != "og" else 1200
                if im.width > maxw:
                    im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
                target = os.path.join(out_dir, key + ".webp")
                im.save(target, "WEBP", quality=80, method=6)
                if key == "og":  # les aperçus sociaux fonctionnent mieux en JPEG
                    im.save(os.path.join(out_dir, "og.jpg"), "JPEG", quality=84, optimize=True)
                IMAGES[key] = (f"{BASE}/assets/img/{key}.webp", im.width, im.height)
                break


# ------------------------------------------------------------------ routes


def esc(s):
    return html.escape(str(s), quote=True)


def trade_by_key(lang, key):
    return next(t for t in C[lang]["TRADES"] if t["key"] == key)


def article_by_key(lang, key):
    return next(a for a in C[lang]["ARTICLES"] if a["key"] == key)


def route_path(lang, rid):
    c = C[lang]
    if rid in c["SLUGS"]:
        s = c["SLUGS"][rid]
        return f"/{lang}/" + (s + "/" if s else "")
    kind, key = rid.split(":", 1)
    if kind == "t":
        return f"/{lang}/{trade_by_key(lang, key)['slug']}/"
    if kind == "a":
        return f"/{lang}/{c['SLUGS']['blog']}/{article_by_key(lang, key)['slug']}/"
    raise KeyError(rid)


def url(lang, rid):
    return BASE + route_path(lang, rid)


def absurl(lang, rid):
    return ORIGIN + url(lang, rid)


def all_routes():
    rids = ["home", "blog", "about", "contact", "legal", "privacy"]
    rids += [f"t:{t['key']}" for t in C["fr"]["TRADES"]]
    rids += [f"a:{a['key']}" for a in C["fr"]["ARTICLES"]]
    return rids


# ------------------------------------------------------------------ composants


def media(key, lang, cls="", eager=False, sizes="(min-width: 900px) 50vw, 100vw"):
    alt = ALT[lang].get(key, "")
    if key in IMAGES:
        u, w, h = IMAGES[key]
        loading = "eager" if eager else "lazy"
        prio = ' fetchpriority="high"' if eager else ""
        return f'<img class="media {cls}" src="{u}" width="{w}" height="{h}" alt="{esc(alt)}" loading="{loading}" decoding="async"{prio}>'
    return f'<div class="media swatch sw-{key} {cls}" role="img" aria-label="{esc(alt)}"></div>'


ICONS = {
    "menuiserie": '<path d="M4 20V8l8-4 8 4v12M9 20v-6h6v6"/><path d="M4 12h16"/>',
    "peinture": '<rect x="4" y="4" width="14" height="6" rx="1"/><path d="M18 7h2v5h-8v3"/><rect x="10" y="15" width="4" height="6" rx="1"/>',
    "carrelage": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M12 4v16M4 12h16"/>',
    "terrasse-bois": '<path d="M3 9h18M3 14h18M3 19h18"/><path d="M6 5v14M18 5v14"/>',
    "revetement-sol": '<path d="M3 18l9-12 9 12z"/><path d="M8 18l4-5 4 5"/>',
    "amenagement-interieur": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 3v18M4 12h16"/>',
    "electricite": '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
}


def icon(key):
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>'


ARROW = '<svg class="arr" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PHONE_ICON = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>'

LOGO = (
    '<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="7" fill="currentColor"/>'
    '<path d="M9 23V9h3l8 10V9h3v14h-3L12 13v10z" fill="var(--paper)"/></svg>'
)


def header(lang, rid):
    c = C[lang]
    ui = c["UI"]
    other = "de" if lang == "fr" else "fr"
    trades_links = "".join(
        f'<li><a href="{url(lang, "t:" + t["key"])}"{" aria-current=page" if rid == "t:" + t["key"] else ""}>{icon(t["key"])}<span>{esc(t["name"])}</span></a></li>'
        for t in c["TRADES"]
    )

    def nav_item(r, label):
        cur = ' aria-current="page"' if rid == r else ""
        return f'<li><a href="{url(lang, r)}"{cur}>{esc(label)}</a></li>'

    return f"""<header class="site-header">
<div class="wrap bar">
<a class="brand" href="{url(lang, 'home')}" aria-label="{esc(BRAND)}, {esc(ui['breadcrumb_home'])}">{LOGO}<span class="brand-name">{esc(BRAND)}</span></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav"><span class="sr">{esc(ui['menu'])}</span><span class="bars" aria-hidden="true"></span></button>
<nav id="main-nav" class="main-nav" aria-label="Navigation">
<ul>
<li class="has-sub"><button class="sub-toggle" type="button" aria-expanded="false">{esc(ui['trades'])}<svg class="chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></button><ul class="sub">{trades_links}</ul></li>
{nav_item('blog', c['NAV']['blog'])}
{nav_item('about', c['NAV']['about'])}
{nav_item('contact', c['NAV']['contact'])}
</ul>
<div class="nav-tools">
<a class="lang" lang="{other}" hreflang="{other}" href="{url(other, rid)}" aria-label="{'Deutsch' if other == 'de' else 'Français'}">{other.upper()}</a>
<a class="btn btn-call" href="tel:{PHONE_TEL}">{PHONE_ICON}<span>{PHONE_DISPLAY}</span></a>
</div>
</nav>
</div>
</header>"""


def footer(lang):
    c = C[lang]
    ui = c["UI"]
    trades = "".join(f'<li><a href="{url(lang, "t:" + t["key"])}">{esc(t["name"])}</a></li>' for t in c["TRADES"])
    pole = "".join(
        f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(n)}</a> <span class="muted">{esc(w)}</span></li>' for n, w, u in POLE_LINKS
    )
    pole_block = f'<div><h2 class="foot-h">{esc(ui["pole"])}</h2><ul>{pole}</ul></div>' if POLE_LINKS else ""
    return f"""<footer class="site-footer">
<div class="wrap foot-grid">
<div class="foot-brand">
<a class="brand brand-light" href="{url(lang, 'home')}">{LOGO}<span class="brand-name">{esc(BRAND)}</span></a>
<p>{esc(ui['footer_about'])}</p>
</div>
<div><h2 class="foot-h">{esc(ui['trades'])}</h2><ul>{trades}</ul></div>
<div><h2 class="foot-h">{esc(ui['footer_nav'])}</h2><ul>
<li><a href="{url(lang, 'blog')}">{esc(c['NAV']['blog'])}</a></li>
<li><a href="{url(lang, 'about')}">{esc(c['NAV']['about'])}</a></li>
<li><a href="{url(lang, 'contact')}">{esc(c['NAV']['contact'])}</a></li>
<li><a href="{url(lang, 'legal')}">{esc(c['PAGES']['legal']['h1'])}</a></li>
<li><a href="{url(lang, 'privacy')}">{esc(c['PAGES']['privacy']['h1'])}</a></li>
</ul></div>
<div><h2 class="foot-h">{esc(ui['footer_contact'])}</h2>
<address><p>{esc(STREET)}<br>{ZIP} {CITY}</p>
<p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p></address>
</div>
{pole_block}
</div>
<div class="wrap foot-bottom"><p>© {datetime.date.today().year} {esc(BRAND)}. {esc(ui['rights'])}</p><p class="muted">{esc(ui['illustration'])}</p></div>
</footer>
<div class="mobile-bar"><a class="btn btn-call" href="tel:{PHONE_TEL}">{PHONE_ICON}<span>{esc(ui['call'])}</span></a><a class="btn btn-primary" href="{url(lang, 'contact')}"><span>{esc(ui['quote'])}</span></a></div>"""


def breadcrumb(lang, crumbs):
    """crumbs: [(label, url_or_None)]"""
    items = []
    for i, (label, href) in enumerate(crumbs):
        if href:
            items.append(f'<li><a href="{href}">{esc(label)}</a></li>')
        else:
            items.append(f'<li aria-current="page">{esc(label)}</li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def breadcrumb_ld(lang, crumbs):
    elems = []
    for i, (label, href) in enumerate(crumbs, 1):
        e = {"@type": "ListItem", "position": i, "name": label}
        if href:
            e["item"] = ORIGIN + href
        elems.append(e)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elems}


def business_ld(lang):
    c = C[lang]
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": f"{ORIGIN}{BASE}/#business",
        "name": BRAND,
        "url": f"{ORIGIN}{BASE}/{lang}/",
        "telephone": PHONE_TEL,
        "image": ORIGIN + (IMAGES["og"][0].replace(".webp", ".jpg") if "og" in IMAGES else BASE + "/assets/logo.svg"),
        "description": c["PAGES"]["home"]["desc"],
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "postalCode": ZIP, "addressLocality": CITY, "addressRegion": "Haut-Rhin", "addressCountry": "FR"},
        "areaServed": [{"@type": "City", "name": a} for a in c["AREAS"]],
        "founder": {"@type": "Person", "name": FOUNDER},
        "knowsAbout": [t["name"] for t in c["TRADES"]],
        "inLanguage": ["fr", "de"],
    }


def cta_band(lang, title=None, text=None):
    c = C[lang]
    ui = c["UI"]
    title = title or c["HOME"]["final_h2"]
    text = text or c["HOME"]["final_text"]
    return f"""<section class="cta-band"><div class="wrap cta-inner">
<div><h2>{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="cta-actions"><a class="btn btn-primary" href="{url(lang, 'contact')}"><span>{esc(ui['quote'])}</span>{ARROW}</a><a class="btn btn-ghost-light" href="tel:{PHONE_TEL}">{PHONE_ICON}<span>{PHONE_DISPLAY}</span></a></div>
</div></section>"""


def process_block(lang):
    c = C[lang]
    steps = "".join(
        f'<li><span class="step-n">{i}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(c["PROCESS"], 1)
    )
    return f'<section class="section"><div class="wrap"><h2 class="h2">{esc(c["UI"]["process_title"])}</h2><ol class="steps">{steps}</ol></div></section>'


def article_card(lang, a):
    ui = C[lang]["UI"]
    t = trade_by_key(lang, a["trade"])
    return f"""<article class="card article-card">
<a class="card-media" href="{url(lang, 'a:' + a['key'])}" tabindex="-1" aria-hidden="true">{media(a['trade'], lang)}</a>
<div class="card-body">
<p class="eyebrow">{esc(t['name'])} · {a['read']} {esc(ui['min_read'])}</p>
<h3><a href="{url(lang, 'a:' + a['key'])}">{esc(a['title'])}</a></h3>
<p>{esc(a['desc'])}</p>
<a class="more" href="{url(lang, 'a:' + a['key'])}">{esc(ui['read_more'])}{ARROW}</a>
</div></article>"""


def trade_card(lang, t):
    ui = C[lang]["UI"]
    return f"""<a class="card trade-card" href="{url(lang, 't:' + t['key'])}">
<div class="card-media">{media(t['key'], lang)}</div>
<div class="card-body"><span class="chip">{icon(t['key'])}</span>
<h3>{esc(t['name'])}</h3><p>{esc(t['short'])}</p>
<span class="more">{esc(ui['see_trade'])}{ARROW}</span></div></a>"""


# ------------------------------------------------------------------ layout


def fit_title(title):
    """Retire le suffixe de marque si le titre dépasse ~62 caractères (troncature Google)."""
    suffix = f" | {BRAND}"
    if len(title) > 62 and title.endswith(suffix):
        return title[: -len(suffix)]
    return title


def page(lang, rid, title, desc, body, jsonld=None, og_type="website", noindex=False, og_image=None):
    title = fit_title(title)
    c = C[lang]
    other = "de" if lang == "fr" else "fr"
    canon = absurl(lang, rid)
    og_img = og_image or (ORIGIN + BASE + "/assets/img/og.jpg" if "og" in IMAGES else "")
    alts = [
        f'<link rel="alternate" hreflang="fr" href="{absurl("fr", rid)}">',
        f'<link rel="alternate" hreflang="de" href="{absurl("de", rid)}">',
        f'<link rel="alternate" hreflang="x-default" href="{ORIGIN + BASE + "/" if rid == "home" else absurl("fr", rid)}">',
    ]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    og_extra = (
        f'<meta property="og:image" content="{og_img}"><meta name="twitter:image" content="{og_img}">' if og_img else ""
    )
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    form_cfg = f' data-form-endpoint="{esc(FORM_ENDPOINT)}"'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{canon}">
{chr(10).join(alts)}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{c['OG_LOCALE']}">
<meta property="og:locale:alternate" content="{C[other]['OG_LOCALE']}">
<meta name="twitter:card" content="summary_large_image">
{og_extra}
<meta name="theme-color" content="#17202B">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{BASE}/assets/fonts/sora-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{BASE}/assets/fonts/manrope-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}/assets/style.css?v={BUILD_DATE}">
{ld}
</head>
<body{form_cfg}>
<a class="skip" href="#main">{esc(c['UI']['skip'])}</a>
{header(lang, rid)}
<main id="main">
{body}
</main>
{footer(lang)}
<script src="{BASE}/assets/main.js?v={BUILD_DATE}" defer></script>
</body>
</html>
"""


def write(path_rel, content):
    p = os.path.join(OUT, path_rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


# ------------------------------------------------------------------ pages


def build_home(lang):
    c = C[lang]
    h = c["HOME"]
    ui = c["UI"]
    p = c["PAGES"]["home"]
    stats = "".join(f'<li><strong>{esc(v)}</strong><span>{esc(l)}</span></li>' for v, l in h["stats"])
    trades = "".join(trade_card(lang, t) for t in c["TRADES"])
    why = "".join(f'<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for t, d in h["why"])
    areas = "".join(f"<li>{esc(a)}</li>" for a in c["AREAS"])
    latest = "".join(article_card(lang, a) for a in sorted(c["ARTICLES"], key=lambda x: x["date"], reverse=True)[:3])
    body = f"""
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">{esc(h['kicker'])}</p>
<h1>{esc(h['h1'])}</h1>
<p class="lead">{esc(h['lead'])}</p>
<div class="hero-actions"><a class="btn btn-primary" href="{url(lang, 'contact')}"><span>{esc(ui['quote'])}</span>{ARROW}</a><a class="btn btn-outline" href="#metiers"><span>{esc(h['cta2'])}</span></a></div>
<p class="hero-phone">{PHONE_ICON}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
</div>
<div class="hero-visual">{media('hero', lang, 'hero-media', eager=True, sizes='(min-width: 900px) 50vw, 100vw')}
<div class="swatch-strip" aria-hidden="true">{''.join(f'<i class="swatch sw-{t["key"]}"></i>' for t in c['TRADES'])}</div></div>
</div></section>
<section class="stats" aria-label="Chiffres clés"><div class="wrap"><ul>{stats}</ul></div></section>
<section id="metiers" class="section"><div class="wrap">
<p class="eyebrow">{esc(h['trades_kicker'])}</p><h2 class="h2">{esc(h['trades_h2'])}</h2><p class="sub">{esc(h['trades_text'])}</p>
<div class="grid grid-trades">{trades}</div></div></section>
<section class="section section-alt"><div class="wrap">
<p class="eyebrow">{esc(h['why_kicker'])}</p><h2 class="h2">{esc(h['why_h2'])}</h2>
<ul class="why">{why}</ul></div></section>
{process_block(lang)}
<section class="section section-alt"><div class="wrap split">
<div><p class="eyebrow">{esc(h['area_kicker'])}</p><h2 class="h2">{esc(h['area_h2'])}</h2><p class="sub">{esc(h['area_text'])}</p><ul class="pills">{areas}</ul></div>
<figure class="founder"><div class="founder-avatar" aria-hidden="true">EZ</div><blockquote><p>{esc(h['founder_quote'])}</p></blockquote><figcaption><strong>{esc(FOUNDER)}</strong><span>{esc(ui['founder_role'])}</span></figcaption></figure>
</div></section>
<section class="section"><div class="wrap">
<div class="row-head"><div><p class="eyebrow">{esc(h['blog_kicker'])}</p><h2 class="h2">{esc(h['blog_h2'])}</h2></div><a class="more" href="{url(lang, 'blog')}">{esc(ui['all_articles'])}{ARROW}</a></div>
<div class="grid grid-articles">{latest}</div></div></section>
{cta_band(lang)}
"""
    ld = [business_ld(lang)]
    write(route_path(lang, "home") + "index.html", page(lang, "home", p["title"], p["desc"], body, ld))


def build_trade(lang, t):
    c = C[lang]
    ui = c["UI"]
    rid = "t:" + t["key"]
    items = "".join(f"<li>{esc(i)}</li>" for i in t["items"])
    faq = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in t["faq"])
    art = article_by_key(lang, t["article"])
    others = "".join(
        f'<li><a href="{url(lang, "t:" + o["key"])}">{icon(o["key"])}<span>{esc(o["name"])}</span></a></li>' for o in c["TRADES"] if o["key"] != t["key"]
    )
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (t["name"], None)]
    body = f"""
<section class="page-hero"><div class="wrap hero-grid">
<div class="hero-copy">
{breadcrumb(lang, crumbs)}
<h1>{esc(t['h1'])}</h1>
<p class="lead">{esc(t['intro'])}</p>
<div class="hero-actions"><a class="btn btn-primary" href="{url(lang, 'contact')}?metier={t['key']}"><span>{esc(ui['quote'])}</span>{ARROW}</a><a class="btn btn-outline" href="tel:{PHONE_TEL}">{PHONE_ICON}<span>{PHONE_DISPLAY}</span></a></div>
</div>
<div class="hero-visual">{media(t['key'], lang, 'hero-media', eager=True)}</div>
</div></section>
<section class="section"><div class="wrap split split-wide">
<div><h2 class="h2">{esc(ui['services_list'])}</h2><ul class="checks">{items}</ul></div>
<aside class="aside-card"><h3>{esc(ui['related_trade'])}</h3>{article_card(lang, art)}</aside>
</div></section>
<section class="section section-alt"><div class="wrap narrow"><h2 class="h2">{esc(ui['faq'])}</h2><div class="faq">{faq}</div></div></section>
{process_block(lang)}
<section class="section section-alt"><div class="wrap"><h2 class="h2">{esc(ui['other_trades'])}</h2><ul class="trade-pills">{others}</ul></div></section>
{cta_band(lang)}
"""
    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": t["h1"],
        "serviceType": t["name"],
        "description": t["desc"],
        "provider": {"@id": f"{ORIGIN}{BASE}/#business"},
        "areaServed": {"@type": "City", "name": CITY},
        "inLanguage": lang,
    }
    ld = [business_ld(lang), service_ld, breadcrumb_ld(lang, [(l, h) for l, h in [(crumbs[0][0], crumbs[0][1]), (crumbs[1][0], url(lang, rid))]])]
    write(route_path(lang, rid) + "index.html", page(lang, rid, t["title"], t["desc"], body, ld))


def build_blog(lang):
    c = C[lang]
    ui = c["UI"]
    p = c["PAGES"]["blog"]
    cards = "".join(article_card(lang, a) for a in sorted(c["ARTICLES"], key=lambda x: x["date"], reverse=True))
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (c["NAV"]["blog"], None)]
    body = f"""
<section class="page-hero page-hero-text"><div class="wrap narrow">
{breadcrumb(lang, crumbs)}
<h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['intro'])}</p>
<div class="notice"><strong>{esc(p['notice_title'])}</strong><p>{esc(p['notice'])}</p></div>
</div></section>
<section class="section"><div class="wrap"><div class="grid grid-articles">{cards}</div></div></section>
{cta_band(lang)}
"""
    ld = [breadcrumb_ld(lang, [(crumbs[0][0], crumbs[0][1]), (crumbs[1][0], url(lang, "blog"))])]
    write(route_path(lang, "blog") + "index.html", page(lang, "blog", p["title"], p["desc"], body, ld))


def build_article(lang, a):
    c = C[lang]
    ui = c["UI"]
    rid = "a:" + a["key"]
    t = trade_by_key(lang, a["trade"])
    sections = "".join(f"<h2>{esc(h)}</h2>" + "".join(f"<p>{esc(p)}</p>" for p in paras) for h, paras in a["sections"])
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (c["NAV"]["blog"], url(lang, "blog")), (a["title"], None)]
    body = f"""
<article class="article">
<header class="page-hero page-hero-text"><div class="wrap narrow">
{breadcrumb(lang, crumbs)}
<p class="eyebrow">{esc(t['name'])}</p>
<h1>{esc(a['title'])}</h1>
<div class="byline"><span class="founder-avatar sm" aria-hidden="true">EZ</span><span>{esc(ui['by'])} <strong>{esc(FOUNDER)}</strong>, {esc(ui['founder_role'])} · {esc(ui['updated'])} {esc(fmt_date(lang, a['date']))} · {a['read']} {esc(ui['min_read'])}</span></div>
</div></header>
<div class="wrap narrow"><div class="figure">{media(a['trade'], lang, 'article-media', eager=True)}</div>
<p class="lead">{esc(a['intro'])}</p>
<div class="prose">{sections}<p class="outro">{esc(a['outro'])}</p></div>
<div class="related"><h2>{esc(ui['related_trade'])}</h2>{trade_card(lang, t)}</div>
</div></article>
{cta_band(lang)}
"""
    img_abs = ORIGIN + BASE + f"/assets/img/{a['trade']}.webp" if a["trade"] in IMAGES else None
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["desc"],
        "datePublished": a["date"],
        "dateModified": a["date"],
        "inLanguage": lang,
        "mainEntityOfPage": absurl(lang, rid),
        "author": {"@type": "Person", "name": FOUNDER},
        "publisher": {"@id": f"{ORIGIN}{BASE}/#business"},
    }
    if img_abs:
        article_ld["image"] = img_abs
    ld = [article_ld, breadcrumb_ld(lang, [(crumbs[0][0], crumbs[0][1]), (crumbs[1][0], crumbs[1][1]), (crumbs[2][0], url(lang, rid))])]
    write(route_path(lang, rid) + "index.html", page(lang, rid, f"{a['title']} | {BRAND}", a["desc"], body, ld, og_type="article", og_image=img_abs))


def build_about(lang):
    c = C[lang]
    ui = c["UI"]
    p = c["PAGES"]["about"]
    paras = "".join(f"<p>{esc(x)}</p>" for x in p["paras"])
    values = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in p["values"])
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (c["NAV"]["about"], None)]
    body = f"""
<section class="page-hero page-hero-text"><div class="wrap narrow">{breadcrumb(lang, crumbs)}<h1>{esc(p['h1'])}</h1></div></section>
<section class="section"><div class="wrap narrow prose">{paras}</div></section>
<section class="section section-alt"><div class="wrap"><h2 class="h2">{esc(p['values_title'])}</h2><ul class="why">{values}</ul></div></section>
<section class="section"><div class="wrap narrow"><div class="founder-card"><div class="founder-avatar lg" aria-hidden="true">EZ</div><div><h2 class="h2">{esc(p['founder_title'])}</h2><p><strong>{esc(FOUNDER)}</strong> · {esc(ui['founder_role'])}</p><p>{esc(p['founder_text'])}</p></div></div></div></section>
{cta_band(lang)}
"""
    ld = [business_ld(lang), breadcrumb_ld(lang, [(crumbs[0][0], crumbs[0][1]), (crumbs[1][0], url(lang, "about"))])]
    write(route_path(lang, "about") + "index.html", page(lang, "about", p["title"], p["desc"], body, ld))


def build_contact(lang):
    c = C[lang]
    ui = c["UI"]
    f = ui["form"]
    p = c["PAGES"]["contact"]
    opts = "".join(f'<option value="{t["key"]}">{esc(t["name"])}</option>' for t in c["TRADES"]) + f'<option value="autre">{esc(f["trade_other"])}</option>'
    msgs = json.dumps({k: f[k] for k in ["required", "invalid_email", "invalid_phone", "success", "unavailable", "error"]}, ensure_ascii=False)
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (c["NAV"]["contact"], None)]
    osm = "https://www.openstreetmap.org/search?query=70%20rue%20du%20Nordfeld%2068100%20Mulhouse"
    body = f"""
<section class="page-hero page-hero-text"><div class="wrap narrow">{breadcrumb(lang, crumbs)}<h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['intro'])}</p></div></section>
<section class="section"><div class="wrap contact-grid">
<form class="form" id="contact-form" novalidate data-msgs='{esc(msgs)}'>
<div class="field"><label for="f-name">{esc(f['name'])} *</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="row2">
<div class="field"><label for="f-phone">{esc(f['phone'])} *</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
<div class="field"><label for="f-email">{esc(f['email'])} *</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
</div>
<div class="row2">
<div class="field"><label for="f-city">{esc(f['city'])}</label><input id="f-city" name="city" type="text" autocomplete="address-level2"></div>
<div class="field"><label for="f-trade">{esc(f['trade'])}</label><select id="f-trade" name="trade">{opts}</select></div>
</div>
<div class="field"><label for="f-message">{esc(f['message'])} *</label><textarea id="f-message" name="message" rows="6" placeholder="{esc(f['message_ph'])}" required></textarea></div>
<div class="field hp" aria-hidden="true"><label>Website<input name="website" type="text" tabindex="-1" autocomplete="off"></label></div>
<div class="field check"><input id="f-consent" name="consent" type="checkbox" required><label for="f-consent">{esc(f['consent'])}</label></div>
<button class="btn btn-primary" type="submit"><span>{esc(f['send'])}</span>{ARROW}</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form>
<aside class="coords">
<h2>{esc(ui['contact_title'])}</h2>
<p class="coord"><span class="coord-l">{esc(p['phone_label'])}</span><a class="coord-big" href="tel:{PHONE_TEL}">{PHONE_ICON}{PHONE_DISPLAY}</a></p>
<address class="coord"><span class="coord-l">{esc(p['address_label'])}</span>{esc(BRAND)}<br>{esc(STREET)}<br>{ZIP} {CITY}</address>
<p><a class="more" href="{osm}" rel="noopener" target="_blank">{esc(p['map'])}{ARROW}</a></p>
</aside>
</div></section>
"""
    ld = [business_ld(lang), breadcrumb_ld(lang, [(crumbs[0][0], crumbs[0][1]), (crumbs[1][0], url(lang, "contact"))])]
    write(route_path(lang, "contact") + "index.html", page(lang, "contact", p["title"], p["desc"], body, ld))


def build_text(lang, rid, blocks):
    c = C[lang]
    ui = c["UI"]
    p = c["PAGES"][rid]
    sections = "".join(f"<h2>{esc(h)}</h2><p>{esc(t)}</p>" for h, t in blocks)
    crumbs = [(ui["breadcrumb_home"], url(lang, "home")), (p["h1"], None)]
    body = f"""
<section class="page-hero page-hero-text"><div class="wrap narrow">{breadcrumb(lang, crumbs)}<h1>{esc(p['h1'])}</h1></div></section>
<section class="section"><div class="wrap narrow prose">{sections}</div></section>
"""
    write(route_path(lang, rid) + "index.html", page(lang, rid, p["title"], p["desc"], body, [], noindex=(rid == "legal")))


def build_root():
    fr, de = C["fr"], C["de"]
    body = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(BRAND)} | Mulhouse · Rénovation / Renovierung</title>
<meta name="description" content="{esc(fr['PAGES']['home']['desc'])}">
<link rel="canonical" href="{ORIGIN}{BASE}/">
<link rel="alternate" hreflang="fr" href="{absurl('fr', 'home')}"><link rel="alternate" hreflang="de" href="{absurl('de', 'home')}"><link rel="alternate" hreflang="x-default" href="{ORIGIN}{BASE}/">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{BASE}/assets/style.css?v={BUILD_DATE}">
</head>
<body class="chooser">
<main class="chooser-box">
<a class="brand" href="{BASE}/" aria-label="{esc(BRAND)}">{LOGO}<span class="brand-name">{esc(BRAND)}</span></a>
<p class="lead">Rénovation et artisanat du bâtiment à Mulhouse<br><span class="muted">Renovierung und Handwerk in Mulhouse</span></p>
<div class="chooser-links"><a class="btn btn-primary" lang="fr" hreflang="fr" href="{url('fr', 'home')}"><span>Français</span>{ARROW}</a><a class="btn btn-outline" lang="de" hreflang="de" href="{url('de', 'home')}"><span>Deutsch</span>{ARROW}</a></div>
<p class="chooser-phone"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
</main>
<script src="{BASE}/assets/main.js?v={BUILD_DATE}" defer></script>
</body></html>
"""
    write("index.html", body)


def build_404():
    body = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 | {esc(BRAND)}</title><meta name="robots" content="noindex"><link rel="stylesheet" href="{BASE}/assets/style.css?v={BUILD_DATE}"></head>
<body class="chooser"><main class="chooser-box"><a class="brand" href="{BASE}/">{LOGO}<span class="brand-name">{esc(BRAND)}</span></a>
<h1>404</h1><p class="lead">Page introuvable · Seite nicht gefunden</p>
<div class="chooser-links"><a class="btn btn-primary" href="{url('fr', 'home')}"><span>Accueil</span></a><a class="btn btn-outline" href="{url('de', 'home')}"><span>Startseite</span></a></div></main></body></html>"""
    write("404.html", body)


def build_seo_files():
    rids = all_routes()
    urls = []
    for lang in LANGS:
        for rid in rids:
            if rid == "legal":
                continue
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{absurl(l, rid)}"/>' for l in LANGS if not (rid == "legal")
            ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{ORIGIN + BASE + "/" if rid == "home" else absurl("fr", rid)}"/>'
            prio = "1.0" if rid == "home" else ("0.8" if rid.startswith("t:") else "0.6")
            urls.append(f"<url><loc>{absurl(lang, rid)}</loc><lastmod>{BUILD_DATE}</lastmod><priority>{prio}</priority>{alts}</url>")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n"
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}{BASE}/sitemap.xml\n")
    write(".nojekyll", "")


def copy_assets():
    for sub in ("fonts",):
        s = os.path.join(SRC, sub)
        d = os.path.join(OUT, "assets", sub)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
    for f in ("style.css", "main.js", "favicon.svg"):
        shutil.copy(os.path.join(SRC, f), os.path.join(OUT, "assets", f))


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    copy_assets()
    process_images()
    for lang in LANGS:
        build_home(lang)
        build_blog(lang)
        build_about(lang)
        build_contact(lang)
        build_text(lang, "legal", C[lang]["LEGAL"][lang])
        build_text(lang, "privacy", C[lang]["PRIVACY"])
        for t in C[lang]["TRADES"]:
            build_trade(lang, t)
        for a in C[lang]["ARTICLES"]:
            build_article(lang, a)
    build_root()
    build_404()
    build_seo_files()
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print(f"OK : {n} fichiers dans {OUT} (origin={ORIGIN}, base='{BASE}', images={len(IMAGES)})")


if __name__ == "__main__":
    main()
