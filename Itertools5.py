from itertools import groupby
s = raw_input()
for X, c in groupby(s, int):#i'm using int because i want to return an integer and not a string
    print (len(list(c)),X),