#!/usr/bin/env python

import re

STR = re.compile(r"\w+['/]\w+|\w+")

def get_word_counts(file):
    counts = {}
    with open(file, 'rt') as f:
        for f in f.readlines():
            words = re.findall(STR, f)
            for word in words:
                word = word.lower()
                counts.setdefault(word, 0)
                counts[word] += 1
    return counts

if __name__ == "__main__":
    file = 'test.txt'
    results = get_word_counts(file)
    for word,count in results.items():
        print(word,':',count)