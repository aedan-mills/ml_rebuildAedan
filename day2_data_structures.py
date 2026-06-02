
# Goals:
# - Stacks (DFS): Last in first out data structure. we all know of the pancake analogy, but try thinking of it as the best way to access the most recently learned information.
# - Queues (BFS): First in first out data structure. everyone has to wait in line for their turn, but again, this is an efficient way to access the oldest information quickly.
# -completed- Lists: ordered collection of items, can be accessed by index, and can contain duplicates
# -completed- Dictionaries: collection of key-value pairs, where each key is unique and maps to a value. This is a powerful data structure for storing and retrieving data based on keys, 
    # and it allows for fast lookups and efficient memory usage.
# -noteworthy- Classes are just variables assigned to a name, but they can also have functions (called methods) and attributes (variables that belong to the class). They are a way to 
    # create custom data structures that can hold both data and functionality, and they are a fundamental building block of object-oriented programming.




class Stack: # similar to c++ we still have classes and structs and we can use those to create data structures
    def __init__(self): # constructor, this is called when we create a new stack object, and it initializes the stack with an empty list to hold the elements
        self.stack = [] # the key here is that we are never explicitly calling this, but it is automatically called upon creation of a new stack object

    #class Model:     EXAMPLE OF HOW THIS WORKS IN A MACHINE LEARNING CONTEXT, THIS IS NOT A FULL MODEL, JUST AN EXAMPLE OF HOW TO USE CLASSES TO CREATE A MODEL
    #def __init__(self, learning_rate):
    #    self.lr = learning_rate
    #    self.weights = []

    def push(self, new_item):
        self.stack.append(new_item) # this is how we add an item to the stack, we use the append method of the list to add the new item to the end of the list, which is the top of the stack

    def pop(self):
        # if self.stack != NULL:  Apparently this is a c++ way to check if the stack is empty, but in python we can just check if the list is empty by checking its length or just using it as a boolean
        # if len(self.stack) > 0: option 1
        if self.stack: # this is a pythonic way to check if the stack is not empty, as an empty list is considered False in a boolean context, and a non-empty list is considered True
            return self.stack.pop() # this is how to remove an item from the stack, use the pop method of the list to remove the last item from the list, which is the top of the stack, and return it
        else:
            return None # if the stack is empty, we return None to indicate that there is nothing to pop

    def peek(self): # we sometimes want to look at the top item without removing it completely from the structure, this is what peek does, it allows us to see the top item without modifying the stack
        if self.stack: # again, we check if the stack is not empty
            return self.stack[-1] # we can use python's negative indexing to access the last item in the list, notice this is only doable because we are only looking at the top item, 
                # if we wanted to look at the second to last item, we could use self.stack[-2], and so on. this is a powerful feature of python lists that allows us to easily access items from the 
                # end of the list without having to calculate their index based on the length of the list
        else:
            return None # if the stack is empty, show there is nothing to peek at

    def empty(self):
        if len(self.stack) == 0: # this is one way to check if the stack is empty, we check if the length of the list is zero, if it is, then the stack is empty, and we return True, otherwise we return False
            return True
        else:
            return False
        # return len(self.stack) == 0 # this is a simple way to check if the stack is empty, we just check if the length of the list is zero, if it is, then the stack is empty, and we return True, otherwise we return False

    def size(self):
        return len(self.stack) # this is how to get the size of the stack, we just return the length of the list that is holding the elements of the stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, new_val):
        self.queue.append(new_val) # used a list, could also use a queue of dictionaries, but this is simpler for now, we can always optimize later if we need to    

    def dequeue(self):
        if(self.queue):
            return self.queue.pop(0) # as this is a first in first out, first item is at index 0, so we can use the pop method of the list to remove and return the first item in the list, which is the front of the queue
        else:
            return None # if empty, show that you cannot dequeue anything
        
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return None # same as above, if empty, show that there is nothing to peek at

def main ():    
    stack = Stack() # this is how we create a new stack object, we call the constructor of the Stack class, which initializes the stack with an empty list
    stack.push(100)
    stack.push("hello")
    stack.push(3.14)
    print("The top item is: ", stack.peek()) # this should print 3.14, as it is the last item we pushed onto the stack
    print("The size of the stack is: ", stack.size()) 

    queue = Queue() # this is how we create a new queue object, we call the constructor of the Queue class, which initializes the queue with an empty list
    queue.enqueue(-10)
    queue.enqueue("world")
    queue.enqueue(2.718)
    print("The front item is: ", queue.peek()) # this should print -10, as it is the first item we enqueued into the queue
    print("The size of the queue is: ", len(queue.queue)) # length of the list that holds the elements of the queue


if __name__ == "__main__":
    main()