# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

import random
import re  # Add this at the top with other imports

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if re.match(r'^[0-9]+$', user_input):
            return int(user_input)
        print("Please enter a valid positive number.")

print("Welcome to the PyPassword Generator!")
nr_letters = get_valid_number("How many letters would you like in your password?\n")
nr_symbols = get_valid_number("How many symbols would you like?\n")
nr_numbers = get_valid_number("How many numbers would you like?\n")
# What is line 15 doing?
password = []
# Below is the guide how to write the for loop you need to write for symbols and numbers
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
password_str = ''.join(password)
print(f"Your password is: {password_str}")
