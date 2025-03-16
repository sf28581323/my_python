from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=640, height=200)
canvas.pack()
canvas.create_text(40,95, text='東海大學', fill='red', font=('新華康綜藝體 Std W7',12))

for x in range(0,110):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
