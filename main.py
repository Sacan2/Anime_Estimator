import anime_lists
import random

character_numbers = len(anime_lists.jujutsu_kaisen)

print(character_numbers)

random_character_number = random.randrange(0, character_numbers)

print(random_character_number)

print(list(anime_lists.jujutsu_kaisen.keys())[random_character_number])
print(list(anime_lists.jujutsu_kaisen.values())[random_character_number])

