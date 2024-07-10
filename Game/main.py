import anime_lists as aL
import random
import tkinter as tk
from PIL import Image, ImageTk

#Fenster machen
root = tk.Tk()


def get_anime_name():
    character_number_length_list = len(aL.anime_list)
    random_character_number = random.randrange(0, character_number_length_list)
    character_name = list(aL.anime_list.keys())[random_character_number]
    aL.anime_list.pop(character_name, None)
    return character_name


image = Image.open(aL.anime_list["Megumin"])
image_groeße = image.resize((250, 200))
python_bild = ImageTk.PhotoImage(image_groeße)
tk.Label(image=python_bild).place(x=120, y=0)


def any_click():
    print(image)


knopf_oben_links = tk.Button(root, text=get_anime_name())
knopf_oben_rechts = tk.Button(root, text=get_anime_name())
knopf_unten_links = tk.Button(root, text=get_anime_name())
knopf_unten_rechts = tk.Button(root, text=get_anime_name(), command=any_click)

knopf_oben_links.place(x=50, y=250, width=120, height=40)
knopf_oben_rechts.place(x=300, y=250, width=120, height=40)
knopf_unten_links.place(x=50, y=350, width=120, height=40)
knopf_unten_rechts.place(x=300, y=350, width=120, height=40)

window_width = 480
window_height = 500

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
