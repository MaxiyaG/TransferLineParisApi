from fastapi import FastAPI, HTTPException, Path

from Dataset.Dataset import (
    load_json,
    dico_station_line,
    transfer_by_station,
    get_station_by_line as get_station_by_line_from_dico,
)

DATASET_PATH = "Dataset/reseau.json"

data = load_json(DATASET_PATH)
dico = dico_station_line(data)


DESCRIPTION = """
API permettant d'interroger les **lignes / correspondances associées à une station**
et les **stations associées à une ligne** d'un **réseau de métro entièrement fictif**.

*API to query the lines/transfers of a station and the stations of a line
of a **fully fictional** metro network.*

## 🎨 Projet fictif / Fictional project

Le réseau comporte **20 lignes de métro** nommées d'après des couleurs
(Rouge, Bleu, Bleu-Ciel…) et plus de **300 stations inventées**.

Tous les noms, lignes, correspondances et chiffres de trafic sont imaginaires.
Toute ressemblance avec une station, une ligne ou un réseau existant
serait purement fortuite.

*The network has **20 metro lines** named after colors and 300+ **invented stations**.
All names, lines, transfers and traffic figures are made up.*

Ce projet n'est lié à aucun opérateur de transport, ni exploité,
approuvé ou sponsorisé par l'un d'eux.

*This project is not affiliated with any transport operator.*

## Source des données / Data source

- **Jeu de données** : `Dataset/reseau.json`
- **Origine** : généré par une IA, de A à Z. Aucune donnée réelle n'a été reprise.
- **Format** : une entrée par station, avec jusqu'à 5 correspondances
  (`correspondance_1` à `correspondance_5`).
- **Transformation** : les données sont restructurées par ce projet
  (index par station et par ligne).

*Dataset generated entirely by an AI. No real-world data was used.*

## Limites / Limitations

Les données sont **fictives** : elles ne décrivent aucun réseau réel
et ne doivent servir qu'à des démonstrations, des tests ou de l'apprentissage.

*Data is **fictional**: it describes no real network and is meant for demos,
tests and learning only.*

## Licence MIT
"""

# App FastAPI
app = FastAPI(
    title="TransferLineApi (réseau fictif)",
    description=DESCRIPTION,
    version="2.0.0",
    license_info={
        "name": "MIT",
        "identifier": "MIT",
    },
)

# Route
@app.get(
    "/",
    summary="Accueil de l'API",
    tags=["Accueil"],
)
def root():
    return {
        "message": "Bienvenue sur TransferLineApi !",
        "description": (
            "API permettant de rechercher les lignes et correspondances "
            "d'une station et les stations d'une ligne."
        ),
        "version": "2.0.0",
        "dataset": DATASET_PATH,
        "documentation": "/docs",
        "documentation_alternative": "/redoc",
        "endpoints": {
            "station": "/get_transfer_by_station/{station}",
            "ligne": "/get_station_by_line/{line}",
        },
    }



# GET Lignes / correspondances d'une station
@app.get(
    "/get_transfer_by_station/{station}",
    summary="Lignes / correspondances d'une station",
    tags=["Stations"],
)
def get_transfer_by_station(
    station: str = Path(
        description=(
            "Nom de la station. Les underscores sont remplacés par des espaces "
            "(ex. PLACE_YVOIVANE). La casse est ignorée."
        ),
        examples=["PLACE_YVOIVANE"],
    ),
):
    # Conversion des underscores en espaces et conversion en majuscules
    name = station.replace("_", " ").upper()

    # Recherche de la station
    res = transfer_by_station(dico, name)

    # Station inexistante
    if not res:
        raise HTTPException(
            status_code=404,
            detail=f"Station introuvable : {station}",
        )
    return res


# GET Stations d'une ligne
@app.get(
    "/get_station_by_line/{line}",
    summary="Stations d'une ligne",
    tags=["Lignes"],
)
def get_station_by_line(
    line: str = Path(
        description=(
            "Nom de la ligne tel qu'il apparaît dans le jeu de données "
            "(ex. « Metro Rouge », « Metro Bleu-Ciel »)."
        ),
        examples=["Metro Rouge"],
    ),
):
    # Recherche des stations de la ligne
    res = get_station_by_line_from_dico(dico, line)

    # Ligne inexistante
    if not res:
        raise HTTPException(
            status_code=404,
            detail=f"Ligne introuvable : {line}",
        )
    return res
