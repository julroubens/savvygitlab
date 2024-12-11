#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

read -p "How is your day going? (good/bad): " day

case $day in
  "good"|"Good"|"GOOD")
    echo "That's wonderful! Keep having a great day!"
    ;;
  "bad"|"Bad"|"BAD") 
    echo "I'm sorry to hear that. I hope your day gets better!"
    ;;
  *)
    echo "I'm not sure what you mean by that response."
    ;;
esac
