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

"""
Evaluation of results
"""
eval_distance_result = []
eval_soundex_result = []
eval_distacne_new_data = []
eval_soundex_new_data = []

for c in distance_result:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['Minimum Levenshtein Distance'] == c['target']:
        single_eval['Minimum Levenshtein Distance'] = 1
    else:
        single_eval['Minimum Levenshtein Distance'] = 0
    if c['3-Gram with Jaccard Best Match'] == c['target']:
        single_eval['3-Gram with Jaccard Best Match'] = 1
    else:
        single_eval['3-Gram with Jaccard Best Match'] = 0
    if c['2-Gram with Jaccard Best Match'] == c['target']:
        single_eval['2-Gram with Jaccard Best Match'] = 1
    else:
        single_eval['2-Gram with Jaccard Best Match'] = 0
    if c['target'] in c['Edit Distance No More Than 2']:
        single_eval['Edit Distance No More Than 2'] = 1
    else:
        single_eval['Edit Distance No More Than 2'] = 0
    if c['target'] in c['Edit Distance No More Than 1']:
        single_eval['Edit Distance No More Than 1'] = 1
    else:
        single_eval['Edit Distance No More Than 1'] = 0
    if c['target'] in c['3-Gram Jaccard Distance No More Than 0.2']:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 1
    else:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 0
    if c['target'] in c['2-Gram Jaccard Distance No More Than 0.2']:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 1
    else:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 0
    eval_distance_result.append(single_eval)

for c in distance_new_data:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['Minimum Levenshtein Distance'] == c['target']:
        single_eval['Minimum Levenshtein Distance'] = 1
    else:
        single_eval['Minimum Levenshtein Distance'] = 0
    if c['3-Gram with Jaccard Best Match'] == c['target']:
        single_eval['3-Gram with Jaccard Best Match'] = 1
    else:
        single_eval['3-Gram with Jaccard Best Match'] = 0
    if c['2-Gram with Jaccard Best Match'] == c['target']:
        single_eval['2-Gram with Jaccard Best Match'] = 1
    else:
        single_eval['2-Gram with Jaccard Best Match'] = 0
    if c['target'] in c['Edit Distance No More Than 2']:
        single_eval['Edit Distance No More Than 2'] = 1
    else:
        single_eval['Edit Distance No More Than 2'] = 0
    if c['target'] in c['Edit Distance No More Than 1']:
        single_eval['Edit Distance No More Than 1'] = 1
    else:
        single_eval['Edit Distance No More Than 1'] = 0
    if c['target'] in c['3-Gram Jaccard Distance No More Than 0.2']:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 1
    else:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 0
    if c['target'] in c['2-Gram Jaccard Distance No More Than 0.2']:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 1
    else:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 0
    eval_distacne_new_data.append(single_eval)

for c in soundex_result:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['target'] in c['same phonetic representation']['metaphone']:
        single_eval['metaphone'] = 1
    else:
        single_eval['metaphone'] = 0
    if c['target'] in c['same phonetic representation']['refined_soundex']:
        single_eval['refined_soundex'] = 1
    else:
        single_eval['refined_soundex'] = 0
    if c['target'] in c['same phonetic representation']['mra']:
        single_eval['mra'] = 1
    else:
        single_eval['mra'] = 0
    eval_soundex_result.append(single_eval)

for c in soundex_new_data:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['target'] in c['same phonetic representation']['metaphone']:
        single_eval['metaphone'] = 1
    else:
        single_eval['metaphone'] = 0
    if c['target'] in c['same phonetic representation']['refined_soundex']:
        single_eval['refined_soundex'] = 1
    else:
        single_eval['refined_soundex'] = 0
    if c['target'] in c['same phonetic representation']['mra']:
        single_eval['mra'] = 1
    else:
        single_eval['mra'] = 0
    eval_soundex_new_data.append(single_eval)
