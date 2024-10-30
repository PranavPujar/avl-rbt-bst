# PRANAV UMAKANT PUJAR 1001965075

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Tests
def test_bst():
    bst = BinarySearchTree()
    
    # insertion
    test_values = [50, 30, 70, 20, 40, 60, 80]
    for value in test_values:
        bst.insert(value)
    
    # inorder traversal
    assert bst.inorder() == sorted(test_values), "Inorder traversal should return sorted values"
    
    # search functionality testing
    assert bst.search(30).value == 30, "Search should find existing value"
    assert bst.search(100) is None, "Search should return None for non-existing value"
    
    # deletion
    bst.delete(30)
    assert 30 not in bst.inorder(), "Value should be deleted"
    assert bst.inorder() == sorted([50, 70, 20, 40, 60, 80]), "Tree should maintain BST property after deletion"
    
    # deletion of root
    bst.delete(50)
    assert 50 not in bst.inorder(), "Root should be deleted"
    assert bst.inorder() == sorted([70, 20, 40, 60, 80]), "Tree should maintain BST property after root deletion"

if __name__ == "__main__":
    test_bst()
    print("All BST tests passed!")