#Asmita Malakar
#06/30/2021
#Lab 9 Problem 2: Comparing two lists


import random

list1 = []

for i in range(4):
    num = random.randint(1, 10)
    list1.append(num)

list2 = []

print("You are asked to pick 4 unique numbers in the range of 1 to 10.")
for i in range(4):
    number_input = int(input("Enter a number: "))
    while number_input < 1 or number_input > 10:
        print("Must be in the range of 1 to 10")
        number_input = int(input("Enter a number: "))
    while number_input in list2:
        print("This number has already been picked")
        number_input = int(input("Enter a number: "))
        while number_input < 1 or number_input > 10:
            print("Must be in the range of 1 to 10")
            number_input = int(input("Enter a number: "))
    else:
        list2.append(number_input)

list3 = []
for x in list1:
    for y in list2:
        if x == y:
            list3.append(x)


list1.sort()
list2.sort()

print(f"Numbers picked:  {sorted(list2)}")
print(f"Balls drawn: : {sorted(list1)}")
print(f"Number of matches: {len(list3)}")