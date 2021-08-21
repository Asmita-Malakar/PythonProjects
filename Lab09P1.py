#Asmita Malakar
#06/30/2021
#Lab 9 Problem 1: Math functions

import random
import math

number = random.uniform(1.5, 4.5)
print(f"Random number generated: {number}")

floor_number = number.__floor__()
print(f"Output of floor function: {floor_number}")

ceilNumber = number.__ceil__()
print(f"Output of ceil function: {ceilNumber}")

squareNumber = math.sqrt(number)
print(f"Output of sqrt function: {squareNumber}")