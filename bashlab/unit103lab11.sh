#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)    

read -p "Enter the first side of the triangle: " a
read -p "Enter the second side of the triangle: " b
read -p "Enter the third side of the triangle: " c
    
if [ $a -eq $b ] && [ $b -eq $c ]; then
    echo "EQUILATERAL"
elif [ $a -eq $b ] || [ $b -eq $c ] || [ $a -eq $c ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi