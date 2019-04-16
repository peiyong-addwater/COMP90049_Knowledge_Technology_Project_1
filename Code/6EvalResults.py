import json
import os

CWD = os.getcwd()
print(CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
a = "distance_matching_result.json"
with open(OUTPUT_DIR + a, 'r') as f:
    data = json.load(f)
print(len(data))
