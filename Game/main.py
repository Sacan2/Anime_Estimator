import anime_lists as aL
import random
import tkinter as tk

#Fenster machen
root = tk.Tk()

#Charakter Namen aus der Liste nehmen und dafür sorgen, dass es sich nicht doppelt.
character_number_for_1 = len(aL.anime_list)
random_character_number_1 = random.randrange(0, character_number_for_1)
character_name_1 = list(aL.anime_list.keys())[random_character_number_1]
character_kraft_1 = list(aL.anime_list.values())[random_character_number_1]
aL.anime_list.pop(character_name_1, None)

character_number_for_2 = len(aL.anime_list)
random_character_number_2 = random.randrange(0, character_number_for_2)
character_name_2 = list(aL.anime_list.keys())[random_character_number_2]
character_kraft_2 = list(aL.anime_list.values())[random_character_number_2]
aL.anime_list.pop(character_name_2, None)

character_number_for_3 = len(aL.anime_list)
random_character_number_3 = random.randrange(0, character_number_for_3)
character_name_3 = list(aL.anime_list.keys())[random_character_number_3]
character_kraft_3 = list(aL.anime_list.values())[random_character_number_3]
aL.anime_list.pop(character_name_3, None)

character_number_for_4 = len(aL.anime_list)
random_character_number_4 = random.randrange(0, character_number_for_4)
character_name_4 = list(aL.anime_list.keys())[random_character_number_4]
character_kraft_4 = list(aL.anime_list.values())[random_character_number_4]
aL.anime_list.pop(character_name_4, None)

text_1 = tk.Label(root, text=character_name_1)
text_2 = tk.Label(root, text=character_name_2)
text_1.pack()
text_2.pack()

window_width = 500
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title('Philipps Game')
root.mainloop()
