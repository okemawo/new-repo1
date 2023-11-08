#!/usr/bin/env python3

import sys

# create a dictionary to store the word and its count
word_count = {}

for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into words
    words = line.split()
    
    if len(words) > 0:
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    else:
        continue

# sort the dictionary by value in descending order
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# clean the dictionary to only contain the top 10 words
word_count = word_count[:10]

# print the top 10 words
for word, count in word_count:
    print('%s\t%s' % (word, count))