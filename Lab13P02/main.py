from Electricity_bill import Electricity_bill
from Water_bill import Water_bill

def main():
    name = input('Enter name: ')
    address = input("Enter address: ")
    bill = int(input("Enter 1 for water bill, 2 for electricity bill: "))
    if bill == 1:
        func = Water_bill(name, address)
        func.calculate_charge()
        print(func.display_bill())
    elif bill == 2:
        func = Electricity_bill(name, address)
        func.calculate_charge()
        print(func.display_bill())







main()