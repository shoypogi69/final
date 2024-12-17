class Student_Info:
    student_list = []

    def __init__(self):
        self.name = ""
        self.age = ""
        self.id = ""
        self.email = ""
        self.phone = ""

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_id(self, id):
        self.id = id
    
    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone
    
    def read_student_info(self):
        file = open("student_data.txt", "r")

        students = file.read().split('\n')
        file.close()

        for student in students:
            if student.strip() == "":
                continue
                
            student_info = student.split("\t")

            if len(student_info) == 5:
                name = student_info[0]
                age = student_info[1]
                id_num = student_info[2]
                email = student_info[3]
                phone_num = student_info[4]

                self.student_list.append([name, age, id_num, email, phone_num])
            else:
                print(f"Skipping invalid student data: {student}")
    