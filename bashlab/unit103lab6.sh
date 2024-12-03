#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:


# For this challenge you must use at least one variable and one function.

function dom_info() {
    # Take a user input string. Presumably the string is a domain name such as Google.com.
    echo "Enter a domain name:"
    read domain
    # Run whois against a user input string.
    whois $domain >> domain_info.txt
    # Run dig against the user input string.
    dig $domain >> domain_info.txt
    # Run host against the user input string.
    host $domain >> domain_info.txt
    # Run nslookup against the user input string.
    nslookup $domain >> domain_info.txt
    echo "Results saved to domain_info.txt"
}

dom_info