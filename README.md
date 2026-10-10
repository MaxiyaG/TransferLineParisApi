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
   git clone https://github.com/votre-utilisateur/TransferLineApi.git
   cd TransferLineApi
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