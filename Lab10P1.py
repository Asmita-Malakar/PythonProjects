# Asmita Malakar
# 07/04/2021
# Lab 10 Problem 1: Counting letters in string


date = str(input("Enter time [hh:mm:ss]: "))
date_list = date.split(':')
if len(date_list) != 3:
    print("Must separate hour, minute and second with colons.")
elif len(date_list[0]) != 2:
    print("Hour must be a 2-digit number.")
elif date_list[0].isdigit() == False:
    print("Hour must be a 2-digit number.")
elif str(date_list[0]) > str(23) or str(date_list[0]) < str(0):
    print("Hour must be a 2-digit number between 0 and 23.")
elif len(date_list[1]) != 2:
    print("Minute must be a 2-digit number.")
elif date_list[1].isdigit() == False:
    print("Minute must be a 2-digit number.")
elif str(date_list[1]) > str(59) or str(date_list[1]) < str(0):
    print("Minute must be a 2-digit number between 0 and 23.")
elif len(date_list[2]) != 2:
    print("Minute must be a 2-digit number.")
elif str(date_list[2]) > str(59) or str(date_list[2]) < str(0):
    print("Second must be a 2-digit number between 0 and 23.")
else:
    date_without_colon = date.replace(":", "")
    print(f"Time without colons: {date_without_colon}")
