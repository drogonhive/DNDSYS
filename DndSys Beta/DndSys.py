import secrets
import Monsters
import DataTypes

def main():
    Monsters.prep_monsters()
    monsters_alive = []
    monsters_dead = []
    players = []
    initiative = []
    initiative_point = 0
    while True:
        print("\n")
        print("<><><><><><><><><><><><>")

        print("0. Exit")
        print("1. Reset Data")
        print("2. Add Monster")
        print("3. View Monsters")
        print("4. Add Player")
        print("5. View Players")
        print("6. Roll Initiative")
        print("7. View Initiative")
        print("8. Current Turn")
        print("9. Next Turn")
        print("10. Damage Monster")
        print("11. Roll Dice")
        choice = input("What would you like to do? ")
        if choice == "0":
            break
        elif choice == "1":
            print("\n")
            print("<><><><><><><><><><><><>")
            print("0. Back")
            print("1. Reset all data")
            print("2. Reset monsters")
            print("3. Reset players")
            print("4. Reset initiative")
            choice = input("What would you like to do? ")
            if choice == "0":
                break
            elif choice == "1":
                monsters_alive = []
                monsters_dead = []
                players = []
                initiative = []
            elif choice == "2":
                monsters_alive = []
                monsters_dead = []
            elif choice == "3":
                players = []
            elif choice == "4":
                initiative = []
        elif choice == "2":
            while True:
                print("\n")
                print("<><><><><><><><><><><><>")
                for i, monster in enumerate(Monsters.__all__):
                    print(f"{i + 1}. {monster['name']}")
                choice = input("Which monster would you like to add? ")
                sub_name = input("What would you like to name it? ")
                data = Monsters.__all__[int(choice) - 1]
                monsters_alive.append(
                    Monsters.new_monster(data, sub_name)
                )
                print("\n")
                print("<><><><><><><><><><><><>")
                print("0. Back")
                print("1. Create another monster")
                choice = input("What would you like to do? ")
                if choice == "0":
                    break
                elif choice == "1":
                    continue
        elif choice == "3":
            while True:
                print("\n")
                print("<><><><><><><><><><><><>")
                for i, monster in enumerate(monsters_alive):
                    print(f"{i + 1}. {monster.name} ({monster.sub_name})")
                choice = input("Which monster would you like to view? ")
                if choice == "" or choice == "0":
                    break
                monsters_alive[int(choice) - 1].print_stats()
                print("\n")
                print("<><><><><><><><><><><><>")
                print("0. Back")
                print("1. View another monster")
                choice = input("What would you like to do? ")
                if choice == "0":
                    break
                elif choice == "1":
                    continue
        elif choice == "4":
            while True:
                print("\n")
                print("<><><><><><><><><><><><>")
                players.append(input("Name of player:"))
                print("\n")
                print("<><><><><><><><><><><><>")
                print("0. Back")
                print("1. Add another player")
                choice = input("What would you like to do? ")
                if choice == "0":
                    break
                elif choice == "1":
                    continue
        elif choice == "5":
            print("\n")
            print("<><><><><><><><><><><><>")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player}")
        elif choice == "6":
            initiative_point = 0
            rolls = []
            d20 = DataTypes.Dice(20)
            for i, monster in enumerate(monsters_alive):
                rolls.append(
                    (monster.name, monster.sub_name, d20.roll() + monster.stats.dexterity_modifier, i)
                )
            for player in players:
                rolls.append(
                    ("Player", player, int(input(f"What is {player}'s initiative? ")), None)
                )
            for type, name, roll, index in rolls:
                #Inserts the roll into the initiative list in order of highest to lowest.
                if len(initiative) == 0:
                    initiative.append((type, name, roll, index))
                else:
                    for i in range(len(initiative)):
                        if roll > initiative[i][2]:
                            initiative.insert(i, (type, name, roll, index))
                            break
                        elif i == len(initiative) - 1:
                            initiative.append((type, name, roll, index))
        elif choice == "7":
            print("\n")
            print("<><><><><><><><><><><><>")
            for type, name, roll, index in initiative:
                if type == "Player":
                    print(f"{name} ({type}) - Initiative: {roll}")
                else:
                    print(f"{name} ({type}) - Initiative: {roll} - Location: ({index}) ")
        elif choice == "8":
            print("\n")
            print("<><><><><><><><><><><><>")
            data = initiative[initiative_point]
            if data[0] == "Player":
                print(f"{data[1]} ({data[0]})")
            else:
                monsters_alive[data[3]].print_stats()
                #TODO: add a way to print attacks and actions to do
        elif choice == "9":
            print("\n")
            print("<><><><><><><><><><><><>")
            initiative_point += 1
            initiative_point %= len(initiative)
            print("Done")
        elif choice == "10":
            while True:
                print("\n")
                print("<><><><><><><><><><><><>")
                for i, monster in enumerate(monsters_alive):
                    print(f"{i + 1}. {monster.name} ({monster.sub_name})")
                choice = input("Which monster would you like to damage? ")
                amount = int(input("How much damage? "))
                if choice == "" or choice == "0":
                    break
                monsters_alive[int(choice) - 1].take_damage(amount)
                print("\n")
                print("<><><><><><><><><><><><>")
                print("0. Back")
                print("1. Damage another monster")
                choice = input("What would you like to do? ")
                if choice == "0":
                    break
                elif choice == "1":
                    continue
        elif choice == "11":
            print("\n")
            print("<><><><><><><><><><><><>")
            print("1. Roll a d4")
            print("2. Roll a d6")
            print("3. Roll a d8")
            print("4. Roll a d10")
            print("5. Roll a d12")
            print("6. Roll a d20")
            print("7. Roll a d100")
            choice = input("What would you like to roll? ")
            amount = int(input("How many dice? "))
            if choice == "1":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d4: {DataTypes.Dice(4, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "2":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d6: {DataTypes.Dice(6, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "3":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d8: {DataTypes.Dice(8, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "4":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d10: {DataTypes.Dice(10, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "5":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d12: {DataTypes.Dice(12, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "6":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d20: {DataTypes.Dice(20, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue
            elif choice == "7":
                while True:
                    print("\n")
                    print(f"Rolled {amount}d100: {DataTypes.Dice(100, amount).roll()}")
                    print("\n")
                    print("<><><><><><><><><><><><>")
                    print("0. Exit")
                    print("1. Roll again")
                    choice = input("What would you like to do? ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        continue






                    
main()

