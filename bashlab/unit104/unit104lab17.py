# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

# Get the total bill amount
bill = float(input("What was the total bill? $"))

# Get the tip percentage
tip_percent = float(input("What percentage tip would you like to give? "))

# Get number of people to split between
num_people = int(input("How many people to split the bill? "))

# Calculate tip amount and total with tip
tip_multiplier = 1 + (tip_percent / 100)
total_with_tip = bill * tip_multiplier

# Calculate amount per person and round to 2 decimal places
amount_per_person = total_with_tip / num_people
final_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${final_amount}")
