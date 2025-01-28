# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

import re

# 🚨 Don't change the code below 👇
while True:
    age_input = input("What is your current age? ")
    if re.match(r'^\d+$', age_input) and 0 <= int(age_input) <= 150:
        age = int(age_input)
        break
    print("Please enter a valid age (0-150)")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_remaining = 90 - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
