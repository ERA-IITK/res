from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

import cv2
import numpy as np

import matplotlib.pyplot as plt 
import matplotlib.image as img 

img = img.imread('pic.jpg') 

rows,cols,ch = img.shape

pts1 = np.float32([[489,465],[1099,404],[1360,688],[207,936]])
pts2 = np.float32([[354,448-328],[808-230,448-214],[354,448-93],[150,448-214]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(808,448))

  
# show image 
plt.imshow(img)
  
# show image 
plt.imshow(dst)
plt.show()  
#cv2.imshow('as', dst)

if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    img = ImageTk.PhotoImage(Image.open('pic.jpg'))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
        #outputting x and y coords to console
        print (event.x,event.y)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)

    root.mainloop()
