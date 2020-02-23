#!/usr/bin/python

import sys
import csv
import json
from os import listdir

print("Files available: ",listdir("to_convert"))

file_path = input("Input file name (default input.csv):")
if file_path == '':
	file_path = "input.csv"
file_path = 'to_convert/' + file_path

save_path = input("Output file name (JSON):")
if save_path == '':
	save_path = "output.json"
save_path = "processed/"+ save_path

print ("Opening "+file_path+" for processing")

with open(file_path, 'r', encoding="utf-8-sig") as f:
	json_data = list(csv.DictReader(f))
	print(json.dumps(json_data, sort_keys=False, indent=4))

with open(save_path, 'w', encoding="utf8") as s:
	json.dump(json_data,s, indent=2)