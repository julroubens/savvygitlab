#!/bin/bash
# Create a script that ask the user for a number between 1 and 10.  Have the script tell the user if there
# number is greater than 5, less than 5, or equal to 5.  Please use an if/else or elif statement to make this happen.  
# Also put the if/else statemnt inside a function.
# -eq = equal   
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
#Here are some helpful commands to make this happen.    

# Function to check number against 5
check_number() {
    read -p "Please enter a number between 1 and 10: " num

    # Validate input is between 1 and 10
    if [[ $num -lt 1 || $num -gt 10 ]]; then
        echo "Invalid input. Please enter a number between 1 and 10."
        return
    fi

    # Compare number with 5
    if [ $num -gt 5 ]; then
        echo "Your number is greater than 5"
    elif [ $num -lt 5 ]; then
        echo "Your number is less than 5"
    else
        echo "Your number is equal to 5"
    fi
}

# Call the function
check_number
