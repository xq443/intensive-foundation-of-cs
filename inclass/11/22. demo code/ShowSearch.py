#ShowSearch.py
""" Includes implementations of linear and binary search
and an application script that checks them out on
a small example.
"""

def BinSearch(x,a):
    """ Returns an int k with the property that
    a[k]==x is True. If no such k exists, then
    -1 is returned.
    
    PreC: a is a nonempty list of ints that is sorted from smallest
    to largest. x is an int.
    """
    if x<a[0] or x>a[-1]:
        # x is outside the interval [a[0],a[-1]]
        return -1
    L = 0
    R = len(a)-1
    while R-L > 1:
        assert a[L]<=x<=a[R], 'x is not in interval [a[L],a[R]]'
        mid = int((L+R)/2)
        if x < a[mid]:
            R = mid
        else:
            L = mid
    assert a[L]<=x<=a[L+1], 'R does not equal L+1'
    if a[L]==x:
        return L
    elif a[L+1]==x:
        return L+1
    else:
        return -1
    
def LinSearch(x,a):
    """ Returns an int k with the property that
    a[k]==x is True. If no such k exists, then
    -1 is returned.
    
    For-loop implementation.
    
    PreC: a is a nonempty list of ints. x is an int.
    """
    for  k in range(len(a)):
        if a[k]==x:
            return k
    # if the loop runs to completion, then no element of a has the
    # same value as x.
    return -1

def LinSearchW(x,a):
    """ Returns an int k with the property that
    a[k]==x is True. If no such k exists, then
    -1 is returned.
    
    While-loop implementation.
    
    PreC: a is a nonempty list of ints. x is an int.
    """
    k=0
    while k<len(a) and x!=a[k]:
        k+=1
    if k<len(a):
        # The loop terminated because x==a[k] is true
        return k
    else:
        # No value element of a has the same value as x
        return -1

if __name__ == '__main__':
    """ Illustrates the use of several search algorithms
    applied to a small list problem."""
    
    a = [10,10,20,30,30,40,50,50]
    print (a)
    x = float(input('Enter x: '))
    iB = BinSearch(x,a)
    iL = LinSearch(x,a)
    iLW = LinSearchW(x,a)
    print (' BinSearch(x,a)  returns %1d' % iB)
    print (' LinSearch(x,a)  returns %1d' % iL)
    print ('LinSearchW(x,a)  returns %1d' % iLW)

