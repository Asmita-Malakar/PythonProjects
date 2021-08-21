#Asmita Malakar
#7/11/2021
#Course Management Project


class Course:
    def __init__(self, course_code, max_size):
        self.course_name = course_code
        self.size = int(max_size)
        self.enrollment = 0.0

    def add_student(self):
        if self.enrollment >= self.size:
            print("Course already full.")
        else:
            self.enrollment = self.enrollment + 1
            print("One student added.")

    def drop_student(self):

        if self.enrollment <= 0:
            print("Course is empty.")

        else:
            self.enrollment = self.enrollment - 1
            print("One student dropped.")
