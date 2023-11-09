# Stack_built_in.py
# The instructor
# March 2023

""" Implements the Stack ADT using Python list data type."""

class Stack:
    def __init__(self, size, data):
        #self.data = list() #an empty list to store stack data
        self.size = size
        self.data = data
        

    def push(self, item):
        if len(self.data) >= self.size: #check if stack is full
            print("Stack full!")
            return
        else:
            self.data.append(item)

    def pop(self):
        if len(self.data) <=0: #check if stack is empty
            print("Stack empty!")
            return
        else:
            return self.data.pop()

    def print_stack(self): #helper function to help with debugging.
        for i in range(len(self.data) -1, -1, -1): #print stack top down
            print(self.data[i])
            
    def peek(self):

        if len(self.data) <=0: #check if stack is empty
            print("Stack empty!")
            return
        return self.data[len(self.data) -1]
            
            


#main script below

my_stack = Stack(6, list())#create a new stack with size=6

#ask user what they want to do with the stack
while True:
    cmd = input("push, pos, print_stack, peek or exit?")
    if cmd == "push":
        value = input("Enter the item to push on stack: ")
        my_stack.push(value)
    elif cmd == "pop":
        value = my_stack.pop()
        print("pop() rturned ", value)
        
    elif cmd == "print_stack":
        my_stack.print_stack()
    elif cmd=="exit":
        break
    elif cmd == "peek":
        value = my_stack.peek()
        print("peek() rturned ", value)
    else:
        #Invalid option
        print("Please try again!") 
