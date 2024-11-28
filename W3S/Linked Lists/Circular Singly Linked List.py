class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")

## below to traverse over the list x times

# Traverse the circular linked list 5 times
currentNode = node1
startNode = node1
cycles = 0  # Count full cycles

print("Circular Linked List Traversal (5 cycles):")
while cycles < 5:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

    # Check if we completed a full cycle
    if currentNode == startNode:
        cycles += 1
        print(f"Cycle {cycles} completed")  # Indicate end of a cycle

print("...")
