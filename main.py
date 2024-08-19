import os
import sys
import random
import tkinter as tk
from PIL import Image, ImageTk
import anime_lists




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Fenster erstellen
root = tk.Tk()


liste_für_überprüfung = []
button_liste = []
abgleich_liste = []
richtige_antworten = 0
falsche_antworten = 0

knopf_starte_game = tk.Button(root, text='Bild Namen erraten', command=lambda: schwierigkeit_einstelllen())

knopf_starte_game.place(x=170, y=150, width=120, height=60)

text_für_schwierigkeit = tk.Label(root, text="Wähle die Schwierigkeit aus")

# Easy List mode
knopf_leichter_modus = tk.Button(root, text="Ich schaue wenig Animes", command=lambda: knöpfe_für_game_zeigen())
# Medium List mode
knopf_medium_modus = tk.Button(root, text="Ich schaue zu viele")
# Weeb List mode
knopf_weeb_modus = tk.Button(root, text="Ich gehe nicht duschen")
kopie_dic_von_anime_bilder = anime_lists.anime_list_easy


def schwierigkeit_einstelllen():
    text_für_schwierigkeit.place(x=170, y=80)
    knopf_leichter_modus.place(x=140, y=150, width=200, height=60)
    knopf_medium_modus.place(x=140, y=220, width=200, height=60)
    knopf_weeb_modus.place(x=140, y=290, width=200, height=60)
    knopf_starte_game.place(x=700)


def get_anime_name(liste_für_überprüfung_parameter, bild_index):
    random.shuffle(liste_für_überprüfung_parameter)
    while True:
        character_number_length_list = len(kopie_dic_von_anime_bilder)
        random_character_number = random.randrange(0, character_number_length_list)
        if bild_index not in liste_für_überprüfung_parameter:
            liste_für_überprüfung_parameter.append(bild_index)
            character_name = list(kopie_dic_von_anime_bilder.keys())[bild_index]
            return character_name
        elif random_character_number not in liste_für_überprüfung_parameter:
            character_name = list(kopie_dic_von_anime_bilder.keys())[random_character_number]
            liste_für_überprüfung_parameter.append(random_character_number)
            return character_name



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
    global richtige_antworten, falsche_antworten
    richtiger_name = list(kopie_dic_von_anime_bilder)[bild_index]

    if gewählter_name == richtiger_name:
        richtige_antworten += 1
        kopie_dic_von_anime_bilder.pop(richtiger_name)
        text_gewonnen.place(x=210, y=300)

        der_knopf.configure(bg="green")
    else:
        falsche_antworten += 1
        kopie_dic_von_anime_bilder.pop(richtiger_name)
        text_verloren.place(x=180, y=300)
        kombinierte_liste = kombiniere_liste()
        kombinierte_liste[richtiger_name].configure(bg="green")




random_Bild_index = random.randrange(0, len(kopie_dic_von_anime_bilder))
bild_roh_unverabreitet = Image.open(resource_path(list(kopie_dic_von_anime_bilder.values())[random_Bild_index]))
bild_größe_setzen = bild_roh_unverabreitet.resize((180, 200))
bild_auslesen = ImageTk.PhotoImage(bild_größe_setzen)
bild_zum_label = tk.Label(image=bild_auslesen)

get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)
get_anime_name(liste_für_überprüfung, random_Bild_index)

knopf_oben_links_name = list(kopie_dic_von_anime_bilder)[liste_für_überprüfung[0]]
knopf_oben_rechts_name = list(kopie_dic_von_anime_bilder)[liste_für_überprüfung[1]]
knopf_unten_links_name = list(kopie_dic_von_anime_bilder)[liste_für_überprüfung[2]]
knopf_unten_rechts_name = list(kopie_dic_von_anime_bilder)[liste_für_überprüfung[3]]

knopf_oben_links = tk.Button(root, text=knopf_oben_links_name,
                             command=lambda: knopf_druck(knopf_oben_links_name, knopf_oben_links, random_Bild_index))
knopf_oben_rechts = tk.Button(root, text=knopf_oben_rechts_name,
                              command=lambda: knopf_druck(knopf_oben_rechts_name, knopf_oben_rechts, random_Bild_index))
knopf_unten_links = tk.Button(root, text=knopf_unten_links_name,
                              command=lambda: knopf_druck(knopf_unten_links_name, knopf_unten_links, random_Bild_index))
knopf_unten_rechts = tk.Button(root, text=knopf_unten_rechts_name,
                               command=lambda: knopf_druck(knopf_unten_rechts_name, knopf_unten_rechts,
                                                           random_Bild_index))

#nächste_runde_knopf = tk.Button(root, text="Nächste Runde", command=lambda: nächste_runde_vom_spiel())
text_gewonnen = tk.Label(root, text="richtig")
text_verloren = tk.Label(root, text="Du hast es verkackt")




def knöpfe_für_game_zeigen():
    # Die alten auswahlen weg machen
    text_für_schwierigkeit.place(x=700)
    knopf_leichter_modus.place(x=700)
    knopf_medium_modus.place(x=700)
    knopf_weeb_modus.place(x=700)
    # Die neuen auswahlen einblenden
    knopf_oben_links.place(x=50, y=250, width=120, height=40)
    knopf_oben_rechts.place(x=300, y=250, width=120, height=40)
    knopf_unten_links.place(x=50, y=350, width=120, height=40)
    knopf_unten_rechts.place(x=300, y=350, width=120, height=40)
    bild_zum_label.place(x=150, y=0)
    knopf_starte_game.destroy()




root.resizable(False, False)

window_width = 480
window_height = 500

#dark mode aber sieht hässlich aus
#root.config(bg="#26242f")

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title('Philipps Game')
root.mainloop()
