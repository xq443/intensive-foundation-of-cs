# ShowLists.py
""" Contains functions that can be used to get practice
with lists and functions that involve lists. """

def Add1(x,y):
    """ Returns a list of numbers whose elements
    are obtained by adding corresponding elements from
    the lists x and y.
    
    PreC: x and y are lists of numbers with len(x)==len(y)
    """
    z = []
    for k in range(len(x)):
        s = x[k]+y[k]
        z.append(s)
    return z
     
def Add2(x,y):
    """ PreC: x and y are lists of numbers with len(x)==len(y)"""
    for k in range(len(x)):
       x[k] = x[k]+y[k]
       
def Add3(x,y):
    """PreC: x and y are lists of numbers with len(x)==len(y)"""
    for k in range(len(x)):
       x[k] = x[k]+y[k]
    return x

def Mul(x,y):
    """Returns a list of numbers whose elements
    are obtained by multiplying corresponding elements from
    the lists x and y.

    PreC: x and y are lists of numbers with len(x)==len(y)"""
    pass
       
if __name__ == '__main__':
   
    # Example 1
    print ('\nExample 1:')
    a = [1,2,3]
    b = [10,20,30]
    c = Add1(a,b)
    print (a)
    print (b)
    print (c)
    
    # Example 2
    print ('\nExample 2:')
    a = [1,2,3]
    b = [10,20,30]
    b = Add1(a,b)
    print (a)
    print (b)
    
    # Example 3
    print ('\nExample 3:')
    a = [1,2,3]
    b = [10,20,30]
    Add2(a,b)
    print (a)
    print (b)
    
    # Example 4
    print ('\nExample 4:')
    a = [1,2,3]
    b = [10,20,30]
    c = Add2(a,b)
    print (a)
    print (b)
    print (c)
    
    # Example 5
    print ('\nExample 5:')
    a = [1,2,3]
    b = [10,20,30]
    b = Add2(a,b)
    print (a)
    print (b)
    
    # Example 6
    print ('\nExample 6:')
    a = [1,2,3]
    b = [10,20,30]
    c = Add3(a,b)
    print (a)
    print (b)
    print (c)
    
    # Example 7
    print ('\nExample 7:')
    a = [1,2,3]
    b = [10,20,30]
    a = Add3(a,b)
    print (a)
    print (b)
    
    #Example 8
    print ('\nExample 8: TODO')
    a = [1,2,3]
    b = [10,20,30]
    x = Mul(a,b)
    print(x)


    
        

    

