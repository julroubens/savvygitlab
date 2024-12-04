#!/bin/bash

# Lets create a script that would work like a DDOS attack by using a while loop 
# In this script we want to contiune to ping our personal pc in a infitine while loop
# Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash
# To End the loop try pressing control z or control c

#use localhost for target ip for ethical reasons
target_ip="127.0.0.1"

echo "Starting infinite DDOS attack simulation with while loop..."
echo "Press Ctrl+C or Ctrl+Z to stop"
while true
do
    ping "$target_ip"
done

# Stretch Goal:
# Can you do this with an until loop to have it execute a specfic number of times?  

echo -e "\nNow demonstrating fixed-count attack with until loop..."
read -p "Enter number of ping attempts: " count

attempts=0
until [ $attempts -eq $count ]
do
    ping -c 1 "$target_ip"
    ((attempts++))
    echo "Completed attempt $attempts of $count"
done
echo "Fixed-count attack completed"







