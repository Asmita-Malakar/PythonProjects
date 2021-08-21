#Asmita Malakar
#June 5, 2021
#Lab 4 Problem 4: Random numbers against computer


#importing random function
import random
#selecting random number for computer and human picks
number = random.randint(6, 9)
human_number = random.randint(1,10)
flag = 0

print(f"Computer's pick: {number}")

# detecting if human picks are greater than computer pick or not
for i in range(3):
    human_number = random.randint(1, 10)
    if human_number > number:
        flag = 1
    print(f"Your pick: {human_number}")


# output messages
if flag > 0:
        print("You have won the game")
else:
        print("Sorry, you have lost the game")
