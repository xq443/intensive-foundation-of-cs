# OrderDates.py
# Xujia Qin
# Nov 30th 2023

""" Module illustrates how to sort a list of SimpleDates.
"""

from TheSimpleDateClass import *
from random import randint as randi


# Put the three getter functions 
def get_year(date):
    return date.y

def get_month(date):
    return date.m

def get_day(date):
    return date.d

def main():
    n = 5
    L = []
    for k in range(n):
        m = randi(1,12)
        d = randi(1,30)
        y = randi(1900,1999)
        dateString = str(m) +  '/' + str(d) + '/' + str(y)
        theDate = SimpleDate(dateString)
        print (theDate)
        L.append(theDate)

    print ('\nSort by year...\n')
    # Code to sort L based on year, and then print nicely (loop through L)
    L.sort(key=get_year)
    for date in L:
        print(date)


    print ('\nSort by month index...\n')
    # Code to sort L based on month index, and then print  nicely (loop through L)
    L.sort(key=get_month)
    for date in L:
        print(date)
        
    print ('\nSort by day...\n')
    # Code to sort L based on day, and then print nicely (loop through L)
    L.sort(key=get_day)
    for date in L:
        print(date)
        
if __name__ == '__main__':
    main()
