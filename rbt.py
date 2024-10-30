# PRANAV UMAKANT PUJAR 1001965075

class Color:
    RED = True
    BLACK = False

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.RED
        
class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL
    
    def insert(self, value):
        node = Node(value)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
            
        self._fix_insert(node)
    
    def _fix_insert(self, k):
        while k.parent and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node == self.NIL or value == node.value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        z = self.search(value)
        if z != self.NIL:
            self._delete_node(z)
    
    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == Color.BLACK:
            self._fix_delete(x)
    
    def _fix_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                    
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK
    
    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node != self.NIL:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Tests
def test_rbt():
    rbt = RedBlackTree()
    
    # Test insertion
    test_values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for value in test_values:
        rbt.insert(value)
    
    # inorder traversal
    assert rbt.inorder() == sorted(test_values), "Inorder traversal should return sorted values"
    
    # search
    assert rbt.search(10).value == 10, "Search should find existing value"
    assert rbt.search(100) == rbt.NIL, "Search should return NIL for non-existing value"
    
    # deletion
    rbt.delete(11)
    assert 11 not in rbt.inorder(), "Value should be deleted"
    assert rbt.inorder() == sorted([7, 3, 18, 10, 22, 8, 26, 2, 6, 13]), "Tree should maintain order after deletion"
    
    # deletion of root
    original_root_value = rbt.root.value
    rbt.delete(original_root_value)
    assert original_root_value not in rbt.inorder(), "Root should be deleted"
    
    # Red-Black properties verification
    def verify_properties(node, blackHeight=-1):
        if node == rbt.NIL:
            return 1
        
        # Every node is either red or black
        assert hasattr(node, 'color'), "Node should have color property"
        
        # The root is black
        if node == rbt.root:
            assert node.color == Color.BLACK, "Root must be black"
        
        # Red nodes should have black children
        if node.color == Color.RED:
            assert node.left.color == Color.BLACK and node.right.color == Color.BLACK, \
                "Red node's children must be black"
        
        # Black height should be same for all paths
        leftHeight = verify_properties(node.left)
        rightHeight = verify_properties(node.right)
        assert leftHeight == rightHeight, "Black height must be same for all paths"
        
        return leftHeight + (1 if node.color == Color.BLACK else 0)
    
    verify_properties(rbt.root)

if __name__ == "__main__":
    test_rbt()
    print("All Red-Black Tree tests passed!")