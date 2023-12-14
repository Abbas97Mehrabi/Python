import math
print(math.ceil(2.4))

print(math.floor(2.4))
#operator precedence
#1 parenthesis
#2 exponentiation
#3 multiplication and division (from left to right)
#4 addition and subtraction (from left to right)
x = (10 + 3) * 2 ** 2
print(x)
y = (2+3) * 10 - 3
print(y)


x = 3.9
print(round(x))


print(abs(-1.3))

#logical operators
has_high_income = False
has_good_credit = True
has_criminal_record = False
#AND: both
#OR: at least one
if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


#comparison operators

temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "mahmut"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a macimum of 50 characters")
else:
    print("Name looks good!")