#!/usr/bin/env python3

import sys

# create a dictionary to store the word and its count
word_count = {}

for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into word and count
    word, count = line.split('\t', 1)
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
    
    # save the word and count in the dictionary
    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count
    
# sort the dictionary by value in descending order
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# clean the dictionary to only contain the top 10 words
word_count = word_count[:10]

# print the top 10 words
for word, count in word_count:
    print('%s\t%s' % (word, count))