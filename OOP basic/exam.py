class Students:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is not currently enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped.")

    def view_student_info(self):
        status = "True" if self.__is_enrolled else "False"
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {status}")

    def get_student_id(self):
        return self.__student_id


class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def view_all_students(self):
        if not self.student_list:
            print("No students found.")
        else:
            for student in self.student_list:
                student.view_student_info()

    def find_student_by_id(self, student_id):
        for student in self.student_list:
            if student.get_student_id() == student_id:
                return student
        return None
database = StudentDatabase()
database.add_student(Students("S101", "Sakir Mohammad Safayet", "CSE", True))
database.add_student(Students("S102", "Riyad", "BBA", False))
database.add_student(Students("S103", "Jhonson", "EEE", True))
def show_menu():
    print("\nStudent Management Menu")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        database.view_all_students()

    elif choice == "2":
        sid = input("Enter Student ID to enroll: ")
        student = database.find_student_by_id(sid)
        if student:
            student.enroll_student()
        else:
            print("Invalid student ID")

    elif choice == "3":
        sid = input("Enter Student ID to drop: ")
        student = database.find_student_by_id(sid)
        if student:
            student.drop_student()
        else:
            print("Invalid student ID")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid input. Please enter a number from 1 to 4.")
