#Asmita Malakar
#June 8, 2021
#Lab 5 Problem 1: Lists Operations


num_list = []
first_input = int(input("Enter an integer from 1 to 10: "))
num_list.append(first_input)

another_input = str(input("Enter another integer?[y/n]"))
while another_input == "y":
    following_inputs = int(input("Enter an integer from 1 to 10: "))
    num_list.append(following_inputs)
    another_input = str(input("Enter another integer?[y/n]"))

largest_element = max(num_list)
smallest_element = min(num_list)
list_length = len(num_list)
sum_list = sum(num_list)
average_list = sum_list/list_length

# Operations with num_list
print(f"Number list: {num_list}")
print(f"Largest element: {largest_element}")
print(f"Smallest element: {smallest_element}")
print(f"Sum of all elements: {sum_list}")
print(f"Length of list: {list_length}")
print(f"Average: {average_list}")

# reverse list
num_list.reverse()
print(f"List reversed: {num_list}")
last_to_first = num_list[-1]
last_to_first_in_list = num_list.insert(0, last_to_first)
del num_list[-1]
print(f"Last element moved to front: {num_list}")