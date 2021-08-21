#Asmita Malakar
#6/8/2021
#Lab 5 Problem 2: Course Schedule


class_action = str(input("Enter A to add course, D to drop course, and E to exit: "))

course_list = []

# adding courses
if class_action == "A":
    course_add = str(input("Enter course to add: "))
    if course_add in course_list:
        print("You are already registered in that course")
    else:
        course_list.append(course_add)
        print("Course added")
        course_list.sort()
        print(f"Courses registered: {course_list}")


# dropping courses
elif class_action == "D":
    course_delete = str(input("Enter course to drop: "))
    if course_delete in course_list:
        course_list.remove(course_delete)
        course_list.sort()
        print(f"Courses registered: {course_list}")
    else:
        print("You are not registered in that course")

class_action = str(input("Enter A to add course, D to drop course, and E to exit: "))
while class_action != "E":
    # User unable to add a course twice
    if class_action == "A":
        course_add = str(input("Enter course to add: "))
        if course_add in course_list:
            print("You are already registered in that course")
        else:
            course_list.append(course_add)
            print("Course added")
            course_list.sort()
            print(f"Courses registered: {course_list}")

    # User unable to drop a course not in the list
    elif class_action == "D":
        course_delete = str(input("Enter course to drop: "))
        if course_delete in course_list:
            course_list.remove(course_delete)
            course_list.sort()
            print(f"Courses registered: {course_list}")
        else:
            print("You are not registered in that course")
    class_action = str(input("Enter A to add course, D to drop course, and E to exit: "))


