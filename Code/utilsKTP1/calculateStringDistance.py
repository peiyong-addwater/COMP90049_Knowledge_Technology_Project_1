import nltk


# String edit distance (Levenshtein), see https://en.wikipedia.org/wiki/Levenshtein_distance
def editDistance(word1, word2):
    return nltk.edit_distance(word1, word2)


# Jaccard distance between two words. See https://en.wikipedia.org/wiki/Jaccard_index
def jaccardDistance(word1, word2):
    return nltk.jaccard_distance(set(word1), set(word2))


# Jaccard distance with n-gram
def jaccardDistanceNGram(word1, word2, n=3):
    w1_chars = nltk.ngrams(word1, n, pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol=' ')
    w2_chars = nltk.ngrams(word2, n, pad_left=True, pad_right=True, left_pad_symbol=' ', right_pad_symbol=' ')
    return nltk.jaccard_distance(set(w1_chars), set(w2_chars))
