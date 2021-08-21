#Asmita Malakar
#7/11/2021
#String method in drone height and speed project



class Drone:
    def __init__(self, speed, height):
        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):
       self.__speed = self.__speed + 10

    def decelerate(self):
        self.__speed = self.__speed - 10

    def ascend(self):
        self.__height = self.__height + 10

    def descend(self):
        self.__height = self.__height - 10

   # def get_height(self):
        #return (self.__height)

    #def get_speed(self):
      #  return (self.__speed)

    def __str__(self):
        return 'Speed:' + ' ' + str(self.__speed) + '  '+ 'Height:' +  '  '+  str(self.__height)


