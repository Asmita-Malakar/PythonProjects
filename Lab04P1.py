#Asmita Malakar
#June 5, 2021
#Lab 4 Problem 1: Implementing the while function


# plasma level input
plasma_level = int(input("Enter fasting plasma glucose level: "))
if plasma_level > 125:
    print("The patient has diabetes")
# detecting whether patient has diabetes
elif 100 < plasma_level <= 125:
    print("The patient has pre-diabetes.")
else:
    print("The patient has a healthy FPG level")

another_patient = str(input("Checking diabetes for another patient? [y/n] "))

#while loop for more patients
while another_patient == "y":
    plasma_level = int(input("Enter fasting plasma glucose level: "))
    if plasma_level > 125:
        print("The patient has diabetes")
    elif 100 < plasma_level <= 125:
        print("The patient has pre-diabetes.")
    else:
        print("The patient has a healthy FPG level")
    another_patient = str(input("Checking diabetes for another patient? [y/n] "))



