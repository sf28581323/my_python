from tkinter import *
import tkinter.messagebox
import sys
import os

tk = Tk()
tk.title("OOXX")
p1 = StringVar()
p2 = StringVar()
bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnClick(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "O"
        bclick = False
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "X"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("OOXX", "X Wins!")

    elif(flag == 8):
        tkinter.messagebox.showinfo("OOXX", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("OOXX", "O Wins!")

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

buttons = StringVar()

button1 = Button(tk, text=' ', width=8, command=lambda: btnClick(button1))
button1.grid(row=0, column=0)

button2 = Button(tk, text=' ', width=8, command=lambda: btnClick(button2))
button2.grid(row=0, column=1)

button3 = Button(tk, text=' ', width=8, command=lambda: btnClick(button3))
button3.grid(row=0, column=2)

button4 = Button(tk, text=' ', width=8, command=lambda: btnClick(button4))
button4.grid(row=1, column=0)

button5 = Button(tk, text=' ', width=8, command=lambda: btnClick(button5))
button5.grid(row=1, column=1)

button6 = Button(tk, text=' ', width=8, command=lambda: btnClick(button6))
button6.grid(row=1, column=2)

button7 = Button(tk, text=' ', width=8, command=lambda: btnClick(button7))
button7.grid(row=2, column=0)

button8 = Button(tk, text=' ', width=8, command=lambda: btnClick(button8))
button8.grid(row=2, column=1)

button9 = Button(tk, text=' ', width=8, command=lambda: btnClick(button9))
button9.grid(row=2, column=2)

button10 = Button(tk, text='重新開始', width=8, command= restart)
button10.grid(row=3, column=1)

tk.mainloop()
