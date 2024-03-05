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
    user_input = input("Welcher Charakter ist es?\n")

    match user_input.lower():
        case "yuji" if selected_random_ability == "Divergent fist":
            game_start = False
            print("Du hast gewonnen")

        case "gojo" if selected_random_ability == "Hollow Purple":
            game_start = False
            print("Du hast gewonnen")

        case "todo" if selected_random_ability == "Boogie Woogie":
            game_start = False
            print("Du hast gewonnen")

        case "toji" if selected_random_ability == "heavenly restriction":
            game_start = False
            print("Du hast gewonnen")
        case _:
            print("Du bist kacke")
