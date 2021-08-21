#Asmita Malakar
#6/23/2021
#Lab 7 Problem 3: Kilowatts used cost with keyword arguments



def main():
    kilowatts_used = int(input("Enter kilowatt hours used: "))
    residential_or_business = input("Enter R for residential customer, B for business customer: ").upper()
    bill_calculator(Kwh = kilowatts_used, R_or_B = residential_or_business)

def bill_calculator(Kwh, R_or_B):
    if  R_or_B == "R":
        if int(Kwh) <= 500:
            print(f"Please pay this amount:{round(Kwh * 0.12, 2)}")
        else:
            print(f"Please pay this amount: {round(((Kwh- 500) * 0.15) + 60, 2)}")
    elif  R_or_B == "B":
        if int(Kwh) <= 800:
            print(f"Please pay this amount:{round(Kwh * 0.16, 2)}")
        else:
            print(f"Please pay this amount: {round(((Kwh - 800) * 0.20) + 128, 2)}")

main()














