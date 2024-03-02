import random
from colorama import Fore, Back, Style

konosuba = ["Kazuma", "Aqua", "Megumin", "Darkness"]
chainsaw_man = ["Denji", "Makima", "Kobeni", "Pochita"]
jujutsu_kaisen = ["Yuji", "Toji", "Satorou", "Todo"]
mashle = ["Lancer", "Mash", "Finn", "Dot"]

random_character = random.randint(0, 3)
random_ability = random.randint(0, 2)

abilities = ["STEALLLLL", "Black Flash", "Boogie Woogie"]

selected_random_ability = abilities[random_ability]

print(Fore.GREEN + selected_random_ability)
print(Style.RESET_ALL)

user_input = input("Which Character is it?")

match user_input:
    case "":
        print("You failed")

if selected_random_ability == "STEALLLLL":
    print("Kazuma")
elif selected_random_ability == "Black Flash":
    print("Yuji")
elif selected_random_ability == "Boogie Woogie":
    print("Todo")
