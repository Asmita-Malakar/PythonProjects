#Asmita Malakar and Sarah Tolman
# 07/18/201
# Course Registration System - Logging in and selecting options



from student import add_course
# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------
from student import add_course
from student import list_courses
from student import drop_course
from billing import calculate_bill

def main():

    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------
    in_state_list = ['1001', '1003']
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    id_list = []
    for i in student_list:
        id_list.append(i[0])
    course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    roster_list = [['1004', '1003'], ['1001'], ['1002'], []]
    max_size_list = [3, 2, 1, 3]
    course_hours = [3, 4, 5, 3]
    id = str(input("Enter ID to log in, or 0 to quit: "))
    while id != str(0):
        while login(id, student_list) not in student_list:
            print("ID or PIN incorrect")
            id = str(input("Enter ID to log in, or 0 to quit: "))
        else:
            print("ID and PIN verified")

        option = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
        while option != 0:
            if option == 1:
                add_course(id, course_list, roster_list, max_size_list)
            if option == 2:
                drop_course(id, course_list, roster_list)
            if option == 3:
                list_courses(id, course_list, roster_list)
            if option == 4:
                calculate_bill(id, in_state_list, roster_list,course_hours)
            option = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
        else:
            print("Session ended.")
            id = str(input("Enter ID to log in, or 0 to quit: "))

    else:
        exit()

def login(id, s_list):
    pin = str(input("Enter PIN: "))
    return (id, pin)




    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------



main()
