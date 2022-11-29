# declaring empty list, and intialising stackPointer.
names = ["", "", "", "", "", "", "", "", "", "", ""]
stackPointer = 0
maxLength = len(names)


# the above are global

def push(element):
    # some of the code is written for you
    global stackPointer
    global maxLength
    global names


# write code to check push an element (passed as parameter) at the stackPoonter


def pop():
    # some of th ecode is written for you
    global stackPointer
    global maxLength
    global names


# write a code to pop the element at stackPointer


def isempty():
    global stackPointer
    global maxLength
    global names

    # write code to check if stack is empty, if so return True
    # otherwise return False


def full():
    global stackPointer
    global maxLength
    global names

    # write code to check if stack is full,
    # if so return True otherwise return False

# ----------------- main program -----------
# write code to test the stack:
# push as many elements as you can until the stack get fulled
# pop elements until the stack get empty
# try to pop when the stack is empty
# try to push element when stack is full
# compare with how stack should work
# save your work
