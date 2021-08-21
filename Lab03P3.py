standard_or_express = input("Enter S for standard shipping, E for express: ")
shipping_weight = float(input("Enter weight(lbs):"))

# Standard or Express
if standard_or_express == "S":
    # Compare shipping weight to set values for standard
    if 0 < shipping_weight <= 4:
        shipping_charge = shipping_weight * 1.05
        print(f"Shipping charge: {shipping_charge}")
    elif 4 < shipping_weight <= 8:
        shipping_charge = shipping_weight * 0.95
        print(f"Shipping charge: {shipping_charge}")
    elif 8 < shipping_weight <= 15:
        shipping_charge = shipping_weight * 0.85
        print(f"Shipping charge: {shipping_charge}")
    else:
        shipping_charge = shipping_weight * 0.80
        print(f"Shipping charge: {shipping_charge}")
elif standard_or_express == "E":
    # Compare shipping weight to set values for express
    if 0 < shipping_weight <= 2:
        shipping_charge = shipping_weight * 3.25
        print(f"Shipping charge: {shipping_charge}")
    elif 2 < shipping_weight <= 5:
        shipping_charge = shipping_weight * 2.95
        print(f"Shipping charge: {shipping_charge}")
    elif 5 < shipping_weight <= 10:
        shipping_charge = shipping_weight * 2.75
        print(f"Shipping charge: {shipping_charge}")
    else:
        shipping_charge = shipping_weight * 2.55
        print(f"Shipping charge: {shipping_charge}")

