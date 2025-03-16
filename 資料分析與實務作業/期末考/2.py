from tkinter import *

tk = Tk()   #視窗標題
canvas = Canvas(tk, width=210, height=120)  #畫布大小
canvas.pack()   #畫圓  
for i in range(0,10,1):
    canvas.create_oval(10+10*i, 10, 110+10*i, 110)  #畫10個每個位移10像素
