# pushing to stacks...
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self._contents = []

    def push(self, value):
        # Add a value to the top of the stack
        self._contents.append(value)

    def top(self):
        # Return the top item without removing it
        if self._contents:
            return self._contents[-1]
        else:
            return None  # Return None if the stack is empty

    def pop(self):
        # Remove and return the top item of the stack
        if self._contents:
            return self._contents.pop()
        else:
            return None  # Return None if the stack is empty

    def count(self):
        # Return the number of items in the stack
        return len(self._contents)


# Example usage:
s = Stack()
s.push(10)
s.push(20)


# print(s.count())  # Output: 2
# print(s.top())    # Output: 20
# print(s.pop())    # Output: 20
# print(s.count())  # Output: 1
# print(s.top())    # Output: 10

# Queue with stacks and dequeue
class Queue:
    def __init__(new_list):
        new_list.contents = []

    def enqueue(list, value):
        list.contents.append(value)

    def front(list):
        return list.contents[0] if list.contents else None

    def dequeue(list):
        return list.contents.pop(0) if list.contents else None

    def count(list):
        return len(list.contents)


new_list = Queue()
new_list.enqueue(10)
new_list.enqueue(20)
new_list.enqueue(30)


# print(new_list.contents)
#
# print(new_list.front())
# new_list.dequeue()
# print(new_list.contents)


# Circular Queue in lists

class CircularQueue:
    def __init__(list1, size):
        list1.size = size
        list1.array = [None] * size
        list1.front = 0
        list1.rear = 0
        list1.count = 0  # To keep tract of the number of elements

        def is_full(list1):
            return list1.count == list1.size

        def is_empty(list1):
            return list1.count == 0

        def enqueue(list1, element):  # Adding an element to the back of the queue.
            if list1.is_full():
                raise OverflowError("Queue is full")
            else:
                list1.array[list1.rear] = element  # This adds the element at the rear if the queue
                list1.rear = (list1.rear + 1) % list1.size  # This moves rear to the next position
                list1.count += 1  # increase the count.


#  Linked Lists

class Node:

    def __init__(node,v):
        node.value = v
        node.next = None

class LinkedList:
    def __init__(linked_list):  # This is parameter name for an instance, points to, not an actual instance
        linked_list.head = None
        linked_list.tail = None

    def add_front(ll, v):
        new_node = Node(v)
        new_node.next = ll.head
        ll.head = new_node

ll = LinkedList()
ll.add_front(30)


