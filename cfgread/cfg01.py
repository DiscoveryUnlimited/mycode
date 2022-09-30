#!/usr/bin/python3
"""Alta3 Research | JPagan
   Read from files."""


def main():

    ######## EXPLORE READ ##########
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the screen - .read()
    print(configfile.read())

    ## close file
    configfile.close()

    ######## EXPLORE READLINES ##########
    ## re-create file object to explore new method
    configfile = open("vlanconfig.cfg", "r")

    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

    ## Iterate through configlist
    print("\n end= \n")
    for x in configlist:
        print(x, end="")

    ## Iterate through configlist
    print("\n .strip() \n")
    for x in configlist:
        print(x.strip())

    ## Always close your file
    configfile.close()

if __name__ == "__main__":
    main()