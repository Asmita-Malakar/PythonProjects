#Asmita Malakar
#June 5, 2021
#Lab 4 Problem 1: Implementing the error loop

# hour error loop
hour = int(input("Enter hour: "))
while hour < 1 or hour > 12:
    print("Hour must be from 1 to 12.")
    hour = int(input("Enter hour: "))

# minute error loop
minute = int(input("Enter minute: "))
while minute < 0 or minute > 59:
    print("Minute must be from 0 to 59.")
    minute = int(input("Enter minute: "))

# second error loop
second = int(input("Enter second: "))
while second < 0 or second > 59:
    print("Second must be from 0 to 59.")
    second = int(input("Enter second: "))

# error loop for time periods
am_pm = str(input("Enter AM or PM:"))
while am_pm != "PM" and am_pm != "AM":
    print("Please enter AM or PM")
    am_pm = str(input("Enter AM or PM:"))

if am_pm == "AM" and hour == 12:
    # No hours passed
    hour = 0
    hour_midnight = hour * 3600
    minute_midnight = minute * 60
    seconds_since_midnight = (hour_midnight) + (minute_midnight) + (second)
    print("Seconds since midnight:", seconds_since_midnight)
elif am_pm == "AM" and 1 <= hour <= 11:
    hour_midnight = hour * 3600
    minute_midnight = minute * 60
    seconds_since_midnight = (hour_midnight) + (minute_midnight) + (second)
    print(f"Seconds since midnight {seconds_since_midnight}")
elif am_pm == "PM" and hour == 12:
    hour_midnight = hour * 3600
    minute_midnight = minute * 60
    seconds_since_midnight = (hour_midnight) + (minute_midnight) + (second)
    print(f"Seconds since midnight {seconds_since_midnight}")
elif am_pm == "PM" and 1 <= hour <= 11:
    # 12 Hours passed in A.M. Time
    hour = hour + 12
    hour_midnight = hour * 3600
    minute_midnight = minute * 60
    seconds_since_midnight = ((hour_midnight) + (minute_midnight) + second)
    print(f"Seconds since midnight {seconds_since_midnight}")

