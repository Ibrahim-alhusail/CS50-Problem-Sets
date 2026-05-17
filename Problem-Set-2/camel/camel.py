'''
camelCase

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words,
whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase.
For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName,
and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase.
For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
'''

case = input("camelCase: ")
snake_case = ''

#I was overthinking it lol
#for letter in name:
#    if letter == letter.lower():
#        print(letter)
#        letters_lst.append(letter)
#    else:
#        print(f"Upper: {letter}")
#        lower_letter = letter.lower()
#        letters_lst.append(f"_{lower_letter}")
#
#snake_case = ''
#for l in letters_lst:
#    snake_case += l
#print(snake_case)

for l in case:
    if l.isupper():
        snake_case+="_"
        snake_case+=l.lower()
    else:
        snake_case+=l
print(snake_case)
