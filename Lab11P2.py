# Asmita Malakar
# 07/07/2021
# Lab 11 Problem 1: Dictionary properties



string = str(input("Enter a string: "))
all_letters = []
stringAll = []

string = string.upper()

for i in string:
    if i.isalpha():
        stringAll.append(i)
        all_letters.append(string.count(i))

dictionary = dict(zip(stringAll, all_letters))

print(dictionary)

word = str(input("Choose a letter: ")).upper()
if word in dictionary:
    print(f"Frequency count of that letter: {string.count(word)}")
    del dictionary[word]
    print(dictionary)

dictionary_list = list(dictionary.keys())
dictionary_list.sort()
print(sorted(dictionary_list))