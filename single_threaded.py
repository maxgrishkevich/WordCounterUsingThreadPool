from os import listdir
from sys import argv
from collections import Counter
from time import time

start = time()
directory = argv[1]
words = []
for file in listdir(directory):
    f = open(f'{directory}/{file}', 'r')
    data = f.read()
    words.append(data.split('\n'))
    f.close()
words = sum(words, [])
c = dict(Counter(words))
# d = dict((x, words.count(x)) for x in set(words))
print(c)
print('Time elapsed:', time() - start, 'sec')
