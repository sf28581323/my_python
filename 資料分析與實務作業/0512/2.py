from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=420, height=420)
canvas.pack()
for i in range(0,20,1):
    for j in range(0,20,1):
        canvas.create_polygon(10+20*i,10+20*j, 30+20*i,10+20*j, 30+20*i,30+20*j, 10+20*i,30+20*j, width=3, fill='', outline='blue')
