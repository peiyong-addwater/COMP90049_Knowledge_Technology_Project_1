import json
import os

import utilsKTP1 as KTP1
import multiprocessing as mp

ON_SERVER = True
if ON_SERVER:
    os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1")
CWD = os.getcwd()
print("Current working directory: ", CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
DATA = OUTPUT_DIR + "data_entries.json"
DICT = OUTPUT_DIR + "dict.json"
with open(DATA, 'r') as fp:
    data = json.load(fp)
with open(DICT, 'r') as fp:
    dict = json.load(fp)

iv_data = [c for c in data if c[2] == "IV"]
phonetics_matching_result = {}


def findMatchForASingleEntry(data_entry):
    result = {}
    result["misspell"] = data_entry[0]
    result["target"] = data_entry[1]
    if data_entry[-1] == True:
        result["original spelling status"] = "correct"
    else:
        result["original spelling status"] = "misspell"
