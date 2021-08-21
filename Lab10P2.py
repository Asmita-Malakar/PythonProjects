# Asmita Malakar
# 07/04/2021
# Lab 10 Problem 2: Counting letters in string

string = str(input("Enter a string: "))
all_letters = []
stringAll = []

string = string.upper()

for i in string:
    if i.isalpha():
        stringAll.append(i)
        all_letters.append(string.count(i))

dictionary = dict(zip(stringAll, all_letters))

for a, b in dictionary.items():
    print(a, b)
