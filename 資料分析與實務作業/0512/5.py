from tkinter import *
from random import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=350)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
canvas.create_text(20,40,text='ball 1')
canvas.create_text(20,140,text='ball 2')
canvas.create_text(40,340,text='哪一個球獲勝:')
e1 = Entry(canvas)
canvas.create_window(115,340,width=70,window = e1)
ballPos1 = canvas.coords(id1)
ballPos2 = canvas.coords(id2)

for x in range(0, 130):
    if randint(1,100) > 40:
        canvas.move(id2, 5, 0)
    if randint(1,100) > 40:
        canvas.move(id1, 5, 0)
    tk.update()
    time.sleep(0.05)



