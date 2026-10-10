<a id="top"></a>

**🌐 Langue / Language :** [🇫🇷 Français](#fr) · [🇬🇧 English](#en)

---

<a id="fr"></a>

# TransferLineApi – API de réseau de métro fictif

API REST développée avec **FastAPI** permettant d'interroger les **lignes / correspondances associées à une station** et les **stations associées à une ligne** d'un réseau de métro **entièrement fictif**.

> ⚠️ **Projet fictif** : le réseau comporte 20 lignes de métro nommées d'après des couleurs et plus de 300 stations inventées. Toutes les données sont générées par une IA. Aucune donnée réelle n'a été utilisée. Ce projet n'est affilié à aucun opérateur de transport.

---

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Endpoints de l'API](#endpoints-de-lapi)
- [Exemples](#exemples)
- [Données](#données)
- [Licence](#licence)

---

## Présentation

**TransferLineApi** est une API de démonstration construite avec FastAPI. Elle charge un jeu de données JSON décrivant un réseau de métro fictif, puis expose deux points d'entrée principaux :

- Obtenir les lignes et correspondances d'une station.
- Obtenir la liste des stations desservies par une ligne.

L'API génère automatiquement une documentation interactive (Swagger UI et ReDoc).

---

## Fonctionnalités

- 🔍 Recherche des lignes/correspondances d'une station (insensible à la casse, underscores acceptés).
- 🚇 Recherche des stations d'une ligne.
- 📚 Documentation interactive intégrée (`/docs` et `/redoc`).
- ⚠️ Gestion des erreurs 404 avec messages explicites.
- 🧪 Données 100 % fictives, idéales pour l'apprentissage ou les tests.

---

## Structure du projet

```
.
├── Dataset/
│   ├── Dataset.py          # Fonctions de chargement et de transformation des données
│   └── reseau.json         # Jeu de données fictif (stations, correspondances)
├── main.py                 # Application FastAPI (routes, documentation)
├── requirements.txt        # Dépendances Python
└── README.md               # Ce fichier
```

---

## Installation

### Prérequis

- Python 3.9 ou supérieur
- pip

### Étapes

1. **Cloner le dépôt** (ou télécharger les fichiers) :

```bash
   git clone https://github.com/MaxiyaG/TransferLineParisApi.git
   cd TransferLineParisApi
```

2. **Créer et activer un environnement virtuel** (recommandé) :

```bash
   python -m venv venv
   # Sous Linux / macOS :
   source venv/bin/activate
   # Sous Windows :
   venv\Scripts\activate
```

3. **Installer les dépendances** :

```bash
   pip install -r requirements.txt
```

---

## Utilisation

Lancez le serveur de développement avec **Uvicorn** :

```bash
uvicorn main:app --reload
```

- `main` : nom du fichier `main.py`
- `app` : instance FastAPI créée dans ce fichier
- `--reload` : redémarre automatiquement le serveur à chaque modification (développement)

Le serveur démarre par défaut sur `http://127.0.0.1:8000`.

### Documentation interactive

- **Swagger UI** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints de l'API

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET` | `/` | Message de bienvenue et liste des endpoints. |
| `GET` | `/get_transfer_by_station/{station}` | Lignes / correspondances d'une station. |
| `GET` | `/get_station_by_line/{line}` | Stations desservies par une ligne. |

### Paramètres

- `{station}` : nom de la station. Les underscores (`_`) sont remplacés par des espaces. La casse est ignorée.
  - Exemple : `PLACE_YVOIVANE` → `PLACE YVOIVANE`
- `{line}` : nom de la ligne tel qu'il apparaît dans le jeu de données.
  - Exemple : `Metro Rouge`, `Metro Bleu-Ciel`
  - ⚠️ Les espaces et caractères spéciaux doivent être encodés dans l'URL (ex. `%20` pour un espace).

---

## Exemples

### 1. Obtenir les correspondances d'une station

**Requête** :

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/PLACE_YVOIVANE"
```

**Réponse** (JSON) :

```json
[
  "Metro Vert",
  "Metro Rose",
  "Metro Rose-Poudre"
]
```

> La station `PLACE YVOIVANE` est desservie par les lignes Vert, Rose et Rose-Poudre.

### 2. Obtenir les stations d'une ligne

**Requête** :

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Rouge"
```

**Réponse** (JSON) :

```json
[
  "COLLINE DE TORELUNE",
  "PORTE DE BRINARETH",
  "MARE D'ALLIMIRE",
  "PLACE LOMRIRETH",
  "SYLINNE"
]
```

> La ligne `Metro Rouge` dessert toutes les stations listées.

### 3. Station inexistante

**Requête** :

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/STATION_INCONNUE"
```

**Réponse** (HTTP 404) :

```json
{
  "detail": "Station introuvable : STATION_INCONNUE"
}
```

### 4. Ligne inexistante

**Requête** :

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Inconnu"
```

**Réponse** (HTTP 404) :

```json
{
  "detail": "Ligne introuvable : Metro Inconnu"
}
```

---

## Données

Le fichier `Dataset/reseau.json` contient une liste d'objets station. Chaque objet possède notamment :

- `station` : nom de la station (ex. `"PLACE YVOIVANE"`)
- `correspondance_1` à `correspondance_5` : noms de lignes (ex. `"vert"`, `"rose-poudre"`) ou `null`
- `trafic`, `ville`, etc.

### Transformation

Le module `Dataset.py` transforme ces données brutes :

- Les noms de lignes sont normalisés : `"vert"` → `"Metro Vert"`, `"rose-poudre"` → `"Metro Rose-Poudre"`, etc.
- Un index par station est créé : `dico_station_line`.
- Un index par ligne est généré à la volée : `get_all_station_by_line`.

---

## Licence

Ce projet est distribué sous **licence MIT**.

```
MIT License

Copyright (c) 2025 MaxiyaG
```

---

*Projet réalisé dans le cadre d'un apprentissage de FastAPI. Les données sont fictives et ne représentent aucun réseau réel.*

[⬆ Retour en haut](#top)

---
---

<a id="en"></a>

# TransferLineApi – Fictional Metro Network API

A REST API built with **FastAPI** that lets you query the **lines / transfers available at a station** and the **stations served by a line** in an **entirely fictional** metro network.

> ⚠️ **Fictional project**: the network has 20 metro lines named after colors and over 300 made-up stations. All data was generated by an AI. No real-world data was used. This project is not affiliated with any transport operator.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Data](#data)
- [License](#license)

---

## Overview

**TransferLineApi** is a demo API built with FastAPI. It loads a JSON dataset describing a fictional metro network and exposes two main endpoints:

- Get the lines and transfers available at a station.
- Get the list of stations served by a line.

The API automatically generates interactive documentation (Swagger UI and ReDoc).

---

## Features

- 🔍 Look up the lines/transfers of a station (case-insensitive, underscores accepted).
- 🚇 Look up the stations of a line.
- 📚 Built-in interactive documentation (`/docs` and `/redoc`).
- ⚠️ Clear 404 error handling with explicit messages.
- 🧪 100% fictional data, ideal for learning or testing.

---

## Project Structure

```
.
├── Dataset/
│   ├── Dataset.py          # Data loading and transformation functions
│   └── reseau.json         # Fictional dataset (stations, transfers)
├── main.py                 # FastAPI application (routes, documentation)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Setup

### Prerequisites

- Python 3.9 or higher
- pip

### Steps

1. **Clone the repository** (or download the files):

```bash
   git clone https://github.com/MaxiyaG/TransferLineParisApi.git
   cd TransferLineParisApi
```

2. **Create and activate a virtual environment** (recommended):

```bash
   python -m venv venv
   # On Linux / macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
```

3. **Install the dependencies**:

```bash
   pip install -r requirements.txt
```

---

## Usage

Start the development server with **Uvicorn**:

```bash
uvicorn main:app --reload
```

- `main`: the name of the `main.py` file
- `app`: the FastAPI instance created in that file
- `--reload`: automatically restarts the server on every change (development only)

By default, the server runs at `http://127.0.0.1:8000`.

### Interactive Documentation

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Welcome message and list of endpoints. |
| `GET` | `/get_transfer_by_station/{station}` | Lines / transfers of a station. |
| `GET` | `/get_station_by_line/{line}` | Stations served by a line. |

### Parameters

- `{station}`: the station name. Underscores (`_`) are replaced with spaces. Case is ignored.
  - Example: `PLACE_YVOIVANE` → `PLACE YVOIVANE`
- `{line}`: the line name as it appears in the dataset.
  - Example: `Metro Rouge`, `Metro Bleu-Ciel`
  - ⚠️ Spaces and special characters must be URL-encoded (e.g. `%20` for a space).

---

## Examples

> Note: the API's error messages are returned in French.

### 1. Get the transfers of a station

**Request**:

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/PLACE_YVOIVANE"
```

**Response** (JSON):

```json
[
  "Metro Vert",
  "Metro Rose",
  "Metro Rose-Poudre"
]
```

> The `PLACE YVOIVANE` station is served by the Green, Pink and Powder Pink lines.

### 2. Get the stations of a line

**Request**:

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Rouge"
```

**Response** (JSON):

```json
[
  "COLLINE DE TORELUNE",
  "PORTE DE BRINARETH",
  "MARE D'ALLIMIRE",
  "PLACE LOMRIRETH",
  "SYLINNE"
]
```

> The `Metro Rouge` (Red) line serves all the stations listed.

### 3. Unknown station

**Request**:

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/STATION_INCONNUE"
```

**Response** (HTTP 404):

```json
{
  "detail": "Station introuvable : STATION_INCONNUE"
}
```

### 4. Unknown line

**Request**:

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Inconnu"
```

**Response** (HTTP 404):

```json
{
  "detail": "Ligne introuvable : Metro Inconnu"
}
```

---

## Data

The `Dataset/reseau.json` file contains a list of station objects. Each object includes:

- `station`: the station name (e.g. `"PLACE YVOIVANE"`)
- `correspondance_1` to `correspondance_5`: line names (e.g. `"vert"`, `"rose-poudre"`) or `null`
- `trafic`, `ville`, etc.

### Data Transformation

The `Dataset.py` module transforms this raw data:

- Line names are normalized: `"vert"` → `"Metro Vert"`, `"rose-poudre"` → `"Metro Rose-Poudre"`, etc.
- A per-station index is built: `dico_station_line`.
- A per-line index is generated on the fly: `get_all_station_by_line`.

---

## License

This project is released under the **MIT License**.

```
MIT License

Copyright (c) 2025 MaxiyaG
```

---

*Project created as a way to learn FastAPI. The data is fictional and does not represent any real network.*

[⬆ Back to top](#top)
