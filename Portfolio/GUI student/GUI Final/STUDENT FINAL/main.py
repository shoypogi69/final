from student import Student_Info
from search_student import Search_Student
from view_all import View_All_Students
from add_student import Add_Student
from main_menu import Main_Menu
from tkinter import *
from functools import partial

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth() - 1280)//2}+{(win.winfo_screenheight() - 800)//2}")
win.title("Student Management System") 
win.configure(bg="#f0f0f0")  

stu = Student_Info()
addstud = Add_Student(stu)
search = Search_Student(stu.student_list)
view = View_All_Students(stu.student_list)
main = Main_Menu(win)

stu.read_student_info()

def login_check():
    global strikes
    student_id = stu_id.get()
    if search.student_exists(student_id):
        student_profile = search.student_profile(student_id)  # Fetch the student's profile
        if student_profile:
            student_name = student_profile.split("\n")[0].split(": ")[1]  # Extract only the student's name
            main.main_screen(student_name)  # Pass the student's name to the main screen
            login_fr.pack_forget()  # Remove the login frame after successful login
        else:
            strikes -= 1
            strikes_lbl.config(text=f"Invalid Student ID. You have {strikes} attempt/s remaining.")
    else:
        strikes -= 1
        strikes_lbl.config(text=f"Invalid Student ID. You have {strikes} attempt/s remaining.", fg="red")
    
    if strikes == 0:
        win.destroy()


login_fr = Frame(win, bg="#f0f0f0") 
login_lbl = Label(login_fr, text="Welcome! Login to Continue.", font=("Century Gothic", 18), bg="#f0f0f0")
stu_id = Entry(login_fr, font=("Century Gothic", 14), bg="#e8e8e8", bd=2)
login_btn = Button(login_fr, text="Login", command=login_check, font=("Century Gothic", 14), width=20, bg="#4CAF50", fg="white", relief="raised", bd=2)
strikes_lbl = Label(login_fr, text="", font=("Century Gothic", 12), bg="#f0f0f0")

strikes = 4

def clear(): 
    main.clear_content()

def search_for(student_id):
    clear()
    if search.student_exists(student_id):
        profile = search.student_profile(student_id)
        profile_frame = Frame(main.content_contain, bg="#ffffff", bd=2, relief="solid", padx=20, pady=20)
        profile_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        Label(profile_frame, text=f"{profile}", font=("Century Gothic", 14), anchor="w", justify=LEFT, bg="#ffffff").pack(pady=10)
        
    else:
        Label(main.content_contain, text="Student does not exist", font=("Century Gothic", 14), fg="red").pack(pady=20)

    # Add some visual separation
    separator = Frame(main.content_contain, height=2, bg="#d3d3d3")
    separator.pack(fill="x", pady=20)



def search_student():
    clear()
    id_entry = Entry(main.content_contain, font=("Century Gothic", 14), bg="#e8e8e8", bd=2, relief="solid")
    id_entry.pack(pady=20, expand=True, ipady=5, ipadx=10)

    search_button = Button(main.content_contain, text="Search", command=lambda: search_for(id_entry.get()), font=("Century Gothic", 14), bg="#4CAF50", fg="white", relief="raised", bd=2)
    search_button.pack(pady=10)

    # Add some visual separation
    separator = Frame(main.content_contain, height=2, bg="#d3d3d3")
    separator.pack(fill="x", pady=20)

    # Add a title or header
    Label(main.content_contain, text="Enter Student ID to Search", font=("Century Gothic", 12, "bold"), bg="#f0f0f0").pack(pady=5,anchor=N)



header_fr = Frame(login_fr, bg="#4CAF50", height=80)
Label(header_fr, text="Student Management System", font=("Century Gothic", 24, "bold"), bg="#4CAF50", fg="white").pack(pady=20)
content_fr = Frame(login_fr, bg="#f0f0f0")
Label(content_fr, text="Student ID:", font=("Century Gothic", 14), bg="#f0f0f0").pack(pady=5)
Label(content_fr, text="Welcome! Please Login to Continue", font=("Century Gothic", 18, "bold"), bg="#f0f0f0").pack(pady=20)


def login():
    # Clear the window
    login_fr.pack(expand=True, fill=BOTH)  # Expand frame to fill the window

    header_fr.pack(fill=X)

    content_fr.pack(expand=True)
    

    # Student ID Entry
    stu_id.pack(pady=10, ipadx=20, ipady=5)

    # Login Button
    login_btn.pack(pady=20)

    # Strikes Label for feedback
    strikes_lbl.config(bg="#f0f0f0", fg="red")
    strikes_lbl.pack(pady=5)



def func1():
    clear()

    # Create a simple frame for the profile
    profile_frame = Frame(main.content_contain, bg="#f0f0f0", padx=20, pady=20)
    profile_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)

    # Fetch the student profile
    student_profile = search.student_profile(stu_id.get())  # Assume this fetches the profile

    if student_profile:
        # Split the profile details into individual lines
        profile_lines = student_profile.split("\n")

        # Add a label for each profile piece (Name, Age, ID, etc.)
        for line in profile_lines:
            Label(profile_frame, text=line, font=("Century Gothic", 14), bg="#f0f0f0").pack(pady=5)

    else:
        # If profile doesn't exist, display a message
        Label(profile_frame, text="Student does not exist", font=("Century Gothic", 14), fg="red", bg="#f0f0f0").pack(pady=20)



def func2():
    clear()
    search_student_frame = Frame(main.content_contain, bg="#f0f0f0")  # Light background for the frame
    search.search_input_ui(search_student_frame)  # Call the UI method for search
    search_student_frame.pack(expand=True, fill=BOTH)  # Add the frame to the content container

    # You can apply additional design adjustments here if needed



def func3():
    clear()
    view.list_ui(main.content_contain)

def func4():
    clear()
    addstud.register_ui(main.content_contain)

def func5():
    clear()  # Clear main content
    global strikes
    strikes = 4
    strikes_lbl.config(text="")
    stu_id.delete(0, END)
    main.menu_contain.pack_forget()
    main.content_contain.pack_forget()
    login()


main.funcs.extend([func1, func2, func3, func4, func5])

main.make_btns()

login()

win.mainloop()
