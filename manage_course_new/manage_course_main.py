#Asmita Malakar
#7/11/2021
#Setter method and private variable


from course import Course

def main():
    name = input("Enter course code: ")
    max_size = input("Enter maximum class size: ")
    courses = Course(name, max_size, enrollment=0)
    option = 4
    while option != 0:
        option = int(input("Enter 1 for add student, 2 for drop student, 3 for course info, "
                           "4 for change maximum class size, 0 for exit: "))
        if option == 1:
            courses.get_class_size()
            courses.get_class_enrollment()
            courses.add_student()
            if courses.get_class_enrollment() > int(max_size):
                print("Course already full.")
                print(f"Enrollment: {max_size}")
            else:
                print(f"Enrollment: {courses.get_class_enrollment()}")
        elif option == 2:
            courses.drop_student()
            print(f"Enrollment: {courses.get_class_enrollment()}")
        elif option == 3:
            print(f"Course code: {name}")
            print(f"Maximum class size: {max_size}")
            print(f"Enrollment: {courses.get_class_enrollment()}")
        elif option == 4:
            size_new = int(input("Enter new maximum class size: "))
            courses.set_newSize(size_new)





main()

