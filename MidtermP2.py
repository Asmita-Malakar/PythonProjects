# Midterm Problem 2 - validating password based on length and letter cases
# Asmita Malakar

password = (input("Enter username: "))
for letter in password:
    if letter.isupper():
        print("Invalid Username. Uppercase character found")
        break
    elif len(password) <= 6:
        print("Invalid Username. The length should be greater than 6 characters")
        break
    else:
        print("Valid Username")
        break