s = input('Enter a string that has length greater than or equal to 2: ')
t = s.replace(s[0],'x')
u = t.replace('x',s[0])

if(s == u):
    print (s,u)