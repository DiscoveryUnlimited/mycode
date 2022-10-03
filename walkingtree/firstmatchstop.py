#!/usr/bin/env python3
"""Alta3 Research | JPagan
os Walk"""

## Script to search and stop on first match
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():

    lookfor = input("What am I looking for? ")
    lookwhere = input("What is the path in which I should search? ")
    
    print(find(lookfor, lookwhere))

if __name__ == "__main__":
    main()