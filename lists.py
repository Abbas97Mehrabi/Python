names = ['abbas', 'kadir', 'mahmut', 'ali']
names[0] = 'Abbas'
print(names[:3])

# exercise largest number in the list
nums = [5, 45, 6, 84, 12, 99]
biggest = nums[0]
for n in nums:
    if biggest < n:
        biggest = n
print(f"The biggest number is : {biggest}")

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