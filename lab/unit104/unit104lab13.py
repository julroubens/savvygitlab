# Create a program that calculates remaining time until 90 years old
# based on birth date

import re
from datetime import datetime

# 🚨 Don't change the code below 👇
while True:
    birth_date = input("Enter your birth date (MM/DD/YYYY): ")
    try:
        birth_date = datetime.strptime(birth_date, '%m/%d/%Y')
        today = datetime.now()
        if birth_date > today:
            print("Birth date cannot be in the future!")
            continue
        age = (today - birth_date).days / 365.25  # Using 365.25 to account for leap years
        if age > 150:
            print("Please enter a valid birth date (age cannot exceed 150)")
            continue
        break
    except ValueError:
        print("Please enter a valid date in MM/DD/YYYY format")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

target_date = birth_date.replace(year=birth_date.year + 90)
time_remaining = target_date - today

days_remaining = int(time_remaining.days)
weeks_remaining = int(days_remaining / 7)
months_remaining = int(days_remaining / 30.44)  # Average days in a month

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.") 