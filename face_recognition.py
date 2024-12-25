from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("algerian", 28, "bold"), bg="gold", fg="indigo")
        title_lbl.place(x=0, y=0, width=1279, height=45)    
        
        # Load image
        img_top = Image.open("college_images/Face-Recognition.jpg") 
        img_top = img_top.resize((1530, 614), resample=Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Display image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=614)     

        # Button
        b1_1 = Button(self.root, text="CLICK TO START RECOGNITION", cursor="hand2", font=("Arial", 12, "bold"), 
                      bg="#ff9999", fg="white", bd=0, relief=FLAT)
        b1_1.place(x=800, y=450, width=300, height=50)
        b1_1.bind("<Enter>", lambda e: b1_1.config(bg="#ff6666"))  
        b1_1.bind("<Leave>", lambda e: b1_1.config(bg="#ff9999"))  

        b1_1.config(command=self.face_recog)  # Add command to button to start recognition

    # ===========================Face recognition==============================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="9158", database="face_recogniser")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 80:
                    cv2.putText(img, f"Roll N0:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)


                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        

        faceCascade = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)  
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Unable to access the webcam.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to retrieve frame from the webcam.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            if cv2.waitKey(1) == 13:

                break

        video_cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
