residential_or_business = str(input("Enter R for residential customer or B for business customer: "))
gallons = float(input("How many gallons of water were used? "))

# Individual possiblities through and statemnets
if gallons <= 6000 and residential_or_business == "R":
    cost = 6000*0.005
    print(f"Please pay this amount: {cost}")
elif gallons > 6000 and residential_or_business == "R":
    gallons_left = gallons - 6000
    cost = 30 + (0.007 * gallons_left)
    print(f"Please pay this amount: {cost}")
elif gallons <= 8000 and residential_or_business == "B":
    cost = 8000 * 0.006
    print(f"Please pay this amount: {cost}")
elif gallons > 8000 and residential_or_business == "B":
    gallons_left = gallons - 8000
    cost = 48 + (0.008 * gallons_left)
    print(f"Please pay this amount: {cost}")
else:
    # Negative gallon values aren't valid
    print("Your values aren't valid")
