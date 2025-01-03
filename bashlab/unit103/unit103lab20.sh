#!/bin/bash
# Write a script that counts the number of the lines in a file.
# Hint need to use the wc command

# Prompt user for filename
echo "Enter the filename:"
read filename

# Check if file exists
if [ -f "$filename" ]; then
    # Count lines using wc -l and store in variable
    line_count=$(wc -l < "$filename")
    echo "Number of lines in $filename: $line_count"
else
    echo "Error: File '$filename' does not exist."
fi
