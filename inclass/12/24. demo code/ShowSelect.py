# ShowSelect.py
""" Uses Selection Sort to illustrate how functions
with list parameters work."""

from random import randint as randi
def Select(x,i):
    """ Swaps the largest value in x[i:] with x[i]
    
    PreC: x is a list of integers and i is an in that
    satifies 0<=i<len(x)
    """
    n = len(x)
    imax = i
    max_x = x[i]
    for k in range(i+1,n):
        if x[k] > max_x:
            # Found a new max value
            imax=k
            max_x = x[k]
    # Swap x[i] with the max value
    temp = x[i]
    x[i] = x[imax]
    x[imax] = temp

def SelectionSort(a):
    """ Permutes the values in list a so that they
    range from smallest to largest.
    
    PreC: a is a nonempty list of numbers.
    """
    n = len(a)
    for k in range(n):
        Select(a,k)
        # a[0:(k+1)] is sorted
        print (a)
    
    
def randiList(L,R,n):
    """ Returns a length-n list of random integers
    selected from the interval [L,R].
    
    PreC: L, R, and n are ints with n>0 and L<R.
    """
    t = []
    for k in range(n):
        r = randi(L,R)
        t.append(r)
    return t
    
    
if __name__ == '__main__':
    # A small example
    a = randiList(100,999,8)
    print (a)
    SelectionSort(a)
    

    
