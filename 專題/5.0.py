from tkinter import *
from PIL import Image, ImageTk
import time

root = Tk()
root.title('tk')
top = Frame(root)
top.pack(side="top")
bottom = Frame(root)
bottom.pack(side="bottom")
x = 500
y = 500
i = 0
lbpic = Label(root, text = 'test', width=x, height=y)
lb = Label(root, text='', fg='blue', font=("黑體", 80))
images_list = ["cat.png", "dog.png", "pig.png"]
img = Image.open(images_list[0])
img = img.resize((x, y), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)
lbpic['image'] = image
lbpic.image = image


def all(lbpic):
    A = 1
    B = 2
    print(A+B)

def prev(lbpic):
    global img
    global i
    if i > 0:
        i -= 1
        img = Image.open(images_list[i])
        img = img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        lbpic.configure(image=image)
        lbpic.image = image
    else:
        i = len(images_list)-1
        img = Image.open(images_list[i])
        img = img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        lbpic.configure(image=image)
        lbpic.image = image


def next(lbpic):
    global img
    global i
    if i >= len(images_list)-1:
        img = Image.open(images_list[0])
        img = img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        lbpic.configure(image=image)
        lbpic.image = image
        i = 0
    else:
        i += 1
        img = Image.open(images_list[i])
        img = img.resize((x, y), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        lbpic.configure(image=image)
        lbpic.image = image

   
def change(event):
    global x
    global y
    image = ImageTk.PhotoImage(img.resize((event.width, event.height),Image.ANTIALIAS))
    x = event.width
    y = event.height
    lbpic['image'] = image
    lbpic.image = image

def sql():
    timestr = time.strftime("%H:%M:%S")
    lbpic.configure(text=timestr)
    root.after(1000, sql)

button = Button(root, text="run all", width=10, height=2, command=lambda: all(lbpic))
button.pack(in_=bottom, side="left")
button = Button(root, text="prev", width=10, height=2, command=lambda: prev(lbpic))
button.pack(in_=bottom, side="left")
button = Button(root, text="next", width=10, height=2, command=lambda: next(lbpic))
button.pack(in_=bottom, side="left")
button = Button(root, text="資料庫", width=10, height=2, command=lambda: sql())
button.pack(in_=bottom, side="left")
lbpic.bind('<Configure>', change)
lbpic.pack(fill=BOTH, expand=YES)
root.mainloop()