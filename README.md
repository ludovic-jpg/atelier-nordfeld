# Atelier Nordfeld : site vitrine bilingue (FR/DE)

Site statique généré par `build.py` (Python 3, Pillow facultatif pour les images).

```
python3 build.py        # génère docs/ (GitHub Pages : dossier /docs)
python3 check.py        # contrôle liens, H1, title/description, hreflang, JSON-LD
```

## Structure
- `content/fr.py`, `content/de.py` : tous les textes
- `src/` : CSS, JS, polices, `img/` (déposer ici les images, voir `docs-projet/PROMPTS-VISUELS.md`)
- `docs/` : site généré (ne pas éditer à la main)
- `brouillons/` : modèle d'étude de cas à remplir avec de vrais chantiers
- `docs-projet/` : audit SEO du pôle, prompts visuels

## Mise en ligne avec un nom de domaine
```
ZR_ORIGIN=https://votre-domaine.fr ZR_BASE= python3 build.py
```
Puis pointer le domaine vers GitHub Pages (fichier `docs/CNAME`).

## Formulaire de contact
Désactivé tant qu'aucun service n'est configuré. Créer un formulaire (Formspree, Web3Forms…) et lancer :
`ZR_FORM_ENDPOINT=https://… python3 build.py`

## À compléter avant publication officielle
- Mentions légales / Impressum : forme juridique, SIRET, TVA, e-mail (champs `[À COMPLÉTER]`)
- Validation par Erol Zor des articles du blog (rédigés dans sa voix)
- Photo du fondateur, vraies photos de chantiers, vrais avis (aucun avis fictif n'est publié)
