"""-- PASSWORD GENERATOR -- 
A program that creates a random password according to the length the user enters.
- It uses the string module to get the characters and the random module to randomize them.

Author: Pedro-r-f
Date: 11/30/2025"""


import string
import random

def password_generator(size, upper_case=True, numbers=True, symbols=True ):
    characters = string.ascii_lowercase

    if upper_case:
        characters += string.ascii_uppercase
    
    if numbers:
        characters += string.digits
    
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(size))
    return password

size = int(input('How long do your want your password to be? '))
password = password_generator(size)
print(f'Your password is: {password}')

