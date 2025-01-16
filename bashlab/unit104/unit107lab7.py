# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random
import re

def play_game():
    secret_number = random.randint(1, 20)
    tries = 0
    
    while True:
        number_str = input("Enter your guess (1-20): ")
        while not re.match(r'^\d+$', number_str):
            print("Please enter a valid number!")
            number_str = input("Enter your guess (1-20): ")
            
        guess = int(number_str)
        
        if guess < 1 or guess > 20:
            print("Number must be between 1 and 20!")
            continue
            
        tries += 1
        
        if guess == secret_number:
            print(f"Yes! You guessed it in {tries} guesses.")
            return True
        elif guess < secret_number:
            print("HIGHER!")
        else:
            print("LOWER!")

# Main game loop with 3 turns
turns_remaining = 3
while turns_remaining > 0:
    print(f"\nYou have {turns_remaining} turns remaining!")
    if play_game():
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    turns_remaining -= 1

if turns_remaining == 0:
    print("\nGame Over! You've used all your turns!")
