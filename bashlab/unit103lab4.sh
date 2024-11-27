#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables


function calcul() {
    num1=5
    num2=4
    subt=$(( num1 - num2 ))
    echo echo "result of subtraction : $subt"

    mult=$(( num1 * num2 ))
    echo echo "result of multipliaction: $mult"

    div=$(( num1 / num2 ))
    echo echo "result of division: $div"
}

calcul


# echo "Enter the first number:"
# read number1
# echo "Enter the second number:"
# read number2

# function subtraction() {
#     result=$(( number1 - number2 ))
#     echo "result of subtraction : $result"
# }

# function multipliaction() {
#     result=$(( number1 * number2 ))
#     echo "result of multipliaction: $result"
# }

# function division() {
#     result=$(( number1 / number2 ))
#     echo "result of division: $result"
# }

# subtraction
# multipliaction
# division