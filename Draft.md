# COMP90049 Knowledge Technologies Project 1 Draft

## Part One: Data Preprocess

- Correct the incorrect words according to the given dictionary. Labelling them with 'OOV' or 'IV' accordingly
- If the misspelling is actually the same as the corrected one, label with true. If not, label with false
- Create data set with data entry [misspell, correctspell, OOV/IV, true/false] and store the dataset in the format of .json

## Part Two: Lexical Normalization on the IV Part of the Dataset

- Basic edit distance (<=2)
- Character level Jaccard Distance
- Character level n-gram (maybe n = 3)
- Soundex matching (soundex, metaphone(with character matching such as Jaccard), refined soundex, fuzzy soundex, match rating approach)
- A combination of those mentioned above.

## Part Three: Dealing with the OOV Part of the Dataset

