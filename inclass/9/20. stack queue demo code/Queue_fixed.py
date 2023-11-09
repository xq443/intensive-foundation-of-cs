# Queue_fixed.py
# The instructor
# April 2023

""" Implements the Queue ADT using a fixed sized list."""

class Queue:
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append("<EMPTY>")#initializing the data list with "<EMPTY>" tags

        self.end = 0 #Tracks the end of the queue; next empty spot
        self.start = 0 #Not needed any more sice front at index=0

    def enqueue(self, item):
        if self.end >= len(self.data): #check if queue is full
            print("Queue full!")
            return
        else:
            self.data[self.end] = item
            self.end = self.end + 1

    #After every dequeue, shift the remaining items one
    #position to left. Hence, front of queue is always at
    #index 0
    def dequeue(self):
        if self.start == self.end: #check if queue is empty
            print("Queue empty!")
            return
        else:
            #item at index 0 is the front of the queue
            item = self.data[0]
            self.end=self.end - 1 #Note, self.end points to the next empty spot
            for i in range(self.end):
                self.data[i] = self.data[i+1]
            self.data[self.end] = "<EMPTY>"
            return item

    def print_q(self): #helper function to help with debugging.
        for i in range(self.start, self.end): #print queue start to end
            print(self.data[i])
        print(self.data, "Start: ", self.start, ", End", self.end)
        


#main script below

my_queue = Queue(6)#create a new queue with size=6

#ask user what they want to do with the queue
while True:
    cmd = input("enq, deq, print_q, or exit?")
    if cmd == "enq":
        value = input("Enter the item to add: ")
        my_queue.enqueue(value)
    elif cmd == "deq":
        value = my_queue.dequeue()
        print("dequeue() rturned ", value)
        
    elif cmd == "print_q":
        my_queue.print_q()

    elif cmd=="exit":
        break
    else:
        #Invalid option
        print("Please try again!") 
