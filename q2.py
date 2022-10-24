# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time
import cv2
import vars
question = vars.question

import random

n = random.randint(0, 14)
while(vars.quebool[n]==False):
    n = random.randint(0, 14)

n = random.randint(0, 14)
zeeko = question[n][0]
ans1 = question[n][1]
ans2 = question[n][2]
ans3 = question[n][3]
ans4 = question[n][4]
soloution = question[n][5]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./quest")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def relative_to_code(path: str) -> Path:
    return OUTPUT_PATH / Path(path)

window = Tk()

window.geometry("1024x768")
window.configure(bg="#000000")


def choose(button_image, ans):
    if (ans == question[n][5]):
        button_image.configure(file=relative_to_assets("button_green.png"))
        vars.quebool[n] = False
        vars.win = True
    else:
        button_image.configure(file=relative_to_assets("button_red.png"))
        if(question[n][5] == 1):
            button_image_5.configure(file=relative_to_assets("button_green.png"))
        elif (question[n][5] == 2):
            button_image_2.configure(file=relative_to_assets("button_green.png"))
        elif (question[n][5] == 3):
            button_image_3.configure(file=relative_to_assets("button_green.png"))
        elif (question[n][5] == 4):
            button_image_4.configure(file=relative_to_assets("button_green.png"))


        vars.win = False



button_image = 0
ans = 0

def toCust():
    window.destroy()
    import custEyes

def toEnd():
    window.destroy()
    import endgame

def check(but, answer):
    if vars.win:
        toCust()
    elif vars.win == False:
        toEnd()


canvas = Canvas(
    window,
    bg="#000000",
    height=768,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_code("img.png"))
image_2 = canvas.create_image(
    281.0,
    300.0,
    image=image_image_2
)


def reset():
    button_image_2.configure(file=relative_to_assets("button.png"))
    button_image_3.configure(file=relative_to_assets("button.png"))
    button_image_4.configure(file=relative_to_assets("button.png"))
    button_image_5.configure(file=relative_to_assets("button.png"))


# def select(n):
#     if n == 5:
#         reset()
#         button_image_5.configure(file=relative_to_assets("selected.png"))
#     if n == 2:
#         reset()
#         button_image_2.configure(file=relative_to_assets("selected.png"))
#     if n == 3:
#         reset()
#         button_image_3.configure(file=relative_to_assets("selected.png"))
#     if n == 4:
#         reset()
#         button_image_4.configure(file=relative_to_assets("selected.png"))


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check(button_image, ans)

)
button_1.place(
    x=86.0,
    y=571.0,
    width=391.0,
    height=106.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    760.0,
    333.0,
    image=image_image_3
)

canvas.create_text(
    662.0,
    87.0,
    anchor="nw",
    text="Game Time",
    fill="#FFFFFF",
    font=("GRANDGALAXY", 31 * -1)
)

canvas.create_text(
    576.0,
    152.0,
    anchor="nw",
    text=zeeko,
    fill="#FFFFFF",
    font=("GRANDGALAXY", 18 * -1)
)

# ====================================================================================================


# =====================================================================================================


button_image_2 = PhotoImage(
    file=relative_to_assets("button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose(button_image_2, 2),
    relief="flat",
    text=ans2,
    compound='center',
    font=("GRANDGALAXY", 15 * -1)

)
button_2.place(
    x=575.0,
    y=322.0,
    width=370.0,
    height=77.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose(button_image_3, 3),
    relief="flat",
    text=ans3,
    compound='center',
    font=("GRANDGALAXY", 15 * -1)
)
button_3.place(
    x=575.0,
    y=414.0,
    width=370.0,
    height=77.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose(button_image_4, 4),
    relief="flat",
    text=ans4,
    compound='center',
    font=("GRANDGALAXY", 16 * -1)
)
button_4.place(
    x=575.0,
    y=506.0,
    width=370.0,
    height=77.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose(button_image_5, 1),
    relief="flat",
    text=ans1,
    compound='center',
    font=("GRANDGALAXY", 15 * -1)

)
button_5.place(
    x=575.0,
    y=230.0,
    width=370.0,
    height=77.0
)
window.resizable(False, False)
window.mainloop()


