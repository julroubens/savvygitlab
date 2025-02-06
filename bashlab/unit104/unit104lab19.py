# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# # Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")

# Use if else statment from here to take you on a journey and have fun with it

while True:
    response = ""
    while response not in directions:
        response = input("Which direction would you like to go? (left/right/forward/backward)\n")
        if response == "left":
            print("You walk left and find a river. You can't cross it.\n")
        elif response == "right":
            print("You walk right and encounter a sleeping dragon. You quietly sneak away.\n")
        elif response == "forward":
            print("You walk forward and find a treasure chest! You open it and find gold!\n")
        elif response == "backward":
            print("You walk backward and find yourself back at the edge of the forest.\n")
        else:
            print("I didn't understand that.\n")
    
    response = ""
    while response not in yes_no:
        response = input("Would you like to continue your adventure? (yes/no)\n")
        if response == "yes":
            print("You continue your adventure.\n")
        elif response == "no":
            print("You decide to end your adventure. Goodbye, " + name + ".")
            quit()
        else:
            print("I didn't understand that.\n")
