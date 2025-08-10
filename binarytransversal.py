# Define the structure of a binary tree node
class Node:
    def __init__(self, value):
        self.value = value            # The data value of the node
        self.left = None              # Pointer to the left child
        self.right = None             # Pointer to the right child

# DFS Traversal: Inorder (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# DFS Traversal: Preorder (Root, Left, Right)
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

# DFS Traversal: Postorder (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

# BFS Traversal (Level Order)
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])  # Start with the root node in the queue
    while queue:
        current = queue.popleft()
        print(current.value, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# A simple DFS (non-recursive) using a stack
def dfs_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value, end=' ')
        # Add right child first so left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

# Create a sample binary tree
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# Traversal Game Simulation
print("Inorder Traversal:")      # Expected: D B E A C F
inorder(root)

print("\nPreorder Traversal:")   # Expected: A B D E C F
preorder(root)

print("\nPostorder Traversal:")  # Expected: D E B F C A
postorder(root)

print("\nBFS Traversal:")        # Expected: A B C D E F
bfs(root)

print("\nDFS Iterative Traversal:")  # Expected (preorder style): A B D E C F
dfs_iterative(root)

