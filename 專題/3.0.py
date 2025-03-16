from tkinter import *
from PIL import Image, ImageTk
import cv2

root = Tk()
root.title('tk')
top = Frame(root)
top.pack(side="top")
bottom = Frame(root)
bottom.pack(side="bottom")
lbpic = Label(root, text = 'test', width=500, height=500)
img = Image.open('cat.png')
image = ImageTk.PhotoImage(img)
lbpic['image'] = image
lbpic.image = image
cap = cv2.VideoCapture("video.mp4")

def video(lbpic):
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.namedWindow('frame', 0)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
def change(event):
    image = ImageTk.PhotoImage(img.resize((event.width, event.height),Image.ANTIALIAS))
    lbpic['image'] = image
    lbpic.image = image


button = Button(root, text="video", width=10, height=2, command=lambda: video(lbpic))
button.pack(in_=bottom, side="left")
lbpic.bind('<Configure>', change)
lbpic.pack(fill=BOTH, expand=YES)

root.mainloop()