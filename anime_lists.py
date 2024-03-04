import random
from colorama import Fore, Back, Style

konosuba = ["Kazuma", "Aqua", "Megumin", "Darkness"]
chainsaw_man = ["Denji", "Makima", "Kobeni", "Pochita"]
jujutsu_kaisen = ["Yuji", "Toji", "Satorou", "Todo"]
mashle = ["Lancer", "Mash", "Finn", "Dot"]

random_character = random.randint(0, 3)
random_ability = random.randint(0, 2)

abilities = ["Hollow Purple", "Divergent fist", "Boogie Woogie", "heavenly restriction"]

selected_random_ability = abilities[random_ability]

print(Fore.GREEN + selected_random_ability)
print(Style.RESET_ALL)

for x in jujutsu_kaisen:
    print(x)

user_input = input("Which Character is it?\n")

