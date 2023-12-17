weight = input("Weight : ")
unit = input("(L)bs or K(g): ")
kg_to_lbs = int(float(weight) * 2.20462262185)
lbs_to_kg = int(float(weight) * 453.59237 / 1000)

if unit.lower() == "k":
    print("Your weight is ", kg_to_lbs, " lbs" )

elif unit.lower() == "l":
    print ("Your Weight is ", lbs_to_kg, "Kilograms")
else:
    print("Invalid Input! Please enter 'L' for Pounds or 'K' for Kilograms.")


