import tkinter as tk
import random
from tkinter import ttk
from PIL import Image, ImageTk


from anime_lists import anime_list_easy, anime_list_medium







class App(tk.Tk):

    def __init__(self, name_start_button):
        super().__init__()
        self.bild_laden = None
        self.bild_aufmachen_nicht_bearbeitet = None
        self.name_start_button = name_start_button
        self.richtige_antwort = None
        self.namen_fuer_buttons_liste = []
        self.liste_easy_game_mode = None
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
        self.button_oben_links = tk.Button(self, text="erraten", height=2, width=12)
        self.button_oben_links.configure(command=lambda: self.ergebnis_ueberpruefen())
        self.button_oben_links.pack()
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
        self.button_medium_mode.place(x=190,y=250)

    def schwierigkeit_ausgesucht(self, ausgesuchte_schwierigkeit):
        self.button_easy_mode.place(x=700)
        self.schwierigkeit_die_ausgesucht_ist = ausgesuchte_schwierigkeit
        pfad_zum_bild = self.random_pfad_geben(ausgesuchte_schwierigkeit)
        self.bild_zeigen(pfad_zum_bild)

    def bild_zeigen(self, der_pfad_zum_bild):
        self.richtige_antwort = der_pfad_zum_bild
        self.bild_aufmachen_nicht_bearbeitet = Image.open(der_pfad_zum_bild)
        # Die größe vom Bild selbst hat keine Relevanz, also nicht im __init__()
        bild_groesse_bearbeiten = self.bild_aufmachen_nicht_bearbeitet.resize((180, 240))
        self.bild_laden = ImageTk.PhotoImage(bild_groesse_bearbeiten)
        self.angezeigtes_bild.configure(image=self.bild_laden)
        self.angezeigtes_bild.pack()

    def ergebnis_ueberpruefen(self):
        self.namen_fuer_buttons_liste.clear()
        self.drei_random_characktere()

    def drei_random_characktere(self):
        print(self.richtige_antwort)



    def random_pfad_geben(self, schwierigkeit):
        if schwierigkeit == "easy":
            # Minus 1, weil es nicht mit index 0, sondern direkt bei 1 anfängt zu zählen.
            liste_länge = len(anime_list_easy) -1
            self.richtige_antwort = random.randint(0, liste_länge)
            bild = list(anime_list_easy.values())[self.richtige_antwort]
            return bild
        elif schwierigkeit == "medium":
            liste_länge = len(anime_list_medium) -1
            self.richtige_antwort = random.randint(0, liste_länge)
            bild = list(anime_list_medium.values())[self.richtige_antwort]
            return bild