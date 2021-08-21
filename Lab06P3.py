# Asmita Malakar
# #June 12, 2021
#Lab 6 Problem 3: Tuple Functions


import random
random_integer = []

for i in range(1, 11):
    random_value = random.randint(1, 15)
    random_integer.append(random_value)

tuple_final = tuple(random_integer)
tuple_slice_1 = tuple_final[0:3]
tuple_slice_2 = tuple_final[-3:]
tuple_concatenated = tuple_slice_1 + tuple_slice_2

print(f"Tuple of 10 random numbers: {tuple_final}")
print(f"Tuple of first 3 numbers: {tuple_slice_1}")
print(f"Tuple of last 3 numbers: {tuple_slice_2}")
print(f"Two tuples concatenated: {tuple_concatenated}")
sort = sorted(tuple_concatenated)
print(f"Two tuples concatenated and sorted: {sort}")