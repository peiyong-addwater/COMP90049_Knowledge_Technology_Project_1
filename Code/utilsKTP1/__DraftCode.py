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
import multiprocessing as mp

data = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 4, 5, 64, 322, 9]


def job(x):
    r = []
    for c in data:
        x = x * c
        r.append(x)
    return r


pool = mp.Pool()


def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)


if __name__ == '__main__':
    multicore()
