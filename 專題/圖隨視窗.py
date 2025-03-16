from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('tk')
top = Frame(root)
top.pack(side="top")
bottom = Frame(root)
bottom.pack(side="bottom")
x = 500
y = 500
lbpic = Label(root, text = 'test', width=x, height=y)
images_list = ["cat.png", "dog.png", "pig.jpg"]
img = Image.open(images_list[0])
img = img.resize((x, y), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)
lbpic['image'] = image
lbpic.image = image

def cat(lbpic):
    global img
    img = Image.open(images_list[0])
    img = img.resize((x, y), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    lbpic.configure(image=image)
    lbpic.image = image

def dog(lbpic):
    global img
    img = Image.open(images_list[1])
    img = img.resize((x, y), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    lbpic.configure(image=image)
    lbpic.image = image


def pig(lbpic):
    global img
    img = Image.open(images_list[2])
    img = img.resize((x, y), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    lbpic.configure(image=image)
    lbpic.image = image
    
def change(event):
    image = ImageTk.PhotoImage(img.resize((event.width, event.height),Image.ANTIALIAS))
    lbpic['image'] = image
    lbpic.image = image


button = Button(root, text="cat", width=10, height=2, command=lambda: cat(lbpic))
button.pack(in_=bottom, side="left")
button = Button(root, text="dog", width=10, height=2, command=lambda: dog(lbpic))
button.pack(in_=bottom, side="left")
button = Button(root, text="pig", width=10, height=2, command=lambda: pig(lbpic))
button.pack(in_=bottom, side="left")
lbpic.bind('<Configure>', change)
lbpic.pack(fill=BOTH, expand=YES)

root.mainloop()