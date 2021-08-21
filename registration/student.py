# Asmita Malakar and Sarah Tolman
# 07/18/201
# Course Registration System - Adding, dropping and displaying courses


#Function to display all courses with count of number of courses registered
def list_courses(id, c_list, r_list):
    count = 0
    print("Courses registered: ")
    #Displaying all courses in roster list with id
    for i in r_list:
        if id in i:
            index = r_list.index(i)
            count = count + 1
            print(f"{c_list[index]}")
    print(f"Total number: {count}")


def add_course(id, c_list, r_list, m_list):
    class_name = str(input("Enter course you want to add: "))
    if class_name not in c_list:
        #course not in list
        print("Course not found")
    elif class_name in c_list:
        index = c_list.index(class_name)
        # Full course
        if len(r_list[index]) == m_list[index]:
            print("This course is full")
        else:
            if id in r_list[index]:
                print("You are already enrolled in that course.")
            elif id not in r_list[index]:
                # r_list[index] = list(r_list[index])
                r_list[index].append(id)
                print("Course added")


def drop_course(id, c_list, r_list):
    class_name = str(input("Enter course you want to drop: "))
    if class_name not in c_list:
        #course not found in list
        print("Course not found")
    else:
        index = c_list.index(class_name)
        if id not in r_list[index]:
            print("You are not enrolled in the course")
        #dropping course
        elif id in r_list[index]:
            r_list[index].remove(id)
            print("Course dropped")
