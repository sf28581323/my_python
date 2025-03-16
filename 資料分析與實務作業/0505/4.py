from tkinter import *

def change1():
    lab1.config(text="+")
def change2():
    lab1.config(text="-")
def change3():
    lab1.config(text="*")
def change4():
    lab1.config(text="/")
def cal():
    if lab1["text"] == "+":
        n3.set(n1.get()+n2.get())
    elif lab1["text"] == "-":
        n3.set(n1.get()-n2.get())
    elif lab1["text"] == "*":
        n3.set(n1.get()*n2.get())
    elif lab1["text"] == "/":
        n3.set(n1.get()/n2.get())
    
window = Tk()
window.title("Calculator")

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window,width=8,textvariable=n1)
lab1 = Label(window,width=8,text="+")
e2 = Entry(window,width=8,textvariable=n2)
btn1 = Button(window,width=5,text="+",command=change1)
btn2 = Button(window,width=5,text="-",command=change2)
btn3 = Button(window,width=5,text="*",command=change3)
btn4 = Button(window,width=5,text="/",command=change4)
btn5 = Button(window,width=5,text="=",command=cal)
e3 = Entry(window,width=8,textvariable=n3)

e1.grid(row=0,column=0)
lab1.grid(row=0,column=1)
e2.grid(row=0,column=2)
btn1.grid(row=1,column=1)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=1)
btn4.grid(row=4,column=1)
btn5.grid(row=5,column=1)
e3.grid(row=6,column=1)

window.mainloop()
