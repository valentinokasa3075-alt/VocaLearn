import json
import os

# absoluter Pfad zu dem Ordner, in dem diese Datei liegt
BASIS_ORDNER = os.path.dirname(os.path.abspath(__file__))

# kompletter Pfad zur JSON-Datei
DATEI_PFAD = os.path.join(BASIS_ORDNER, "vocalearn_data.json")


def lade_vokabeln():
    try:
        with open(DATEI_PFAD, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        return []


def speichere_vokabeln(vokabeln):
    with open(DATEI_PFAD, "w", encoding="utf-8") as datei:
        json.dump(vokabeln, datei, indent=4, ensure_ascii=False)