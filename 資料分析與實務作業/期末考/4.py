from tkinter import *
from tkinter import messagebox

def printInfo():
    selection = ''
    for i in checkboxes:    #檢查此字典
        if checkboxes[i].get() == True:     #被選取則執行
            selection = selection + breakfast[i] + "\t"
    messagebox.showinfo("核取結果",selection)

window = Tk()
window.title("tk")  #視窗標題
window.geometry("200x175")  #視窗大小

Label(window,text="請核取您喜歡的早餐:").pack()

breakfast = {0:"三明治",1:"潛水艇",2:"燒餅",3:"飯糰",4:"蘿蔔糕"}     #早餐字典
checkboxes = {}     #字典存放被選取項目
for i in range(len(breakfast)):     #將早餐字典轉成核取方塊
    checkboxes[i] = BooleanVar()    #布林變數物件
    Checkbutton(window,text=breakfast[i],
                variable=checkboxes[i]).pack()

Button(window,text="確定",command=printInfo).pack()

window.mainloop()
