# Tree Data Structure Implementations

Simple Python implementations of three fundamental tree data structures: Binary Search Tree (BST), Red-Black Tree, and AVL Tree.

## Files

- `binary_search_tree.py`: Basic BST implementation (unbalanced)
- `red_black_tree.py`: Self-balancing BST using node coloring
- `avl_tree.py`: Self-balancing BST using height balance

## Usage

```python

from binary_search_tree import BinarySearchTree
from red_black_tree import RedBlackTree
from avl_tree import AVLTree

# Create tree
tree = BinarySearchTree()  # or RedBlackTree() or AVLTree()

# Basic operations
tree.insert(10)
tree.search(10)
tree.delete(10)
print(tree.inorder())
```

## Time Complexities

| Operation | BST (worst) | Red-Black | AVL      |
| --------- | ----------- | --------- | -------- |
| Search    | O(n)        | O(log n)  | O(log n) |
| Insert    | O(n)        | O(log n)  | O(log n) |
| Delete    | O(n)        | O(log n)  | O(log n) |

## Testing

Each file includes comprehensive tests. Run:

```python
python binary_search_tree.py
python red_black_tree.py
python avl_tree.py
```
