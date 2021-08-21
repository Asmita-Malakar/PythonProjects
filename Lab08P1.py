# Asmita Malakar
# 6/27/2021
# Lab 8 Problem 1: Calculating the amount paid for certain kWH hours


def main():
    kWH_utilize = get_KWH_used()
    print(f"Please pay this amount: ${bill_calculator(kWH_utilize)}")


def get_KWH_used():
    kWH_used = int(input("Enter kilowatt hours used: "))
    while kWH_used < 0:
        print("kWh cannot be negative.")
        kWH_used = int(input("Enter kilowatt hours used: "))
    return kWH_used


def bill_calculator(kWH_utilize):
    if int(kWH_utilize) <= 500:
        energy_cost = round(kWH_utilize * 0.12, 2)
    else:
        energy_cost = round(((kWH_utilize - 500) * 0.15) + 60, 2)
    return energy_cost


main()
