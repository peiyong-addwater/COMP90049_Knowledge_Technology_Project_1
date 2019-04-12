import os
import json
import utilsKTP1 as KTP1
import multiprocessing as mp

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
    jaccard_distance = float("inf")
    two_gram_distance = float("inf")
    three_gram_distance = float("inf")
    print("finding match for: ", data_entry[0])
    for word in dict:
        print("Finding match for %s \n" % data_entry[0])
        edit_distance_word = KTP1.calculateStringDistance.editDistance(data_entry[0], word)
        j_distance_word = KTP1.calculateStringDistance.jaccardDistance(data_entry[0], word)
        two_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(data_entry[0], word, 2)
        three_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(data_entry[0], word, 3)
        # compare for Levenshtein
        if edit_distance_word < edit_distance:
            result["Levenshtein"] = word
            edit_distance = edit_distance_word
        # compare for jaccard
        if j_distance_word < jaccard_distance:
            result["Jaccard Distance"] = word
            jaccard_distance = j_distance_word
        # compare for 3-gram with jaccard
        if three_gram_distance_word < three_gram_distance:
            result["3-Gram with Jaccard"] = word
            three_gram_distance = three_gram_distance_word
        # compare for 2-gram with jaccard
        if two_gram_distance_word < two_gram_distance:
            result["2-Gram with Jaccard"] = word
            two_gram_distance = two_gram_distance_word
    return result


def multicore():
    pool = mp.Pool()
    res = pool.map(findMatchForASingleEntry, iv_data)
    return res


if __name__ == '__main__':
    res = multicore()
    print("Saving results...")
    with open(OUTPUT_DIR + "distance_matching_result.json", 'r') as fp:
        json.dump(res, fp)







'''
def getResults(iv):
    distance_matching_result = {}
    for misspell in iv:
        result = {}
        if misspell[-1] == True:
            result["original spelling status"] = "correct"
        else:
            result["original spelling status"] = "misspell"
        result["target"] = misspell[1]
        edit_distance = float("inf")
        jaccard_distance = float("inf")
        two_gram_distance = float("inf")
        three_gram_distance = float("inf")
        print("finding match for: ", misspell[0])
        for word in dict:
            edit_distance_word = KTP1.calculateStringDistance.editDistance(misspell[0], word)
            j_distance_word = KTP1.calculateStringDistance.jaccardDistance(misspell[0], word)
            two_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(misspell[0], word, 2)
            three_gram_distance_word = KTP1.calculateStringDistance.jaccardDistanceNGram(misspell[0], word, 3)
            # compare for Levenshtein
            if edit_distance_word < edit_distance:
                result["Levenshtein"] = word
                edit_distance = edit_distance_word
            # compare for jaccard
            if j_distance_word < jaccard_distance:
                result["Jaccard Distance"] = word
                jaccard_distance = j_distance_word
            # compare for 3-gram with jaccard
            if three_gram_distance_word < three_gram_distance:
                result["3-Gram with Jaccard"] = word
                three_gram_distance = three_gram_distance_word
            # compare for 2-gram with jaccard
            if two_gram_distance_word < two_gram_distance:
                result["2-Gram with Jaccard"] = word
                two_gram_distance = two_gram_distance_word
        distance_matching_result[misspell[0]] = result
        print(result)
    return distance_matching_result
'''
