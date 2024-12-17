from tkinter import *
from functools import partial

class Main_Menu:
    def __init__(self, window):
        self.win = window
        
        # Menu container - modern green with subtle shadow
        self.menu_contain = Frame(self.win, bg="#2E7D32", height=100, bd=2, relief="ridge")
        self.menu_lbl = Label(self.menu_contain, text="Main Menu", font=("Century Gothic", 20, "bold"),
                              fg="white", bg="#2E7D32", padx=20, anchor="center")
        
        self.btns = []
        self.btn_txt = ["View Profile", "Search Student's Profiles", "View All Student Profiles", "Add New Student", "Logout"]
        self.funcs = []

        # Content area (main working space)
        self.content_contain = Frame(self.win, bg="#F8F9FA", relief="flat", bd=0)

    def make_btns(self):
        for i, txt in enumerate(self.btn_txt):
            # Buttons with modern styling and hover effects
            btn = Button(self.menu_contain, text=txt, font=("Century Gothic", 14, "bold"),
                         bg="#FFFFFF", fg="#2E7D32", activebackground="#A5D6A7", activeforeground="black",
                         bd=0, relief="flat", cursor="hand2", width=25, height=2)
            btn.config(command=partial(self.funcs[i]))
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#A5D6A7", fg="#1B5E20"))  # Hover effect
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#FFFFFF", fg="#2E7D32"))  # Remove hover effect
            self.btns.append(btn)

    def main_screen(self, student_name=None):
        # Style and pack the menu container
        self.menu_contain.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.menu_lbl.pack(pady=20)
        
        # Arrange buttons with padding
        for btn in self.btns:
            btn.pack(pady=10, padx=10)
        
        # Style content area
        self.content_contain.pack(fill=BOTH, expand=True, padx=15, pady=10)
        self.content_frame = Frame(self.content_contain, bg="#FFFFFF", bd=2, relief="groove")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

        # Display the welcome message if student_name is provided
        if student_name:
            Label(self.content_frame, text=f"Welcome, {student_name}!", font=("Century Gothic", 24, "bold"), bg="#FFFFFF", fg="#2E7D32").pack(pady=20)

            # Load and display the PNG image when logged in
            try:
                # Load the PNG image (Ensure the path to the image is correct)
                img = PhotoImage(file="photo.png")
                img_label = Label(self.content_frame, image=img, bg="#FFFFFF")
                img_label.image = img  # Keep a reference to the image object
                img_label.pack(pady=20)  # Display the image below the welcome message
            except Exception as e:
                print(f"Error loading image: {e}")

    def clear_content(self):
        for widget in self.content_contain.winfo_children():
            widget.destroy()
