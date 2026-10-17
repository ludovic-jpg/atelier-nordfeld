# Audit SEO du pôle rénovation (17/10/2026)

Aucune modification n'a été poussée sur les deux dépôts existants : ce document liste les corrections proposées, à valider.

## 1. DM Reformas (reformasorihuelacosta.com)
Le domaine `dm-reformas-showcase.lovable.app` redirige (302) vers `reformasorihuelacosta.com`, qui est en ligne.

**Déjà bon** : titres < 60 car., descriptions 140-158 car., canonical, hreflang ES/EN, x-default, sitemap dynamique, JSON-LD HomeAndConstructionBusiness, robots.txt propre.

**À corriger / améliorer**
1. **Avis clients fabriqués** : `src/lib/site.ts` contient 6 témoignages avec notes (noms inventés, dont une note affichée). Sur un site réel, de faux avis sont illégaux dans l'UE (pratique commerciale déloyale) et risquent une sanction Google. À remplacer par de vrais avis Google (ou à retirer). Même remarque pour les projets « avant/après » s'ils ne sont pas réels.
2. **Pages de service dédiées** : une seule page « Servicios » pour 10 métiers. Créer une page par service (ex. reformas de baños Torrevieja, reformas integrales Torrevieja, reformas de cocinas Torrevieja) : c'est le premier levier de visibilité locale.
3. **Blog** : absent. Ajouter des guides par service (même modèle que le blog Atelier Nordfeld).
4. **Sitemap** : ajouter `lastmod`.
5. **Google Business Profile** : fiche à créer/optimiser, même NAP que le site.
6. **Schema** : ajouter `sameAs` complet, `hasMap`, et des `Service` par page de service.

## 2. Multiservicios Gaitán (torrevieja-reformas.es)
Le domaine n'a pas pu être vérifié (accès bloqué pour mon outil de lecture). Analyse faite sur le code du dépôt.

**À corriger / améliorer**
1. **Site en une seule page** (une seule URL indexable) : créer des pages par service (ventanas PVC Torrevieja, ventanas aluminio Torrevieja, reformas integrales, baños).
2. **Sitemap** : seulement 4 URL, aucune `lastmod`.
3. **Titre** de 63 caractères : à raccourcir sous 60.
4. **Données structurées** : ajouter `geo`, `openingHoursSpecification`, `sameAs`, `areaServed` en liste de villes.
5. Ajouter FAQ, page « Proyectos » avec vraies photos, et Google Business Profile.
6. Vérifier que `/admin` et `/auth` restent hors index (robots + noindex).

## 3. Atelier Nordfeld (nouveau site)
Appliqué : hreflang fr/de/x-default, canonical, JSON-LD (entreprise, service, article, fil d'Ariane), sitemap avec alternates, une page par métier, blog, polices auto-hébergées (RGPD), zéro traceur, Core Web Vitals visés (HTML statique, CSS unique, JS de 4 Ko).

## 4. Liens entre les sites du pôle
Les trois entreprises sont distinctes et dans des pays différents. Un lien en pied de page vers DM Reformas est en place (liens vérifiés uniquement). Valeur SEO faible mais sans risque ; ne pas multiplier les liens croisés, ce qui ressemblerait à un réseau de liens. Le vrai gain vient de contenus locaux, de Google Business Profile et de vrais avis.
