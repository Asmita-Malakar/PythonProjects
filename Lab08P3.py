# Asmita Malakar
# 6/27/2021
# Lab 8 Problem 3: Importing currency modules and using it


import currency


def main():
    print("Converting US Dollar to a foreign currency.")
    number_input = int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
    while number_input > 3 or number_input < 0:
        print("Error: Invalid Choice")
        number_input = int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
    if number_input == 1:
        dollar_input = float(input("Enter US Dollar: "))
        if dollar_input < 0:
            print("Error: US Dollar cannot be negative.")
            dollar_input = float(input("Enter US Dollar: "))
        else:
            print(f"It is converted to: {currency.to_euro(dollar_input)} euro")

    if number_input == 2:
        dollar_input = float(input("Enter US Dollar: "))
        while dollar_input < 0:
            print("Error: US Dollar cannot be negative.")
            dollar_input = float(input("Enter US Dollar: "))
        else:
            print(f"It is converted to: {currency.to_yen(dollar_input)} yen")

    if number_input == 3:
        dollar_input = float(input("Enter US Dollar: "))
        while dollar_input < 0:
            print("Error: US Dollar cannot be negative.")
            dollar_input = float(input("Enter US Dollar: "))
        else:
            print(f"It is converted to: {currency.to_peso(dollar_input)} peso")


main()
