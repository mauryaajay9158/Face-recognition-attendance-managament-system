import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 28, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1283, height=45) 

        img_top = Image.open("college_images/developer.png") 
        img_top = img_top.resize((1200,600), resample=Image.BILINEAR)

        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1200, height=600)

        # Frame
        btn_frame = Frame(f_lbl, bd=2, bg="lightpink")
        btn_frame.place(x=450, y=0, width=650, height=550)

        # Project Description
        desc_lbl = Label(btn_frame, text="Welcome to our Face Recognition System project!", 
                         font=("times new roman", 20, "bold"), bg="white", fg="green")
        desc_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Developers Names
        dev_lbl = Label(btn_frame, text="Developers Names: ", 
                        font=("times new roman", 17, "bold"), bg="white", fg="blue")
        dev_lbl.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        dev1_lbl = Label(btn_frame, text="1) Ajay Kushwaha (SE-IT[Theem College of Engineering])", 
                         font=("times new roman", 18, "bold"), bg="white", fg="maroon")
        dev1_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        dev2_lbl = Label(btn_frame, text="2) Mayur Prajapati (TE-IT[Theem College of Engineering])", 
                         font=("times new roman", 18, "bold"), bg="white", fg="maroon")
        dev2_lbl.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        dev3_lbl = Label(btn_frame, text="3) Jaivesh Vaidya (TE-IT[Theem College of Engineering])", 
                         font=("times new roman", 18, "bold"), bg="white", fg="maroon")
        dev3_lbl.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        dev4_lbl = Label(btn_frame, text="4) Harshal Kadam (TE-IT[Theem College of Engineering])", 
                         font=("times new roman", 18, "bold"), bg="white", fg="maroon")
        dev4_lbl.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
