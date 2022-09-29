#!/usr/bin/env python3
"""
    Alta3 Research | JPagan
    input if, non-case sensitive"""

def main():
    
    #input
    hostname = input("What value should we set for hostname?")
    
    # print if true, converting any character to lower case
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
main()

