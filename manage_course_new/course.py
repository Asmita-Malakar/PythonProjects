#Asmita Malakar
#7/11/2021
#Setter method and private variable


class Course:
    def __init__(self, course_code, max_size, enrollment):
        self.__course_name = course_code
        self.__size = int(max_size)
        self.__enrollment = enrollment


    def add_student(self):
        if self.__enrollment >= self.__size:
            print("Course already full.")
        else:
            self.__enrollment = self.__enrollment + 1
            print("One student added.")

    def drop_student(self):
            if self.__enrollment <= 0:
                print("Course is empty.")

            else:
                self.__enrollment = self.__enrollment - 1
                print("One student dropped.")


    def get_class_size(self):
        return self.__size
    def get_class_enrollment(self):
        return self.__enrollment

    def set_newSize(self, newSize):
        self.newClassSize = int(newSize)
        if self.newClassSize < 0:
            print("maximum class size cannot be negative")
        elif self.newClassSize < self.__enrollment:
            print("maximum class size cannot be lower than current enrollment")
        else:
            self.__size = self.newClassSize
