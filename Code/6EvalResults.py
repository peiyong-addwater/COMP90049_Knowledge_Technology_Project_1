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
# print("----------Sample Result----------")
# print(distance_result[0])
# print(soundex_result[0])
# print(distance_new_data[0])
# print(soundex_new_data[0])

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

# print("----------Single Result Evaluation Sample----------")
# print(eval_distance_result[99],'\n')
#print(eval_distacne_new_data[99])
print(eval_soundex_result[99])
#print(eval_soundex_new_data[99])

'''
Statistics of the Results
'''
original_dict = {}
original_dict['Minimum Levenshtein Distance'] = {}
original_dict['Edit Distance No More Than 2'] = {}
original_dict['Edit Distance No More Than 1'] = {}
original_dict['3-Gram with Jaccard Best Match'] = {}
original_dict['2-Gram with Jaccard Best Match'] = {}
original_dict['2-Gram Jaccard Distance No More Than 0.2'] = {}
original_dict['3-Gram Jaccard Distance No More Than 0.2'] = {}
original_dict['metaphone'] = {}
original_dict['refined_soundex'] = {}
original_dict['mra'] = {}

updated_dict = {}
updated_dict['Minimum Levenshtein Distance'] = {}
updated_dict['Edit Distance No More Than 2'] = {}
updated_dict['Edit Distance No More Than 1'] = {}
updated_dict['3-Gram with Jaccard Best Match'] = {}
updated_dict['2-Gram with Jaccard Best Match'] = {}
updated_dict['2-Gram Jaccard Distance No More Than 0.2'] = {}
updated_dict['3-Gram Jaccard Distance No More Than 0.2'] = {}
updated_dict['metaphone'] = {}
updated_dict['refined_soundex'] = {}
updated_dict['mra'] = {}



# Average precision = corrected ones in the returned words / total number of returned words on the entire dataset
# Recall is calculated based on the correct words (treat correct words as 'relevant')
###############################
# Statistics for original_dict#
###############################

ALL_IV_NEED_CORRECTION = len(
    [c for c in eval_distance_result if c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
ALL_CORRECT_SPELLING = len(
    [c for c in eval_distance_result if c['original spelling status'] == 'correct'])  # to calculate the recall
ALL_CORRECT_SPELLING_IV = len([c for c in eval_distance_result if c['original spelling status'] == 'correct' and c[
    'OOV/IV'] == 'IV'])  # to calculate the recall

ALL_IV_NEED_CORRECTION_PH = len(
    [c for c in eval_soundex_result if c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
ALL_CORRECT_SPELLING_PH = len(
    [c for c in eval_soundex_result if c['original spelling status'] == 'correct'])  # to calculate the recall
ALL_CORRECT_SPELLING_IV_PH = len([c for c in eval_soundex_result if c['original spelling status'] == 'correct' and c[
    'OOV/IV'] == 'IV'])  # to calculate the recall

mld_status_corrected = sum(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result if c['Minimum Levenshtein Distance'] == 1])
original_dict['Minimum Levenshtein Distance'][
    'Precision for Minimum Levenshtein Distance on Entire Dataset'] = mld_status_corrected / len(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result])
original_dict['Minimum Levenshtein Distance'][
    'Precision for Minimum Levenshtein Distance on the Misspellings which are IV'] = sum(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
original_dict['Minimum Levenshtein Distance']['Recall for Minimum Levenshtein Distance on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
original_dict['Minimum Levenshtein Distance']['Recall for Minimum Levenshtein Distance on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

original_dict['Edit Distance No More Than 2']['Precision for Edit Distance No More Than 2 on Entire Dataset'] = sum(
    [c['Edit Distance No More Than 2'] for c in eval_distance_result]) / sum(
    [c['Edit Distance No More Than 2 Total'] for c in eval_distance_result])
original_dict['Edit Distance No More Than 2'][
    'Precision for Edit Distance No More Than 2 on the Misspellings which are IV'] = sum(
    [c['Edit Distance No More Than 2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['Edit Distance No More Than 2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['Edit Distance No More Than 2']['Recall for Edit Distance No More Than 2 on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 2'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
original_dict['Edit Distance No More Than 2']['Recall for Edit Distance No More Than 2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

original_dict['Edit Distance No More Than 1']['Precision for Edit Distance No More Than 1 on Entire Dataset'] = sum(
    [c['Edit Distance No More Than 1'] for c in eval_distance_result]) / sum(
    [c['Edit Distance No More Than 1 Total'] for c in eval_distance_result])
original_dict['Edit Distance No More Than 1'][
    'Precision for Edit Distance No More Than 1 on the Misspellings which are IV'] = sum(
    [c['Edit Distance No More Than 1'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['Edit Distance No More Than 1 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['Edit Distance No More Than 1']['Recall for Edit Distance No More Than 1 on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 1'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
original_dict['Edit Distance No More Than 1']['Recall for Edit Distance No More Than 1 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 1'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

original_dict['3-Gram with Jaccard Best Match']['Precision for 3-Gram with Jaccard Best Match on Entire Dataset'] = sum(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result]) / len(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result])
original_dict['3-Gram with Jaccard Best Match'][
    'Precision for 3-Gram with Jaccard Best Match on the Misspellings which are IV'] = sum(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result if
     c['3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
original_dict['3-Gram with Jaccard Best Match']['Recall for 3-Gram with Jaccard Best Match on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
original_dict['3-Gram with Jaccard Best Match'][
    'Recall for 3-Gram with Jaccard Best Match on Entire Dataset, IV'] = len([c for c in eval_distance_result if c[
    '3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct' and c[
                                                                                  'OOV/IV'] == 'IV']) / \
                                                                         ALL_CORRECT_SPELLING_IV

original_dict['2-Gram with Jaccard Best Match']['Precision for 2-Gram with Jaccard Best Match on Entire Dataset'] = sum(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result]) / len(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result])
original_dict['2-Gram with Jaccard Best Match'][
    'Precision for 2-Gram with Jaccard Best Match on the Misspellings which are IV'] = sum(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result if
     c['2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
original_dict['2-Gram with Jaccard Best Match']['Recall for 2-Gram with Jaccard Best Match on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
original_dict['2-Gram with Jaccard Best Match'][
    'Recall for 2-Gram with Jaccard Best Match on Entire Dataset, IV'] = len([c for c in eval_distance_result if c[
    '2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct' and c[
                                                                                  'OOV/IV'] == 'IV']) / \
                                                                         ALL_CORRECT_SPELLING_IV

original_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = sum(
    [c['3-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result]) / sum(
    [c['3-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result])
original_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 3-Gram Jaccard Distance No More Than 0.2 on the Misspellings which are IV'] = sum(
    [c['3-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['3-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = len([c for c in eval_distance_result if
                                                                                    c[
                                                                                        '3-Gram Jaccard Distance No '
                                                                                        'More Than 0.2'] == 1 and
                                                                                    c[
                                                                                        'original spelling status']
                                                                                    == 'correct']) / \
                                                                               ALL_CORRECT_SPELLING
original_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['3-Gram Jaccard Distance No More Than 0.2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

original_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = sum(
    [c['2-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result]) / sum(
    [c['2-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result])
original_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 2-Gram Jaccard Distance No More Than 0.2 on the Misspellings which are IV'] = sum(
    [c['2-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['2-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = len([c for c in eval_distance_result if
                                                                                    c[
                                                                                        '2-Gram Jaccard Distance No '
                                                                                        'More Than 0.2'] == 1 and
                                                                                    c[
                                                                                        'original spelling status']
                                                                                    == 'correct']) / \
                                                                               ALL_CORRECT_SPELLING
original_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['2-Gram Jaccard Distance No More Than 0.2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

original_dict['metaphone']['Precision for metaphone on Entire Dataset'] = sum(
    [c['metaphone'] for c in eval_soundex_result]) / sum([c['metaphone total'] for c in eval_soundex_result])
original_dict['metaphone']['Precision for metaphone on the Misspellings which are IV'] = sum(
    [c['metaphone'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['metaphone total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['metaphone']['Recall for metaphone on Entire Dataset'] = len([c for c in eval_soundex_result if
                                                                            c['metaphone'] == 1 and c[
                                                                                'original spelling status'] ==
                                                                            'correct']) / ALL_CORRECT_SPELLING_PH
original_dict['metaphone']['Recall for metaphone on Entire Dataset, IV'] = len([c for c in eval_soundex_result if
                                                                                c['metaphone'] == 1 and c[
                                                                                    'original spelling status'] ==
                                                                                'correct' and
                                                                                c[
                                                                                    'OOV/IV'] == 'IV']) / \
                                                                           ALL_CORRECT_SPELLING_IV_PH

original_dict['refined_soundex']['Precision for refined_soundex on Entire Dataset'] = sum(
    [c['refined_soundex'] for c in eval_soundex_result]) / sum(
    [c['refined_soundex total'] for c in eval_soundex_result])
original_dict['refined_soundex']['Precision for refined_soundex on the Misspellings which are IV'] = sum(
    [c['refined_soundex'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['refined_soundex total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['refined_soundex']['Recall for refined_soundex on Entire Dataset'] = len(
    [c for c in eval_soundex_result if
     c['refined_soundex'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING_PH
original_dict['refined_soundex']['Recall for refined_soundex on Entire Dataset, IV'] = len(
    [c for c in eval_soundex_result if c['refined_soundex'] == 1 and c['original spelling status'] == 'correct' and c[
        'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV_PH

original_dict['mra']['Precision for mra on Entire Dataset'] = sum([c['mra'] for c in eval_soundex_result]) / sum(
    [c['mra total'] for c in eval_soundex_result])
original_dict['mra']['Precision for mra on the Misspellings which are IV'] = sum(
    [c['mra'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['mra total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
original_dict['mra']['Recall for mra on Entire Dataset'] = len([c for c in eval_soundex_result if c['mra'] == 1 and c[
    'original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING_PH
original_dict['mra']['Recall for mra on Entire Dataset, IV'] = len([c for c in eval_soundex_result if
                                                                    c['mra'] == 1 and c[
                                                                        'original spelling status'] == 'correct' and c[
                                                                        'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV_PH

##############################
# Statistics for updated_dict#
##############################


ALL_IV_NEED_CORRECTION = len(
    [c for c in eval_distance_result if c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
ALL_CORRECT_SPELLING = len(
    [c for c in eval_distance_result if c['original spelling status'] == 'correct'])  # to calculate the recall
ALL_CORRECT_SPELLING_IV = len([c for c in eval_distance_result if c['original spelling status'] == 'correct' and c[
    'OOV/IV'] == 'IV'])  # to calculate the recall

ALL_IV_NEED_CORRECTION_PH = len(
    [c for c in eval_soundex_result if c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
ALL_CORRECT_SPELLING_PH = len(
    [c for c in eval_soundex_result if c['original spelling status'] == 'correct'])  # to calculate the recall
ALL_CORRECT_SPELLING_IV_PH = len([c for c in eval_soundex_result if c['original spelling status'] == 'correct' and c[
    'OOV/IV'] == 'IV'])  # to calculate the recall

mld_status_corrected = sum(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result if c['Minimum Levenshtein Distance'] == 1])
updated_dict['Minimum Levenshtein Distance'][
    'Precision for Minimum Levenshtein Distance on Entire Dataset'] = mld_status_corrected / len(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result])
updated_dict['Minimum Levenshtein Distance'][
    'Precision for Minimum Levenshtein Distance on the Misspellings which are IV'] = sum(
    [c['Minimum Levenshtein Distance'] for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
updated_dict['Minimum Levenshtein Distance']['Recall for Minimum Levenshtein Distance on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
updated_dict['Minimum Levenshtein Distance']['Recall for Minimum Levenshtein Distance on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Minimum Levenshtein Distance'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

updated_dict['Edit Distance No More Than 2']['Precision for Edit Distance No More Than 2 on Entire Dataset'] = sum(
    [c['Edit Distance No More Than 2'] for c in eval_distance_result]) / sum(
    [c['Edit Distance No More Than 2 Total'] for c in eval_distance_result])
updated_dict['Edit Distance No More Than 2'][
    'Precision for Edit Distance No More Than 2 on the Misspellings which are IV'] = sum(
    [c['Edit Distance No More Than 2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['Edit Distance No More Than 2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['Edit Distance No More Than 2']['Recall for Edit Distance No More Than 2 on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 2'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
updated_dict['Edit Distance No More Than 2']['Recall for Edit Distance No More Than 2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

updated_dict['Edit Distance No More Than 1']['Precision for Edit Distance No More Than 1 on Entire Dataset'] = sum(
    [c['Edit Distance No More Than 1'] for c in eval_distance_result]) / sum(
    [c['Edit Distance No More Than 1 Total'] for c in eval_distance_result])
updated_dict['Edit Distance No More Than 1'][
    'Precision for Edit Distance No More Than 1 on the Misspellings which are IV'] = sum(
    [c['Edit Distance No More Than 1'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['Edit Distance No More Than 1 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['Edit Distance No More Than 1']['Recall for Edit Distance No More Than 1 on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 1'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
updated_dict['Edit Distance No More Than 1']['Recall for Edit Distance No More Than 1 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['Edit Distance No More Than 1'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

updated_dict['3-Gram with Jaccard Best Match']['Precision for 3-Gram with Jaccard Best Match on Entire Dataset'] = sum(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result]) / len(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result])
updated_dict['3-Gram with Jaccard Best Match'][
    'Precision for 3-Gram with Jaccard Best Match on the Misspellings which are IV'] = sum(
    [c['3-Gram with Jaccard Best Match'] for c in eval_distance_result if
     c['3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
updated_dict['3-Gram with Jaccard Best Match']['Recall for 3-Gram with Jaccard Best Match on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
updated_dict['3-Gram with Jaccard Best Match'][
    'Recall for 3-Gram with Jaccard Best Match on Entire Dataset, IV'] = len([c for c in eval_distance_result if c[
    '3-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct' and c[
                                                                                  'OOV/IV'] == 'IV']) / \
                                                                         ALL_CORRECT_SPELLING_IV

updated_dict['2-Gram with Jaccard Best Match']['Precision for 2-Gram with Jaccard Best Match on Entire Dataset'] = sum(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result]) / len(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result])
updated_dict['2-Gram with Jaccard Best Match'][
    'Precision for 2-Gram with Jaccard Best Match on the Misspellings which are IV'] = sum(
    [c['2-Gram with Jaccard Best Match'] for c in eval_distance_result if
     c['2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'misspell' and c[
         'OOV/IV'] == 'IV']) / ALL_IV_NEED_CORRECTION
updated_dict['2-Gram with Jaccard Best Match']['Recall for 2-Gram with Jaccard Best Match on Entire Dataset'] = len(
    [c for c in eval_distance_result if
     c['2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING
updated_dict['2-Gram with Jaccard Best Match'][
    'Recall for 2-Gram with Jaccard Best Match on Entire Dataset, IV'] = len([c for c in eval_distance_result if c[
    '2-Gram with Jaccard Best Match'] == 1 and c['original spelling status'] == 'correct' and c[
                                                                                  'OOV/IV'] == 'IV']) / \
                                                                         ALL_CORRECT_SPELLING_IV

updated_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = sum(
    [c['3-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result]) / sum(
    [c['3-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result])
updated_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 3-Gram Jaccard Distance No More Than 0.2 on the Misspellings which are IV'] = sum(
    [c['3-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['3-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = len([c for c in eval_distance_result if
                                                                                    c[
                                                                                        '3-Gram Jaccard Distance No '
                                                                                        'More Than 0.2'] == 1 and
                                                                                    c[
                                                                                        'original spelling status']
                                                                                    == 'correct']) / \
                                                                               ALL_CORRECT_SPELLING
updated_dict['3-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 3-Gram Jaccard Distance No More Than 0.2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['3-Gram Jaccard Distance No More Than 0.2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

updated_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = sum(
    [c['2-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result]) / sum(
    [c['2-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result])
updated_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Precision for 2-Gram Jaccard Distance No More Than 0.2 on the Misspellings which are IV'] = sum(
    [c['2-Gram Jaccard Distance No More Than 0.2'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['2-Gram Jaccard Distance No More Than 0.2 Total'] for c in eval_distance_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset'] = len([c for c in eval_distance_result if
                                                                                    c[
                                                                                        '2-Gram Jaccard Distance No '
                                                                                        'More Than 0.2'] == 1 and
                                                                                    c[
                                                                                        'original spelling status']
                                                                                    == 'correct']) / \
                                                                               ALL_CORRECT_SPELLING
updated_dict['2-Gram Jaccard Distance No More Than 0.2'][
    'Recall for 2-Gram Jaccard Distance No More Than 0.2 on Entire Dataset, IV'] = len(
    [c for c in eval_distance_result if
     c['2-Gram Jaccard Distance No More Than 0.2'] == 1 and c['original spelling status'] == 'correct' and c[
         'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV

updated_dict['metaphone']['Precision for metaphone on Entire Dataset'] = sum(
    [c['metaphone'] for c in eval_soundex_result]) / sum([c['metaphone total'] for c in eval_soundex_result])
updated_dict['metaphone']['Precision for metaphone on the Misspellings which are IV'] = sum(
    [c['metaphone'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['metaphone total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['metaphone']['Recall for metaphone on Entire Dataset'] = len([c for c in eval_soundex_result if
                                                                           c['metaphone'] == 1 and c[
                                                                               'original spelling status'] ==
                                                                           'correct']) / ALL_CORRECT_SPELLING_PH
updated_dict['metaphone']['Recall for metaphone on Entire Dataset, IV'] = len([c for c in eval_soundex_result if
                                                                               c['metaphone'] == 1 and c[
                                                                                   'original spelling status'] ==
                                                                               'correct' and
                                                                               c[
                                                                                   'OOV/IV'] == 'IV']) / \
                                                                          ALL_CORRECT_SPELLING_IV_PH

updated_dict['refined_soundex']['Precision for refined_soundex on Entire Dataset'] = sum(
    [c['refined_soundex'] for c in eval_soundex_result]) / sum(
    [c['refined_soundex total'] for c in eval_soundex_result])
updated_dict['refined_soundex']['Precision for refined_soundex on the Misspellings which are IV'] = sum(
    [c['refined_soundex'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['refined_soundex total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['refined_soundex']['Recall for refined_soundex on Entire Dataset'] = len(
    [c for c in eval_soundex_result if
     c['refined_soundex'] == 1 and c['original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING_PH
updated_dict['refined_soundex']['Recall for refined_soundex on Entire Dataset, IV'] = len(
    [c for c in eval_soundex_result if c['refined_soundex'] == 1 and c['original spelling status'] == 'correct' and c[
        'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV_PH

updated_dict['mra']['Precision for mra on Entire Dataset'] = sum([c['mra'] for c in eval_soundex_result]) / sum(
    [c['mra total'] for c in eval_soundex_result])
updated_dict['mra']['Precision for mra on the Misspellings which are IV'] = sum(
    [c['mra'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV']) / sum(
    [c['mra total'] for c in eval_soundex_result if
     c['original spelling status'] == 'misspell' and c['OOV/IV'] == 'IV'])
updated_dict['mra']['Recall for mra on Entire Dataset'] = len([c for c in eval_soundex_result if c['mra'] == 1 and c[
    'original spelling status'] == 'correct']) / ALL_CORRECT_SPELLING_PH
updated_dict['mra']['Recall for mra on Entire Dataset, IV'] = len([c for c in eval_soundex_result if
                                                                   c['mra'] == 1 and c[
                                                                       'original spelling status'] == 'correct' and c[
                                                                       'OOV/IV'] == 'IV']) / ALL_CORRECT_SPELLING_IV_PH





print(original_dict, '\n')
print(updated_dict,'\n')
