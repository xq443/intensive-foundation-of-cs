# Roman.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Oct 28th, 2023
""" A framework for checking Roman numeral strings and their value."""

def AllCharsOK(R):
    """
    Check if a string is character-legal according to the given rules.

    Args:
        R (str): The input string to be checked.

    Returns:
        bool: True if the string is character-legal, False otherwise.
    """
    characters = ['M','D','C','L','X','V','I'] #initialze the good characters list
    counter = 0 #counter for calculate the good chars in R
    
    for ch in R: #set a for loop
        if ch in characters: #if char in R is good character, then increment counter by 1
            counter += 1 
            
    if(counter == len(R)): #check if the counter of good chars is equal to the length of R
        return True
    else:
        return False
            
            
def AllFreqsOK(R):
    """
    Check if a string is frequency-legal according to the given rules.

    Args:
        R (str): The input string to be checked.

    Returns:
        bool: True if the string is frequency-legal, False otherwise.
    """
    return (
        R.count('M') <= 3 and
        R.count('C') <= 3 and
        R.count('X') <= 3 and
        R.count('I') <= 3 and
        R.count('D') <= 1 and
        R.count('L') <= 1 and
        R.count('V') <= 1
    )

def SingleOK(c,s,R):
    """
    Returns True if c is not in R,
    OR, if c is in R and not preceded by any character in s.
    Otherwise, False is returned.

    PreC: c is a character, s is a nonempty string, R is a nonempty string,
    and c is not in s.
    """

    # If c is not in R, return True
    if c not in R:
        return True
  
    # Find the last occurrence of c in R
    last_occurrence = R.rfind(c)
    # Check if the character in s appears after the last occurrence of c
    for ch in s:
        if ch in R and R.find(ch) < last_occurrence:
            return False
    #if ch not in s, there is no need to check, return true directly
    return True

def AllSinglesOK(R):
    """
    Returns True if and only if R is a single-legal string.

    PreC: R is a non-null string.
    
    Returns: 
    bool: True if R is a single-legal string, False otherwise.
    
    """
    M_ok = SingleOK('M','DLXVI',R)
    D_ok = SingleOK('D','LXVI',R)
    C_ok = SingleOK('C','LVI',R)
    L_ok = SingleOK('L','VI',R)
    X_ok = SingleOK('X','V',R)
    return M_ok and D_ok and C_ok and L_ok and X_ok


def DoubleOK(s,R):
    """
    Returns True if s is not in R or if s occurs once in R
    and the first occurrence of s[0] is the first occurrence of s.
    Otherwise, the value False is returned.

    Args:
    s (str): A length-2 string.
    R (str): A non-empty string in which we want to check for the occurrence of s.

    Returns:
    bool: True if the conditions are met, False otherwise.
    """
    # Check if s is not in R
    if s not in R:
        return True
    # Check if s occurs once in R and the first occurrence of s[0] is the first occurrence of s
    if R.count(s) == 1 and R.find(s[0]) == R.find(s):
        return True
     # If none of the conditions are met, return False
    return False
    

def AllDoublesOK(R):
    """Returns True if and only if R is a double-legal string.

    PreC: R is a non-null string.
    """
    C_ok = DoubleOK('CD',R) and DoubleOK('CM',R)
    X_ok = DoubleOK('XL',R) and DoubleOK('XC',R)
    I_ok = DoubleOK('IV',R) and DoubleOK('IX',R)
    return C_ok and X_ok and I_ok


def Value(R):
    """
    Calculate the numerical value of a Roman numeral string without using a dictionary.

    Args:
    R (str): A Roman numeral string.

    Returns:
    int: The numerical value of the Roman numeral.

    Precondition:
    - R is a valid Roman numeral string (no validation is performed here).

    """

    def roman_char_value(char):  
        """
        This function assigns numerical values to Roman numeral characters.
        For example, 'M' is assigned a value of 1000, 'D' is assigned 500, and so on.

        Args:
            char: every character in Roman expression

        Returns:
            int: The numerical value of the Roman numeral.
        """
        if char == 'M':
            return 1000
        elif char == 'D':
            return 500
        elif char == 'C':
            return 100
        elif char == 'L':
            return 50
        elif char == 'X':
            return 10
        elif char == 'V':
            return 5
        elif char == 'I':
            return 1
        else:
            return 0 ## Return 0 for characters that are not valid Roman numerals.

    # Initialize the total value to 0
    current_value = 0
    
    # Iterate through the characters in the Roman numeral string 'R'
    for char in R:
        current_value += roman_char_value(char) ## Add the value of the current character to the total value
        
    if R.count('CM') > 0 or R.count('CD') > 0: # Check for subtractive notations (e.g., 'CM', 'CD') and adjust the total value if they occur
        current_value -= 100 * 2 # Subtract 200 because 'CM' or 'CD' means we need to subtract 100 twice
    
    if R.count('XC') > 0 or R.count('XL') > 0: # Check for other subtractive notations (e.g., 'XC', 'XL') and adjust the total value if they occur
        current_value -= 10 * 2 # Subtract 20 because 'XC' or 'XL' means we need to subtract 10 twice
        
    if R.count('IX') > 0 or R.count('IV') > 0: # Check for the last subtractive notations (e.g., 'IX', 'IV') and adjust the total value if they occur
        current_value -= 1 * 2  # Subtract 2 because 'IX' or 'IV' means we need to subtract 10 twice

    return current_value

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
