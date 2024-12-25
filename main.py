from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student
import os
import tkinter                                                                     #only used in exit button
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
class face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
#img
        img = Image.open("college_images/facial-recognition-system-concept-with-face-recognition-3d-scanning-interface.jpeg") 
        img = img.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)
#img1
        img1 = Image.open("college_images/images.png") 
        img1 = img1.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=130)
#img2
        img2 = Image.open("college_images/downloade.jpg") 
        img2 = img2.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=130)
#Background image
        img3 = Image.open("college_images/bgimg.jpg") 
        img3 = img3.resize((1280, 550), resample=Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1280, height=550)

        title_lbl=Label(bg_img,text=" FACE RECOGNITION SYSTEM ",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=45)

#Student details
        img4 = Image.open("college_images/studnetsicon.jpg") 
        img4 = img4.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100, y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=250,width=220,height=40)


 #Detect face button
        img5 = Image.open("college_images/download (2).jpg") 
        img5 = img5.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=390, y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=390, y=250,width=220,height=40) 

  #Attendance button
        img6 = Image.open("college_images/attendance.jpg") 
        img6 = img6.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=680, y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680, y=250,width=220,height=40)  

 #help button
        img7 = Image.open("college_images/help desk.jpg") 
        img7 = img7.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=970, y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=970, y=250,width=220,height=40)  

 #Train button
        img8 = Image.open("college_images/train button.jpg") 
        img8 = img8.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100, y=310,width=220,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=475,width=220,height=40)  

  #photos button
        img9 = Image.open("college_images/photos.jpg") 
        img9 = img9.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=390, y=310,width=220,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=390, y=475,width=220,height=40)     

  #developer button 
        img10 = Image.open("college_images/developer.png") 
        img10 = img10.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=680, y=310,width=220,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680, y=475,width=220,height=40)                         

#Exit button 
        img11 = Image.open("college_images/exit.jpg") 
        img11 = img11.resize((220, 220), resample=Image.BILINEAR)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=970, y=310,width=220,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=970, y=475,width=220,height=40)
    def open_img(self):
        os.startfile("data")   

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return         

# Function definition for student_details should be within the class definition
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)       

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 

        


if __name__ == "__main__":
    root = Tk()
    obj = face_Recognition_System(root)
    root.mainloop()
