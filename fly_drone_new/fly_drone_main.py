#Asmita Malakar
#7/11/2021
#String method in drone height and speed project

from Drone import Drone


def main():
    drone2 = Drone(speed=0, height=0)
    action = 5
    while action != 0:
        action = int(input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))
        if action == 1:
            drone2.accelerate()
            print(drone2.__str__())

        elif action == 2:
            drone2.decelerate()
            print(drone2.__str__())


        elif action == 3:
            drone2.ascend()
            print(drone2.__str__())

        elif action == 4:
            drone2.descend()
            print(drone2.__str__())

        elif action == 0:
            print(drone2.__str__())

            exit()


main()