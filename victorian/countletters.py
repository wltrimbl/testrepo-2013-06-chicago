#!/usr/bin/env python
'''This program opens a file, makes a histogram of the 
characters present, and prints a table of the characters
and their occurrence frequency.'''

fh = open("Waroftheworlds.txt")
worddict = {

for line in fh:
    for pos in range(0, len(line)-1):
        ch = line[pos]
        if ch in wordict.keys():
            worddict[ch] += 1
        else:
            worddict[ch] = 1

for leter, count in sorted(worddict.items(), key=lambda(x): x[1])  :
    print letter + "\t" + str(count)
