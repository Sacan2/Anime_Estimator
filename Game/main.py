import anime_lists
import random
import tkinter as tk

#Fenster machen
root = tk.Tk()
# Index vom JSON entnehmen

#Charakter Namen aus der Liste nehmen und dafür sorgen, dass es sich nicht doppelt.
character_number_for_1 = len(anime_lists.anime_list)
random_character_number_1 = random.randrange(0, character_number_for_1)
character_name_1 = list(anime_lists.anime_list.keys())[random_character_number_1]
character_kraft_1 = list(anime_lists.anime_list.values())[random_character_number_1]
anime_lists.anime_list.pop(character_name_1, None)

character_number_for_2 = len(anime_lists.anime_list)
random_character_number_2 = random.randrange(0, character_number_for_2)
character_name_2 = list(anime_lists.anime_list.keys())[random_character_number_2]
character_kraft_2 = list(anime_lists.anime_list.values())[random_character_number_2]
anime_lists.anime_list.pop(character_name_2, None)

character_number_for_3 = len(anime_lists.anime_list)
random_character_number_3 = random.randrange(0, character_number_for_3)
character_name_3 = list(anime_lists.anime_list.keys())[random_character_number_3]
character_kraft_3 = list(anime_lists.anime_list.values())[random_character_number_3]
anime_lists.anime_list.pop(character_name_3, None)

character_number_for_4 = len(anime_lists.anime_list)
random_character_number_4 = random.randrange(0, character_number_for_4)
character_name_4 = list(anime_lists.anime_list.keys())[random_character_number_4]
character_kraft_4 = list(anime_lists.anime_list.values())[random_character_number_4]
anime_lists.anime_list.pop(character_name_4, None)


text_1 = tk.Label(root, text=character_name_1)
text_2 = tk.Label(root, text=character_name_2)
text_1.pack()
text_2.pack()

root.mainloop()