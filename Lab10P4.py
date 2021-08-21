# Asmita Malakar
# 07/04/2021
# Lab 10 Problem 4: Reading text document and completing operations through it


doc = open("water.txt", "r")

for line in doc:
    word = line.split()
    price = int(word[2])
    if word[1] == "R":
        if price <= 6000:
            price = price * 0.005
            print(f"Account number: {word[0]}" + "    " + f"Water charge: {price}")
        elif price > 6000:
            price = 30 + ((price - 6000) * 0.007)
            print(f"Account number: {word[0]}" + "    " + f"Water charge: {price}")
    if word[1] == "B":
        if price <= 8000:
            price = price * 0.006
            print(f"Account number: {word[0]}" + "    " + f"Water charge: {price}")
        elif price >= 8000:
            price = 48 + ((price - 8000) * 0.008)
            print(f"Account number: {word[0]}" + "    " + f"Water charge: {price}")
