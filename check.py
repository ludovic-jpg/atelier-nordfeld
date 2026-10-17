#!/usr/bin/env python3
"""Contrôles automatiques du build : liens internes, H1, title/description, hreflang, JSON-LD."""
import os, re, sys, json
from html.parser import HTMLParser
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
BASE = os.environ.get("ZR_BASE", "/ze-renov")

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.links=[]; s.h1=0; s.title=""; s.in_title=False; s.meta={}; s.ld=[]; s.in_ld=False; s.hreflang=[]; s.canon=None; s.imgs_noalt=0; s.ids=set()
    def handle_starttag(s, t, a):
        a=dict(a)
        if "id" in a: s.ids.add(a["id"])
        if t=="a" and a.get("href"): s.links.append(a["href"])
        if t=="h1": s.h1+=1
        if t=="title": s.in_title=True
        if t=="meta" and a.get("name"): s.meta[a["name"]]=a.get("content","")
        if t=="link" and a.get("rel")=="canonical": s.canon=a["href"]
        if t=="link" and a.get("rel")=="alternate" and a.get("hreflang"): s.hreflang.append((a["hreflang"],a["href"]))
        if t=="script" and a.get("type")=="application/ld+json": s.in_ld=True
        if t=="img" and not a.get("alt"): s.imgs_noalt+=1
    def handle_endtag(s,t):
        if t=="title": s.in_title=False
        if t=="script": s.in_ld=False
    def handle_data(s,d):
        if s.in_title: s.title+=d
        if s.in_ld: s.ld.append(d)

errors=[]; warns=[]; pages={}
for root,_,files in os.walk(OUT):
    for f in files:
        if f.endswith(".html"):
            p=os.path.join(root,f); pages[p]=P(); pages[p].feed(open(p,encoding="utf-8").read())
def exists(href):
    href=href.split("#")[0].split("?")[0]
    if not href.startswith(BASE+"/") and href!=BASE: return None
    rel=href[len(BASE):].lstrip("/")
    cand=os.path.join(OUT,rel)
    if os.path.isdir(cand): cand=os.path.join(cand,"index.html")
    return os.path.exists(cand)
for p,pp in pages.items():
    r=os.path.relpath(p,OUT)
    if r=="404.html" or r=="index.html": continue
    if pp.h1!=1: errors.append(f"{r}: {pp.h1} H1")
    t=pp.title.strip(); d=pp.meta.get("description","")
    if len(t)>70: warns.append(f"{r}: title {len(t)} car.")
    if not (70<=len(d)<=175): warns.append(f"{r}: description {len(d)} car.")
    if pp.imgs_noalt: errors.append(f"{r}: img sans alt")
    for l in pp.links:
        if l.startswith(("tel:","mailto:","http","#")): continue
        e=exists(l)
        if e is False: errors.append(f"{r}: lien cassé {l}")
    langs={h for h,_ in pp.hreflang}
    if not {"fr","de","x-default"}<=langs: errors.append(f"{r}: hreflang incomplet {langs}")
    for h,u in pp.hreflang:
        if u.startswith("https://ludovic-jpg.github.io"):
            if not exists(u.replace("https://ludovic-jpg.github.io","")): errors.append(f"{r}: hreflang cible absente {u}")
    for blob in ["".join(pp.ld)] if pp.ld else []:
        pass
    for chunk in pp.ld:
        try: json.loads(chunk)
        except Exception as ex: errors.append(f"{r}: JSON-LD invalide {ex}")
print(f"{len(pages)} pages HTML contrôlées")
print("ERREURS:",len(errors)); [print("  ",e) for e in errors]
print("AVERTISSEMENTS:",len(warns)); [print("  ",w) for w in warns]
sys.exit(1 if errors else 0)
