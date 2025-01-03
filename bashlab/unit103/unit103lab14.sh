#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 
# This script helps automate daily network connectivity checks and IP management

#resource used CHATGPT and Gemini

# Function to ping devices in the local network
ping_network() {
    echo "Pinging devices in local network (192.168.1.0/24)..."
    for ip in 192.168.1.{1..254}; do
        ping -c 1 -W 1 $ip >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo " Device at $ip is UP"
        fi
    done
}

# Function to reset network interface
reset_network() {
    echo "Resetting network interface..."
    sudo ifconfig eth0 down
    sleep 2
    sudo ifconfig eth0 up
    echo "Network interface reset complete"
}

# Main menu
while true; do
    echo -e "\nNetwork Management Tool"
    echo "1. Ping devices in network"
    echo "2. Reset network interface"
    echo "3. Exit"
    read -p "Select an option (1-3): " choice

    case $choice in
        1)
            ping_network
            ;;
        2)
            reset_network
            ;;
        3)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done
