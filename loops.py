#while
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")
#for loop
for index in range(5,10):
    print(index)

#exercise
prices = [10, 20, 30, 40]
total_price = 0
for price in prices:
    total_price += price
print("Total Price :", total_price)

# nested loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# exercise
nums = [5, 2, 5, 2, 2]
for x_range in nums:
    output = ''
    for y in range(x_range):
        output += 'x'
    print(output)