# Input1
number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))
number_three = float(input("Enter third number: "))

if number_one > number_two and number_one > number_three:
    print(f"The largest number is: {number_one}")

elif number_two > number_three and number_two > number_one:
    print(f"The largest number is: {number_two}")

elif number_three > number_two and number_three > number_one:
    print(f"The largest number is: {number_three}")

else:
    # Individual comparisons
    if number_two == number_three and number_two > number_one:
        print(f"The largest number is: {number_three}")
    elif number_one == number_two and number_one > number_three:
        print(f"The largest number is: {number_one}")
    elif number_one == number_three and number_one > number_two:
        print(f"The largest number is: {number_one}")
    elif number_two == number_three and number_two < number_one:
        print(f"The largest number is: {number_one}")
    elif number_one == number_two and number_one < number_three:
        print(f"The largest number is: {number_three}")
    elif number_one == number_three and number_one > number_two:
        print(f"The largest number is: {number_one}")
    else:
        print(f"The largest number is: {number_one}")