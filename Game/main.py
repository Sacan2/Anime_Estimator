import anime_lists
import random
import tkinter as tk
from PIL import Image, ImageTk

#Fenster machen
root = tk.Tk()
liste_für_überprüfung = []
random_Bild_index = random.randrange(0, len(anime_lists.anime_dictionarie))
image = Image.open(list(anime_lists.anime_dictionarie.values())[random_Bild_index])
image_groeße = image.resize((250, 200))
python_bild = ImageTk.PhotoImage(image_groeße)
tk.Label(image=python_bild).place(x=120, y=0)


def get_anime_name():
    random.shuffle(liste_für_überprüfung)
    while True:
        character_number_length_list = len(anime_lists.anime_dictionarie)
        random_character_number = random.randrange(0, character_number_length_list)
        if random_Bild_index not in liste_für_überprüfung:
            liste_für_überprüfung.append(random_Bild_index)
            character_name = list(anime_lists.anime_dictionarie.keys())[random_Bild_index]
            return character_name
        elif random_character_number not in liste_für_überprüfung:
            character_name = list(anime_lists.anime_dictionarie.keys())[random_character_number]
            liste_für_überprüfung.append(random_character_number)
            return character_name


get_anime_name()
get_anime_name()
get_anime_name()
get_anime_name()

knopf_oben_links_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[0]]
knopf_oben_rechts_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[1]]
knopf_unten_links_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[2]]
knopf_unten_rechts_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[3]]

knopf_oben_links = tk.Button(root, text=knopf_oben_links_name,
                             command=lambda: knopf_druck(knopf_oben_links_name, knopf_oben_links))
knopf_oben_rechts = tk.Button(root, text=knopf_oben_rechts_name,
                              command=lambda: knopf_druck(knopf_oben_rechts_name, knopf_oben_rechts))
knopf_unten_links = tk.Button(root, text=knopf_unten_links_name,
                              command=lambda: knopf_druck(knopf_unten_links_name, knopf_unten_links))
knopf_unten_rechts = tk.Button(root, text=knopf_unten_rechts_name,
                               command=lambda: knopf_druck(knopf_unten_rechts_name, knopf_unten_rechts))

knopf_oben_links.place(x=50, y=250, width=120, height=40)
knopf_oben_rechts.place(x=300, y=250, width=120, height=40)
knopf_unten_links.place(x=50, y=350, width=120, height=40)
knopf_unten_rechts.place(x=300, y=350, width=120, height=40)


def knopf_druck(gewählter_name, der_knopf):
    richtiger_name = list(anime_lists.anime_dictionarie)[random_Bild_index]
    print(der_knopf)

    if gewählter_name == richtiger_name:
        print("Richtige")
        knopf_oben_links.configure(bg="red")
        knopf_oben_rechts.configure(bg="red")
        knopf_unten_links.configure(bg="red")
        knopf_unten_rechts.configure(bg="red")
        der_knopf.configure(bg="green")


window_width = 480
window_height = 500

# get the screen dimension  ##### habe ich net geschrieben
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point ##### habe ich net geschrieben
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen ##### habe ich net geschrieben
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title('Philipps Game')
root.mainloop()
