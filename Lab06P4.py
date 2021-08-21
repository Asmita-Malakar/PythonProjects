# Asmita Malakar
# #June 12, 2021
#Lab 6 Problem 4: List comprehension


list1 = [2, 5, 7, 8]
list2 = [1, 2]

new_number = [(number*2) + 1 for number in list1]
print(f"Part a: {new_number}")

second_new_number = [number + 1 for number in list1]
second_result = [second_new_number[0], second_new_number[-1]]
print(f"Part b:{second_result}")

third_result = [[x,x+1] for x in list1]
print(f"Part c: {third_result}")

fourth_result = [[x,y] for x in list1 for y in list2]
print(f"Part d: {fourth_result}")

fifth_result = [[x+y for y in list2] for x in list1]
print(f"Part e: {fifth_result}")