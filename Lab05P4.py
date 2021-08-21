#Asmita Malakar
#June 8, 2021
#Lab 5 Problem 4: Printing list with random values

# import random function for random numbers
import random
first_list = []
second_list = []

# 5 random number between 1 to 9
for i in range(5):
    first_list.append(random.randint(1,9))
print(f"First list: {first_list}")

# 5 random number between 2 to 8
for i in range(5):
    second_list.append(random.randint(2,8))
print(f"Second list: {second_list}")

# compare numbers in each list
print("Larger number in each comparion: ")
for f,s in zip(first_list, second_list):
    if f > s:
        print(f)
    else:
        print(s)
