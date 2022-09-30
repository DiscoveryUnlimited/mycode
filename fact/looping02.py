#!/usr/bin/python3
"""Alta3 Research | JPagan
   For - Using a file's lines as a source for the for-loop"""


def main():
    
    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")

    # create list of lines
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="") # the line we read ALREADY contains a \n (newline)
        
    # close the file (we created the list of lines)
    dnsfile.close() # best practice to close your file


if __name__ == "__main__":
    main()