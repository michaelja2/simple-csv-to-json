#!/usr/bin/python

import sys
import csv
import json
from os import listdir

print("Files available: ",listdir("to_convert"))
file_path = ("to_convert/"+ input("Input file name (CSV): " ))
save_path = ("processed/"+ input("Output file name (JSON):"))

print ("Opening "+file_path+" for processing")

with open(file_path, 'r', encoding="utf-8-sig") as f:
	# reader = csv.DictReader(f)
	json_data = list(csv.DictReader(f))
	print(json.dumps(json_data, sort_keys=False, indent=4))

with open(save_path, 'w', encoding="utf8") as s:
	json.dump(json_data,s, indent=2)