import csv 
import json

def convert_csv_to_json(filename):
    try:
        data = []
        with open(filename, 'r') as f:
            for i in csv.DictReader(f):
                data.append(json.dumps(i))
        print(data)
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except FileNotFoundError:
        return False

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")