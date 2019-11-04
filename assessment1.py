import sys
import json
import csv
import os

def main(argv):

    if len(sys.argv) is 3 or len(sys.argv) is 4:

        read_csvfile = sys.argv[1]
        write_jsonfile = sys.argv[2]
        
        if len(sys.argv) is 3:
            csvdelimiter = ","

        elif len(sys.argv) is 4:
            csvdelimiter = sys.argv[3]
            
        if (read_csvfile.endswith('.csv') or read_csvfile.endswith('.txt')) and os.path.exists(read_csvfile):

                if not (write_jsonfile.endswith('.json') or write_jsonfile.endswith('.txt')):
                    write_jsonfile += '.json'

                data = {}
                with open(read_csvfile, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=csvdelimiter, skipinitialspace=True)
                    data = list(csv_reader)
                    with open(write_jsonfile, 'w') as json_file:
                        json_file.write(json.dumps(data, indent = 4))
                        print("Success!")
                        
        else:
            print("Csv file does not exist. Please check the file name and file extension.\n")
    else:
        print("Please follow the format: assessment1.py <csv_filename.csv> <json_filename.json> <delimiter(optional)>\nIf the delimiter is omitted, the default is , \nExamples: assessment1.py csvtest.csv newfile.json & \n\t  assessment1.py csvfile.csv writehere.json")
        sys.exit()
    
if __name__ == "__main__":
    main(sys.argv[1:])