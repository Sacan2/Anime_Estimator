import tkinter as tk

class App(tk.Tk):
    def __init__(self, name_start_button):
        super().__init__()
        self.name_start_button = name_start_button


        self.title("Philipps Game")
        self.geometry("400x500")




        self.start_button_bild_aussuchen = tk.Button(self, text=self.name_start_button, height=2, width=9)
        self.start_button_bild_aussuchen.configure(command=self.schwierigkeit_wählen)
        self.start_button_bild_aussuchen.place(x=200, y=160)

        #Schwierigkeit Auswählen
        self.leichter_modus = tk.Button(self, text="leichter Modus", height=2,width=12)
        self.leichter_modus.configure(command=self.zurück_gehen)
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


    def schwierigkeit_wählen(self):
        self.start_button_bild_aussuchen.place(x=700)
        self.leichter_modus.place(x=190, y=160)

    def zurück_gehen(self):
        self.start_button_bild_aussuchen.place(x=200)
        self.leichter_modus.place(x=700)