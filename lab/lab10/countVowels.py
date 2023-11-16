#countVowels.py


def countVowels(s):
    """ Returns the number of vowels in input s
    
    Recursive implementation
    
    PreC: s is a string.
    """
    #base case: consider s[0] (if it is a vowel or not)
    if len(s) == 0:
        return 0
    elif s[0] in 'AEIOUaeiou':
        smaller = s[1:] #shrink smaller cases as s[1:]
        return 1 + countVowels(smaller) #if s[0] is vowel, total is 1 + number of vowel of s[1:]
    else: #when s[0] not in 'AEIOUaeiou':
        smaller = s[1:] #if s[0] is not vowel, total is number of vowel of s[1:]
        return countVowels(smaller)
        
if __name__ == '__main__':

    inp_s = input("Enter a string: ")
    num_vowels = countVowels(inp_s)
    print("Number of vowels in the entered string = %d " %num_vowels)
    

