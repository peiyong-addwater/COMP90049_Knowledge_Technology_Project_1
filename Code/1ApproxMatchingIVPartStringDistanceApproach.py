import os
import json
from tqdm import tqdm
import utilsKTP1 as KTP1

N_GRAM = 2

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
iv_bar = tqdm(iv_data)
distance_matching_result = {}
for misspell in iv_bar:
    result = {}
    if misspell[-1] == True:
        result["original spelling status"] = "correct"
    else:
        result["original spelling status"] = "misspell"
    result["target"] = misspell[1]
    edit_distance = float("inf")
    jaccard_distance = float("inf")
    ngram_distance = float("inf")
    iv_bar.set_description("Finding match for %s" % misspell[0])
    for word in dict:
        edit_distance_word = KTP1.calculateStringDistance.editDistance(misspell[0], word)
        j_distance_word = KTP1.calculateStringDistance.jaccardDistance(misspell[0], word)
        ngram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(misspell[0], word, N_GRAM)
        if edit_distance_word < edit_distance:
            result["Levenshtein"] = word
            edit_distance = edit_distance_word
        if j_distance_word < jaccard_distance:
            result["Jaccard Distance"] = word
            jaccard_distance = j_distance_word
        if ngram_distance_word < ngram_distance:
            result["N-Gram with Jaccard"] = word
            ngram_distance = ngram_distance_word
    distance_matching_result[misspell[0]] = result

print("Saving results...")
with open(OUTPUT_DIR + "distance_matching_result.json", 'r') as fp:
    json.dump(distance_matching_result, fp)
