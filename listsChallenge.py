#!/usr/bin/env python3
"""Alta3 Research | JPagan
   List Challenge"""

#imports
import random

#function
def main():

    # Lists
    wordbank= ["indentation", "spaces"]

    tlgstudents= ["Cat", "Chris", "Dao", "David", "Henwin", 
                "Herman", "Jose", "Justin", "Kris", "Mannie", 
                "Marcos", "Marshall", "Michael", "Mike", "Nikko", 
                "Phil", "Ryan", "Sachin", "Samekh", "Will"]

    # Appends the integer 4 to the wordbank list
    wordbank.append(4)
    
    # Student names
    print("Student Names:")
    print(", ".join(tlgstudents))
    print()

    # User instructions
    print("""Do one of the following:
            - Enter a number between 1 and 20
            - Type in a student's name
            - Type in the word 'random'
            """)

    # Loop through input
    condition = False
    
    while condition != True:
        # User's input
        userInput = input(": ")
        print()

        # Number case:
        if userInput.isdigit() and int(userInput) >= 1 and int(userInput) <=  20:
            name = tlgstudents[int(userInput)-1]
            condition = True

        # Name case:
        elif userInput in tlgstudents:
            name = userInput
            condition = True

        # Random case
        elif userInput == "random":
            name = random.choice(tlgstudents)
            condition = True

        # Unauthorized input
        else:
            print("Please enter a valid input.")

    # Print statement
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
