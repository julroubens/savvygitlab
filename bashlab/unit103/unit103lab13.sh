#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
 
#Main
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply) 
read -p "Please enter a number: " num

    if [ $num -ge 2 ] && [ $num -le 5 ]; then
        echo "Valid Number"
        echo "your number is $num"
    else
        echo "wrong number!"
        $test=false
    fi
    
    cd ~/Documents
    echo "Files in Documents directory:"
    ls

    read -p "Would you like to create a new file or edit an existing one? (create/edit): " choice

    case $choice in
        "create"|"Create"|"CREATE")
            read -p "Enter the name for your new file: " filename
            nano "$filename"
            ;;
        "edit"|"Edit"|"EDIT")
            read -p "Enter the name of the file to edit: " filename
            if [ -f "$filename" ]; then
                nano "$filename"
            else
                echo "File does not exist!"
            fi
            ;;
        *)
            echo "Invalid choice!"
            ;;
    esac


