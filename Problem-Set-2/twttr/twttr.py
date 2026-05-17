'''
Just setting up my twttr

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
'''

VOWELS = ["A","E","I","O","U"]

txt = input("Input: ")
new_txt = ""

for c in txt:
    if c.upper() not in VOWELS:
        new_txt+=c
    else:
        new_txt+=""
    
print(new_txt)