
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import cv2
from customtkinter import *
import GuiFn as fn

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./cust")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def relative_to_code(path: str) -> Path:
    return OUTPUT_PATH / Path(path)


def relative_to_trans_imgs(path: str) -> Path:
    return OUTPUT_PATH / Path("./Transparent images") / Path(path)


def relative_to_mapp(path: str) -> Path:
    return OUTPUT_PATH / Path("./Mapprojected") / Path(path)


def toQuest():
    window.destroy()
    import q6


window = Tk()

window.geometry("1024x768")
window.configure(bg="#000000")

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

width = 400
heigth = 400
# imgpath = ""


mouths = ["hats/1221-removebg-preview.png",
         "hats/1222-removebg-preview.png",
         "hats/1223-removebg-preview.png",
         "hats/1224-removebg-preview.png",
         "hats/1225-removebg-preview.png",
         "hats/1226-removebg-preview.png",
         "hats/1227-removebg-preview.png",
         "hats/1228-removebg-preview.png",
         "hats/1229-removebg-preview.png"]

customimgs = mouths

jupbg = cv2.imread("img.png", -1)

# body_image_1 = PhotoImage(
#     file=relative_to_code("img.png"))
# body = canvas.create_image(
#     537.0,
#     409.0,
#     image=body_image_1,
# )


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

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    760.0,
    333.0,
    image=image_image_3
)


def Reset():
    button_1.configure(border_color="white", fg_color="#443D42")
    button_2.configure(border_color="white", fg_color="#443D42")
    button_3.configure(border_color="white", fg_color="#443D42")
    button_4.configure(border_color="white", fg_color="#443D42")
    button_5.configure(border_color="white", fg_color="#443D42")
    button_6.configure(border_color="white", fg_color="#443D42")
    button_7.configure(border_color="white", fg_color="#443D42")
    button_8.configure(border_color="white", fg_color="#443D42")
    button_9.configure(border_color="white", fg_color="#443D42")


def Select(button):
    # if n == 1:
    Reset()
    button.configure(border_color="#672DB2", fg_color="#9747FF", )
    # if n == 2:
    #     Reset()
    #     button_2.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 3:
    #     Reset()
    #     button_3.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 4:
    #     Reset()
    #     button_4.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 5:
    #     Reset()
    #     button_5.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 6:
    #     Reset()
    #     button_6.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 7:
    #     Reset()
    #     button_7.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 8:
    #     Reset()
    #     button_8.configure(border_color="#672DB2",fg_color="#9747FF",)
    # if n == 9:
    #     Reset()
    #     button_9.configure(border_color="#672DB2",fg_color="#9747FF",)


button_image_1 = PhotoImage(
    file=relative_to_code(customimgs[0]))
button_1 = CTkButton(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[0], button_1, 1),
    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_1.place(
    x=571.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_2 = PhotoImage(
    file=relative_to_code(customimgs[1]))

button_2 = CTkButton(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[1], button_2, 2),
    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_2.place(
    x=571.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_3 = PhotoImage(
    file=relative_to_code(customimgs[2]))

button_3 = CTkButton(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[2], button_3, 3),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)

button_3.place(
    x=571.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_4 = PhotoImage(
    file=relative_to_code(customimgs[3]))
button_4 = CTkButton(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[3], button_4, 4),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)

button_4.place(
    x=703.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_5 = PhotoImage(
    file=relative_to_code(customimgs[4]))

button_5 = CTkButton(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[4], button_5, 5),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_5.place(
    x=703.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_6 = PhotoImage(
    file=relative_to_code(customimgs[5]))

button_6 = CTkButton(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[5], button_6, 6),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_6.place(
    x=703.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_7 = PhotoImage(
    file=relative_to_code(customimgs[6]))

button_7 = CTkButton(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[6], button_7, 7),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)

button_7.place(
    x=835.0,
    y=141.0,
    width=116.0,
    height=107.0
)

button_image_8 = PhotoImage(
    file=relative_to_code(customimgs[7]))

button_8 = CTkButton(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[7], button_8, 8),

    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_8.place(
    x=835.0,
    y=267.0,
    width=116.0,
    height=107.0
)

button_image_9 = PhotoImage(
    file=relative_to_code(customimgs[8]))

button_9 = CTkButton(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choosecust(customimgs[8], button_9, 9),
    text="",
    relief="flat",
    corner_radius=5,
    border_width=10,
    border_color="white",
    fg_color="#443D42",
    hover=False
)
button_9.place(
    x=835.0,
    y=393.0,
    width=116.0,
    height=107.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=toQuest,

)
button_10.place(
    x=86.0,
    y=571.0,
    width=391.0,
    height=106.0
)
x, y = 0, 0


# def motion(event):
#     # global x, y
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
# window.bind('<Motion>', motion)

def place(event):
    x, y = event.x, event.y
    cust = cv2.imread(imgpath, -1)
    x_org = 281 - 230
    y_org = 300 - 233
    if x > x_org + int(cust.shape[1] / 2) and x < 511 - int(cust.shape[1] / 2) and y > y_org + int(cust.shape[0] / 2) and y < 533 - int(cust.shape[0] / 2):
        x = x - x_org
        y = y - y_org
        custjup = fn.blendWithTransparent(jupbg, cust, cust.shape[1], cust.shape[0], x - int(cust.shape[1] / 2),
                                          y - int(cust.shape[0] / 2))
        custjup = cv2.cvtColor(custjup, cv2.COLOR_BGRA2BGR)
        cv2.imwrite("img.png", custjup)
        global image_image_2
        image_image_2.configure(file="img.png")


def choosecust(path, button, n):
    global imgpath
    imgpath = path
    cust = cv2.imread(path, -1)
    custjup = fn.blendWithTransparent(jupbg, cust, cust.shape[1], cust.shape[0], 230-int(cust.shape[0]/2), 233-int(cust.shape[1]/2))
    custjup = cv2.cvtColor(custjup, cv2.COLOR_BGRA2BGR)
    cv2.imwrite("img.png", custjup)
    # global image_image_2
    image_image_2.configure(file="img.png")
    Select(button)


cust = cv2.imread("Transparent images/1-removebg-preview.png", -1)
window.bind('<Button>', place)

window.resizable(False, False)
window.mainloop()
