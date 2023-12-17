def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if max_num < number:
            max_num = number
    return max_num
