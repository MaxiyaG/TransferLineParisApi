import json
from typing import Any, Dict, List
from pprint import pprint

def load_json(path: str) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def dico_station_line(tab_json: list) -> Dict[str, str]:
    dico = {}
    for station in tab_json:
        k = station['station']
        v = [
            station['correspondance_1'],
            station['correspondance_2'],
            station['correspondance_3'],
            station['correspondance_4'],
            station['correspondance_5']
        ]

        tab = []
        for transfer in v:
            if transfer is not None:
                if transfer.isdigit():
                    transfer = "Metro "+ transfer
                elif transfer.isalpha():
                    transfer = "RER "+ transfer
                
                elif "bis" in transfer:
                    transfer = "Metro "+ transfer

                else:
                    raise ValueError(f"{transfer} : Error with this name")

            if transfer:
                tab.append(transfer)
        

        dico[k] = tab

    return dico

    
def get_line_list(dico: dict[str, List[str]]) -> List[str]:
    dico_line = [v[0] for v in dico.values() if len(v) == 1]
    
    tab_line = []
    for line in dico_line:
        if line not in tab_line:
            tab_line.append(line)
    
    return tab_line

def get_all_station_by_line(dico: dict[str, List[str]]) -> dict[str, List[str]]:
    line_dict = {}
    lines = get_line_list(dico)

    for line in lines:
        line_dict[line] = []

    for station, station_lines in dico.items():
        for line in station_lines:
            if line in line_dict:
                line_dict[line].append(station)
            else:
                line_dict[line] = [station]  

    return line_dict
        

def get_station_by_line(dico: dict[str, List[str]], key: str) -> dict[str, List[str]]:
    dico = get_all_station_by_line(dico)
    try: 
        return dico[key]
    except:
        print("Key not exist, try for exemple 'Metro 1-14' or RER A-B")
        return {}


def transfer_by_station(dico: dict[str, List[str]], key: str) -> dict[str, List[str]]:
    try: 
        return dico[key]
    except:
        print("Key not exist, try for exemple 'PORTE_DE_LA_VILLETTE")
        return {}

