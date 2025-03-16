from tkinter import *

def cal():
    n3.set(n2.get()/(n1.get()/100)**2)

window = Tk()
window.title("tk")

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

lab1 = Label(window,text="請輸入身高(公分):").pack()
e1 = Entry(window,width=20,textvariable=n1).pack()
lab2 = Label(window,text="請輸入體重(公斤):").pack()
e2 = Entry(window,width=20,textvariable=n2).pack()
btn = Button(window,width=20,text="計算BMI",command=cal).pack()
e3 = Entry(window,width=20,textvariable=n3).pack()

window.mainloop()
