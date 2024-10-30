# PRANAV UMAKANT PUJAR 1001965075

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):

        if not node:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node  
        
        # Update height of current node
        self.update_height(node)
        

        balance = self.balance_factor(node)
        
        # Left-Left Case
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        # Right-Right Case
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        
        # Left-Right Case
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right-Left Case
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if not node:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:

            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        
        if not node:
            return None
        
        self.update_height(node)        

        balance = self.balance_factor(node)
        
        # Left Left Case
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        
        # Left Right Case
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Right Case
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        
        # Right Left Case
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
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
def test_avl():
    avl = AVLTree()
    
    #insertion and automatic balancing
    test_values = [10, 20, 30, 40, 50, 25]  # This would cause multiple rotations
    for value in test_values:
        avl.insert(value)
    
    # Verify balanced structure
    def verify_balance(node):
        if not node:
            return True
        
        balance = avl.balance_factor(node)
        if abs(balance) > 1:
            return False
        
        return verify_balance(node.left) and verify_balance(node.right)
    
    assert verify_balance(avl.root), "Tree should be balanced after insertions"
    
    # inorder traversal
    assert avl.inorder() == sorted(test_values), "Inorder traversal should return sorted values"
    
    # search function
    assert avl.search(30).value == 30, "Search should find existing value"
    assert avl.search(100) is None, "Search should return None for non-existing value"
    
    # deletion and rebalancing
    avl.delete(30)
    assert 30 not in avl.inorder(), "Value should be deleted"
    assert verify_balance(avl.root), "Tree should be balanced after deletion"
    
    # height property
    def verify_height(node):
        if not node:
            return True
        
        left_height = avl.height(node.left)
        right_height = avl.height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        if node.height != max(left_height, right_height) + 1:
            return False
        
        return verify_height(node.left) and verify_height(node.right)
    
    assert verify_height(avl.root), "Height property should be maintained"
    
    new_values = [15, 5, 35, 45, 8, 3]
    for value in new_values:
        avl.insert(value)
    
    for value in [20, 35, 15]:
        avl.delete(value)
    
    assert verify_balance(avl.root), "Tree should remain balanced after complex operations"
    assert verify_height(avl.root), "Height property should be maintained after complex operations"

if __name__ == "__main__":
    test_avl()
    print("All AVL Tree tests passed!")