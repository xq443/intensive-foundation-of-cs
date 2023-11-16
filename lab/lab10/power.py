#power.py


""" Compares a recursive and nonrecursive implemenatation of
the factorial function.
"""

def power(base, exp):
    """ Returns an int equal to  base**exp
    
    Recursive implementation
    
    PreC: base, exp are nonnegative ints.
    """
    #base case when base^0 = 1
    if exp == 0:
        return 1
    else:
        #shrink to smaller cases that base^(exp-1)
        smaller = power(base, exp -1)
        return base * smaller

if __name__ == '__main__':
    base = int(input("Enter the base (enter a positive int): "))
    exp = int(input("Enter the exponent (enter a positive int): "))

    if base < 0 or exp < 0:
        print("Base and exponent should be positive integers!")
        exit(0)

    ans =  power(base, exp)
    print ('%d**%d = %d' % (base, exp, ans))

  
    

