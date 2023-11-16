#recursiveMatch.py

def recursiveMatch(l1, l2):
    """ returns the number of indexes where lists
    l1 has the same value as list l2
    
    Recursive implementation
    
    PreC: l1, l2 are lists of integers and have equal length.
    """
    #if either of these lists dont contain any elements, non recursive match available
    if len(l1) == 0 or len(l2) == 0:
        return 0
    #base case to analyse the if l1[0] l2[0] have the same value
    elif l1[0] == l2[0]:
        smaller = recursiveMatch(l1[1:], l2[1:])# shrink the cases in terms of comparing l1[1:] and l2[1:]
        return 1 + smaller #if l1[0] == l2[0], total will be 1 + the number of equal cases for index >= 1
    else:
        smaller = recursiveMatch(l1[1:], l2[1:])
        return smaller #if l1[0] != l2[0], total will be the number of equal cases for index >= 1
        
if __name__ == '__main__':

    #Sample lists for testing. Vary the contents, lengths of the
    #following lists to thoroughly test your code
    list1 = [4, 2, 1, 6]
    list2 = [4, 3, 7, 6]

    if len(list1) != len(list2):
        print("Both the lists should have the same number of elements!")
        exit(1)
    
    common_indx_vals = recursiveMatch(list1, list2)
    print("number of indexes where lst1 has the same value as lst2 = %d " %common_indx_vals)
