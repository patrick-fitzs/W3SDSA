## Steps of reversing linked list

class Stack:  # Defining the class called stack
    def __init__(numList):  # Function to initialise my node object
        numList.contents = []  # initialising an attribute contents which holds an empty array

    def push(list, value):
        # This is to add a value to the top of the stack
        list.contents.append(value)

    def top(list):
        if list.contents:  # If contents have something in do the following
            return list.contents[-1]  # The top of the stack
        else:
            return None

    def pop(list):
        if list.contents:
            return list.contents.pop()
        else:
            return None


# new_list = Stack()
# new_list.push(4)
# new_list.push(7)
# new_list.push(9)
# new_list.push(3)
# print(f"List after pushing numbers: {new_list.contents}")
# new_list.pop()
# print(f"List after pop: {new_list.contents}")
# print("\nBelow: Linked Lists\n")


class Node:
    def __init__(self, value):  # initialise  a node  with a value
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def add_front(ll, v):
        new_node = Node(v)
        new_node.next = ll.head
        ll.head = new_node

    def reverse(array):  # The head is the starting point of the list that we want to reverse

        prev = None  # Initialise the previous pointer to 'None' as this will now be our new tail of the reversed list
        current = array.head  # Start off with the head of the list

        while current:  # Loop through the list while at current

            # Temporarily store the next node
            next_node = current.next

            # Reverse the current nodes pointer
            current.next = prev

            # Move the previous and current pointers one step forward
            prev = current
            current=next_node

        # At the end prev will be pointing to the new head of the reversed list
        array.head = prev

    def display(array):  # Display the list
        current = array.head
        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

new_list = LinkedList()


new_list.add_front(4)
new_list.add_front(7)
new_list.add_front(3)
new_list.add_front(9)
print("List after adding values")
new_list.display()

print("List after reversing")
new_list.reverse()
new_list.display()