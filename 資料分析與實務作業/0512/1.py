from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=250)
canvas.pack()
for i in range(0,20,1):
    canvas.create_polygon(10+5*i,10+5*i, 390-5*i,10+5*i, 390-5*i,240-5*i, 10+5*i,240-5*i, fill='', outline='blue')
