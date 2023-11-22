# ShowSimpleDateClass.py

""" Module contains a script that illustrates
the use of the class SimpleDate. This class has
a class variable.
"""

from TheSimpleDateClass import *
from datetime import date

def Today():
    """ Returns a SimpleDate encoding of today's date.
    """
    d = date.today()
    x = d.timetuple()
    return SimpleDate(str(x[1])+'/' + str(x[2]) + '/' + str(x[0]))

 
    
if __name__ == '__main__':
    # Illustrates the methods in SimpleDate
    
    T = Today()
    print ('Today''s date is ',T,'.')
    
    USA = SimpleDate('7/4/1776')
    # The number of days since the founding of the USA...
    m = T - USA
    
    print ('USA Founding:',USA)
    s = 'There are %1d days from' % m
    print (s,USA,' to ',T,'.')
    
    Northeastern = SimpleDate('1/1/1898') #Approximate founding date
    print ('Northeastern Founding:',Northeastern)
    # The number of days since Northeastern's founding...
    m = T - Northeastern
    # The date m days from now...
    D = T + m
    
    s = 'There are %1d days from' % m
    print (s,Northeastern,' to ',T,'.')
    print ('Northeastern will be twice as old on',D, 'as it is today.')

    
  
