# Setting Variables
hour = int(input("Enter hour:"))
minute = int(input("Enter minute:"))
second = int(input("Enter second:"))
am_pm = input("Enter AM or PM:")
# Different values based on different time periods and hour
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

else:
    print("Your values aren't applicable")
