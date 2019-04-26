
import json
import os

ON_SERVER = True
if ON_SERVER:
    os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1")
CWD = os.getcwd()
print("Current working directory: ", CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
"""
Raw data from LMS
"""
DATA_DIR = CWD + "/Data/"
DICT_FILENAME = DATA_DIR + "dict.txt"
CORRECT_FILENAME = DATA_DIR + "correct.txt"
MISSPELL_FILENAME = DATA_DIR + "misspell.txt"

dictionary = []
with open(DICT_FILENAME, 'r') as fp:
    for line in fp:
        dictionary.append(line.rstrip('\n'))

# save dictionary list to .json file
print("Saving dictionary as .json...")
with open(OUTPUT_DIR + "dict.json", 'w') as fp:
    json.dump(dictionary, fp, indent=4)
print("Dictionary saved to ", OUTPUT_DIR + "dict.json")

data_entries = []
mis = open(MISSPELL_FILENAME, 'r').readlines()
correct = open(CORRECT_FILENAME, 'r').readlines()

for i in range(len(mis)):
    if correct[i].rstrip('\n') in dictionary:
        entry = [mis[i].rstrip('\n'), correct[i].rstrip('\n'), 'IV']
    else:
        entry = [mis[i].rstrip('\n'), correct[i].rstrip('\n'), 'OOV']
    if mis[i].rstrip('\n') == correct[i].rstrip('\n'):
        entry.append(True)  # Means the misspell and the corrected one is actually the same
    else:
        entry.append(False)  # Means the misspell and the corrected one is not the same
    data_entries.append(entry)
print("Saving misspelling-correct spelling data entries...")
with open(OUTPUT_DIR + "data_entries.json", 'w') as fp:
    json.dump(data_entries, fp, indent=4)
print("Data entries saved to ", OUTPUT_DIR + "data_entries.json")
iv = 0
for c in data_entries:
    if c[2] is 'IV':
        iv = iv + 1
oov = len(mis) - iv
total = len(data_entries)
print("IV: ", iv, "/", total, '\t', "IV Ratio: ", iv / total)
print("OOV: ", oov, "/", total, '\t', "OOV Ratio: ", oov / total)
'''
IV:  8543 / 10322 	 IV Ratio:  0.8276496802945166
OOV:  1779 / 10322 	 OOV Ratio:  0.17235031970548342
'''
