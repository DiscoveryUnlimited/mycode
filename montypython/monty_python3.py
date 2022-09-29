#!/usr/bin/env python3
""" Alta3 Research | JPagan
    Conditionals - Life of Brian guessing game using a while True loop."""

def main():
    
    # integer round initiated to 0
    round = 0
    answer = " "       

    # sets up an infinite loop condition
    while round < 3 and answer != "Brian":
        round += 1     # increase the round counter by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        answer = answer.capitalize()
        
        if answer == "Brian": # logic to check if user gave correct answer
            print("Correct!")
        elif answer == "Shrubbery":
            print("You gave the super secret answer!")
            break
        elif round == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")

main()