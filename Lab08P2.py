# Asmita Malakar
# 6/27/2021
# Lab 8 Problem 2: Calculating the amount paid for certain kWH hours based on residential or business purpose



def main():
    kwh_utilized, R_or_B = get_user_input()
    print(f"Please pay this amount: ${bill_calculator(kwh_utilized, R_or_B)}")


def get_user_input():
    kWH_used = int(input("Enter kilowatt hours used: "))
    while kWH_used < 0:
        print("kWh cannot be negative.")
        kWH_used = int(input("Enter kilowatt hours used: "))
    residential_or_business = str(input("Enter R for residential customer, B for business customer: ")).upper()
    while residential_or_business != "R" and residential_or_business != "B":
        print("Invalid customer type.")
        residential_or_business = str(input("Enter R for residential customer, B for business customer: ")).upper()
    return kWH_used, residential_or_business


def bill_calculator(kwh_utilized, R_or_B):
    if R_or_B == "R":
        if 0 < kwh_utilized <= 500:
            cost = round(kwh_utilized * 0.12, 2)
        elif kwh_utilized > 500:
            cost = round(((kwh_utilized- 500) * 0.15) + 60, 2)
    elif R_or_B == 'B':
        if 0 < kwh_utilized <= 800:
            cost = round(kwh_utilized * 0.16, 2)
        elif kwh_utilized > 800:
            cost = round(((kwh_utilized - 800) * 0.20) + 128, 2)
    return cost


main()