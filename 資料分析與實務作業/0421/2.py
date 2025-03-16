from tkinter import *

window = Tk()
window.title("好友名單")
lab1 = Label(window,text="Peter",
             bg="lightyellow",
             width=15)
lab2 = Label(window,text="Kevin",
             bg="lightgreen",
             width=15)
lab3 = Label(window,text="Tracy",
             bg="lightblue",
             width=15)
lab4 = Label(window,text="John",
             bg="lightpink",
             width=15)
lab5 = Label(window,text="Tommy",
             bg="skyblue",
             width=15)
lab6 = Label(window,text="Mike",
             bg="lightcoral",
             width=15)
lab7 = Label(window,text="Notron",
             bg="lightseagreen",
             width=15)
lab8 = Label(window,text="Mary",
             bg="lightcyan",
             width=15)
lab9 = Label(window,text="Vicent",
             bg="lightgray",
             width=15)


lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)
lab4.grid(row=1,column=0)
lab5.grid(row=1,column=1)
lab6.grid(row=1,column=2)
lab7.grid(row=2,column=0)
lab8.grid(row=2,column=1)
lab9.grid(row=2,column=2)

window.mainloop()
