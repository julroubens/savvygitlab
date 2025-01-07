# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.



# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

# Hint:  a = int(input("Enter a number "))

# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Equal comparison


# Not equal comparison
if a != b:
    print(f"{a} is not equal to {b}")

# Less than comparison
if a < b:
    print(f"{a} is less than {b}")

# Less than or equal comparison
if a <= b:
    print(f"{a} is less than or equal to {b}")

# Greater than comparison
if a > b:
    print(f"{a} is greater than {b}")

# Greater than or equal comparison
if a >= b:
    print(f"{a} is greater than or equal to {b}")

# if-elif-else statement
if a > 100:
    print(f"{a} is a large number")
elif a > 50:
    print(f"{a} is a medium number")
else:
    print(f"{a} is a small number")

# Stretch Goals

# Using 'and' operator
if a > 0 and b > 0:
    print("Both numbers are positive")

# Using 'or' operator
if a < 0 or b < 0:
    print("At least one number is negative")

# Nested if statement
if a > b:
    if a % 2 == 0:
        print(f"{a} is greater than {b} and is even")
    else:
        print(f"{a} is greater than {b} and is odd")
