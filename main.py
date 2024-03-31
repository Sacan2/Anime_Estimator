import anime_lists
import random

character_numbers = len(anime_lists.anime_list)

print(character_numbers)

random_character_number_1 = random.randrange(0, character_numbers)

random_character_number_2 = random.randrange(0, character_numbers)
random_character_number_3 = random.randrange(0, character_numbers)
random_character_number_4 = random.randrange(0, character_numbers)

print(random_character_number_1)

print(list(anime_lists.anime_list.keys())[random_character_number_1])
print(list(anime_lists.anime_list.values())[random_character_number_1] + "\n")

print(list(anime_lists.anime_list.keys())[random_character_number_2])
print(list(anime_lists.anime_list.values())[random_character_number_2] + "\n")

print(list(anime_lists.anime_list.keys())[random_character_number_3])
print(list(anime_lists.anime_list.values())[random_character_number_3] + "\n")

print(list(anime_lists.anime_list.keys())[random_character_number_4])
print(list(anime_lists.anime_list.values())[random_character_number_4] + "\n")

