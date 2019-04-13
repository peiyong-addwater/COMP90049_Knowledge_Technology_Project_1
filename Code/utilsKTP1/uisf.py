import re

import numba
from num2words import num2words

string = "0newr 180"


@numba.jit()
def wordPreprocess(word):
    charList = list(word)
    for i in range(len(charList)):
        if i == 0 and charList[i] == '0':
            charList[i] = 'o'
        elif charList[i] == '0' and (charList[i - 1] not in '123456789'):
            charList[i] = 'o'
    return "".join(charList)


string = wordPreprocess(string)
string = re.sub(r' ', "", string)
dp = re.compile(r"(\d+)")
m = dp.findall(string)
print(m)
for c in m:
    num = int(c)
    p = re.compile(re.escape(c))
    string = re.sub(p, num2words(num), string)
    string = re.sub(r'-', "", string)
    string = re.sub(r' ', "", string)
    string = re.sub(r',', "", string)
    print(string)
