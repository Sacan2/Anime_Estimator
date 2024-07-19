import anime_lists
import random
import tkinter as tk
from PIL import Image, ImageTk

#Fenster machen
root = tk.Tk()


def get_anime_name(liste_für_überprüfung_parameter, bild_index):
    random.shuffle(liste_für_überprüfung_parameter)
    while True:
        character_number_length_list = len(anime_lists.anime_dictionarie)
        random_character_number = random.randrange(0, character_number_length_list)
        if bild_index not in liste_für_überprüfung_parameter:
            liste_für_überprüfung_parameter.append(bild_index)
            character_name = list(anime_lists.anime_dictionarie.keys())[bild_index]
            return character_name
        elif random_character_number not in liste_für_überprüfung_parameter:
            character_name = list(anime_lists.anime_dictionarie.keys())[random_character_number]
            liste_für_überprüfung_parameter.append(random_character_number)
            return character_name


def nächste_runde_vom_spiel():
    random_Bild_index_neu = random.randrange(0, len(anime_lists.anime_dictionarie))
    bild_vom_charackter = Image.open(list(anime_lists.anime_dictionarie.values())[random_Bild_index_neu])
    character_bild_groeße = bild_vom_charackter.resize((250, 200))
    verarbeitetes_bild = ImageTk.PhotoImage(character_bild_groeße)
    label.config(image=verarbeitetes_bild)
    label.image = verarbeitetes_bild
    liste_für_überprüfung.clear()
    button_liste.clear()
    abgleich_liste.clear()

    print(f" der Index beim ersten durchfall {random_Bild_index}")

    knopf_aktievieren()

    get_anime_name(liste_für_überprüfung, random_Bild_index_neu)
    get_anime_name(liste_für_überprüfung, random_Bild_index_neu)
    get_anime_name(liste_für_überprüfung, random_Bild_index_neu)
    get_anime_name(liste_für_überprüfung, random_Bild_index_neu)

    knopf_oben_links_name_neue_runde = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[0]]
    knopf_oben_rechts_name_neue_runde = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[1]]
    knopf_unten_links_name_neue_runde = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[2]]
    knopf_unten_rechts_name_neue_runde = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[3]]

    knopf_oben_links.config(text=knopf_oben_links_name_neue_runde,
                            command=lambda: knopf_druck(knopf_oben_links_name_neue_runde, knopf_oben_links, random_Bild_index_neu))
    knopf_oben_rechts.config(text=knopf_oben_rechts_name_neue_runde,
                             command=lambda: knopf_druck(knopf_oben_rechts_name_neue_runde, knopf_oben_rechts, random_Bild_index_neu))
    knopf_unten_links.config(text=knopf_unten_links_name_neue_runde,
                             command=lambda: knopf_druck(knopf_unten_links_name_neue_runde, knopf_unten_links, random_Bild_index_neu))
    knopf_unten_rechts.config(text=knopf_unten_rechts_name_neue_runde,
                              command=lambda: knopf_druck(knopf_unten_rechts_name_neue_runde, knopf_unten_rechts, random_Bild_index_neu))

    kombinierte_liste = kombiniere_liste()
    print("liste wie sie ist")

    print(kombinierte_liste)
    print(liste_für_überprüfung)
    print(abgleich_liste)


def next_round_knopf():
    nächste_runde_knopf.place(x=180, y=410, width=120, height=40)


def knopf_deaktieviren():
    knopf_oben_links.configure(bg="red")
    knopf_oben_links["state"] = "disabled"
    knopf_oben_rechts.configure(bg="red")
    knopf_oben_rechts["state"] = "disabled"
    knopf_unten_links.configure(bg="red")
    knopf_unten_links["state"] = "disabled"
    knopf_unten_rechts.configure(bg="red")
    knopf_unten_rechts["state"] = "disabled"


def knopf_aktievieren():
    knopf_oben_links.configure(bg="SystemButtonFace")
    knopf_oben_links["state"] = "active"
    knopf_oben_rechts.configure(bg="SystemButtonFace")
    knopf_oben_rechts["state"] = "active"
    knopf_unten_links.configure(bg="SystemButtonFace")
    knopf_unten_links["state"] = "active"
    knopf_unten_rechts.configure(bg="SystemButtonFace")
    knopf_unten_rechts["state"] = "active"


def kombiniere_liste():
    button_liste.append(knopf_oben_links)
    button_liste.append(knopf_oben_rechts)
    button_liste.append(knopf_unten_links)
    button_liste.append(knopf_unten_rechts)

    abgleich_knopf_0 = knopf_oben_links.cget("text")
    abgleich_knopf_1 = knopf_oben_rechts.cget("text")
    abgleich_knopf_2 = knopf_unten_links.cget("text")
    abgleich_knopf_3 = knopf_unten_rechts.cget("text")

    abgleich_liste.append(abgleich_knopf_0)
    abgleich_liste.append(abgleich_knopf_1)
    abgleich_liste.append(abgleich_knopf_2)
    abgleich_liste.append(abgleich_knopf_3)

    kombinierte_liste = dict(zip(abgleich_liste, button_liste))
    return kombinierte_liste


def knopf_druck(gewählter_name, der_knopf, bild_index):
    richtiger_name = list(anime_lists.anime_dictionarie)[bild_index]
    print(f"das ist der richtige Name {richtiger_name}")
    next_round_knopf()
    if gewählter_name == richtiger_name:
        text_gewonnen.place(x=210, y=300)
        knopf_deaktieviren()
        der_knopf.configure(bg="green")

    else:
        text_verloren.place(x=180, y=300)
        knopf_deaktieviren()
        kombinierte_liste = kombiniere_liste()
        kombinierte_liste[richtiger_name].configure(bg="green")


liste_für_überprüfung = []
button_liste = []
abgleich_liste = []
random_Bild_index = random.randrange(0, len(anime_lists.anime_dictionarie))
print(f" der Index beim ersten durchfall {random_Bild_index}")
image = Image.open(list(anime_lists.anime_dictionarie.values())[random_Bild_index])
image_groeße = image.resize((250, 200))
python_bild = ImageTk.PhotoImage(image_groeße)
label = tk.Label(image=python_bild)
label.place(x=120, y=0)

get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)

knopf_oben_links_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[0]]
knopf_oben_rechts_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[1]]
knopf_unten_links_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[2]]
knopf_unten_rechts_name = list(anime_lists.anime_dictionarie)[liste_für_überprüfung[3]]

print(liste_für_überprüfung)

knopf_oben_links = tk.Button(root, text=knopf_oben_links_name,
                             command=lambda: knopf_druck(knopf_oben_links_name, knopf_oben_links, random_Bild_index))
knopf_oben_rechts = tk.Button(root, text=knopf_oben_rechts_name,
                              command=lambda: knopf_druck(knopf_oben_rechts_name, knopf_oben_rechts, random_Bild_index))
knopf_unten_links = tk.Button(root, text=knopf_unten_links_name,
                              command=lambda: knopf_druck(knopf_unten_links_name, knopf_unten_links, random_Bild_index))
knopf_unten_rechts = tk.Button(root, text=knopf_unten_rechts_name,
                               command=lambda: knopf_druck(knopf_unten_rechts_name, knopf_unten_rechts,
                                                           random_Bild_index))

nächste_runde_knopf = tk.Button(root, text="Nächste Runde", command=lambda: nächste_runde_vom_spiel())
text_gewonnen = tk.Label(root, text="richtig")
text_verloren = tk.Label(root, text="Du hast es verkackt")

knopf_oben_links.place(x=50, y=250, width=120, height=40)
knopf_oben_rechts.place(x=300, y=250, width=120, height=40)
knopf_unten_links.place(x=50, y=350, width=120, height=40)
knopf_unten_rechts.place(x=300, y=350, width=120, height=40)

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
