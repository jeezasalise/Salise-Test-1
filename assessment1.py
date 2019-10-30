import sys
import json
import csv
from os import path

def csvjsonf():
    read_csvfile = sys.argv[1]
    write_jsonfile = sys.argv[2]
    if read_csvfile.endswith('.txt') or read_csvfile.endswith('.csv') and path.exists(read_csvfile):
        if write_jsonfile.endswith('.txt') or write_jsonfile.endswith('.json'):
            pass
        else:
            write_jsonfile += '.txt'
            
        data = {}
        with open(read_csvfile, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
            data = list(csv_reader)
            with open(write_jsonfile, 'w') as json_file: # okay part
                json_file.write(json.dumps(data, indent = 4))
                print("Success!")
    else:
        print("Csv does not exist. Please check your input.\n")

csvjsonf()