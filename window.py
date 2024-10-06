import tkinter as tk
import random
from tkinter import ttk
from PIL import Image, ImageTk

from anime_lists import anime_list_easy, anime_list_medium, anime_list_hard


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
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah = {}
        self.liste_fuer_das_gesamte = None
        self.schwierigkeit_die_ausgesucht_ist = None
        #Auswertungsvariabeln
        self.richtig_geratene_antworten = 0
        self.falsch_geratene_antworten = 0

        self.title("Philipps Game")
        self.geometry("400x500")

        self.start_button_bild_aussuchen = tk.Button(self, text=self.name_start_button, height=2, width=9)
        self.start_button_bild_aussuchen.configure(command=self.schwierigkeit_anzeigen)
        self.start_button_bild_aussuchen.place(x=200, y=160)

        self.naechste_runde_button = tk.Button(self, text="Nächste Runde", height=2, width=11,
                                               command=lambda: self.naechste_runde())

        #Schwierigkeit Auswählen
        # leichter modus
        self.button_easy_mode = tk.Button(self, text="leichter Modus", height=2, width=12)
        self.button_easy_mode.configure(command=lambda: self.schwierigkeit_ausgesucht("easy"))
        #medium modus
        self.button_medium_mode = tk.Button(self, text="medium Modus", height=2, width=12)
        self.button_medium_mode.configure(command=lambda: self.schwierigkeit_ausgesucht("medium"))
        #harter modus
        self.button_hard_mode = tk.Button(self, text="harter modus", height=2, width=12)
        self.button_hard_mode.configure(command=lambda: self.schwierigkeit_ausgesucht("hard"))

        #Die Game Buttons
        self.button_oben_links = tk.Button(self, height=2, width=12)

        self.button_oben_rechts = tk.Button(self, height=2, width=12)

        self.button_unten_links = tk.Button(self, height=2, width=12)

        self.button_unten_rechts = tk.Button(self, height=2, width=12)

        #das Bild
        self.angezeigtes_bild = ttk.Label(self)

        #Auswertung
        self.richtige_antworten_text = tk.Label(self)
        self.richtige_antworten = tk.Label(self)
        self.falsche_antworten_text = tk.Label(self)
        self.falsche_antworten = tk.Label(self)

        #Der Nochmal spielen Button
        self.nochmal_spielen_button = tk.Button(self,text="Nochmal Spielen", command=lambda:self.nochmal_spielen())

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
        self.resizable(False, False)
        self.standard_farbe = self.button_oben_rechts['bg']

    def schwierigkeit_anzeigen(self):
        self.start_button_bild_aussuchen.place(x=700)
        self.button_easy_mode.place(x=190, y=150)
        self.button_medium_mode.place(x=190, y=210)
        self.button_hard_mode.place(x=190, y=270)

    def schwierigkeit_ausgesucht(self, ausgesuchte_schwierigkeit):
        self.button_easy_mode.place(x=700)
        self.button_medium_mode.place(x=700)
        self.button_hard_mode.place(x=700)
        #Buttons Zeigen
        self.button_oben_links.place(x=80, y=300)
        self.button_oben_rechts.place(x=280, y=300)
        self.button_unten_links.place(x=80, y=400)
        self.button_unten_rechts.place(x=280, y=400)

        self.schwierigkeit_die_ausgesucht_ist = ausgesuchte_schwierigkeit
        pfad_zum_bild = self.random_pfad_geben(ausgesuchte_schwierigkeit)
        self.bild_zeigen(pfad_zum_bild)

    def bild_zeigen(self, der_pfad_zum_bild):
        #Aus dem Internet verstehe ich selber nicht
        self.richtige_antwort = list(self.liste_fuer_das_gesamte.keys())[
            list(self.liste_fuer_das_gesamte.values()).index(der_pfad_zum_bild)]
        #Das schon
        self.namen_aus_der_liste_holen()

        self.bild_aufmachen_nicht_bearbeitet = Image.open(der_pfad_zum_bild)
        # Die größe vom Bild selbst hat keine Relevanz, also nicht im __init__()
        bild_groesse_bearbeiten = self.bild_aufmachen_nicht_bearbeitet.resize((180, 240))
        self.bild_laden = ImageTk.PhotoImage(bild_groesse_bearbeiten)
        self.angezeigtes_bild.configure(image=self.bild_laden)
        self.angezeigtes_bild.pack()

    def naechste_runde(self):
        self.naechste_runde_button.place(x=700)
        self.buttons_anschalten_und_zuruecksetzen()
        naechster_pfad_index = random.randrange(0, len(self.liste_fuer_das_gesamte))
        naechster_character_pfad = list(self.liste_fuer_das_gesamte.values())[naechster_pfad_index]
        self.bild_zeigen(naechster_character_pfad)

    def ueberpruefen_ob_das_spiel_fertig_ist(self,ausgesuchte_antwort):
        if ausgesuchte_antwort == self.richtige_antwort:

            self.richtig_geratene_antworten += 1
        else:
            self.falsch_geratene_antworten += 1
        self.buttons_ausschalten_und_antwort_zeigen()
        if len(self.liste_fuer_das_gesamte) >= 4:
            self.naechste_runde_button.pack()
        else:
            self.liste_fuer_das_gesamte.clear()
            self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah.clear()
            self.namen_fuer_buttons_liste.clear()
            self.auswertung()

    def namen_aus_der_liste_holen(self):
        self.liste_fuer_das_gesamte.pop(self.richtige_antwort)

        random_namen = random.sample(list(self.liste_fuer_das_gesamte), k=3)
        self.namen_fuer_buttons_liste = random_namen
        self.namen_fuer_buttons_liste.append(self.richtige_antwort)
        random.shuffle(self.namen_fuer_buttons_liste)

        self.namen_verteilen()
        self.entschiedener_button()

    def entschiedener_button(self):
        # Auswahl übergeben
        self.button_oben_links.configure(command=lambda: self.ueberpruefen_ob_das_spiel_fertig_ist(self.button_oben_links.cget("text")))
        self.button_oben_rechts.configure(command=lambda: self.ueberpruefen_ob_das_spiel_fertig_ist(self.button_oben_rechts.cget("text")))
        self.button_unten_links.configure(command=lambda: self.ueberpruefen_ob_das_spiel_fertig_ist(self.button_unten_links.cget("text")))
        self.button_unten_rechts.configure(command=lambda: self.ueberpruefen_ob_das_spiel_fertig_ist(self.button_unten_rechts.cget("text")))

    def namen_verteilen(self):
        # Namen_verteilen
        self.button_oben_links.configure(text=self.namen_fuer_buttons_liste[0])
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah[
            self.namen_fuer_buttons_liste[0]] = self.button_oben_links

        self.button_oben_rechts.configure(text=self.namen_fuer_buttons_liste[1])
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah[
            self.namen_fuer_buttons_liste[1]] = self.button_oben_rechts

        self.button_unten_links.configure(text=self.namen_fuer_buttons_liste[2])
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah[
            self.namen_fuer_buttons_liste[2]] = self.button_unten_links

        self.button_unten_rechts.configure(text=self.namen_fuer_buttons_liste[3])
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah[
            self.namen_fuer_buttons_liste[3]] = self.button_unten_rechts

    def random_pfad_geben(self, schwierigkeit):
        if schwierigkeit == "easy":
            # Minus 1, weil es nicht mit index 0, sondern direkt bei 1 anfängt zu zählen.
            liste_laenge = len(anime_list_easy) - 1
            random_index = random.randint(0, liste_laenge)
            bild = list(anime_list_easy.values())[random_index]
            self.liste_fuer_das_gesamte = anime_list_easy.copy()
            return bild
        elif schwierigkeit == "medium":
            liste_laenge = len(anime_list_medium) - 1
            random_index = random.randint(0, liste_laenge)
            bild = list(anime_list_medium.values())[random_index]
            self.liste_fuer_das_gesamte = anime_list_medium.copy()
            return bild
        elif schwierigkeit == "hard":
            liste_laenge = len(anime_list_hard) - 1
            random_index = random.randint(0, liste_laenge)
            bild = list(anime_list_hard.values())[random_index]
            self.liste_fuer_das_gesamte = anime_list_hard.copy()
            return bild

    def buttons_ausschalten_und_antwort_zeigen(self):
        self.button_oben_links["state"] = "disabled"
        self.button_oben_rechts["state"] = "disabled"
        self.button_unten_links["state"] = "disabled"
        self.button_unten_rechts["state"] = "disabled"

        self.button_oben_links.configure(bg="red")
        self.button_oben_rechts.configure(bg="red")
        self.button_unten_links.configure(bg="red")
        self.button_unten_rechts.configure(bg="red")

        # Den richtigen Namen Grün machen
        self.button_liste_aber_nur_damit_ich_den_richtigen_finde_yeah[self.richtige_antwort].configure(bg="green")

    def buttons_anschalten_und_zuruecksetzen(self):
        self.button_oben_links["state"] = "normal"
        self.button_oben_rechts["state"] = "normal"
        self.button_unten_links["state"] = "normal"
        self.button_unten_rechts["state"] = "normal"

        self.button_oben_links.configure(bg=self.standard_farbe)
        self.button_oben_rechts.configure(bg=self.standard_farbe)
        self.button_unten_links.configure(bg=self.standard_farbe)
        self.button_unten_rechts.configure(bg=self.standard_farbe)

    def auswertung(self):

        #Alle widgets zu Seite schmeißen
        self.button_oben_links.place(x=700)
        self.button_oben_rechts.place(x=700)
        self.button_unten_links.place(x=700)
        self.button_unten_rechts.place(x=700)
        self.angezeigtes_bild.place(x=700)
        self.naechste_runde_button.place(x=700)

        self.richtige_antworten_text.configure(text="Anzahl der Richtigen Antworten")
        self.richtige_antworten_text.place(x=10,y=180)

        self.richtige_antworten.configure(text=self.richtig_geratene_antworten,bg="green")
        self.richtige_antworten.place(x=150, y=200)

        self.falsche_antworten_text.configure(text="Anzahl an falschen Antworten:")
        self.falsche_antworten_text.place(x=280,y=180)

        self.falsche_antworten.configure(text=self.falsch_geratene_antworten,bg="red")
        self.falsche_antworten.place(x=420,y=200)

        self.nochmal_spielen_button.place(x=200,y=300)

    def nochmal_spielen(self):
        self.buttons_anschalten_und_zuruecksetzen()
        self.nochmal_spielen_button.place(x=700)
        self.richtige_antworten_text.place(x=700)
        self.richtige_antworten.place(x=700)
        self.falsche_antworten_text.place(x=700)
        self.falsche_antworten.place(x=700)
        self.richtig_geratene_antworten = 0
        self.falsch_geratene_antworten = 0


        self.schwierigkeit_anzeigen()