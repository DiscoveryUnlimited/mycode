#!/usr/bin/python3
"""Alta3 Research | JPagan
   JSON to CSV
   CSV to Excel
   JSON to Excel"""

import pandas

def json_csv():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

def csv_excel():
    
    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

def json_excel():
    
    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

def main():

    json_csv()
    csv_excel()
    json_excel()

if __name__ == "__main__":
    main()
