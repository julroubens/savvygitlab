#!/Bin/Bash

# Challenge today is to create a script that list all the devices on the network and ask the user to ping one of the ip address.
# There is a few different ways to list all deivices on your network you could use an arp command or an nmap command.
# We will run the a command that prints all address then ask the user to ping a specific one by entering an ip address.

# Function to list devices and ping an IP
network_scan() {
    echo "Scanning network for devices..."
    
    # Check if nmap is installed
    if ! command -v nmap &> /dev/null; then
        echo "nmap is not installed. Please install it first or use arp -a instead."
        return 1
    fi
    
    # Use nmap to scan the local network (requires sudo)
    # Adjust the network range according to your network (e.g., 192.168.1.0/24)
    sudo nmap -sn 192.168.1.0/24
    
    # Rest of the function remains the same...
    read -p "Enter an IP address from the list above to ping: " ip_address
    
    if [[ $ip_address =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "Pinging $ip_address..."
        ping -c 4 $ip_address
    else
        echo "Invalid IP address format"
        return 1
    fi
}


# Call the function
network_scan
