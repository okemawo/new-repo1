#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    quality = line[92:93]
    year_month_day = line[15:23]
    if quality in ['0','1','4','5','9'] and temperature != 9999:
        print("%s\t%s" % (year_month_day, temperature))