# -*- coding: utf-8 -*-
"""Computes the area of
a circle and prints out the radius"""
from math import sqrt,pi
A = input("Please type in the area of the circle: ")
r = sqrt(float(A)/pi)
print('The radius of the circle is ' + str(round(r,3)))

         
