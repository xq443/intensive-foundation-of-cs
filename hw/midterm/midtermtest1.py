def Q1(s):
    """ Returns True if the characters at the start and
end of s are the same and occur nowhere else in s
PreCondition: s is a string with length greater
than or equal to 3. """
    n = len(s)
    for i in range(len(s)):
        if(s[0] == s(len(s) - 1)):
            if(s.count[s[0]] == 1):
                return True
            else:
                return False
            
    
    
    
    n = len(s)
    t = s[1:n-1]
    if(s[0] == s[n-1]) and (t.count[s[0] == 0):
        return False
    elif(t.count(s[0]) >0):
        return False
    else:
        return True


    n = len(s)
    t = s[1:n-1]
    if(s[0] == s[n-1]) and (t.count[s[0] == 0):
        return True
 
