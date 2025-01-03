#!/bin/Bash

# Today's challenges is to create a script in bash that naviagetes to the document directory and list the files in there
# Then ask the user to create or edit a file and opens the file up in the terminal

# Navigate to Documents directory
cd ~

# List files in Documents directory
echo "Files in Documents directory:"
ls

# Ask user if they want to create or edit a file
# c or C for create new, e or E for editing
read -p "Would you like to (c)reate a new file or (e)dit an existing file? " choice

case $choice in
    [cC])
        # Create new file
        read -p "Enter name for new file: " filename
        touch "$filename"
        nano "$filename"
        ;;
    [eE])
        # Edit existing file
        read -p "Enter name of file to edit: " filename
        if [ -f "$filename" ]; then
            nano "$filename"
        else
            echo "File does not exist"
            exit 1
        fi
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
