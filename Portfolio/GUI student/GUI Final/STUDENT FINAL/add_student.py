from tkinter import *

class Add_Student:

    def __init__(self, student):
        self.student_data = student
        self.message_label = None  # For feedback messages

    def write_student_info(self, name, age, id_num, email, phone_num):
        try:
            with open('student_data.txt', 'a') as file:
                file.write(name + '\t')
                file.write(age + "\t")
                file.write(id_num + "\t")
                file.write(email + "\t")
                file.write(phone_num + "\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def add_student(self, name, age, id, email, phone):
        if not all([name, age, id, email, phone]):
            if self.message_label:
                self.message_label.config(text="All fields must be filled!", fg="red")
            return False

        student = [name, age, id, email, phone]
        self.student_data.student_list.append(student)
        self.write_student_info(name, age, id, email, phone)

        if self.message_label:
            self.message_label.config(text=f"Student '{name}' added successfully!", fg="green")
        return True

    def register(self, flds):
        student = [fld.get() for fld in flds]
        self.add_student(*student)

    def register_ui(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()  # Clear the frame

        # Main frame container with padding
        frame.configure(bg="#f0f0f0")
        
        # Title label with bold font and bigger size
        title_label = Label(frame, text="Register New Student", font=("Century Gothic", 20, "bold"), bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=2, pady=25)

        lbls = ['Name:', 'Age:', 'ID Number:', 'Email Address:', 'Phone Number:']
        flds = []

        # Create labels and fields with grid layout for alignment
        for i, txt in enumerate(lbls):
            # Label for the field
            Label(frame, text=txt, font=("Century Gothic", 14), bg="#f0f0f0").grid(row=i+1, column=0, sticky="w", padx=15, pady=5)

            # Input field (Entry widget)
            fld = Entry(frame, font=("Century Gothic", 14), bg="#e8e8e8", bd=2, relief="solid", width=30)
            fld.grid(row=i+1, column=1, padx=15, pady=15)
            flds.append(fld)

        # Styled register button
        register_button = Button(frame, text="REGISTER", command=lambda: self.register(flds), font=("Century Gothic", 14, "bold"),
                                 bg="#4CAF50", fg="white", relief="raised", bd=2, width=20, height=2)
        register_button.grid(row=len(lbls)+1, column=0, columnspan=2, pady=20)

        # Feedback message label with green or red color
        self.message_label = Label(frame, text="", font=("Century Gothic", 12), bg="#f0f0f0")
        self.message_label.grid(row=len(lbls)+2, column=0, columnspan=2, pady=5)
