import Classes as C
import Functions as F
import Variables as V


def main():
    V.json_data = F.get_json()
    F.setup_dice()
    F.setup_menus()
    def div():
        F.br()
        F.hr2(1)
    while True:
        for i, option in enumerate(V.menus["Main"]):
            print(f"{i + 1}. {option}")
        choice = input("Select an option: ")

main()
 