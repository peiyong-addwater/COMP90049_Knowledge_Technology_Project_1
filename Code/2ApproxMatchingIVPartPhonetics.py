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
OUTPUT_DIR = CWD + "/Code_Output/"
DATA = OUTPUT_DIR + "data_entries.json"
DICT = OUTPUT_DIR + "dict.json"
with open(DATA, 'r') as fp:
    data = json.load(fp)
with open(DICT, 'r') as fp:
    dict = json.load(fp)

iv_data = [c for c in data if c[2] == "IV"]
phonetics_matching_result = {}
soundexAlgorithmNames = ['metaphone', 'refined_soundex']
algoDict = {}
for c in soundexAlgorithmNames:
    algoDict[c] = KTP1.generatePhoneticRepresentations.PhoneticRepresentation(c)

def findMatchForASingleEntry(data_entry):
    result = {}
    result["misspell"] = data_entry[0]
    misspell = data_entry[0]
    print("Finding match for %s" % misspell)
    result["target"] = data_entry[1]
    if data_entry[-1] == True:
        result["original spelling status"] = "correct"
    else:
        result["original spelling status"] = "misspell"
    best_distances = {}
    soundexMaxOneEdit = {}
    soundexMaxTwoEdit = {}
    result["soundex best match"] = {}
    for c in soundexAlgorithmNames:
        best_distances[c] = float("inf")
        soundexMaxOneEdit[c] = []
        soundexMaxTwoEdit[c] = []
    for word in dict:
        word_distance = {}
        for c in soundexAlgorithmNames:
            word_distance[c] = algoDict[c].edit_distance(misspell, word)
            if word_distance[c] < best_distances[c]:
                best_distances[c] = word_distance[c]
                result["soundex best match"][c] = word
            if word_distance[c] <= 1:
                soundexMaxTwoEdit[c].append(word)
            if word_distance[c] <= 2:
                soundexMaxTwoEdit[c].append(word)
    result["soundex representation max 1 edit"] = soundexMaxOneEdit
    result["soundex representation max 2 edit"] = soundexMaxTwoEdit
    print("Match for %s found" % data_entry[0])
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
        p_t = str(datetime.timedelta(seconds=passed_time))
        # print(y)
        res.append(y)
        cnt += 1
        itr_time = str(datetime.timedelta(seconds=passed_time / cnt))
        est_remain_time = str(datetime.timedelta(seconds=(len(iv_data) - cnt) * (passed_time / cnt)))
        print('Running Time: %s, Progress %d/%d; Average Single Match Time %s; Estimate Time Remaining: '
              '%s.\r' % (p_t, cnt, len(iv_data), itr_time, est_remain_time))
    print("Saving results...")
    with open(OUTPUT_DIR + "soundex_matching_result.json", 'w') as fp:
        json.dump(res, fp, indent=4)
