number = int(input("Enter a number: "))
if number >= 0:
    if number % 2 == 0 or number == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Negative number")