from tkinter import *
from PIL import ImageTk, Image
from tkvideo import tkvideo

def cat(panel):
    path = "cat.png"
    img = Image.open(path)
    img = img.resize((x, y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

def dog(panel):
    path = "dog.png"
    img = Image.open(path)
    img = img.resize((x, y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

def pig(panel):
    path = "pig.png"
    img = Image.open(path)
    img = img.resize((x, y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

def video(panel):
    player = tkvideo("C:\\Users\\charles\\Desktop\\python\\video.mp4", panel, loop = 1, size = (x,y))
    player.play()

 
window = Tk()

top = Frame(window)
top.pack(side="top")
bottom = Frame(window)
bottom.pack(side="bottom")

x = 500
y = 500
img = Image.open('cat.png')
img = img.resize((x, y), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(window, image = img, width=x, height=y)
panel.pack(side = "top", fill = "both", expand = "yes")

prev_button = Button(window, text="cat", width=10, height=2, command=lambda: cat(panel))
prev_button.pack(in_=bottom, side="left")
next_button = Button(window, text="dog", width=10, height=2, command=lambda: dog(panel))
next_button.pack(in_=bottom, side="left")
next_button = Button(window, text="pig", width=10, height=2, command=lambda: pig(panel))
next_button.pack(in_=bottom, side="left")
next_button = Button(window, text="video", width=10, height=2, command=lambda: video(panel))
next_button.pack(in_=bottom, side="left")


window.mainloop()