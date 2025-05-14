import DataTypes
import json



"""
class Goblin(DataTypes.Monster):
    def __init__(self, sub_name="Goblin"):
        super().__init__(
            "Goblin", 
            sub_name,
            DataTypes.Stats(
                strength=8,
                dexterity=14,
                constitution=10,
                intelligence=10,
                wisdom=8,
                charisma=8,
                hit_points=7,
                armor_class=15,
                speed=30
            ),
            [
                DataTypes.Attack(
                    name="Scimitar",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="slashing"
                ),
                DataTypes.Attack(
                    name="Shortbow",
                    attack_isranged=True,
                    attack_range=(80, 320),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                )
            ],
            [
                ("Stealth", 6)
            ],
            [
                ("Nimble Escape", "Goblin can take the Disengage or Hide action as a bonus action on each of its turns.")
            ]
        )   
class Kobold(DataTypes.Monster):
    def __init__(self, sub_name="Kobold"):
        super().__init__(
            "Kobold", 
            sub_name,
            DataTypes.Stats(
                strength=7,
                dexterity=15,
                constitution=9,
                intelligence=8,
                wisdom=7,
                charisma=8,
                hit_points=5,
                armor_class=12,
                speed=30
            ),
            [
                DataTypes.Attack(
                    name="Dagger",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=4,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                ),
                DataTypes.Attack(
                    name="Sling",
                    attack_isranged=True,
                    attack_range=(30, 120),
                    attack_bonus=4,
                    damage_dice_type=4,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="bludgeoning"
                )
            ],
            [
                ("Stealth", 6)
            ],
            [
                ("Pack Tactics", "Kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated.")
            ]
        )
class Skeleton(DataTypes.Monster):
    def __init__(self, sub_name="Skeleton"):
        super().__init__(
            "Skeleton", 
            sub_name,
            DataTypes.Stats(
                strength=10,
                dexterity=14,
                constitution=10,
                intelligence=1,
                wisdom=6,
                charisma=1,
                hit_points=13,
                armor_class=13,
                speed=30
            ),
            [
                DataTypes.Attack(
                    name="Shortsword",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                ),
                DataTypes.Attack(
                    name="Shortbow",
                    attack_isranged=True,
                    attack_range=(80, 320),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                )
            ],
            [
                ("Stealth", 2)
            ],
            [
                ("Undead Fortitude", "If damage reduces the skeleton to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the skeleton drops to 1 hit point instead.")
            ]
        )
class Zombie(DataTypes.Monster):
    def __init__(self, sub_name="Zombie"):
        super().__init__(
            "Zombie", 
            sub_name,
            DataTypes.Stats(
                strength=13,
                dexterity=6,
                constitution=16,
                intelligence=1,
                wisdom=3,
                charisma=1,
                hit_points=22,
                armor_class=8,
                speed=20
            ),
            [
                DataTypes.Attack(
                    name="Slam",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="bludgeoning"
                )
            ],
            [
                ("Stealth", -2)
            ],
            [
                ("Undead Fortitude", "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead.")
            ]
        )
class Hobgobline(DataTypes.Monster):
    def __init__(self, sub_name="Hobgoblin"):
        super().__init__(
            "Hobgoblin", 
            sub_name,
            DataTypes.Stats(
                strength=14,
                dexterity=12,
                constitution=14,
                intelligence=10,
                wisdom=11,
                charisma=9,
                hit_points=11,
                armor_class=18,
                speed=30
            ),
            [
                DataTypes.Attack(
                    name="Longsword",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=8,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="slashing"
                ),
                DataTypes.Attack(
                    name="Longbow",
                    attack_isranged=True,
                    attack_range=(150, 600),
                    attack_bonus=4,
                    damage_dice_type=8,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                )
            ],
            [
                ("Stealth", 2)
            ],
            [
                ("Martial Advantage", "Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated.")
            ]
        )
class Bugbear(DataTypes.Monster):
    def __init__(self, sub_name="Bugbear"):
        super().__init__(
            "Bugbear", 
            sub_name,
            DataTypes.Stats(
                strength=14,
                dexterity=12,
                constitution=16,
                intelligence=8,
                wisdom=11,
                charisma=10,
                hit_points=27,
                armor_class=16,
                speed=30
            ),
            [
                DataTypes.Attack(
                    name="Morningstar",
                    attack_isranged=False,
                    attack_range=(5, 5),
                    attack_bonus=4,
                    damage_dice_type=8,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                ),
                DataTypes.Attack(
                    name="Shortbow",
                    attack_isranged=True,
                    attack_range=(80, 320),
                    attack_bonus=4,
                    damage_dice_type=6,
                    damage_dice_amount=1,
                    damage_bonus=2,
                    damage_type="piercing"
                )
            ],
            [
                ("Stealth", 2)
            ],
            [
                ("Sneak Attack", "Once per turn, the bugbear can deal an extra 7 (2d6) damage to one creature it hits with an attack if that creature is within 5 feet of an ally of the bugbear that isn't incapacitated.")
            ]
        )
"""

__all__ = []
monsters = []
def prep_monsters():
    with open("/Users/ethanliscomb/Documents/DndSys/Monsters.json", "r") as file:
        monsters = json.load(file)
    for monster in monsters:
        __all__.append(monster)
    print(__all__[0].keys())
def new_monster(data, sub_name):
    return DataTypes.Monster(
                        data["name"],
                        sub_name,
                        DataTypes.Stats(
                            strength=data["stats"]["strength"],
                            dexterity=data["stats"]["dexterity"],
                            constitution=data["stats"]["constitution"],
                            intelligence=data["stats"]["intelligence"],
                            wisdom=data["stats"]["wisdom"],
                            charisma=data["stats"]["charisma"],
                            hit_points=data["stats"]["hit_points"],
                            armor_class=data["stats"]["armor_class"],
                            speed=data["stats"]["speed"]
                        ),
                        [
                            DataTypes.Attack(
                                name=attack["name"],
                                attack_isranged=attack["attack_isranged"],
                                attack_range=attack["attack_range"],
                                attack_bonus=attack["attack_bonus"],
                                damage_dice_type=attack["damage_dice_type"],
                                damage_dice_amount=attack["damage_dice_amount"],
                                damage_bonus=attack["damage_bonus"],
                                damage_type=attack["damage_type"]
                            )
                            for attack in data["attacks"]
                        ],
                        [
                            proficent_skills
                            for proficent_skills in data["proficient_skills"]
                        ],
                        [
                            special_action
                            for special_action in data["special_actions"]
                        ],
                        data["flavor_text"]
                    )









