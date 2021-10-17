# python 3
# PROJECT: REMOVING THE HEADER FROM CSV FILES
# removeCSVHeader.py
"""
Project Task: Removing the first line from several hundred CSV files.
The program will need to open every file with the .csv extension in the current working directory, 
read in the contents of the CSV file, and rewrite the contents without the first row to a file of the same name. 
This will replace the old contents of the CSV file with the new, headless contents.

At a high level, the program must do the following:
    1. Find all the CSV files in the current working directory.
    2. Read in the full contents of each file.
    3. Write out the contents, skipping the first line, to a new CSV file.

At the code level, this means the program will need to do the following:
    1. Loop over a list of files from os.listdir(), skipping the non-CSV files.
    2. Create a CSV reader object and read in the contents of the file, using the 
       line_num attribute to figure out which line to skip.
    3. Create a CSV writer object and write out the read-in data to the new file.

For this project, open a new file editor window and save it as removeCsvHeader.py.
"""

import os, csv
from pathlib import Path

print(f"\n\nCurrent Working Path ==> {Path.cwd()}")

folder_path = f"{Path.cwd()}/c16_CSV_and_JSON/CSVHeader"
print(folder_path)

backup_folder = f"{Path.cwd()}/c16_CSV_and_JSON/removeCSVHeader"
os.makedirs(backup_folder, exist_ok=True)

for folder, subforlders, filenames in os.walk(folder_path):
    for filename in filenames:
        print('\n', filename)
        if filename.endswith('csv'):
            csv_file = open(f"{folder}/{filename}")
            csv_reader = csv.reader(csv_file)
            removed_head_file = open(f"{backup_folder}/{filename}", 'w', newline='')
            removed_head_writer = csv.writer(removed_head_file)
            for row in csv_reader:
                # print(str(csv_reader.line_num), row)
                if csv_reader.line_num == 1:
                    continue
                # print(row)
                removed_head_writer.writerow(row)
            csv_file.close()
            removed_head_file.close()