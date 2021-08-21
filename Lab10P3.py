# Asmita Malakar
# 07/04/2021
# Lab 10 Problem 3: Writing text file


def main():
    water = open("water.txt", "w+")
    for i in range(4):
        water.write(input("Enter account number: "))
        water.write(" ")

        water.write(input("Enter R for residential, B for business: "))
        water.write(" ")

        water.write(input("Enter number of gallons used: "))
        water.write('\n')
    water.close()


main()
