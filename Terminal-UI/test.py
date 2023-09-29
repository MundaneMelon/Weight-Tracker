import os
import io
import sys
import json
import importlib


def main():
    f = open('jsons/data.json')
    file = json.load(f)
    file = add_entry(file)


def add_entry(file):
    print("Welcome to whatever this is\n")
    input1 = input("Weight?  ")
    input2 = input("Date? (MM/DD/YY)  ")
    input3 = input("Time in 24hr format? (optional)  ")
    dict = {
        "weight" : float(input1),
        "date" : input2,
        "time" : input3
    }
    file["entries"].append(dict)
    with open("jsons/data.json", "w") as outfile:
        json.dump(file, outfile, indent=4, sort_keys=True)

    return file







if __name__ == "__main__":
    main()
