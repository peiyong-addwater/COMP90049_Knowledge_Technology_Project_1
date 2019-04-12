import datetime
import json
import multiprocessing as mp
import os
import time

import utilsKTP1 as KTP1

"""
Approximate String Matching with String Distance Metrics
"""

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
distance_matching_result = {}


def findMatchForASingleEntry(data_entry):
    result = {}
    result["misspell"] = data_entry[0]
    result["target"] = data_entry[1]
    if data_entry[-1] == True:
        result["original spelling status"] = "correct"
    else:
        result["original spelling status"] = "misspell"
    edit_distance = float("inf")
    two_gram_distance = float("inf")
    three_gram_distance = float("inf")
    for word in dict:
        edit_2 = []  # words with maximum 2 edits
        edit_1 = []  # words with maximum 1 edits
        jaccard3_20 = []  # 3 gram with jaccard distance no greater than 0.20
        jaccard3_10 = []  # 3 gram with jaccard distance no greater than 0.10
        jaccard2_20 = []  # 2 gram with jaccard distance no greater than 0.20
        jaccard2_10 = []  # 2 gram with jaccard distance no greater than 0.10
        edit_distance_word = KTP1.calculateStringDistance.editDistance(data_entry[0], word)
        two_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(data_entry[0], word, 2)
        three_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(data_entry[0], word, 3)
        # compare for Levenshtein
        if edit_distance_word < edit_distance:
            result["Minimum Levenshtein Distance"] = word
            edit_distance = edit_distance_word
        if edit_distance_word <= 2:
            edit_2.append(word)
        if edit_distance_word <= 1:
            edit_1.append(word)
        # compare for 3-gram with jaccard
        if three_gram_distance_word < three_gram_distance:
            result["3-Gram with Jaccard Best Match"] = word
            three_gram_distance = three_gram_distance_word
        if three_gram_distance_word <= 0.2:
            jaccard3_20.append(word)
        if three_gram_distance_word <= 0.1:
            jaccard3_10.append(word)
        # compare for 2-gram with jaccard
        if two_gram_distance_word < two_gram_distance:
            result["2-Gram with Jaccard Best Match"] = word
            two_gram_distance = two_gram_distance_word
        if two_gram_distance_word <= 0.2:
            jaccard2_20.append(word)
        if two_gram_distance_word <= 0.1:
            jaccard2_10.append(word)
        result["Edit Distance No More Than 2"] = edit_2
        result["Edit Distance No More Than 1"] = edit_1
        result["3-Gram Jaccard Distance No More Than 0.2"] = jaccard3_20
        result["3-Gram Jaccard Distance No More Than 0.1"] = jaccard3_10
        result["2-Gram Jaccard Distance No More Than 0.2"] = jaccard2_20
        result["2-Gram Jaccard Distance No More Than 0.1"] = jaccard2_10
    # print("Match for %s found"%data_entry[0])
    return result


if __name__ == '__main__':
    pool = mp.Pool()
    res = []
    start_time = time.time()
    # res = pool.map(findMatchForASingleEntry, iv_data)
    cnt = 0
    for y in pool.imap_unordered(findMatchForASingleEntry, iv_data):
        now = time.time()
        passed_time = now - start_time
        # print(y)
        res.append(y)
        cnt += 1
        itr_time = passed_time / cnt
        est_remain_time = str(datetime.timedelta(seconds=len(iv_data) * itr_time))
        print('Progress %d/%d; Average Single Match Time %d seconds; Estimate Time Remaining: %s.\r' % (cnt,
                                                                                                        len(iv_data),
                                                                                                        itr_time,
                                                                                                        est_remain_time))
    print("Saving results...")
    with open(OUTPUT_DIR + "distance_matching_result.json", 'r') as fp:
        json.dump(res, fp, indent=4)
