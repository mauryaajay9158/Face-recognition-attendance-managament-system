import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        pass
#=======================variables================================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

#img
        img = Image.open("D:/C programming/college_images/student tab.jpg") 
        img = img.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)
#img1
        img1 = Image.open("D:/C programming/college_images/student tab1.png") 
        img1 = img1.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=130)
#img2
        img2 = Image.open("D:/C programming/college_images/student tab2.jpg") 
        img2 = img2.resize((450, 130), resample=Image.BILINEAR)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=130)

#Background image
        img3 = Image.open("D:/C programming/college_images/bgimg.jpg") 
        img3 = img3.resize((1280, 550), resample=Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1280, height=550)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",28,"bold"),bg="White",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1283,height=45)        

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1247,height=455)

    #left label frame 
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=585,height=430)
   #img1
        # img_left = Image.open("D:/C programming/college_images/student tab4.png") 
        # img_left = img_left.resize((565, 130), resample=Image.BILINEAR)

        # self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        # f_lbl = Label(left_frame, image=self.photoimg_left)
        # f_lbl.place(x=5, y=0, width=565, height=80)   
#current course information 
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=20,width=570,height=105)

#department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
 #course
        course_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#year
        year_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=0,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 
#semester
        semester_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=0,column=0,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)   

#Class student information 
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=140,width=570,height=262) 

#studentID
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=16,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


#student name 
        studenName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studenName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studenName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",12,"bold"))
        studenName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",9,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W) 
#Roll no.
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=16,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
#gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",9,"bold"),state="readonly",width=20)
        gender_combo["values"]=("MALE","FEMALE","OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W) 

#date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=16,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W) 

#Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=16,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W) 
#phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=16,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)      
#radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)     

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo sample",value="No")
        radiobtn2.grid(row=6,column=1)     

#buttons frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=165,width=566,height=35)     

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0) 

        update_btn=Button(btn_frame,text="Update",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1) 

        delete_btn=Button(btn_frame,text="delete",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2) 

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3) 

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=566,height=35)    

        take_photo_btn=Button(btn_frame1,command=self.start_face_capture,text="Take Photo Sample",width=27,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)               

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=27,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)  
        


        #Right label frame 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        right_frame.place(x=605,y=10,width=628,height=430)
# img2
        img_right = Image.open("D:/C programming/college_images/student tab4.png") 
        img_right = img_right.resize((610, 130), resample=Image.BILINEAR)

        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=610, height=80) 
     
        #==========================SEARCH SYSTEM===========================================
 #search frame
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=85,width=614,height=65) 

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 


        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)  

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3) 

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3) 
#======================================================Table Frame==============================================================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=614,height=252)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
          
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DateOfBirth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="PhoneNo.")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
#====================================function declaration===============================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "all fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="9158",
                                               database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_radio1.get(),
                ))
                conn.commit()  # Commit the transaction
                self.fetch_data()
                conn.close()  # Close the connection
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
#====================fetch data===============================

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="9158", database="face_recogniser")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

#============================Get cursor=================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_radio1.set(data[12])
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    def start_face_capture(self):
        face_classifier = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        cap = cv2.VideoCapture(1)
        img_id = 0

        while True:
            ret, my_frame = cap.read()
            cropped_face = self.face_cropped(my_frame, face_classifier)
            if cropped_face is not None:
                img_id += 1
                face = cv2.resize(cropped_face, (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                os.makedirs("data", exist_ok=True)
                file_name_path = "data/user." + str(self.va_std_id.get()) + "." + str(img_id) + ".jpg"
                print("Saving images to :",file_name_path)
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or int(img_id) == 100:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Generating Data sets completed!")
    def face_cropped(self, img, face_classifier):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_cropped = img[y:y+h, x:x+w]
            return face_cropped
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="9158", database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s, course=%s, year=%s, semester=%s, Student_id=%s,Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Photosamle=%s where Student_id=%s",
                              (self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                               self.var_semester.get(), self.va_std_id.get(), self.var_std_name.get(),
                               self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),
                               self.var_email.get(), self.var_phone.get(), self.var_radio1.get(),
                               id + 1
                               ))
                self.start_face_capture(id)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"An error occured: {str(e)}",parent=self.root)
                
               

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
