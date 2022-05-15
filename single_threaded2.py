from functools import reduce
from os import listdir
from sys import argv
from collections import Counter
from time import time

start = time()
directory = argv[1]
files = listdir(directory)


def counter(file):
    f = open(f'{directory}/{file}', 'r')
    data = f.read()
    words = data.split('\n')
    f.close()
    return Counter(words)


def merge(d1, d2):
    d1.update(d2)
    return d1


file_words = map(counter, files)
print(dict(reduce(merge, file_words)))
print('Time elapsed:', time() - start, 'sec')
