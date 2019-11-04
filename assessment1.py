import sys
import json
import csv
from os import path

if len(sys.argv) > 2:

    read_csvfile = sys.argv[1]
    write_jsonfile = sys.argv[2]
    if read_csvfile.endswith('.csv') and path.exists(read_csvfile):
        if write_jsonfile.endswith('.json'):
            pass
        else:
            write_jsonfile += '.json'
        data = {}
        with open(read_csvfile, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
            data = list(csv_reader)
            with open(write_jsonfile, 'w') as json_file:
                json_file.write(json.dumps(data, indent = 4))
                print("Success!")
    else:
        print("Csv file does not exist. Please check the file name and file extension.\n")

else:
    print("Please follow the format: assessment1.py <csv_filename.csv> <json_filename.json> \nExample: assessment1.py csvtest.csv newfile.json")