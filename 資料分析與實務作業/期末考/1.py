from tkinter import *

def myMsg():
    label["text"] = "Hello, World!"

window = Tk()
window.title("tk")           #視窗標題
window.geometry("230x70")    #視窗大小
label = Label(window)        #視窗內容
btn = Button(window,text="顯示訊息",command=myMsg)
btn.pack()                   #按鈕
label.pack()                 #字串
window.mainloop()
