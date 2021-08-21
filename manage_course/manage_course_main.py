#Asmita Malakar
#7/11/2021
#Course Management Project


from course import Course

def main():
    name = input("Enter course code: ")
    max_size = input("Enter maximum class size: ")
    courses = Course(name, max_size)
    option = 4
    while option != 0:
        option = int(input("Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: "))
        if option == 1:
            courses.add_student()
            if courses.enrollment > int(max_size):
                print("Course already full.")
                print(f"Enrollment: {max_size}")
            else:
                print(f"Enrollment: {courses.enrollment}")
        elif option == 2:
            courses.drop_student()
            print(courses.enrollment)
        elif option == 3:
            print(f"Course code: {name}")
            print(f"Maximum class size: {max_size}")
            print(f"Enrollment: {courses.enrollment}")





main()

