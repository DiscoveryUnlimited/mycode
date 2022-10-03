#!/usr/bin/env python3
"""Alta3 Research | JPagan
Learning imports"""

#imports
from subprocess import call

def main():

    call(["ip", "link", "show", "up"])
    print("This program will check your interfaces.")
    interface = input("Enter an interface, like, ens3: ")
    call(["ip", "addr", "show", "dev", interface])
    call(["ip", "route", "show", "dev", interface])

if __name__ == "__main__":
    main()