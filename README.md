# COMP90049_Knowledge_Technology_Project_1

*Author: Peiyong Wang*  
*Student ID: 955986*

The file structure of this repository is shown as follows:

```xml
COMP90049_Knowledge_Technology_Project_1
│   README.md
│   LICENSE    
│   requirements.txt
|
└───Code
│   │   0DataPreprocess.py
│   │   1ApproxMatchingIVPartStringDistanceApproach.py
|   |		2ApproxMatchingIVPartPhonetics.py	
│   │   3DealingWithOOVsExpandDictionary.py
|   |   4ApproxMatchingEditDistanceOnNewDataEntry.py
|   |   5ApproxMatchingNewDataPhonetics.py
|   |
│   └───utilsKTP1
│       │   __init__.py
│       │   calculateStringDistance.py
│       │   exceptions.py
|       |   generatePhoneticRepresentations.py
|       |   phonetics.py
│   
└───Code_Output
│   |   data_entries.json
│   |   dict.json
|   |   distance_matching_result.json.zip
|   |   new_data_entries.json
|   |   distance_matching_new_data_result.json
|   |   distance_matching_result.json
|   |   new_dict.json
|   |   soundex_matching_result.json
|   |   result_evaluation.json
|   |   soundex_matching_result.json.zip
|   |   distance_matching_new_data_result.json.zip
|   |   soundex_matching_new_data_result.json.zip
|   |   soundex_matching_new_data_result.json
|
└───Data
│   |   google-10000-english-usa.txt
│   |   google-10000-english.txt
|   |   words.txt
|   |   dict.txt
|   |   correct.txt
|   |   misspell.txt
|
```
The Code folder contains the  scripts for this project. All the required packages are listed in the requirements.txt. Run the scripts in the Code folder of which filename start with a digit will get the output files in the Code_Output folder.
The Data folder contains the original data provided alongside with the project specifications as well as new data added by the author to complete the project. New data is obtained from https://github.com/first20hours/google-10000-english and https://github.com/dwyl/english-words.
Code/utilsKTP1/phonetics.py is modified from python package "PyPhonetics" (https://github.com/Lilykos/pyphonetics).