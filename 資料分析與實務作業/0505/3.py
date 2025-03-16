from tkinter import *

def cal():
    n2.set(n1.get()*(9/5)+32)

window = Tk()
window.title("溫度轉換程式")

n1 = IntVar()
n2 = IntVar()

lab1 = Label(window,text="攝氏:")
e1 = Entry(window,width=20,textvariable=n1)
lab2 = Label(window,text="華氏:")
lab3 = Label(window,textvariable=n2)
btn = Button(window,text="轉換",command=cal)

lab1.grid(row=0,column=0)
e1.grid(row=0,column=1)
lab2.grid(row=1,column=0)
lab3.grid(row=1,column=1)
btn.grid(row=2,column=1)

window.mainloop()
