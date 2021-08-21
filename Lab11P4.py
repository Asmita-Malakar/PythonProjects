# Asmita Malakar
# 07/07/2021
# Lab 11 Problem 4: Exception errors with if and else statements


total_value = 0
while True:
    try:
        hotdog = int(input("How many hotdogs? "))
        if hotdog >= 0:
            total_value = total_value + (hotdog * 2.5)
            break
        else:
            print("Invalid input.")
            continue
    except ValueError:
        print("Invalid input.")

while True:
    try:
        chips = int(input("How many chips? "))
        if chips >= 0:
            total_value = total_value + (chips * 1.5)
            break
        else:
            print("Invalid input.")
            continue
    except ValueError:
        print("Invalid input.")

while True:
    try:
        sodas = int(input("How many sodas? "))
        if sodas >= 0:
            total_value = total_value + (sodas * 1.25)
            break
        else:
            print("Invalid input.")
            continue
    except ValueError:
        print("Invalid input.")




print(f"Please pay this amount: {total_value}")


