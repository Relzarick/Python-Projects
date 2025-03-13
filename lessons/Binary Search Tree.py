class TreeNode:
    #* init is used to define vars for other methods to access within the class
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    #! helper methods
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        #* Smaller values goes to the left subtree, larger values to the right.
        #* node.key == current key||Key == child value
        if key < node.key:
            #* using := will overide because its not a treenode????
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
  
        return node
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        
        return self._search(node.right, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        #* Else block is if there are 2 children
        else:
            #! no idea what is going on here
            if node.left is None:
                return node.right 
            elif node.right is None:
                return node.left
            
            node.key = self._min_value(node.right) 
            node.right = self._delete(node.right, node.key)

        return node  
      

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        #* Replaces the node after it has been deleted
        return node.key


    #* result = list keys are appended to sorted
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


    #! user facing methods
    def insert(self, key):
        #? Encapsulation: ensures that the user interacts with a simple interface
        self.root = self._insert(self.root, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key) 

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    

nodes = [50, 30, 20, 40, 70, 60, 80]

bst = BinarySearchTree()

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))

print('Inorder traversal after deleting 40:', bst.inorder_traversal())