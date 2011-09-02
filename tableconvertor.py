#!/usr/bin/env python
import sys
from csv import reader

infile = open(sys.argv[1], 'U')
outfile = open(sys.argv[1][:-4] + '-out.csv', 'w')
csvreader = reader(infile, delimiter=';')

lines = []
lines = [line for line in csvreader]

records = []
record = []
for i, line in enumerate(lines):
    line = map(lambda s: s.strip(), line)
    line = filter(None, line)
    if not line:
        if record:
            records.append(record)
            record = []
    else:
        record.append(line)

for record in records:
    first = record[0][0]

    if len(record[0]) > 1:
        second = record[0][1]
    else:
        second = ''
    if len(record) > 1:
        third = record[-1][0]
        fourth = ''
        for item in record[1:-1]:
            if fourth:
                fourth += '\n'
            fourth += item[0]
    else:
        third = ''
        fourth = ''
    text = first + ';' + second + ';' + third + ';' + '"' + fourth + '"'
    #text = text.decode('utf8').encode('cp1251')
    print >> outfile, text
