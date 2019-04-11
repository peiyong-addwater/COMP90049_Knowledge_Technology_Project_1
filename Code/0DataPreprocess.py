import os
import json
import nltk

CWD = os.getcwd()
# Should be .../COMP90049_Knowledge_Technology_Project_1 if run "python .../Code/0DataPreprocess.py" in terminal
print("Current working directory: ", CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
"""
Raw data from LMS
"""
DATA_DIR = CWD + "/Data/"
DICT_FILENAME = DATA_DIR+"dict.txt"
CORRECT_FILENAME = DATA_DIR+"correct.txt"
MISSPELL_FILENAME = DATA_DIR+"misspell.txt"

dictionary = []
with open(DICT_FILENAME, 'r') as fp:
    for line in fp:
        dictionary.append(line)
# save dictionary list to .json file


data_entries = []
mis = open(MISSPELL_FILENAME, 'r').readlines()
correct = open(CORRECT_FILENAME, 'r').readlines()

for i in range(len(mis)):
    if correct[i] in dictionary:
        entry = [mis[i], correct[i], 'IV']
    else:
        entry = [mis[i], correct[i], 'OOV']
    data_entries.append(entry)

iv = 0
for c in data_entries:
    if c[2] is 'IV':
        iv = iv + 1
oov = len(mis)-iv
total = len(data_entries)
print("IV: ", iv, "/", total, '\t', "IV Ratio: ", iv/total) 
print("OOV: ",  oov, "/", total, '\t', "OOV Ratio: ", oov/total)


