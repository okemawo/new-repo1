#!/usr/bin/env python3

import sys

current_date = None
max_temp = None

for line in sys.stdin:
    line = line.strip()
    date, temp = line.split('\t', 1)
    temp = int(temp)

    if current_date == date:
        max_temp = max(max_temp, temp)
    else:
        if current_date:
            print('%s\t%s' % (current_date, max_temp))
        current_date = date
        max_temp = temp

if current_date == date:
    print('%s\t%s' % (current_date, max_temp))