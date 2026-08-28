# BadgeMaster Pro — Documentation

**Version :** 5.3  
**Langue :** Français  
**Type :** Application web mono-fichier (HTML/CSS/JS)  
**Compatibilité :** Desktop & Mobile (responsive)

---

## Table des matières

1. [Présentation générale](#présentation-générale)
2. [Fonctionnalités principales](#fonctionnalités-principales)
3. [Structure de l'interface](#structure-de-linterface)
4. [Modules détaillés](#modules-détaillés)
   - [Tableau de bord](#tableau-de-bord)
   - [Créer un badge](#créer-un-badge)
   - [Mes badges](#mes-badges)
   - [Événements](#événements)
   - [Visiteurs](#visiteurs)
   - [Journal des visites](#journal-des-visites)
   - [Paramètres](#paramètres)
5. [Formats de badges supportés](#formats-de-badges-supportés)
6. [Exports disponibles](#exports-disponibles)
7. [Stockage des données](#stockage-des-données)
8. [Technologies utilisées](#technologies-utilisées)
9. [Utilisation sur mobile](#utilisation-sur-mobile)

---

## Présentation générale

BadgeMaster Pro est une application web complète de **gestion et création de badges d'identification**. Elle fonctionne entièrement dans le navigateur, sans serveur ni installation requise. Elle est conçue pour les événements, les accueils d'entreprise, les conférences et la gestion des visiteurs.

L'application propose un design sombre moderne avec un système de couleurs cohérent, une navigation latérale sur desktop et une navigation en bas d'écran sur mobile.

---

## Fonctionnalités principales

| Fonctionnalité | Description |
|---|---|
| 🎫 Création de badges | Création manuelle avec prévisualisation en temps réel |
| 📷 Photo intégrée | Capture via webcam ou import depuis l'appareil |
| 🔲 QR Code automatique | Génération de QR code sur chaque badge |
| 🖨️ Impression | Export PDF et impression directe (A4, format badge) |
| 📋 Gestion des événements | Création et association d'événements aux badges |
| 👤 Gestion des visiteurs | Enregistrement entrée/sortie avec horodatage |
| 📓 Journal des visites | Historique filtrable avec statistiques |
| 📤 Export CSV / Excel / PDF | Export des données de visiteurs |
| 📥 Import Excel | Création de badges en masse via fichier XLSX |
| 📱 Interface mobile | Navigation adaptée avec barre inférieure |

---

## Structure de l'interface

### Desktop
- **Barre latérale gauche** (260px) : navigation principale avec groupes et icônes
- **Zone de contenu principale** : pages dynamiques avec animation de transition
- **En-tête de page** : titre, sous-titre et actions contextuelles

### Mobile (< 768px)
- **Barre supérieure** : logo, date et bouton menu hamburger
- **Navigation inférieure** : icônes + labels pour les 5 sections principales
- **Menu latéral** : accessible via le bouton hamburger (overlay)

---

## Modules détaillés

### Tableau de bord

Page d'accueil de l'application affichant :

- **4 cartes de statistiques** : Total badges, Événements actifs, Visiteurs du jour, Badges imprimés
- **Actions rapides** : raccourcis vers Nouveau badge, Importer Excel, Nouveau visiteur, Imprimer, Événements, Journal
- **Liste des événements récents** avec statut et nombre de badges associés
- **Derniers badges créés** : aperçu des 5 badges les plus récents

---

### Créer un badge

Formulaire de création avec les champs suivants :

**Informations personnelles**
- Nom et Prénom
- Poste / Fonction
- Organisation / Société
- Département

**Paramètres du badge**
- Événement associé (liste déroulante)
- Type de badge : Participant, Intervenant, Staff, VIP, Presse, Visiteur
- Couleur principale (palette de couleurs prédéfinie)

**Photo**
- Import depuis l'appareil
- Capture par webcam (modal dédié avec aperçu vidéo)

**Prévisualisation en temps réel**
- Mise à jour instantanée du badge lors de la saisie
- Choix du format de badge (voir section [Formats](#formats-de-badges-supportés))

**Actions disponibles**
- Enregistrer le badge
- Imprimer directement
- Réinitialiser le formulaire

---

### Mes badges

Liste complète des badges enregistrés avec :

- **Barre de recherche** : filtrage par nom, organisation, événement
- **Filtres** : par événement, par type de badge
- **Chaque badge affiche** : aperçu miniature, nom complet, organisation, type, événement, date de création
- **Actions par badge** : Modifier ✏️, Imprimer 🖨️, Supprimer 🗑️

**Import en masse**
- Bouton "Importer Excel" : chargement d'un fichier `.xlsx` pour créer plusieurs badges d'un coup
- Colonnes attendues : Nom, Prénom, Poste, Organisation, Département, Type, Événement

---

### Événements

Gestion des événements auxquels les badges sont rattachés :

- **Créer un événement** : Nom, Date, Lieu, Description
- **Liste des événements** : avec compteur de badges associés
- **Actions** : Modifier, Supprimer, Voir les badges associés
- **Statut automatique** : Passé / En cours / À venir selon la date

---

### Visiteurs

Enregistrement des visites en temps réel :

**Formulaire d'accueil visiteur**
- Nom, Prénom
- Société
- Département
- Personne / Organisation hôte
- Date de visite
- Heure d'entrée et heure de sortie

**Badge visiteur dédié**
- Format spécifique avec bandeau orange
- QR code intégré
- Impression directe

---

### Journal des visites

Historique complet de toutes les visites avec :

**Statistiques en temps réel**
- Visites aujourd'hui
- Visites cette semaine
- Visites ce mois
- Durée moyenne de visite

**Tableau filtrable**

| Colonne | Description |
|---|---|
| Date | Date de la visite (format JJ/MM/AAAA) |
| Entrée | Heure d'arrivée (en vert) |
| Sortie | Heure de départ (en rouge) |
| Durée | Calculée automatiquement |
| Visiteur | Nom et prénom |
| Société | Entreprise du visiteur |
| Département | Service concerné |
| Hôte | Organisation ou personne accueillante |

**Filtres disponibles**
- Plage de dates (de / à)
- Recherche textuelle (nom, société, département, hôte)

**Actions**
- Modifier un enregistrement ✏️
- Imprimer un badge visiteur individuel 🖨️
- Export CSV (séparateur `;`, encodage UTF-8 BOM)
- Export PDF (impression via fenêtre navigateur)

---

### Paramètres

Configuration générale de l'application :

- Nom de l'organisation (affiché sur les badges)
- Logo personnalisé
- Réinitialisation des données
- Sauvegarde / restauration de la base de données (export JSON)

---

## Formats de badges supportés

| Nom | Dimensions (px) | Usage typique |
|---|---|---|
| CR80 | 342 × 216 | Carte standard (taille carte bancaire) |
| CR79 | 394 × 269 | Légèrement plus grand |
| CR100 | 392 × 592 | Format vertical allongé |
| 85×90 mm | 321 × 340 | Format carré personnalisé |
| Personnalisé | Variable | Dimensions définies par glissières |

Le format personnalisé est ajustable via deux curseurs (largeur et hauteur) avec prévisualisation immédiate.

---

## Exports disponibles

### Badges
- **PDF** : impression au format A4 avec 2 badges par ligne (grille)
- **Image PNG** : via html2canvas (capture du badge affiché)

### Journal des visites
- **CSV** : fichier texte séparé par `;`, compatible Excel, encodé en UTF-8 avec BOM
  - Nom du fichier : `journal-visites-AAAA-MM-JJ.csv`
- **PDF** : génération d'une page HTML optimisée pour l'impression, ouverte dans un nouvel onglet

---

## Stockage des données

L'application utilise **IndexedDB** (base de données locale du navigateur) pour stocker toutes les données :

| Store (table) | Contenu |
|---|---|
| `badges` | Tous les badges créés |
| `events` | Événements créés |
| `visitors` | Enregistrements de visites |
| `settings` | Paramètres de l'application |

> ⚠️ Les données sont stockées **localement dans le navigateur**. Elles ne sont pas synchronisées entre appareils. Un export de sauvegarde est recommandé régulièrement.

---

## Technologies utilisées

| Bibliothèque | Version | Usage |
|---|---|---|
| [QRCode.js](https://github.com/davidshimjs/qrcodejs) | 1.0.0 | Génération des QR codes |
| [html2canvas](https://html2canvas.hertzen.com/) | 1.4.1 | Capture des badges en image |
| [jsPDF](https://github.com/parallax/jsPDF) | 2.5.1 | Génération de PDF |
| [SheetJS (xlsx)](https://sheetjs.com/) | 0.18.5 | Import/Export Excel |
| [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) | — | Police principale |
| [JetBrains Mono](https://www.jetbrains.com/lp/mono/) | — | Police monospace (statistiques, codes) |

Toutes les dépendances sont chargées via **CDN (cdnjs.cloudflare.com)** — une connexion internet est requise au premier chargement.

---

## Utilisation sur mobile

L'application est entièrement responsive et optimisée pour les appareils mobiles :

- **PWA-ready** : balises meta `apple-mobile-web-app-capable` pour ajout à l'écran d'accueil (iOS)
- **Thème de couleur** : `#1a237e` (bleu foncé) pour la barre de statut mobile
- **Viewport** : verrouillé à `maximum-scale=1.0` pour éviter le zoom accidentel
- **Navigation inférieure** : 5 onglets (Accueil, Badges, Créer, Visiteurs, Événements)
- **Modales** : s'affichent en slide-up depuis le bas sur mobile, en fenêtre centrée sur desktop

---


