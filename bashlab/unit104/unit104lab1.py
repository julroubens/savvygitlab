# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.

'''
Name: Rougens Jules
Favorite Food: Diri ak lalo "Rice and llegume"
Dream Job: Software Engineer and IT Support
'''

# assign 5 different data types to 5 different variables. At least one datatype must be a string.

my_string = "Hello World"
my_integer = 42 
my_float = 3.14
my_boolean = True
my_list = [1, 2, 3]

# print the length of your string.

print(len(my_string))

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"

savvy = "Learning Python is Awesome!"
print(savvy)
# Replace "Awesome" with "great" in the string

savvy = savvy.replace("Awesome", "great")
print(savvy)

# Create and assign 3 more variables called name, age and length using the multi-variable naming method.

name, age, length = "Jules", 32, "6 feet"

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."

miniBio = "Hi my name is {}, I am {} and {} old today.".format(name, length, age)
print(miniBio)