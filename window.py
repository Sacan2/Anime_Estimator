import tkinter as tk
import random
from operator import index
from tkinter import ttk
from PIL import Image, ImageTk


from anime_lists import anime_list_easy, anime_list_medium





class App(tk.Tk):

    def __init__(self, name_start_button):
        super().__init__()
        #Manche Variablen wurden erstellt, weil ich es besser finde, wenn man diese nicht innerhalb der Methode macht aber wenig unterschied.
        self.bild_laden = None
        self.bild_aufmachen_nicht_bearbeitet = None
        self.name_start_button = name_start_button
        #Sehr wichtige Variablen
        self.richtige_antwort = None
        self.namen_fuer_buttons_liste = None
        self.liste_fuer_das_gesamte = None
        self.schwierigkeit_die_ausgesucht_ist = None

        self.title("Philipps Game")
        self.geometry("400x500")


        self.start_button_bild_aussuchen = tk.Button(self, text=self.name_start_button, height=2, width=9)
        self.start_button_bild_aussuchen.configure(command=self.schwierigkeit_anzeigen)
        self.start_button_bild_aussuchen.place(x=200, y=160)

        #Schwierigkeit Auswählen
        # leichter modus
        self.button_easy_mode = tk.Button(self, text="leichter Modus", height=2, width=12)
        self.button_easy_mode.configure(command=lambda: self.schwierigkeit_ausgesucht("easy"))
        #medium modus
        self.button_medium_mode = tk.Button(self, text="medium Modus", height=2, width=12)
        self.button_medium_mode.configure(command=lambda: self.schwierigkeit_ausgesucht("medium"))

        #Die Game Buttons
        self.button_oben_links = tk.Button(self, height=2, width=12)
        self.button_oben_links.configure(command=lambda: self.ergebnis_ueberpruefen())

        self.button_oben_rechts = tk.Button(self, height=2, width=12)
        self.button_oben_rechts.configure(command=lambda: self.ergebnis_ueberpruefen())

        self.button_unten_links = tk.Button(self, height=2, width=12)
        self.button_unten_links.configure(command=lambda: self.ergebnis_ueberpruefen())

        self.button_unten_rechts = tk.Button(self, height=2, width=12)
        self.button_unten_rechts.configure(command=lambda: self.ergebnis_ueberpruefen())
        #das Bild
        self.angezeigtes_bild = ttk.Label(self)

        # Standard sachen
        self.window_width = 480
        self.window_height = 500

        # get the screen dimension
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        #Fenster nicht vergrößern
        self.resizable(False,False)

    def schwierigkeit_anzeigen(self):
        self.start_button_bild_aussuchen.place(x=700)
        self.button_easy_mode.place(x=190, y=150)
        self.button_medium_mode.place(x=190,y=350)

    def schwierigkeit_ausgesucht(self, ausgesuchte_schwierigkeit):
        self.button_easy_mode.place(x=700)
        self.button_medium_mode.place(x=700)
        #Buttons Zeigen
        self.button_oben_links.place(x=80,y=300)
        self.button_oben_rechts.place(x=280,y=300)
        self.button_unten_links.place(x=80,y=400)
        self.button_unten_rechts.place(x=280,y=400)


        self.schwierigkeit_die_ausgesucht_ist = ausgesuchte_schwierigkeit
        pfad_zum_bild = self.random_pfad_geben(ausgesuchte_schwierigkeit)
        self.bild_zeigen(pfad_zum_bild)

    def bild_zeigen(self, der_pfad_zum_bild):
        #Aus dem Internet verstehe ich selber nicht
        self.richtige_antwort = list(self.liste_fuer_das_gesamte.keys())[list(self.liste_fuer_das_gesamte.values()).index(der_pfad_zum_bild)]
        self.namen_aus_der_liste_holen()

        self.bild_aufmachen_nicht_bearbeitet = Image.open(der_pfad_zum_bild)
        # Die größe vom Bild selbst hat keine Relevanz, also nicht im __init__()
        bild_groesse_bearbeiten = self.bild_aufmachen_nicht_bearbeitet.resize((180, 240))
        self.bild_laden = ImageTk.PhotoImage(bild_groesse_bearbeiten)
        self.angezeigtes_bild.configure(image=self.bild_laden)
        self.angezeigtes_bild.pack()

    def ergebnis_ueberpruefen(self):
        print(self.namen_fuer_buttons_liste)


    def namen_aus_der_liste_holen(self):
        self.liste_fuer_das_gesamte.pop(self.richtige_antwort)
        random_namen = random.sample(list(self.liste_fuer_das_gesamte),k=3)
        self.namen_fuer_buttons_liste = random_namen
        self.namen_fuer_buttons_liste.append(self.richtige_antwort)
        random.shuffle(self.namen_fuer_buttons_liste)
        #Namen_verteilen
        self.button_oben_links.configure(text=self.namen_fuer_buttons_liste[0])
        self.button_oben_rechts.configure(text=self.namen_fuer_buttons_liste[1])
        self.button_unten_links.configure(text=self.namen_fuer_buttons_liste[2])
        self.button_unten_rechts.configure(text=self.namen_fuer_buttons_liste[3])

    def random_pfad_geben(self, schwierigkeit):
        if schwierigkeit == "easy":
            # Minus 1, weil es nicht mit index 0, sondern direkt bei 1 anfängt zu zählen.
            liste_länge = len(anime_list_easy) -1
            random_index = random.randint(0, liste_länge)
            bild = list(anime_list_easy.values())[random_index]
            self.liste_fuer_das_gesamte = anime_list_easy
            return bild
        elif schwierigkeit == "medium":
            liste_länge = len(anime_list_medium) -1
            random_index = random.randint(0, liste_länge)
            bild = list(anime_list_medium.values())[random_index]
            self.liste_fuer_das_gesamte = anime_list_medium
            return bild

