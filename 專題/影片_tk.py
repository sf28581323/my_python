import cv2
from tkinter import *
from PIL import Image, ImageTk

#Creating Tkinter Window and Label
root = Tk()
video = Label(root)
video.pack()

vid = cv2.VideoCapture('video.mp4')

while(True):
    
    ret, frame = vid.read()

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    video.config(image=imgtk)

    root.update()

vid.release()

cv2.destroyAllWindows()