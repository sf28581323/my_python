from tkinter import *
import time

def move(event):
    if event.keysym == "Up":
            canvas.move(1,0,-5) 
    elif event.keysym == "Down":
            canvas.move(1,0,5)
    elif event.keysym == "Left":            
            canvas.move(1,-5,0)            
    elif event.keysym == "Right":            
            canvas.move(1,5,0)

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_oval(10,10,11,11,fill='red')
canvas.bind_all('KeyPress-Up',move)
canvas.bind_all('KeyPress-Down',move)
canvas.bind_all('KeyPress-Left',move)
canvas.bind_all('KeyPress-Right',move)

tk.mainloop()
