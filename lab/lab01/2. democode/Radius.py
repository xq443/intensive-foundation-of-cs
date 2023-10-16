
""" Read in the area of a circle and displays its radius.
"""
from math import sqrt,pi
A = input('Enter the circle area: ')
r = sqrt(float(A)/pi)
C = 2* pi * r
print ('The radius is '+str(round(r,3)))
print('The circum is ' + str(round(C,3)))


