from find_max_number import find_max
price = 10
rating = 4.9
name = 'Abbas'
is_published = False
isNot_published = True
print(price)
full_name = 'John Smith'
age = 20
is_newPatient = True
if(is_newPatient):
    print("Welcome to our clinic, Mr", full_name)
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

# using module
nums = [5, 8, 3, 71, 2, 3, 4, 33, 55, 43, 99]
maximum = find_max(nums)
print(maximum)
