# Write a program that works out whether if a given number is an 
# odd or even number
# 🚨 Don't change the code below 👇
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


import re

number_str = input("Which number do you want to check? ")
while not re.match(r'^\d+$', number_str):
    print("Please enter a valid number!")
    number_str = input("Which number do you want to check? ")

number = int(number_str)

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
