import json
import os

os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1/")
CWD = os.getcwd()
print("Current working directory: ", CWD)
OUTPUT_DIR = CWD + "/Code_Output/"

"""
Load results
"""
a = "distance_matching_result.json"
b = "soundex_matching_result.json"
c = "distance_matching_new_data_result.json"
d = "soundex_matching_new_data_result.json"
with open(OUTPUT_DIR + d, 'r') as f:
    soundex_new_data = json.load(f)
with open(OUTPUT_DIR + a, 'r') as f:
    distance_result = json.load(f)
with open(OUTPUT_DIR + b, 'r') as f:
    soundex_result = json.load(f)
with open(OUTPUT_DIR + c, 'r') as f:
    distance_new_data = json.load(f)

"""
Print sample results
"""
print(distance_result[0])
print(soundex_result[0])
print(distance_new_data[0])
print(soundex_new_data[0])
