#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

istrue=true
while $istrue; do
    echo "1. Hello World"
    echo "2. Ping a website or IP address"
    echo "3. Run ifconfig"
    read -p "Enter your choice (1, 2, 3): " choice
    if [ $choice -eq 1 ]; then
        #just echo hello world
        echo "Hello World"
    elif [ $choice -eq 2 ]; then
        read -p "Enter the website or IP address to ping: " website
        ping -c 4 $website
    elif [ $choice -eq 3 ]; then
        echo "Running ifconfig and saving to ifconfig.txt"
        ifconfig>>ifconfig.txt
    else
        echo "Invalid entry"
        istrue=false
    fi
done