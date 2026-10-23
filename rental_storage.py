import json
import os


def save_equipments(equipment):
    with open("equipment.json", "w", encoding="utf-8") as file:
        json.dump(equipment, file, indent=4, ensure_ascii=False)

def load_equipments():
    if not os.path.exists("equipment.json"):
        return []

    with open("equipment.json", "r", encoding="utf-8") as file:
        equipments = json.load(file)
    return equipments

