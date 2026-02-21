from Dataset.Dataset import load_json, dico_station_line, get_station_by_line, transfer_by_station
from fastapi import FastAPI, Path

json = load_json("Dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021.json")
dico = dico_station_line(json)

app = FastAPI()

@app.get("/get_transfer_by_station/{station}")
def get_transfer_by_station(station: str):
    station = station.replace("_", " ")
    station = station.upper()
    res = transfer_by_station(dico, station)

    if res: 
        return res
    
    return None
    

@app.get("/get_station_by_line/{line}")
def get_station_by_line(line: str):
    res = get_station_by_line(dico, line)

    if res: 
        return res
    
    return None



