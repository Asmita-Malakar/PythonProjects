from Dinner_Combo import Dinner_combo
from deluxe_Dinner_Combo import Deluxe_dinner_combo


def main():
    dinner = input('Enter Number Here:')
    if dinner == '1':
        type = Dinner_combo()
    elif dinner == '2':
        type = Deluxe_dinner_combo()
    print(type.displayOrder())

main()