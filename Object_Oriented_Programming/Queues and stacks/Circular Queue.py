class Queue:

    def __init__(self, given_size):
        self.head = 0
        self.tail = 0
        self.size = given_size
        self.alist = []

        while len(self.alist) < given_size:
            self.alist.append("")

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.alist[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.alist[self.head]
        self.alist[self.head] = ""
        self.head = (self.head + 1) % self.size
        return item

    def print_queue(self):
        print(self.alist)


if __name__ == "__main__":
    testqueue = Queue(11)
    for i in range(10):
        testqueue.enqueue(i)
    testqueue.print_queue()
    print(testqueue.dequeue())
    print(testqueue.dequeue())
    print(testqueue.dequeue())
