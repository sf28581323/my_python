from tkinter import *
from tkinter import messagebox

def myMsg():
    messagebox.showinfo("我的對話方塊","Hello, World!")

window = Tk()
window.title("tk")
window.geometry("230x70")

Button(window,text="顯示訊息",command=myMsg).pack()

window.mainloop()
