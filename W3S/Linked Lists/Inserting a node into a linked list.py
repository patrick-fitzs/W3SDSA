class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printNodes(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for i in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list: ")
printNodes(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print(f"\nAfter node {newNode.data} is inserted at position 2:")
printNodes(node1)