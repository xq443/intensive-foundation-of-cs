def fib(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n -1) + fib(n -2)


if __name__ =='__main__':
    
    n = int(input("please enter an integer number: "))
    print(fib(n))
    
