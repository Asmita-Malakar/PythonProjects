# Asmita Malakar
# 07/07/2021
# Lab 11 Problem 1: Set properties


import random

set1 = set()
for i in range(5):
    set1.add(random.randint(1,10))

set2 = set()
for i in range(5):
    set2.add(random.randint(1,10))

set3 = set1 | set2
set4 = set()
for i in set3:
    if i % 2 != 0:
        set4.add(i)


print(f"set1: {set1}")
print(f"set1: {set2}")
print(f"Union of set1 and set2:{set3}" )
print(f"Union of set1 and set2:{set4}" )
print("Intersection of set1 and set2:", set1 & set2)
print("Symmetric difference of set1 and set2: ", set1^set2)