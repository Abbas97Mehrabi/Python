names = ['abbas', 'kadir', 'mahmut', 'ali']
names[0] = 'Abbas'
print(names[:3])


# 2 dimensional list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2 , 1, 7, 4, 7]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(1)
#numbers.clear()
numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers.index(7))
print(numbers.count(7))
numbers2 = numbers.copy()
numbers.append(15)
print(numbers2)

# exercise remove duplicate items from list
numbers = [5, 3, 4, 1, 5, 2 , 1, 7, 4, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# tuple
number = (1, 2, 3)
print(number)

# unpacking

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)
print(y)
print(z)