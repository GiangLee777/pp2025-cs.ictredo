# 1.student.mark.py

def input_students():
    num_students = int(input("Enter number of std in the class: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter std ID: ")
        student_name = input("Enter std name: ")
        dob = input("Enter std's Date of Birth (DD/MM/YYYY): ")
        students.append((student_id, student_name, dob))
    return students

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(students, courses):
    marks = {}
    for course in courses:
        course_id, course_name = course
        marks[course_id] = {}
        for student in students:
            student_id, student_name, _ = student
            mark = float(input(f"Enter mark for {student_name} in {course_name}: "))
            marks[course_id][student_id] = mark
    return marks

def list_courses(courses):
    print("\nCourses List:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("\nStudents List:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks(marks, students, courses):
    student_id = input("Enter std ID to view marks: ")
    found = False
    for course in courses:
        course_id, course_name = course
        if student_id in marks[course_id]:
            print(f"{course_name}: {marks[course_id][student_id]} marks")
            found = True
    if not found:
        print("No marks found for this std.")

def show_course_marks(marks, courses):
    course_id = input("Enter course ID to view marks: ")
    if course_id in marks:
        print(f"\nMarks for Course ID {course_id}:")
        for student_id, mark in marks[course_id].items():
            print(f"std ID: {student_id}, Mark: {mark}")
    else:
        print("Invalid course ID.")

def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("1. Input std information")
        print("2. Input course information")
        print("3. Input marks for stds")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show std marks for a given course")
        print("7. Show marks for a given std")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            students = input_students()
        elif choice == '2':
            courses = input_courses()
        elif choice == '3':
            if not students or not courses:
                print("Please input students and courses first.")
            else:
                marks = input_marks(students, courses)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_course_marks(marks, courses)
        elif choice == '7':
            show_student_marks(marks, students, courses)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
