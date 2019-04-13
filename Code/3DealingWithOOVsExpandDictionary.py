import json
import os

from tqdm import tqdm

"""
Expanding the dictionary with words from https://github.com/first20hours/google-10000-english and
https://github.com/dwyl/english-words
"""

ON_SERVER = True
if ON_SERVER:
    os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1")
CWD = os.getcwd()
print("Current working directory: ", CWD)
DATA_DIR = CWD + "/Data/"
DICT_FILENAME = DATA_DIR + "dict.txt"
ADDITIONAL_DATA_1 = DATA_DIR + 'words.txt'
ADDITIONAL_DATA_2 = DATA_DIR + 'google-10000-english.txt'
ADDITIONAL_DATA_3 = DATA_DIR + 'google-10000-english-usa.txt'
CORRECT_FILENAME = DATA_DIR + "correct.txt"
MISSPELL_FILENAME = DATA_DIR + "misspell.txt"

OUTPUT_DIR = CWD + "/Code_Output/"
DATA = OUTPUT_DIR + "data_entries.json"
DICT = OUTPUT_DIR + "dict.json"

additional_dict = []
with open(ADDITIONAL_DATA_1, 'r') as fp:
    for line in fp:
        additional_dict.append(line.rstrip('\n'))
with open(ADDITIONAL_DATA_2, 'r') as fp:
    for line in fp:
        additional_dict.append(line.rstrip('\n'))
with open(ADDITIONAL_DATA_3, 'r') as fp:
    for line in fp:
        additional_dict.append(line.rstrip('\n'))

with open(DICT, 'r') as fp:
    dict = json.load(fp)

new_dict = additional_dict + dict
print("Original Dictionary Length: ", len(dict))
new_dict = list(set(new_dict))
print("Expanded Dictionary Length: ", len(new_dict))
new_data_entries = []
mis = open(MISSPELL_FILENAME, 'r').readlines()
correct = open(CORRECT_FILENAME, 'r').readlines()
print("Saving expanded dictionary as .json...")
with open(OUTPUT_DIR + "new_dict.json", 'w') as fp:
    json.dump(new_dict, fp, indent=4)
print("Expanded dictionary saved to ", OUTPUT_DIR + "new_dict.json")
print("Processing data according to expanded dictionary...")
for i in tqdm(range(len(mis))):
    # print("Progress %d/%d\r" % (i + 1, len(mis)))
    if correct[i].rstrip('\n') in new_dict:
        entry = [mis[i].rstrip('\n'), correct[i].rstrip('\n'), 'IV']
    else:
        entry = [mis[i].rstrip('\n'), correct[i].rstrip('\n'), 'OOV']
    if mis[i].rstrip('\n') == correct[i].rstrip('\n'):
        entry.append(True)  # Means the misspell and the corrected one is actually the same
    else:
        entry.append(False)  # Means the misspell and the corrected one is not the same
    new_data_entries.append(entry)

print("Saving misspelling-correct spelling data entries...")
with open(OUTPUT_DIR + "new_data_entries.json", 'w') as fp:
    json.dump(new_data_entries, fp, indent=4)
print("New Data entries saved to ", OUTPUT_DIR + "new_data_entries.json")

iv = 0
for c in new_data_entries:
    if c[2] is 'IV':
        iv = iv + 1
oov = len(mis) - iv
total = len(new_data_entries)
print("IV: ", iv, "/", total, '\t', "IV Ratio: ", iv / total)
print("OOV: ", oov, "/", total, '\t', "OOV Ratio: ", oov / total)
"""
Current working directory:  /home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1
Original Dictionary Length:  370099
Expanded Dictionary Length:  500808
Saving expanded dictionary as .json...
Expanded dictionary saved to  /home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1
/Code_Output/new_dict.json
Processing data according to expanded dictionary...
100%|█████████████████████████████████████| 10322/10322 [05:20<00:00, 31.34it/s]
Saving misspelling-correct spelling data entries...
New Data entries saved to  /home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1/Code_Output
/new_data_entries.json
IV:  8832 / 10322 	 IV Ratio:  0.8556481302073241
OOV:  1490 / 10322 	 OOV Ratio:  0.14435186979267584
"""
