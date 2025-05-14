import secrets



class Monster:
    def __init__(self, name, sub_name, stats, attacks, proficent_skills, special_actions, flavor_text=None):
        self.name = name
        self.sub_name = sub_name
        self.stats = stats
        self.attacks = attacks
        self.proficient_skills = proficent_skills
        self.special_actions = special_actions  
        self.flavor_text = flavor_text
        self.initiative = None
    def print_stats(self):
        print(f"{self.name} ({self.sub_name})")
        print("<><><><><><><><><><><><>")
        print(f"Hit Points: {self.stats.hit_points}/{self.stats.hit_points_max}")
        print(f"Armor Class: {self.stats.armor_class}")
        print(f"Speed: {self.stats.speed}")
        print("<><><><><><><><><><><><>")
        print(f"Strength: {self.stats.strength} ({self.stats.strength_modifier})")
        print(f"Dexterity: {self.stats.dexterity} ({self.stats.dexterity_modifier})")
        print(f"Constitution: {self.stats.constitution} ({self.stats.constitution_modifier})")
        print(f"Intelligence: {self.stats.intelligence} ({self.stats.intelligence_modifier})")
        print(f"Wisdom: {self.stats.wisdom} ({self.stats.wisdom_modifier})")
        print(f"Charisma: {self.stats.charisma} ({self.stats.charisma_modifier})")
        print("<><><><><><><><><><><><>")
        print("Proficient Skills:")
        for skill in self.proficient_skills:
            print(f"  {skill[0]}: {skill[1]}")
        print("<><><><><><><><><><><><>")
        print("Special Actions:")
        for action in self.special_actions:
            print(f"  {action[0]}: {action[1]}")
        print("<><><><><><><><><><><><>")
        print("Attacks:")
        for attack in self.attacks:
            print(f"  {attack.name}: {attack.attack_isranged} ({attack.attack_range[0]}-{attack.attack_range[1]})")
            print(f"    Attack Bonus: {attack.attack_bonus}")
            print(f"    Damage: {attack.damage_dice_amount}d{attack.damage_dice_type} + {attack.damage_bonus} ({attack.damage_type})")
        print("<><><><><><><><><><><><>")
        print("Flavor Text:")
        if self.flavor_text:
            print(f"  {self.flavor_text}")
        else:
            print("  None")
    def take_damage(self, damage):
        self.stats.hit_points -= damage
        if self.stats.hit_points <= 0:
            print(f"{self.sub_name} ({self.name}) is dead")
            return True
        else:
            print(f"{self.sub_name} ({self.name}) takes {damage} damage - {self.stats.hit_points}/{self.stats.hit_points_max} HP remaining.")
            return False
        
class Stats:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, armor_class, speed):
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
        self.hit_points = hit_points
        self.hit_points_max = hit_points
        self.armor_class = armor_class
        self.speed = speed
class Attack:
    def __init__(self, name, attack_isranged, attack_range, attack_bonus, damage_dice_type, damage_dice_amount, damage_bonus, damage_type):
        self.name = name
        self.attack_isranged = attack_isranged
        self.attack_range = attack_range
        self.attack_bonus = attack_bonus
        self.damage_dice_type = damage_dice_type
        self.damage_dice_amount = damage_dice_amount
        self.damage_bonus = damage_bonus
        self.damage_type = damage_type
    def roll_attack(self):
        if int(input("What is the AC?")) <= Dice(20).roll() + self.attack_bonus:
            return Dice(self.damage_dice_type, self.damage_dice_amount).roll() + self.damage_bonus
        else:
            return "Miss"
class Dice:
    def __init__(self, sides, amount = 1):
        self.sides = sides
        self.amount = amount
    def roll(self):
        total = 0
        for _ in range(self.amount):
            total += secrets.randbelow(self.sides) + 1
        return total
    def roll_advantage(self):
        return max(self.roll(), self.roll())
    def roll_disadvantage(self):
        return min(self.roll(), self.roll())