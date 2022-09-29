#!/usr/bin/env python3
"""
    Alta3 Research | JPagan
    input if, customized"""

def main():
    
    # Input
    hostname = input("What value should we set for hostname?")
    
    # Print if true, converting any character to lower case
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")
    
    # Exit display
    print("Exiting the script")
main()