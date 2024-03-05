import random
from colorama import Fore, Back, Style

konosuba = ["Kazuma", "Aqua", "Megumin", "Darkness"]
chainsaw_man = ["Denji", "Makima", "Kobeni", "Pochita"]
jujutsu_kaisen = ["Yuji", "Toji", "Gojo", "Todo"]
mashle = ["Lancer", "Mash", "Finn", "Dot"]

random_character = random.randint(0, 3)
random_ability = random.randint(0, 2)

abilities = ["Hollow Purple", "Divergent fist", "Boogie Woogie", "heavenly restriction"]

selected_random_ability = abilities[random_ability]

print(Fore.GREEN + selected_random_ability)
print(Style.RESET_ALL)

for x in jujutsu_kaisen:
    print(x)

game_start = True

while game_start:
    user_input = input("Which Character is it?\n")
    if selected_random_ability == "Hollow Purple" and user_input == "Gojo":
        game_start = False
        print("Du hast gewonnen")

    elif selected_random_ability == "Divergent fist" and user_input == "Yuji":
        game_start = False
        print("Du hast gewonnen")

    elif selected_random_ability == "Boogie Woogie" and user_input == "Todo":
        game_start = False
        print("Du hast gewonnen")

    elif selected_random_ability == "heavenly restriction" and user_input == "Toji":
        game_start = False
        print("Du hast gewonnen")
    else:
        print("Versuch nochmal, du spastie!!!!!!!!")