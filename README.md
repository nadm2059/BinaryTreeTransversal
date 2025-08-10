
# 🌳 Binary Tree Traversal in Python

This project demonstrates various **binary tree traversal algorithms** implemented in Python, including both **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** methods.

---

## ✨ Features
- **Binary Tree Node Structure** – Simple `Node` class with `value`, `left`, and `right`.
- **DFS Traversals**
  - 🟢 **Inorder** (Left → Root → Right)
  - 🔵 **Preorder** (Root → Left → Right)
  - 🟣 **Postorder** (Left → Right → Root)
  - 🟠 **Iterative DFS** using a stack
- **BFS Traversal** (Level Order) using a queue.

---

## 🛠 Code Structure

### 1️⃣ Node Class
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
````

### 2️⃣ Traversal Methods

#### 🟢 Inorder Traversal

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)
```

#### 🔵 Preorder Traversal

```python
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)
```

#### 🟣 Postorder Traversal

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')
```

#### 🟡 BFS Traversal

```python
from collections import deque
def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
```

#### 🟠 Iterative DFS

```python
def dfs_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value, end=' ')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
```

---

## 🌲 Example Tree

```diff
        A
       / \
      B   C
     / \   \
    D   E   F
```

---

## 📜 Sample Output

```diff
+ Inorder Traversal:
D B E A C F

+ Preorder Traversal:
A B D E C F

+ Postorder Traversal:
D E B F C A

+ BFS Traversal:
A B C D E F

+ DFS Iterative Traversal:
A B D E C F
```

---

## ▶ How to Run

```bash
python binary_tree.py
```

---

## 📦 Requirements

* Python 3.x
* No external dependencies (uses `collections` module).


---

**Author:** Nadhirah Michael-Ho
**License:** MIT



