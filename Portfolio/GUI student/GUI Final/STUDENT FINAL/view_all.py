from tkinter import *
import tkinter.scrolledtext as scrolledtext

class View_All_Students:
    def __init__(self, student_list):
        self.student_list = student_list
    
    def show_list(self):
        student_info_str = ""
        for student in self.student_list:
            student_info_str += f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}\n\n"
        return student_info_str

    def list_ui(self, frame):
        # Create a ScrolledText widget
        text_widget = scrolledtext.ScrolledText(frame, wrap=WORD, height=20, width=50)
        text_widget.insert(INSERT, self.show_list())
        text_widget.config(state=DISABLED)  # Make the text widget read-only
        
        # Pack the text widget to fill the available space
        text_widget.pack(expand=True, fill=BOTH)
