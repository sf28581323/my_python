from tkinter import *
from PIL import Image, ImageTk
import time

root = Tk()
root.title('tk')
top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side="bottom")
x = 500
y = 500
i = 0
var = StringVar()
lb = Label(root, textvariable=var, fg='blue', font=("黑體", 40))
lb.pack()
lbpic = Label(root, text = 'test', width=x, height=y)
lbpic.pack()
images_list = ["cat.png", "dog.png", "pig.png"]
img = Image.open(images_list[0])
img = img.resize((x, y), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)
lbpic['image'] = image
lbpic.image = image

on_hit = False

def all(lb):
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('執行所有程式')
    else:
        on_hit = False
        var.set('')

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
    var.set(time.strftime("%H:%M:%S"))
    # 每隔一秒呼叫函式自身獲取時間
    root.after(1000, sql)

button = Button(bottom, text="run all", width=10, height=2, command=lambda: all(lbpic))
button.pack(in_=bottom, side="left")
button = Button(bottom, text="prev", width=10, height=2, command=lambda: prev(lbpic))
button.pack(in_=bottom, side="left")
button = Button(bottom, text="next", width=10, height=2, command=lambda: next(lbpic))
button.pack(in_=bottom, side="left")
button = Button(bottom, text="資料庫", width=10, height=2, command=lambda: sql())
button.pack(in_=bottom, side="left")
lbpic.bind('<Configure>', change)
lbpic.pack(fill=BOTH, expand=YES)
root.mainloop()