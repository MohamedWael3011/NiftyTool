
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./start")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def toColour():
    window.destroy()
    import custPlants
window = Tk()

window.geometry("1024x768")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    389.0,
    image=image_image_1)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=toColour,
    relief="flat"
)
button_1.place(
    x=252.0,
    y=397.0,
    width=519.0,
    height=50.0
)

canvas.create_text(
    226.0,
    328.0,
    anchor="nw",
    text="---- Nifty Tool ----",
    fill="#FFFFFF",
    font=("GRANDGALAXY", 49 * -1)
)
window.resizable(False, False)
window.mainloop()
