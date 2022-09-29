#!/usr/bin/env python3
""" Alta3 Research | JPagan
    Conditionals - Life of Brian guessing game using a while True loop."""

def main():
    
    # integer round initiated to 0
    round = 0           

    # sets up an infinite loop condition
    while True:        
        round = round + 1       # increase the round counter
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")    # string ans collected from user
        if answer == 'Brian':   # logic to check if user gave correct answer
            print('Correct!')
            break               # break statement escapes the while loop
        elif round == 3:        # logic to ensure round has not yet reached 3
            print('Sorry, the answer was Brian.')
            break               # break statement escapes the while loop
        else:                   # if answer was wrong, and round is not yet equal to 3
            print('Sorry. Try again!')

main()