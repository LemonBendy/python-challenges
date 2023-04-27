class Stack():
    def __init__(self, size): # size is the size of the stack, variable
        self.__sp = 0
        self.stacksize = size
        self.alist = [] # list to hold the stack
        while len(self.alist) < self.stacksize: # fill the list with spaces
            self.alist.append(" ") # " " is the default value for the stack


    def get_sp(self):
        return self.__sp

    def is_empty(self):
        return get_sp() == 0

    def is_full(self):
        return get_sp() == self.stacksize

    def push(self, item):
        if self.is_full(): # check if the stack is full
            raise Exception("STACK IS FULL")
        else:
            self.alist[sp()] = item # add the item to the stack
            self.__sp += 1 # increment the stack pointer

    def pop(self):
        if self.is_empty(): # check if the stack is empty
            raise Exception("STACK IS EMPTY")
        else:
            self.__sp -= 1 # decrement the stack pointer
            item = self.alist[self.sp] # get the item from the stack
            self.alist[self.sp] = " " # set the item to the default value
            return item

if __name__ == "__main__":
    teststack = Stack(10)
    for i in range(10):
        teststack.push(i+1)
    print(teststack.alist)
    print(teststack.pop())
    print(teststack.alist)

