#Asmita Malakar
#06/30/2021
#Lab 9 Problem 3: Blackjack game


import random

cards = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
player = []
dealer = []


card_value = 0
dealer_card = 0
for i in range(2):
        random_choice = random.choice(cards)
        if random_choice == "A":
            card_value = card_value + 11
        elif random_choice == "J":
            card_value = card_value + 10
        elif random_choice == "Q":
            card_value = card_value + 10
        elif random_choice == "K":
            card_value = card_value + 10
        else:
            card_value = card_value + int(random_choice)
        print(f"Card drawn: {random_choice}" + "   " + f"Player's total: {card_value}")



while card_value < 21:
    input_question = str(input("Want another card? [y/n] ")).lower()
    if input_question == "y":
        random_choice = random.choice(cards)
        if random_choice == "A":
            card_value = card_value + 11
        elif random_choice == "J":
            card_value = card_value + 10
        elif random_choice == "Q":
            card_value = card_value + 10
        elif random_choice == "K":
            card_value = card_value + 10
        else:
            card_value = card_value + int(random_choice)

        print(f"Card drawn: {random_choice}" + "   " + f"Player's total: {card_value}")
    elif input_question == "n":
        while dealer_card < 17:
            random_choice = random.choice(cards)
            if random_choice == "A":
                dealer_card = dealer_card + 11
            elif random_choice == "J":
                dealer_card = dealer_card + 10
            elif random_choice == "Q":
                dealer_card = dealer_card + 10
            elif random_choice == "K":
                dealer_card = dealer_card + 10
            else:
                dealer_card = dealer_card + int(random_choice)

            print(f"Card drawn: {random_choice}" + "   " + f"Player's total: {dealer_card}")
        else:
            if dealer_card == 21:
                print("Blackjack! Dealer has won!")
                exit()
            elif dealer_card > 21:
                print("Bust! Dealer has lost!")
                exit()
            else:
                if dealer_card > card_value:
                    print("Dealer has won!")
                    exit()
                else:
                    print("You have won!")
                    exit()




else:
    if card_value == 21:
        print("Blackjack! You have won!")
    elif card_value > 21:
        print("Bust! You have lost!")
    else:
        random_choice = random.choice(cards)
        if random_choice == "A":
            dealer_card = dealer_card + 11
        elif random_choice == "J":
            dealer_card = dealer_card + 10
        elif random_choice == "Q":
            dealer_card = dealer_card + 10
        elif random_choice == "K":
            dealer_card = dealer_card + 10
        else:
            dealer_card = dealer_card + int(random_choice)













