# Asmita Malakar
# 07/07/2021
# Lab 11 Problem 3: ValueError exception


list = []

for i in range(5):
    integer = input("Enter an integer: ")
    try:
        list.append(int(integer))
        continue
    except ValueError:
        print("Input value cannot be converted to integer")

print(list)
