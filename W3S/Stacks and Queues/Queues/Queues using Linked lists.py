class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        # Initialize an empty queue with front, rear, and length
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        # Add an element to the end of the queue
        new_node = Node(element)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
            self.length += 1
            return
        # Link the current rear node to the new node and update the rear
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        # Remove an element from the front of the queue
        if self.isEmpty():  # Check if the queue is empty
            return "Queue is empty"
        # Remove the front node and update the front pointer
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        return temp.data  # Return the dequeued data

    def peek(self):
        # Get the data from the front element without removing it
        if self.isEmpty():  # Check if the queue is empty
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        # Check if the queue is empty
        return self.length == 0

    def size(self):
        # Return the number of elements in the queue
        return self.length

    def printQueue(self):
        # Print all elements in the queue from front to rear
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Create a queue
myQueue = Queue()

# Add elements to the queue
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()  # Print the current queue

# Remove the front element and print it
print("Dequeue: ", myQueue.dequeue())

# Peek at the front element without removing it
print("Peek: ", myQueue.peek())

# Check if the queue is empty
print("isEmpty: ", myQueue.isEmpty())

# Print the size of the queue
print("Size: ", myQueue.size())
