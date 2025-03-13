class TreeNode:
    #* init is used to define vars for other methods to access within the class
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(self.key)
    
class BinarySearchTree:

    def __init__(self):
        self.root = None

    #? helper method
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        #* Values smaller than node.key are placed in the left subtree
        #* Values greater than node.key are placed in the right subtree
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
        #* else if there are 2 children
        else:
            #! no idea what is going on here
            if node.left is None:
                return node.right 
            elif node.right is None:
                return node.left



    #? user facing method
    def insert(self, key):
        #* Encapsulation: ensures that the user interacts with a simple interface
        self.root = self._insert(self.root, key)
    
    def search(self, key):
        return self._search(self.root, key)
    

nodes = [50, 30, 20, 40, 70, 60, 80]

bst = BinarySearchTree()

for node in nodes:
    bst.insert(node)
