import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 28, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1283, height=45) 

        img_top = Image.open("college_images/Service-Help-Desk.png") 
        img_top = img_top.resize((1273,600), resample=Image.BILINEAR)

        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1273, height=600)

        dev_label=Label(f_lbl,text="Email:Kushwahaajay9158@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=420,y=530)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
