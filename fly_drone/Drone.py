#Asmita Malakar
#7/11/2021
#Drone height and speed project


class Drone:
    def __init__(self, speed, height):
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
       self.speed = self.speed + 10

    def decelerate(self):
        self.speed = self.speed - 10

    def ascend(self):
        self.height = self.height + 10

    def descend(self):
        self.height = self.height - 10