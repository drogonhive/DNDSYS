import Classes as C
import json
import os
import Variables as V

"""
    JSON file functions
"""
def get_json():
    file_path = os.path.join(os.path.dirname(__file__), 'Save.json')

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def save_json(data):
    file_path = os.path.join(os.path.dirname(__file__), 'Save.json')

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
def reset_json():
    V.json_data = {
        "monsters": {

        },
    }
def reset_json_part(part):
    V.json_data[part] = {}
def monster_json(data, sub_name = None):
    return C.Monster(
        name=data["name"],
        sub_name=sub_name,
        flavor_text=data["flavor_text"],
        stats=C.Stats(
            hit_points=data["stats"]["hit_points"],
            armor_class=data["stats"]["armor_class"],
            speed=data["stats"]["speed"],
            strength=data["stats"]["strength"],
            dexterity=data["stats"]["dexterity"],
            constitution=data["stats"]["constitution"],
            intelligence=data["stats"]["intelligence"],
            wisdom=data["stats"]["wisdom"],
            charisma=data["stats"]["charisma"]
        ),
        proficient_skills=[[skill, modifier] for skill, modifier in data["proficient_skills"]],
        attacks=[C.Attack(
            name=attack["name"],
            attack_isranged=attack["attack_isranged"],
            attack_range=attack["attack_range"],
            attack_bonus=attack["attack_bonus"],
            damage_dice_type=attack["damage_dice_type"],
            damage_dice_amount=attack["damage_dice_amount"],
            damage_bonus=attack["damage_bonus"],
            damage_type=attack["damage_type"]
        ) for attack in data["attacks"]],
        special_actions=[[action, description] for action, description in data["special_actions"]]
    )
    
"""
    Formatting functions
"""
def title(text):
    print(f"\n{text}\n")
def br():
    print("\n")
def hr(t = False):
    if t:
        print("--------------------------------------------------")
    return "--------------------------------------------------"
def hr2(t = False):
    if t:
        print("==================================================")
    return "=================================================="
def hr3(t = False):
    if t:
        print("<><><><><><><><><><><><><><><><><><><><><><><><><>")
    return "<><><><><><><><><><><><><><><><><><><><><><><><><>"
"""
    Setup functions
"""
def setup_dice():
    V.dice = {
        "d4": C.Dice(4),
        "d6": C.Dice(6),
        "d8": C.Dice(8),
        "d10": C.Dice(10),
        "d12": C.Dice(12),
        "d20": C.Dice(20),
        "d100": C.Dice(100)
    }
def setup_menus():
    V.menus = {
        "Main": [
            "Exit",
            "Reset Data",
            "Save Data",
            "Load Data",
            "Monster",
            "Dice",
            "Initiative",
        ],
        "Reset Data": [
            "Main",
            ("Clear JSON", reset_json()),
        ],
        "Save Data": [
            "Main",
            ("Save JSON", save_json(V.json_data)),
        ],
        "Load Data": [
            "Main",
            ("Load JSON", get_json()),
        ],
        "Monster": [
            "Main",
            ("View Monsters", print_monsters()),
            ("Reset Monsters", reset_json_part("monsters")),
            "Add Monster",
            "Remove Monster",
            "Edit Monster",
        ],
        "Dice": [
            "Main",
            "Reset Dice"
            "Roll Dice",
            "View Dice",
            "Add Dice",
            "Remove Dice",
            "Set Modifier"
        ]
    }
"""
    Runtime Functions
"""
def print_monsters():
    if V.json_data["monsters"] == {}:
        print("No monsters found.")
        return False
    for i, monster in enumerate(V.json_data["monsters"]):
        print(f"{i + 1}. {monster}")
    return True
def new_monster(name, flavor_text, stats, proficient_skills, attacks, special_actions):
    return {
        "name": name,
        "flavor_text": flavor_text,
        "stats": {
            "hit_points": stats.hit_points,
            "armor_class": stats.armor_class,
            "speed": stats.speed,
            "strength": stats.strength,
            "dexterity": stats.dexterity,
            "constitution": stats.constitution,
            "intelligence": stats.intelligence,
            "wisdom": stats.wisdom,
            "charisma": stats.charisma
        },
        "proficient_skills": [
            [skill, modifier] for skill, modifier in proficient_skills
        ],
        "attacks": [
            {
                "name": attack.name,
                "attack_isranged": attack.attack_isranged,
                "attack_range": attack.attack_range,
                "attack_bonus": attack.attack_bonus,
                "damage_dice_type": attack.damage_dice_type,
                "damage_dice_amount": attack.damage_dice_amount,
                "damage_bonus": attack.damage_bonus,
                "damage_type": attack.damage_type
            } for attack in attacks
        ],
        "special_actions": [
            [action, description] for action, description in special_actions
        ]
    }




