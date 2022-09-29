#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Input if testing"""

def main():

    ipchk = input("Apply an IP address: ") # this line now prompts the user for input

    # a provided string will test true
    if ipchk:
        print("Looks like the IP address was set: " + ipchk) # indented under if
    else:    # if data is NOT provided
        print("You did not provide input.") # indented under else

main()