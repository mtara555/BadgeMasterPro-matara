# BadgeMaster Pro — Version 6.1 Professional

Application web professionnelle de **création et gestion de badges d'identification**.

Fonctionne entièrement dans le navigateur (PWA), sans serveur. Idéale pour :
- Conférences & salons
- Accueils d'entreprise
- Événements & séminaires
- Gestion des visiteurs

## Nouveautés v6.1 Professional

- ✅ **Page Paramètres** complète (organisation, logo, options d'impression)
- ✅ **Logo & organisation** appliqués automatiquement sur les nouveaux badges
- ✅ **Modales de confirmation** professionnelles (plus de `confirm()` navigateur)
- ✅ **Empty states** soignés avec actions contextuelles
- ✅ **PWA corrigée** : installation sur écran d'accueil, cache offline fiable
- ✅ **Service Worker v6** avec stratégie cache-first + mise à jour automatique
- ✅ **Store settings** (IndexedDB v3) pour persistance des préférences
- ✅ Interface et versioning professionnel

## Fonctionnalités

| Module | Description |
|--------|-------------|
| 🏠 Tableau de bord | Stats en direct, actions rapides, événements récents |
| 🎪 Événements | Création, association badges, statut auto (passé / en cours / à venir) |
| ✏️ Créer un badge | Prévisualisation temps réel, photo webcam/import, QR code, formats CR80/CR79/CR100… |
| 📊 Import Excel | Création de badges en masse (.xlsx) |
| 📋 Tous les badges | Recherche, filtres, sélection multiple, impression |
| 🪪 Badges Visiteurs | Enregistrement entrée/sortie + badge dédié |
| 📓 Journal des visites | Stats, filtres date, export CSV / PDF |
| ⚙️ Paramètres | Organisation, logo, qualité impression, sauvegarde/restauration |
| 🖨️ Impression A4 | Grille multi-badges |
| 💾 Sauvegarde JSON | Export / import complet des données |

## Utilisation

1. Ouvrir `index.html` dans un navigateur moderne (Chrome, Edge, Firefox, Safari).
2. Pour une utilisation hors-ligne : installer en PWA (menu navigateur → « Installer l'application »).
3. Créer d'abord un **événement**, puis des badges associés.

## Technologies

- HTML / CSS / JS vanilla (mono-fichier)
- IndexedDB (stockage local)
- QRCode.js, html2canvas, jsPDF, SheetJS (CDN)
- PWA (manifest + service worker)

## Stockage

Toutes les données restent **localement** dans le navigateur.  
Pensez à exporter régulièrement une sauvegarde depuis **Paramètres**.

---

**BadgeMaster Pro v6.1 Professional** — Application de gestion de badges niveau pro.
