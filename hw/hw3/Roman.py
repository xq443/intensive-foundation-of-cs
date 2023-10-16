# Roman.py
# skeleton provided
# PUT YOUR NAME(S) AND ID(S) HERE
# PUT YOUR DATE OF COMPLETION HERE
""" A framework for checking Roman numeral strings and their
value."""


def AllCharsOK(R):
    pass


def AllFreqsOK(R):
    pass


def SingleOK(c,s,R):
    pass


def AllSinglesOK(R):
    """Returns True if and only if R is a single-legal string.

    PreC: R is a non-null string.
    """
    M_ok = SingleOK('M','DLXVI',R)
    D_ok = SingleOK('D','LXVI',R)
    C_ok = SingleOK('C','LVI',R)
    L_ok = SingleOK('L','VI',R)
    X_ok = SingleOK('X','V',R)
    return M_ok and D_ok and C_ok and L_ok and X_ok


def DoubleOK(s,R):
    pass


def AllDoublesOK(R):
    """Returns True if and only if R is a double-legal string.

    PreC: R is a non-null string.
    """
    C_ok = DoubleOK('CD',R) and DoubleOK('CM',R)
    X_ok = DoubleOK('XL',R) and DoubleOK('XC',R)
    I_ok = DoubleOK('IV',R) and DoubleOK('IX',R)
    return C_ok and X_ok and I_ok


def Value(R):
    pass

if __name__ == '__main__':
    R = input('Enter a Roman Numeral String (do not surround with quotes): ')
    print ('AllCharsOK(R)   is ',AllCharsOK(R))
    print ('AllFreqsOK(R)   is ',AllFreqsOK(R))
    print ('AllSinglesOK(R) is ',AllSinglesOK(R))
    print ('AllDoublesOK(R) is ',AllDoublesOK(R))
    OK = AllCharsOK(R) and AllFreqsOK(R) and AllSinglesOK(R) and AllDoublesOK(R)
    if OK:
       print ('Value = %1d' % Value(R))
    else:
      print ('Not a valid Roman numeral string.')
