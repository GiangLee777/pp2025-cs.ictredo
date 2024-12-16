# 2.student.mark.py

class Student:
    def __init__(self, student_id, student_name, dob):
        self.student_id = student_id
        self.student_name = student_name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, Date of Birth: {self.dob}"

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}"

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"{self.course.course_name}: {self.mark} marks for {self.student.student_name}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        num_students = int(input("Enter number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            dob = input("Enter student's Date of Birth (DD/MM/YYYY): ")
            student = Student(student_id, student_name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        for course in self.courses:
            for student in self.students:
                mark = float(input(f"Enter mark for {student.student_name} in {course.course_name}: "))
                mark_record = Mark(student, course, mark)
                self.marks.append(mark_record)

    def list_courses(self):
        print("\nCourses List:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("\nStudents List:")
        for student in self.students:
            print(student)

    def show_student_marks(self):
        student_id = input("Enter student ID to view marks: ")
        found = False
        for mark in self.marks:
            if mark.student.student_id == student_id:
                print(mark)
                found = True
        if not found:
            print("No marks found for this student.")

    def show_course_marks(self):
        course_id = input("Enter course ID to view marks: ")
        found = False
        for mark in self.marks:
            if mark.course.course_id == course_id:
                print(mark)
                found = True
        if not found:
            print("Invalid course ID.")

    def main(self):
        while True:
            print("\n1. Input student information")
            print("2. Input course information")
            print("3. Input marks for students")
            print("4. List all courses")
            print("5. List all students")
            print("6. Show student marks for a given course")
            print("7. Show marks for a given student")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                if not self.students or not self.courses:
                    print("Please input students and courses first.")
                else:
                    self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_course_marks()
            elif choice == '7':
                self.show_student_marks()
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    school = School()
    school.main()
