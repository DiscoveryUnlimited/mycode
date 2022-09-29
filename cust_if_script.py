#!/usr/bin/env python3
""" Alta3 Research | JPagan
    if, elif, else - A simple program using conditionals to give percentile of runners."""

def main():
    
    # Welcome message
    print()
    print("Welcome Runners!")
    print()
    print("................")
    print()

    # prompt
    pace = float(input("How fast can you run a 5k (min)? "))
    print()

    # pace if else

    if pace <= 18.6:
        percentile = 'realy fast and among the 1st'
    elif pace <= 30.5:
        percentile = 'quick and among the 30th'
    elif pace <= 37:
        percentile = 'about average and among the 60th'
    elif pace <= 50:
        percentile = 'pretty slow and among the 90th'
    else:
        percentile = 'among the slowest and worse than the 90th'
    
    # Print statement
    print(f"You are {percentile} percentile of runners.")
    print()

main()