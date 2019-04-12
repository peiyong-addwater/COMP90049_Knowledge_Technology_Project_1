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
