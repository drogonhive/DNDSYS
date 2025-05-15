import secrets

class Monster:
    def __init__(
            self,
            name,
            sub_name,
            flavor_text,
            stats,
            proficient_skills,
            attacks,
            special_actions,
    ):
        self.name = name
        self.sub_name = sub_name
        self.flavor_text = flavor_text
        self.stats = stats
        self.proficient_skills = proficient_skills
        self.attacks = attacks
        self.special_actions = special_actions
        self.local_vars = {
            "count1": 0,
            "count2": 0,
            "count3": 0,

        }
    def __str__(self):
        hr = "=================================================="
        return "".join((
            hr,
            f"\n {self.name} ({self.sub_name})\n",
            f" Flavor Text: {self.flavor_text}\n",
            hr,
            f"\n Stats:\n{self.stats}\n",
            hr,
            f"\n Proficient Skills: \n{"\n".join([
                f'  {skill[0]}: {skill[1]}' for skill in self.proficient_skills
            ])}\n",
            hr,
            f"\n Attacks: \n{"\n".join([
                f'  {attack.name}: Ranged - {attack.attack_isranged} ({attack.attack_range[0]}-{attack.attack_range[1]})\n'
                f'    Attack Bonus: {attack.attack_bonus}\n'
                f'    Damage: {attack.damage_dice_amount}d{attack.damage_dice_type} + {attack.damage_bonus} ({attack.damage_type})'
                for attack in self.attacks
            ])}\n",
            hr,
            f"\n Special Actions: \n{"\n".join([
                f'  {action[0]}: {action[1]}' for action in self.special_actions
            ])}\n",
            hr,
        ))   
class Stats:
    def __init__(self, hit_points, armor_class, speed, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.hit_points = hit_points
        self.hit_points_max = hit_points
        self.armor_class = armor_class
        self.speed = speed
        self.strength = strength
        self.strength_modifier = (strength - 10) // 2
        self.dexterity = dexterity
        self.dexterity_modifier = (dexterity - 10) // 2
        self.constitution = constitution
        self.constitution_modifier = (constitution - 10) // 2
        self.intelligence = intelligence
        self.intelligence_modifier = (intelligence - 10) // 2
        self.wisdom = wisdom
        self.wisdom_modifier = (wisdom - 10) // 2
        self.charisma = charisma
        self.charisma_modifier = (charisma - 10) // 2
    def __str__(self):
        return (
            f"  Hit Points: {self.hit_points}/{self.hit_points_max}\n"
            f"  Armor Class: {self.armor_class}\n"
            f"  Speed: {self.speed}\n"
            f"  Strength: {self.strength} ({self.strength_modifier})\n"
            f"  Dexterity: {self.dexterity} ({self.dexterity_modifier})\n"
            f"  Constitution: {self.constitution} ({self.constitution_modifier})\n"
            f"  Intelligence: {self.intelligence} ({self.intelligence_modifier})\n"
            f"  Wisdom: {self.wisdom} ({self.wisdom_modifier})\n"
            f"  Charisma: {self.charisma} ({self.charisma_modifier})"
        )
class Attack:
    def __init__(self, name, attack_bonus, damage_dice_amount, damage_dice_type, damage_bonus, damage_type, attack_isranged, attack_range):
        self.name = name
        self.attack_bonus = attack_bonus
        self.damage_dice_amount = damage_dice_amount
        self.damage_dice_type = damage_dice_type
        self.damage_bonus = damage_bonus
        self.damage_type = damage_type
        self.attack_isranged = attack_isranged
        self.attack_range = attack_range
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Attack Bonus: {self.attack_bonus}\n"
            f"Damage: {self.damage_dice_amount}d{self.damage_dice_type} + {self.damage_bonus} ({self.damage_type})\n"
            f"Attack Type: {'Ranged' if self.attack_isranged else 'Melee'}\n"
            f"Attack Range: {self.attack_range[0]}-{self.attack_range[1]}"
        )
    def roll_to_hit(self, other_armor_class):
        roll = Dice(20).roll()
        total = roll + self.attack_bonus
        if total >= other_armor_class:
            return True
        else:
            return False
    def roll_damage(self):
        damage = Dice(self.damage_dice_type).roll(self.damage_dice_amount, self.damage_bonus)
        return damage, self.damage_type        
class Dice:
    def __init__(self, sides, amount = 1, modifier = 0):
        self.sides = sides
        self.amount = amount
        self.modifier = modifier
    def roll(self, amount = 1, modifier = 0):
        total = 0
        for _ in range(self.amount * amount):
            total += secrets.randbelow(self.sides) + 1
        return total + self.modifier + modifier