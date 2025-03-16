import tkinter
import time

def gettime():
    # 獲取當前時間並轉為字串
    timestr = time.strftime("%H:%M:%S")
    # 重新設定標籤文字
    lb.configure(text=timestr)
    # 每隔一秒呼叫函式gettime自身獲取時間
    root.after(1000, gettime)

root = tkinter.Tk()
root.title('電子時鐘')
# 設定字型大小顏色
lb = tkinter.Label(root, text='', fg='blue', font=("黑體", 80))
lb.pack()
gettime()
root.mainloop()
