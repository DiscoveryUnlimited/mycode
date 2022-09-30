#!/usr/bin/python3
"""Alta3 Research | JPagan
   Read from files."""


def main():

    default_file = "vlanconfig.cfg"

    # prompt to user for file name
    file = input("Enter the name of file to load: ")

    if len(file) == 0:
        print("\n... loading default\n")
        file = default_file

    ## create file object in "r"ead mode
    with open(file, "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()

    ## file was just auto closed (no more indenting)

    ## each item of the list now has the "\n" characters back
    print(configlist)

    print("\nNumber of lines in file: " + str(len(configlist)))

if __name__ == "__main__":
    main()