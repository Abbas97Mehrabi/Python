customer = {
    "name": "Abbas Mehrabi",
    "age": 26,
    "is_verified": True
}
customer["name"] = "Mohammadt talha Mehrabi"
customer["birthdate"] = "Sep 17 1997"
print(customer["name"])
print(customer["birthdate"])

# exercise
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
    }
output = ""
phone = input("Phone: ")
for item in phone:
    output += digit_mapping.get(item, "!") + " "

print(output)