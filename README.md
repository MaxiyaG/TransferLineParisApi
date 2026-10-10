TransferLineApi – API de réseau de métro fictif

API REST développée avec FastAPI permettant d'interroger les lignes et correspondances associées à une station ainsi que les stations associées à une ligne d'un réseau de métro entièrement fictif.

⚠️ Projet fictif : le réseau comporte 20 lignes de métro nommées d'après des couleurs et plus de 300 stations inventées. Toutes les données sont générées par une IA. Aucune donnée réelle n'a été utilisée. Ce projet n'est affilié à aucun opérateur de transport.
Français
Sommaire
Présentation
Fonctionnalités
Structure du projet
Installation
Utilisation
Endpoints de l'API
Exemples
Données
Licence
Présentation

TransferLineApi est une API de démonstration construite avec FastAPI. Elle charge un jeu de données JSON décrivant un réseau de métro fictif, puis expose deux points d'entrée principaux :

Obtenir les lignes et correspondances d'une station.
Obtenir la liste des stations desservies par une ligne.

L'API génère automatiquement une documentation interactive avec Swagger UI et ReDoc.

Fonctionnalités
🔍 Recherche des lignes et correspondances d'une station, insensible à la casse et acceptant les underscores.
🚇 Recherche des stations desservies par une ligne.
📚 Documentation interactive intégrée (/docs et /redoc).
⚠️ Gestion des erreurs HTTP 404 avec des messages explicites.
🧪 Données 100 % fictives, idéales pour l'apprentissage et les tests.
Structure du projet
.
├── Dataset/
│   ├── Dataset.py          # Fonctions de chargement et de transformation des données
│   └── reseau.json         # Jeu de données fictif (stations, correspondances)
├── main.py                 # Application FastAPI (routes, documentation)
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet

Installation
Prérequis
Python 3.9 ou supérieur
pip
Étapes
Cloner le dépôt ou télécharger les fichiers :
   git clone https://github.com/votre-utilisateur/TransferLineApi.git
   cd TransferLineApi

Créer et activer un environnement virtuel (recommandé) :
   python -m venv venv


Sous Linux ou macOS :

   source venv/bin/activate


Sous Windows :

   venv\Scripts\activate

Installer les dépendances :
   pip install -r requirements.txt

Utilisation

Lancer le serveur de développement avec Uvicorn :

uvicorn main:app --reload

main : nom du fichier main.py.
app : instance FastAPI créée dans ce fichier.
--reload : redémarre automatiquement le serveur à chaque modification, en mode développement.

Le serveur démarre par défaut à l'adresse http://127.0.0.1:8000.

Documentation interactive
Swagger UI : http://127.0.0.1:8000/docs
ReDoc : http://127.0.0.1:8000/redoc
Endpoints de l'API
Méthode	Route	Description
GET	/	Message de bienvenue et liste des endpoints.
GET	/get_transfer_by_station/{station}	Lignes et correspondances d'une station.
GET	/get_station_by_line/{line}	Stations desservies par une ligne.
Paramètres
{station} : nom de la station. Les underscores (_) sont remplacés par des espaces et la casse est ignorée.
Exemple : PLACE_YVOIVANE → PLACE YVOIVANE.
{line} : nom de la ligne tel qu'il apparaît dans le jeu de données.
Exemples : Metro Rouge, Metro Bleu-Ciel.
⚠️ Les espaces et caractères spéciaux doivent être encodés dans l'URL (par exemple, %20 pour un espace).
Exemples
1. Obtenir les correspondances d'une station

Requête :

curl "http://127.0.0.1:8000/get_transfer_by_station/PLACE_YVOIVANE"


Réponse (JSON) :

[
  "Metro Vert",
  "Metro Rose",
  "Metro Rose-Poudre"
]


La station PLACE YVOIVANE est desservie par les lignes Vert, Rose et Rose-Poudre.

2. Obtenir les stations d'une ligne

Requête :

curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Rouge"


Réponse (JSON) :

[
  "COLLINE DE TORELUNE",
  "PORTE DE BRINARETH",
  "MARE D'ALLIMIRE",
  "PLACE LOMRIRETH",
  "SYLINNE"
]


La ligne Metro Rouge dessert toutes les stations listées.

3. Station inexistante

Requête :

curl "http://127.0.0.1:8000/get_transfer_by_station/STATION_INCONNUE"


Réponse (HTTP 404) :

{
  "detail": "Station introuvable : STATION_INCONNUE"
}

4. Ligne inexistante

Requête :

curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Inconnu"


Réponse (HTTP 404) :

{
  "detail": "Ligne introuvable : Metro Inconnu"
}

Données

Le fichier Dataset/reseau.json contient une liste d'objets représentant les stations. Chaque objet possède notamment les champs suivants :

station : nom de la station (par exemple, "PLACE YVOIVANE").
correspondance_1 à correspondance_5 : noms de lignes (par exemple, "vert", "rose-poudre") ou null.
trafic, ville, etc. : autres informations associées aux stations.
Transformation des données

Le module Dataset/Dataset.py transforme les données brutes :

Les noms des lignes sont normalisés : "vert" → "Metro Vert", "rose-poudre" → "Metro Rose-Poudre", etc.
Un index par station est créé : dico_station_line.
Un index par ligne est généré à la demande avec get_all_station_by_line.
Licence

Ce projet est distribué sous licence MIT.

MIT License

Copyright (c) 2025 MaxiyaG


Projet réalisé dans le cadre de l'apprentissage de FastAPI. Les données sont fictives et ne représentent aucun réseau réel.

English
Table of Contents
Overview
Features
Project Structure
Installation
Usage
API Endpoints
Examples
Data
License
Overview

TransferLineApi is a demonstration REST API built with FastAPI. It loads a JSON dataset describing a fictional metro network and exposes two main endpoints:

Retrieve the lines and transfer connections associated with a station.
Retrieve the list of stations served by a line.

FastAPI automatically provides interactive API documentation through Swagger UI and ReDoc.

⚠️ Fictional project: The network consists of 20 metro lines named after colors and more than 300 fictional stations. All data was generated by AI. No real-world data was used. This project is not affiliated with any public transportation operator.
Features
🔍 Search for the lines and transfer connections serving a station, with case-insensitive matching and underscore support.
🚇 Retrieve all stations served by a specific line.
📚 Built-in interactive documentation (/docs and /redoc).
⚠️ HTTP 404 error handling with descriptive error messages.
🧪 100% fictional data, suitable for learning, experimentation, and testing.
Project Structure
.
├── Dataset/
│   ├── Dataset.py          # Data loading and transformation functions
│   └── reseau.json         # Fictional dataset (stations and connections)
├── main.py                 # FastAPI application (routes and documentation)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Installation
Requirements
Python 3.9 or later
pip
Steps
Clone the repository or download the project files:
   git clone https://github.com/votre-utilisateur/TransferLineApi.git
   cd TransferLineApi


Replace votre-utilisateur with the appropriate GitHub username or repository owner.

Create and activate a virtual environment (recommended):
   python -m venv venv


On Linux or macOS:

   source venv/bin/activate


On Windows:

   venv\Scripts\activate

Install the dependencies:
   pip install -r requirements.txt

Usage

Start the development server with Uvicorn:

uvicorn main:app --reload

main: the name of the main.py file.
app: the FastAPI application instance defined in that file.
--reload: automatically restarts the server whenever a file changes (development mode).

By default, the server runs at http://127.0.0.1:8000.

Interactive Documentation
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
API Endpoints
Method	Route	Description
GET	/	Welcome message and list of available endpoints.
GET	/get_transfer_by_station/{station}	Retrieve the lines and transfer connections associated with a station.
GET	/get_station_by_line/{line}	Retrieve the stations served by a line.
Parameters
{station}: the station name. Underscores (_) are replaced with spaces, and matching is case-insensitive.
Example: PLACE_YVOIVANE → PLACE YVOIVANE.
{line}: the line name as it appears in the dataset.
Examples: Metro Rouge, Metro Bleu-Ciel.
⚠️ Spaces and special characters must be URL-encoded (for example, %20 for a space).
Examples
1. Retrieve the transfer connections for a station

Request:

curl "http://127.0.0.1:8000/get_transfer_by_station/PLACE_YVOIVANE"


Response (JSON):

[
  "Metro Vert",
  "Metro Rose",
  "Metro Rose-Poudre"
]


The PLACE YVOIVANE station is served by the Green, Pink, and Powder Pink lines (Metro Vert, Metro Rose, and Metro Rose-Poudre).

2. Retrieve the stations served by a line

Request:

curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Rouge"


Response (JSON):

[
  "COLLINE DE TORELUNE",
  "PORTE DE BRINARETH",
  "MARE D'ALLIMIRE",
  "PLACE LOMRIRETH",
  "SYLINNE"
]


The Metro Rouge line serves all the stations listed above.

3. Non-existent station

Request:

curl "http://127.0.0.1:8000/get_transfer_by_station/STATION_INCONNUE"


Response (HTTP 404):

{
  "detail": "Station introuvable : STATION_INCONNUE"
}


The API returns an HTTP 404 error when the requested station cannot be found.

4. Non-existent line

Request:

curl "http://127.0.0.1:8000/get_station_by_line/Metro%20Inconnu"


Response (HTTP 404):

{
  "detail": "Ligne introuvable : Metro Inconnu"
}


The API returns an HTTP 404 error when the requested line cannot be found.

Data

The Dataset/reseau.json file contains a list of station objects. Each object includes fields such as:

station: the station name (for example, "PLACE YVOIVANE").
correspondance_1 to correspondance_5: line names (for example, "vert", "rose-poudre") or null.
trafic, ville, etc.: additional station-related information.
Data Transformation

The Dataset/Dataset.py module processes the raw data:

Line names are normalized: "vert" → "Metro Vert", "rose-poudre" → "Metro Rose-Poudre", and so on.
A station-based index is created: dico_station_line.
A line-based index is generated on demand using get_all_station_by_line.
License

This project is distributed under the MIT License.

MIT License

Copyright (c) 2025 MaxiyaG


This project was created as part of learning FastAPI. All data is fictional and does not represent any real-world metro network.
