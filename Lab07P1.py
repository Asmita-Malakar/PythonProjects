#Asmita Malakar
#6/23/2021
#Lab 7 Problem 1: Kilowatts used cost


kHW = 0

def main():
    kWH = int(input("Enter kilowatt hours used: "))
    bill_calculator(kWH)


def bill_calculator(kWH):
    if int(kWH) <= 500:
        print(f"Please pay this amount:{round(kWH * 0.12,2)}")
    else:
        print(f"Please pay this amount: {round(((kWH-500) * 0.15) + 60, 2)}")

main()

