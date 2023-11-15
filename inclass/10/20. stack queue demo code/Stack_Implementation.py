# Stack_Implementation.py
# The instructor
# March 2023

""" Implements the Stack ADT using a fixed sized list."""

class Stack:
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append(0)#initializing the data list with all zeros

        self.end = 0 #Tracks the number of elements in the stack

    def push(self, item):
        if self.end >= len(self.data): #check if stack is full
            print("Stack full!")
            return
        else:
            self.data[self.end] = item
            self.end = self.end + 1

    def pop(self):
        if self.end <=0: #check if stack is empty
            print("Stack empty!")
            return
        else:
            self.end = self.end - 1
            return self.data[self.end]

    def print_stack(self): #helper function to help with debugging.
        for i in range(self.end -1, -1, -1): #print stack top down
            print(self.data[i])
        


#main script below

my_stack = Stack(6)#create a new stack with size=6

#ask user what they want to do with the stack
while True:
    cmd = input("push, pos, print_stack, or exit?")
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
    else:
        #Invalid option
        print("Please try again!") 
