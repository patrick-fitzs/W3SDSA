


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Function to delete a node with a specific value from the BST
def delete(node, data):
    if not node:  # Base case: If the node is None, return None
        return None

    # Traverse the left subtree if the data to delete is smaller
    if data < node.data:
        node.left = delete(node.left, data)

    # Traverse the right subtree if the data to delete is larger
    elif data > node.data:
        node.right = delete(node.right, data)

    else:  # Found the node to delete
        # Case 1: Node with only a right child or no children
        if not node.left:
            temp = node.right  # Store the right child (if any)
            node = None  # Delete the current node
            return temp  # Return the right child

        # Case 2: Node with only a left child
        elif not node.right:
            temp = node.left  # Store the left child (if any)
            node = None  # Delete the current node
            return temp  # Return the left child

        # Case 3: Node with two children
        # Find the in-order successor (smallest value in the right subtree)
        temp = minValueNode(node.right)
        node.data = temp.data  # Replace current node's data with the in-order successor's data
        # Delete the in-order successor
        node.right = delete(node.right, temp.data)

    return node  # Return the updated node


    #      13
    #    /    \
    #   7      15
    #  / \    /  \
    # 3   8  14  19
    #            /
    #          18

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

inOrderTraversal(root)


# Call the delete function to remove the node with value 19
root = delete(root, 19)

        #           After :
        #     13
        #     / \
        #   7      15
        #  /  \    / \
        # 3  8    14 18
        #
        #
        #
print()
inOrderTraversal(root)



