import datetime
import json
import multiprocessing as mp
import os
import time

import utilsKTP1 as KTP1

"""
Approximate String Matching with String Distance Metrics
Running on a workstation with double Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz (total 32 threads) and 128 GiB memory
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





def findMatchForASingleEntry(data_entry):
    result = {}
    result["misspell"] = data_entry[0]
    result["target"] = data_entry[1]
    if data_entry[-1] == True:
        result["original spelling status"] = "correct"
    else:
        result["original spelling status"] = "misspell"
    result["OOV/IV"] = data_entry[2]
    edit_distance = float("inf")
    two_gram_distance = float("inf")
    three_gram_distance = float("inf")
    edit_2 = []  # words with maximum 2 edits
    edit_1 = []  # words with maximum 1 edits
    jaccard3_20 = []  # 3 gram with jaccard distance no greater than 0.20
    jaccard2_20 = []  # 2 gram with jaccard distance no greater than 0.20
    for word in dict:
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
        # compare for 2-gram with jaccard
        if two_gram_distance_word < two_gram_distance:
            result["2-Gram with Jaccard Best Match"] = word
            two_gram_distance = two_gram_distance_word
        if two_gram_distance_word <= 0.2:
            jaccard2_20.append(word)

    result["Edit Distance No More Than 2"] = edit_2
    result["Edit Distance No More Than 1"] = edit_1
    result["3-Gram Jaccard Distance No More Than 0.2"] = jaccard3_20
    result["2-Gram Jaccard Distance No More Than 0.2"] = jaccard2_20
    print("Match for %s found" % data_entry[0])
    return result


if __name__ == '__main__':
    pool = mp.Pool()
    res1 = []
    start_time = time.time()
    cnt = 0
    for y in pool.imap_unordered(findMatchForASingleEntry, data):
        now = time.time()
        passed_time = now - start_time
        p_t = str(datetime.timedelta(seconds=passed_time))
        print(y)
        res1.append(y)
        print("Number of results: ", len(res1))
        cnt += 1
        itr_time = str(datetime.timedelta(seconds=passed_time / cnt))
        est_remain_time = str(datetime.timedelta(seconds=(len(data) - cnt) * (passed_time / cnt)))
        print(
            '"1ApproxMatchingIVPartStringDistanceApproach.py" Running Time: %s, Progress %d/%d; Average Single Match '
            'Time %s; Estimate Time Remaining: '
              '%s.\r' % (p_t, cnt, len(data), itr_time, est_remain_time))
    print("Saving results...")
    with open(OUTPUT_DIR + "distance_matching_result.json", 'w') as fp1:
        json.dump(res1, fp1, indent=4)
