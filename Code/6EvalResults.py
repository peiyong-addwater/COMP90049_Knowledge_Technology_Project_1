import json
import os

os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1/")
CWD = os.getcwd()
print(CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
a = "soundex_matching_result.json"
with open(OUTPUT_DIR + a, 'r') as f:
    data = json.load(f)
print(len(data))
