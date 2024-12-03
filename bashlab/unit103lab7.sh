#!/bin/bash
# Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

# Create a new bash script that performs the following:

# Prompts user for input directory path or file.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777, 775, 664)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory or file you selected.
ls -l

read -p "Enter the directory path or file: " input
read -p "Enter the permissions number (e.g. 777, 775, 664): " permissions

# Navigate to the directory
cd "$input"

# Change permissions of all files in the directory
chmod -R "$permissions" .

ls -l
