from tkinter import *

class Search_Student:
    def __init__(self, student_list):
        self.student_list = student_list
    
    def student_profile(self, id):    
        for student in self.student_list:
            if student[2] == id:
                return f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}"
        return f"Student not found."
    
    def student_exists(self, id):
        for student in self.student_list:
            if student[2] == id:
                return True
        return False
    
    def search_ui(self, frame, id):
        # Clear existing content
        for widget in frame.winfo_children():
            widget.destroy()

        profile_text = self.student_profile(id)

        # Display the profile text in a label
        profile_label = Label(frame, text=profile_text, font=("Century Gothic", 14), anchor="w", justify=LEFT, padx=10)
        profile_label.pack(pady=20)

    def search_input_ui(self, frame):
        # Clear existing content
        for widget in frame.winfo_children():
            widget.destroy()

        # Title label for the search UI with increased size
        title_label = Label(frame, text="Search for Student Profile", font=("Century Gothic", 18, "bold"), bg="#4CAF50", fg="white")
        title_label.pack(pady=20)

        # Entry label and input field for student ID
        Label(frame, text="Enter Student ID:", font=("Century Gothic", 14), bg="#f0f0f0").pack(pady=10)
        
        id_entry = Entry(frame, font=("Century Gothic", 14), width=30, bd=3, relief="solid")
        id_entry.pack(pady=20)

        # Search button with bigger size
        search_button = Button(frame, text="Search", font=("Century Gothic", 16, "bold"), bg="#4CAF50", fg="white", activebackground="#66bb6a",
                               command=lambda: self.search_ui(frame, id_entry.get()))
        search_button.pack(pady=20)
