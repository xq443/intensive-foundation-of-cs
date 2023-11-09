# ShowCertainLength.py
# The instructor
# 2023

""" Illustrates the function CertainLength
"""

from GetData import fileToStringList

def CertainLength(L,m):
    """ Returns the number of strings in L that have length m.
    
    PreC: L is a list of strings and m is a positive int
    """
    counter = 0 #track the number of strings that have length m
    for s in L:
        if len(s) == m:
            counter += 1
    return counter
   

if __name__ == '__main__':
    L = fileToStringList('EnglishWords.txt')
    #L = L[:5000]   # Shorten L for quicker runs
    print ('\nlen(L) = %1d \n' % len(L))
    
    print (' m  ShowCertainLength(L,m)')
    print ('----------------------------')
    for m in range(5,9):
        x = CertainLength(L,m)
        print ('%2d       %6d'% (m,x))
    

    
   
    
            

