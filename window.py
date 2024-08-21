import tkinter as tk


class App(tk.Tk):
    def __init__(self,name):
        super().__init__()
        self.name = name

        self.title("Philipps Game")
        self.geometry("400x500")



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
