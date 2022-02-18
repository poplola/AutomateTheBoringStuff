# Youtube link: https://www.youtube.com/watch?v=-51jxlQaxyA
# JSON = JavaScript Object Notation, Data type likes python library
# ⭐️ Timestamps ⭐️
# 00:00 | JSON Defined
# 01:15 | Loading JSON Strings
# 02:20 | Creating JSON Strings
# 03:46 | Reading JSON Files
# 04:51 | Writing JSON To A File

import json, os
from textwrap import indent

print("\n========== Practice #1: Read Json as string ==========\n")
json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Lisa",
                "age": 40,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Tim",
                "age": 21,
                "full-time": false
            }
        ]
    }
'''

data = json.loads(json_string)
# print(data['students'][1])

data['test'] = True

# print json data format with "indent=4", 
# sort the keys with "sort_keys=True"
new_json = json.dumps(data, indent=4, sort_keys=True)
print(new_json)




print("\n========== Practice #2: Read Json file ==========\n")

print(os.getcwd())
newDir = "/Users/flaviolago/Documents/Education/Liping/Python/Projects/Project Practice/Python with Tim/JSON in Python/"
os.chdir(newDir)
print(os.getcwd())

## read json file
with open("data.json", "r") as f:
    data = json.load(f)

## wrire json to a file
with open("data2.json", 'w') as f:
    json.dump(data, f, indent=4)

print(data)
print(data.items())
print(data.keys())
