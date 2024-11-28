class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C') # adding to the back of the list
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue()) # removing first in queue

print("Peek: ", myQueue.peek()) # showing front of queue

print("isEmpty: ", myQueue.isEmpty()) # checking if the queue is empty

print("Size: ", myQueue.size()) # return the size of the queue