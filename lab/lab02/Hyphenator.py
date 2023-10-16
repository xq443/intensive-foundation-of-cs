# Hyphenator.py
# -*- coding: utf-8 -*-
""" Inputs a string and inserts hyphens.
If the string has even length, the hyphen splits
the first and second halves. Otherwise, a hyphen
is inserted on either side of the middle character.
"""

s = input('Enter a string:' )
n = len(s)

if n%2==0:
    # s has even length
    m = int(n/2)
    h = s[0:m] + '-' + s[m:]
    s2 = s[0]+ '-' + s[1:]

    
else:
    # s has odd length
    m = int(n/2)
    h = s[0:m]+'-'+s[m]+'-'+s[m+1:]
    s2 = s[0: n-1] +'-'+ s[n-1]
    
print s,h,s2

