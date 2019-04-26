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
print("----------Sample Result----------")
print(distance_result[0])
print(soundex_result[0])
print(distance_new_data[0])
print(soundex_new_data[0])

"""
Evaluation of single result
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
        single_eval['Edit Distance No More Than 2 Total'] = len(c['Edit Distance No More Than 2'])
    else:
        single_eval['Edit Distance No More Than 2 Total'] = len(c['Edit Distance No More Than 2'])
        single_eval['Edit Distance No More Than 2'] = 0
    if c['target'] in c['Edit Distance No More Than 1']:
        single_eval['Edit Distance No More Than 1'] = 1
        single_eval['Edit Distance No More Than 1 Total'] = len(c['Edit Distance No More Than 1'])
    else:
        single_eval['Edit Distance No More Than 1'] = 0
        single_eval['Edit Distance No More Than 1 Total'] = len(c['Edit Distance No More Than 1'])
    if c['target'] in c['3-Gram Jaccard Distance No More Than 0.2']:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 1
        single_eval['3-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['3-Gram Jaccard Distance No More Than 0.2'])
    else:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 0
        single_eval['3-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['3-Gram Jaccard Distance No More Than 0.2'])
    if c['target'] in c['2-Gram Jaccard Distance No More Than 0.2']:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 1
        single_eval['2-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['2-Gram Jaccard Distance No More Than 0.2'])
    else:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 0
        single_eval['2-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['2-Gram Jaccard Distance No More Than 0.2'])
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
        single_eval['Edit Distance No More Than 2 Total'] = len(c['Edit Distance No More Than 2'])
    else:
        single_eval['Edit Distance No More Than 2 Total'] = len(c['Edit Distance No More Than 2'])
        single_eval['Edit Distance No More Than 2'] = 0
    if c['target'] in c['Edit Distance No More Than 1']:
        single_eval['Edit Distance No More Than 1'] = 1
        single_eval['Edit Distance No More Than 1 Total'] = len(c['Edit Distance No More Than 1'])
    else:
        single_eval['Edit Distance No More Than 1'] = 0
        single_eval['Edit Distance No More Than 1 Total'] = len(c['Edit Distance No More Than 1'])
    if c['target'] in c['3-Gram Jaccard Distance No More Than 0.2']:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 1
        single_eval['3-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['3-Gram Jaccard Distance No More Than 0.2'])
    else:
        single_eval['3-Gram Jaccard Distance No More Than 0.2'] = 0
        single_eval['3-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['3-Gram Jaccard Distance No More Than 0.2'])
    if c['target'] in c['2-Gram Jaccard Distance No More Than 0.2']:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 1
        single_eval['2-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['2-Gram Jaccard Distance No More Than 0.2'])
    else:
        single_eval['2-Gram Jaccard Distance No More Than 0.2'] = 0
        single_eval['2-Gram Jaccard Distance No More Than 0.2 Total'] = len(
            c['2-Gram Jaccard Distance No More Than 0.2'])
    eval_distacne_new_data.append(single_eval)

for c in soundex_result:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['target'] in c['same phonetic representation']['metaphone']:
        single_eval['metaphone'] = 1
        single_eval['metaphone total'] = len(c['same phonetic representation']['metaphone'])
    else:
        single_eval['metaphone total'] = len(c['same phonetic representation']['metaphone'])
        single_eval['metaphone'] = 0
    if c['target'] in c['same phonetic representation']['refined_soundex']:
        single_eval['refined_soundex'] = 1
        single_eval['refined_soundex total'] = len(c['same phonetic representation']['refined_soundex'])
    else:
        single_eval['refined_soundex'] = 0
        single_eval['refined_soundex total'] = len(c['same phonetic representation']['refined_soundex'])
    if c['target'] in c['same phonetic representation']['mra']:
        single_eval['mra total'] = len(c['same phonetic representation']['mra'])
        single_eval['mra'] = 1
    else:
        single_eval['mra'] = 0
        single_eval['mra total'] = len(c['same phonetic representation']['mra'])
    eval_soundex_result.append(single_eval)

for c in soundex_new_data:
    single_eval = {}
    single_eval['misspell'] = c['misspell']
    single_eval['target'] = c['target']
    single_eval['original spelling status'] = c['original spelling status']
    single_eval['OOV/IV'] = c['OOV/IV']
    if c['target'] in c['same phonetic representation']['metaphone']:
        single_eval['metaphone'] = 1
        single_eval['metaphone total'] = len(c['same phonetic representation']['metaphone'])
    else:
        single_eval['metaphone total'] = len(c['same phonetic representation']['metaphone'])
        single_eval['metaphone'] = 0
    if c['target'] in c['same phonetic representation']['refined_soundex']:
        single_eval['refined_soundex'] = 1
        single_eval['refined_soundex total'] = len(c['same phonetic representation']['refined_soundex'])
    else:
        single_eval['refined_soundex'] = 0
        single_eval['refined_soundex total'] = len(c['same phonetic representation']['refined_soundex'])
    if c['target'] in c['same phonetic representation']['mra']:
        single_eval['mra total'] = len(c['same phonetic representation']['mra'])
        single_eval['mra'] = 1
    else:
        single_eval['mra'] = 0
        single_eval['mra total'] = len(c['same phonetic representation']['mra'])
    eval_soundex_new_data.append(single_eval)

print("----------Single Result Evaluation Sample----------")
print(eval_distance_result[99])
print(eval_distacne_new_data[99])
print(eval_soundex_result[99])
print(eval_soundex_new_data[99])
"""
{'misspell': 'usa', 'target': 'use', 'original spelling status': 'misspell', 'OOV/IV': 'IV', 'Minimum Levenshtein 
Distance': 0, '3-Gram with Jaccard Best Match': 0, '2-Gram with Jaccard Best Match': 0, 'Edit Distance No More Than 
2': 1, 'Edit Distance No More Than 2 Total': 561, 'Edit Distance No More Than 1': 1, 'Edit Distance No More Than 1 
Total': 20, '3-Gram Jaccard Distance No More Than 0.2': 0, '3-Gram Jaccard Distance No More Than 0.2 Total': 1, 
'2-Gram Jaccard Distance No More Than 0.2': 0, '2-Gram Jaccard Distance No More Than 0.2 Total': 1}
{'misspell': 'in', 'target': 'in', 'original spelling status': 'correct', 'OOV/IV': 'IV', 'Minimum Levenshtein 
Distance': 1, '3-Gram with Jaccard Best Match': 1, '2-Gram with Jaccard Best Match': 1, 'Edit Distance No More Than 
2': 1, 'Edit Distance No More Than 2 Total': 2137, 'Edit Distance No More Than 1': 1, 'Edit Distance No More Than 1 
Total': 89, '3-Gram Jaccard Distance No More Than 0.2': 1, '3-Gram Jaccard Distance No More Than 0.2 Total': 1, 
'2-Gram Jaccard Distance No More Than 0.2': 1, '2-Gram Jaccard Distance No More Than 0.2 Total': 1}
{'misspell': 'c', 'target': 'see', 'original spelling status': 'misspell', 'OOV/IV': 'IV', 'metaphone total': 82, 
'metaphone': 0, 'refined_soundex': 0, 'refined_soundex total': 14, 'mra': 0, 'mra total': 37}
{'misspell': 'c', 'target': 'see', 'original spelling status': 'misspell', 'OOV/IV': 'IV', 'metaphone total': 206, 
'metaphone': 0, 'refined_soundex': 0, 'refined_soundex total': 39, 'mra': 0, 'mra total': 112}
"""

'''
Statistics of the Results
'''
original_dict = {}
updated_dict = {}
# Average precision = corrected ones in the returned words / total number of returned words on the entire dataset
# Recall is calculated based on the correct words (treat correct words as 'relevant')
# Statistics for original_dict
mld_status_corrected = sum([c['Minimum Levenshtein Distance'] for c in eval_distance_result])
mld_avg_pre = mld_status_corrected / len(eval_distance_result)
original_dict['Average Precision for Minimum Levenshtein Distance'] = mld_avg_pre
# print(mld_avg_pre)
all_correct = sum([c['original spelling status'] == 'correct' for c in eval_distance_result])
mld_correct_still_correct = sum([c['original spelling status'] == 'correct' and c['Minimum Levenshtein Distance'] ==
                                 1 for c in eval_distance_result])
mld_recall_for_corrected_ones = mld_correct_still_correct / all_correct
# print(mld_recall_for_corrected_ones)
original_dict['Recall (Based on Corrected Spellings) for Minimum Levenshtein Distance'] = mld_recall_for_corrected_ones
edit_less_than_2_pre = sum([c['Edit Distance No More Than 2'] for c in eval_distance_result]) / sum(
    [c['Edit Distance No '
       'More Than 2 Total']
     for c in eval_distance_result])

# print(edit_less_than_2_pre)
original_dict['Average Precision for Edit Distance No More Than 2'] = edit_less_than_2_pre
edit_less_than_2_recall = sum([c['original spelling status'] == 'correct' and c['Edit Distance No More Than 2'] == 1
                               for c in eval_distance_result]) / all_correct
# print(edit_less_than_2_recall)
