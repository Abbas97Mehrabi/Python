#format string
first_name = 'Abbas'
last_name = 'Mehrabi'
message = f'{first_name} {last_name} is a coder'
print(message)

#single, double and triple quotes
single = 'this "is" Abbas'
print(single)
double = "This 'is' Abbas"
print(double)
triple = '''
This is Abbas

and i'm writing python code

thank you.
'''
print(triple)

#string methods
sentence = 'Do I love coding?'
print(len(sentence))

upper_case = sentence.upper()
print(upper_case)

lower_case = sentence.lower()
print(lower_case)

find_character = sentence.find('l')
print(find_character)

replace = sentence.replace("Do", "Don't")
print(replace)

check_if_exists = 'love' in sentence
print(check_if_exists)

check_if_exists = 'hate' in sentence
print(check_if_exists)

#make upper case first character of word in sentence
title = sentence.title()
print(title)