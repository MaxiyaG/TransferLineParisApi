# TransferLineParisApi

FR 🇫🇷 | [EN](#english)

API Python (FastAPI) basée sur des données en Open Licence, fournissant des informations sur les stations du réseau ferré RATP à Paris (2021).

---

## Français

### Description
Ce projet expose une API FastAPI qui charge un fichier JSON de données publiques (RATP) et permet :
- d’obtenir les correspondances (lignes) associées à une station
- d’obtenir la liste des stations associées à une ligne

Le projet utilise le jeu de données **`trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`** issu de :
https://www.data.gouv.fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021

### Prérequis
- **Python >= 3.13**
- Dépendances Python (voir [`requierment.txt`](./requierment.txt))

### Jeu de données (obligatoire)
1. Télécharger le fichier **`trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`** depuis la page data.gouv.fr ci-dessus.
2. Placer le fichier **sans le renommer** dans le dossier :
   - `Dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`

Le code charge ce fichier via :
- `main.py` → `load_json("Dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json")`

### Installation
Créer un environnement virtuel (optionnel mais recommandé), puis installer les dépendances :

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requierment.txt
```

### Lancer l’API
Le point d’entrée FastAPI est `main.py` et l’objet FastAPI s’appelle `app`.

Exemple avec Uvicorn :

```bash
uvicorn main:app --reload
```

### Utilisation (exemples)
> Remarque : pour l’endpoint station, le code remplace les `_` par des espaces, puis met en majuscules.

#### 1) Correspondances / transferts par station
- **GET** `/get_transfer_by_station/{station}`

Exemple :

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/PORTE_DE_LA_VILLETTE"
```

Réponse (exemple) :

```json
[
  "Metro 7"
]
```

#### 2) Stations par ligne
- **GET** `/get_station_by_line/{line}`

Exemple (ligne “Metro 1”) :

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%201"
```

Réponse (exemple) :

```json
[
  "LA DEFENSE (GRANDE ARCHE)",
  "ESPLANADE DE LA DEFENSE",
  "PONT DE NEUILLY",
  "LES SABLONS",
  "PORTE MAILLOT",
  "ARGENTINE",
  "CHARLES DE GAULLE ETOILE",
  "GEORGE V",
  "FRANKLIN D. ROOSEVELT",
  "CHAMPS-ELYSEES CLEMENCEAU",
  "CONCORDE",
  "TUILERIES",
  "PALAIS ROYAL - MUSEE DU LOUVRE",
  "LOUVRE RIVOLI",
  "CHATELET",
  "HOTEL DE VILLE",
  "SAINT-PAUL (LE MARAIS)",
  "BASTILLE",
  "GARE DE LYON",
  "REUILLY-DIDEROT",
  "NATION",
  "PORTE DE VINCENNES",
  "SAINT-MANDE",
  "BERAULT",
  "CHATEAU DE VINCENNES"
]
```

> Important : les réponses exactes dépendent du fichier JSON téléchargé (contenu/format). Les exemples ci-dessus illustrent **le format** renvoyé par l’API (listes JSON).

### Licence des données / Attribution
Jeu de données : **Attributions**
- (Créateur) **RATP**
- (Éditeur) **RATP**
- Licence : **Licence Ouverte / Open Licence**

Source : https://www.data.gouv.fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021

---

## English

### Description
This project provides a FastAPI-based Python API that loads a public RATP dataset (Open Licence) and allows:
- retrieving transfers/lines for a given station
- retrieving stations for a given line

It uses the dataset **`trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`** from:
https://www.data.gouv.fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021

### Requirements
- **Python >= 3.13**
- Python dependencies (see [`requierment.txt`](./requierment.txt))

### Dataset (required)
1. Download **`trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`** from the data.gouv.fr page above.
2. Put the file **without renaming it** into:
   - `Dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json`

The code loads it from:
- `main.py` → `load_json("Dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json")`

### Installation
Create a virtual environment (optional but recommended), then install dependencies:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requierment.txt
```

### Run the API
The FastAPI entrypoint is `main.py` and the FastAPI instance is named `app`.

Example using Uvicorn:

```bash
uvicorn main:app --reload
```

### Usage (examples)
> Note: for the station endpoint, the code replaces `_` with spaces and then uppercases the station name.

#### 1) Transfers by station
- **GET** `/get_transfer_by_station/{station}`

Example:

```bash
curl "http://127.0.0.1:8000/get_transfer_by_station/PORTE_DE_LA_VILLETTE"
```

Response (example):

```json
[
  "Metro 7"
]
```

#### 2) Stations by line
- **GET** `/get_station_by_line/{line}`

Example (“Metro 1”):

```bash
curl "http://127.0.0.1:8000/get_station_by_line/Metro%201"
```

Response (example):

```json
[
  "LA DEFENSE (GRANDE ARCHE)",
  "ESPLANADE DE LA DEFENSE",
  "PONT DE NEUILLY",
  "LES SABLONS",
  "PORTE MAILLOT",
  "ARGENTINE",
  "CHARLES DE GAULLE ETOILE",
  "GEORGE V",
  "FRANKLIN D. ROOSEVELT",
  "CHAMPS-ELYSEES CLEMENCEAU",
  "CONCORDE",
  "TUILERIES",
  "PALAIS ROYAL - MUSEE DU LOUVRE",
  "LOUVRE RIVOLI",
  "CHATELET",
  "HOTEL DE VILLE",
  "SAINT-PAUL (LE MARAIS)",
  "BASTILLE",
  "GARE DE LYON",
  "REUILLY-DIDEROT",
  "NATION",
  "PORTE DE VINCENNES",
  "SAINT-MANDE",
  "BERAULT",
  "CHATEAU DE VINCENNES"
]
```

> Important: actual responses depend on the downloaded JSON file (its content/format). The examples above illustrate the **JSON format** returned by the API (JSON lists).

### Data license / Attribution
Dataset: **Attributions**
- (Creator) **RATP**
- (Publisher) **RATP**
- License: **Licence Ouverte / Open Licence**

Source: https://www.data.gouv.fr/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021
