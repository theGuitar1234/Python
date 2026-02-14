import json
import sys

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)    

def load_from_json_file(filename):
    with open(filename, 'r+') as f:
        return json.load(f)
    
save_to_json_file(sys.argv[1:], "add_item.json")
print(load_from_json_file("add_item.json"))