import datetime
import json
import multiprocessing as mp
import os
import time

import tqdm
import utilsKTP1 as KTP1

"""
Approximate String Matching with String Distance between Phonetic Representation of Words
Running on a workstation with double Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz (total 32 threads) cpus and 128 GiB 
memory
Total time:  ; Average Single Match Time  
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


phonetics_matching_result = {}
soundexAlgorithmNames = ['metaphone', 'refined_soundex', 'mra']
algoDict = {}
for c in soundexAlgorithmNames:
    algoDict[c] = KTP1.generatePhoneticRepresentations.PhoneticRepresentation(c)

# Generate phonetic representation for the whole dictionary
phone_dict = {}
dict_bar = tqdm.tqdm(dict)
for word in dict_bar:
    phone_dict[word] = {}
    dict_bar.set_description("Generating Phonetic Representation for Dictionary Words")
    for c in soundexAlgorithmNames:
        phone_dict[word][c] = algoDict[c].phonetics(word)

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
    result["OOV/IV"] = data_entry[2]
    soundexMaxOneEdit = {}
    soundexMaxTwoEdit = {}
    result["same phonetic representation"] = {}
    for c in soundexAlgorithmNames:
        soundexMaxOneEdit[c] = []
        soundexMaxTwoEdit[c] = []
    for word in dict:
        word_distance = {}
        phone_entry = phone_dict[word]
        for c in soundexAlgorithmNames:
            phone_misspell = algoDict[c].phonetics(misspell)
            word_distance[c] = KTP1.calculateStringDistance.editDistance(phone_misspell, phone_entry[c])
            # algoDict[
            # c].edit_distance(misspell,
            # word)
            result["same phonetic representation"][c] = []  # list of words with the same phonetic representation
            if word_distance[c] == 0:
                result["same phonetic representation"][c].append(word)
            # if word_distance[c] <= 1:
            #    soundexMaxTwoEdit[c].append(word)
            # if word_distance[c] <= 2:
            #    soundexMaxTwoEdit[c].append(word)
    # result["soundex representation max 1 edit"] = soundexMaxOneEdit
    # result["soundex representation max 2 edit"] = soundexMaxTwoEdit
    print("Match for %s found" % data_entry[0])
    return result


if __name__ == '__main__':
    pool = mp.Pool()
    res = []
    start_time = time.time()
    # res = pool.map(findMatchForASingleEntry, iv_data)
    cnt = 0
    for y in pool.imap_unordered(findMatchForASingleEntry, data):
        now = time.time()
        passed_time = now - start_time
        p_t = str(datetime.timedelta(seconds=passed_time))
        print(y)
        res.append(y)
        print("Number of results: ", len(res))
        cnt += 1
        itr_time = str(datetime.timedelta(seconds=passed_time / cnt))
        est_remain_time = str(datetime.timedelta(seconds=(len(data) - cnt) * (passed_time / cnt)))
        print(
            '"2ApproxMatchingIVPartPhonetics.py" Running Time: %s, Progress %d/%d; Average Single Match Time %s; '
            'Estimate Time Remaining: '
              '%s.\r' % (p_t, cnt, len(data), itr_time, est_remain_time))
    print("Saving results...")
    with open(OUTPUT_DIR + "soundex_matching_result.json", 'w') as fp:
        json.dump(res, fp, indent=4)
