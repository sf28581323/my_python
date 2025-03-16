from tkinter import *

window = Tk()
window.title("台灣企業")
lab1 = Label(window,text="台塑企業",
             bg="lightyellow",
             width=15)
lab2 = Label(window,text="台積電",
             bg="lightgreen",
             width=15)
lab3 = Label(window,text="聯發科",
             bg="lightblue",
             width=15)
lab4 = Label(window,text="華碩電腦",
             bg="lightpink",
             width=15)
lab5 = Label(window,text="宏碁電腦",
             bg="skyblue",
             width=15)
lab1.pack()
lab2.pack()
lab3.pack()
lab4.pack()
lab5.pack()

window.mainloop()
