# CloseWords.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: 27th Nov, 2023

""" Illustrates various ideas about what it means
for two strings to be close.
"""
import string # gives us ascii_lowercase
from GetData import fileToStringList

def offByOne(s1, s2):
    """
    Check if two strings are off-by-one.

    Args:
    s1 (str): First input string
    s2 (str): Second input string

    Returns:
    bool: True if the strings are off-by-one, False otherwise
    """
    # Check if the strings have different lengths
    if len(s1) != len(s2):
        return False
    
    # Initialize a counter for differences
    counter = 0
    # Iterate through each character in the strings
    for i in range(len(s1)):
        # If characters at the same position are different, increment the counter
        if s1[i] != s2[i]:
            counter += 1

    # Check if exactly one difference is found
    return counter == 1


def offBySwap(s1, s2):
    """
    Check if two strings are off-by-one by swapping an adjacent pair of characters.

    Args:
    s1 (str): First input string
    s2 (str): Second input string

    Returns:
    bool: True if the strings are off-by-one by swapping, False otherwise
    """

    # Check if the strings have different lengths or are identical
    if len(s1) != len(s2) or s1 == s2:
        return False
    
    # Initialize a counter for valid adjacent swaps
    swap_count = 0
    leftCheck, rightCheck = -1, -1  # Initialize indices for checking equality

    # Iterate through the characters in the strings
    for i in range(len(s1) - 1):
        # Check if the adjacent characters in s1 and s2 can be swapped to make s2
        if s1[i] != s2[i] and s1[i+1] != s2[i+1] and s1[i] == s2[i+1] and s2[i] == s1[i+1]:
            swap_count += 1
            leftCheck = i  #left check is to mark the left adjacent index of the swapping point i to check if the left part is equal
            rightCheck = i + 2  #right check is to mark the right adjacent index of the swapping point i+1 to check if the right part is equal
        
    # Check if exactly one valid adjacent swap is found
    return swap_count == 1 and checkEqual(s1, s2, rightCheck, len(s1)) and checkEqual(s1, s2, 0, leftCheck) #checks if the string within the starting and ending indices are equal. 

def checkEqual(s1, s2, start, end):
    """
    This is the helper function of offBySwap(s1, s2) to check if the characters in specified sections of two strings are equal.

    Args:
    s1 (str): First input string
    s2 (str): Second input string
    start (int): Starting index for comparison
    end (int): Ending index (exclusive) for comparison

    Returns:
    bool: True if characters in the specified sections of the strings are equal, False otherwise
    """

    # Iterate through the specified section of characters in the strings
    for i in range(start, end):
        # Check if characters at each index are not equal
        if s1[i] != s2[i]:
            return False
    # If no differing characters found, return True indicating equality
    return True


def offByExtra(s1, s2):
    """
    Check if two strings are off-by-extra by removing one character from one string to obtain the other.

    Args:
    s1 (str): First input string
    s2 (str): Second input string

    Returns:
    bool: True if the strings are off-by-extra, False otherwise
    """
    # Generate lists of strings obtained by deleting one character from s1 and s2
    delete_ones_s1 = ListOfDeleteOnes(s1)
    delete_ones_s2 = ListOfDeleteOnes(s2)
    
    # Check if s2 is in the list generated from s1, or if s1 is in the list generated from s2
    return s2 in delete_ones_s1 or s1 in delete_ones_s2

def ListOfDeleteOnes(s):
    """
    Generate a list of strings obtained by deleting one character from the input string.

    Args:
    s (str): Input string

    Returns:
    list: List of strings resulting from deleting one character from the input string
    """
    delete_ones = []#create an empty list to house the list that deletes one char from string

    # Iterate through each index of the input string
    for i in range(len(s)):
        # Create a new string by excluding the character at index i
        modified_string = s[:i] + s[i+1:]
        delete_ones.append(modified_string)  # Add the modified string to the list
    
    return delete_ones


def ListOfNeighbors(s, L):
    """
    Returns a list of all entries in L that are neighbors of string s.

    Args:
    s (str): Input string
    L (list): List of nonempty strings

    Returns:
    list: List of entries in L that are neighbors of s
    """
    neighbors = [] #create an empty list to house the neighnors

    # Iterate through each string in L
    for string in L:
        # Check if the string is not the same as s and is a neighbor of s
        if string != s and (offByOne(s, string) or offByExtra(s, string) or offBySwap(s, string)):
            neighbors.append(string)  # Add the string to neighbors list
    
    return neighbors


def ListOfNeighbors2(s, L):
    """
    Returns a sorted list of all entries in L that are neighbors of neighbors of s without duplicates.

    Args:
    s (str): Input string
    L (list): List of nonempty strings

    Returns:
    list: Sorted list of entries in L that are neighbors of neighbors of s without duplicates
    """
    neighbors_of_neighbors = [] # Set to store unique neighbors of neighbors
    
    # Find neighbors of s using ListOfNeighbors function
    neighbors_s = ListOfNeighbors(s, L)

    # Find neighbors of neighbors of s
    for neighbor in neighbors_s:
        # Find neighbors of each neighbor of s using ListOfNeighbors function
        neighbors_of_neighbor = ListOfNeighbors(neighbor, L)
        for n in neighbors_of_neighbor:
            # Add neighbors of neighbors to the list
            neighbors_of_neighbors.append(n)
    
    return sorted(set(neighbors_of_neighbors)) # Return sorted list（type cast from  set) of unique neighbors of neighbors
    

def ScrabbleScore(s):
    """ Returns the Scrabble value of the uppercase version of s.

    PreC: s is a nonempty string comprised of letters
    (of any, or mixed, case).
    """
    Letters = string.ascii_uppercase
    # Letter distribution and values for each letter in the game of Scrabble
    Supply = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
    Value = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    s = s.upper()  # Convert input string to uppercase
    scrabbleScore = 0  # Initialize the total score as 0

    # Iterate through each letter in the input string
    for letter in s:
        i = Letters.find(letter)
        # Check if the count of a letter in the input string is greater than available supply
        if s.count(letter) > Supply[i]:
            return 0  # Return 0 if the word uses more tiles than available

        scrabbleScore += Value[i]  # Add the value of the letter to the total score

    return scrabbleScore  # Return the total Scrabble score of the input string

def testem():
    """Skeleton of code you can use to test your functions.
    Use of this (kind of) function is optional."""
    
    for answer in [["abcd", "abcd", False],
                    ["abcd", "bacd", True],
                    ["abcd", "abdc", True],
                    ["abcdef", "abcdfe", True]
                   ]:
        response = offBySwap(answer[0], answer[1])
        right = answer[2]
        if response != right:
            print ("problem with", answer)
    L = fileToStringList('EnglishWords.txt')
    print(ListOfNeighbors("largest", L))
    print(ListOfNeighbors2("largest", L))
    print ("done testing off-by-one")

def main():
    """Showcases the code in this module."""
    # Read in the list of English words ...
    L = fileToStringList('EnglishWords.txt')

    # Until the user complies, keep prompting for a string of lowercase letters.
    while True:
        s = input('Enter a nonempty string of lowercase letters: ')
        if all(char in string.ascii_lowercase for char in s): # Check if the input string is entirely composed of lowercase letters
            break #The while loop body should break as soon as the string s is made up entirely of lowercase letters;
        
        # Print all the neighbors of s and their Scrabble scores...
        print ('\nNeighbors...\n')
        for neighbor in ListOfNeighbors(s, L): # ListOfNeighbors(s, L) retrieves neighbors of the input string 's'
            score = ScrabbleScore(neighbor) # For each neighbor, it prints the neighbor's string and its corresponding Scrabble score.
            print(neighbor, score) #For each neighbor, it prints the neighbor's string and its corresponding Scrabble score.
        
        # Print all the neighbors of the neighbors of s and their Scrabble scores...
        print ('\nNeighbors of the Neighbors...\n')
        for neighbor_of_neighbor in ListOfNeighbors2(s, L): #ListOfNeighbors2(s, L) retrieves neighbors of neighbors of the input string 's'
            score = ScrabbleScore(neighbor_of_neighbor) # iterates through each neighbor to calculate and print its Scrabble score.
            print(neighbor_of_neighbor, score) #For each neighbor of the neighbor, it prints the string and its corresponding Scrabble score.
    
if __name__ == '__main__':
    main() # Call to the main function


