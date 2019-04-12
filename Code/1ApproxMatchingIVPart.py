import os
import json
import utilsKTP1 as KTP1

ON_SERVER = True
if ON_SERVER:
    os.chdir("/home/peiyongw/Research/KT_Project1/COMP90049_Knowledge_Technology_Project_1")
CWD = os.getcwd()
print("Current working directory: ", CWD)
OUTPUT_DIR = CWD + "/Code_Output/"
