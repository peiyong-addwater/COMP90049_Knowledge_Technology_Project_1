import datetime
import json
import multiprocessing as mp
import os
import time

import utilsKTP1 as KTP1

ON_SERVER = True
if ON_SERVER:
    os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1")
CWD = os.getcwd()
print("Current working directory: ", CWD)
DATA_DIR = CWD + "/Data/"
DICT_FILENAME = DATA_DIR + "dict.txt"
ADDITIONAL_DATA = DATA_DIR + '/Data/words.txt'
CORRECT_FILENAME = DATA_DIR + "correct.txt"
MISSPELL_FILENAME = DATA_DIR + "misspell.txt"

OUTPUT_DIR = CWD + "/Code_Output/"
DATA = OUTPUT_DIR + "data_entries.json"
DICT = OUTPUT_DIR + "dict.json"

additional_dict = []
with open(ADDITIONAL_DATA, 'r') as fp:
    for line in fp:
        additional_dict.append(line.rstrip('\n'))
print(len(additional_dict))

with open(DATA, 'r') as fp:
    data = json.load(fp)
with open(DICT, 'r') as fp:
    dict = json.load(fp)

# oov_data = [c for c in data if c[2] == "OOV"]


# expand the dictionary with words.txt from https://github.com/dwyl/english-words
