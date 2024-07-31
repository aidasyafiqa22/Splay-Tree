
#This Splay Tree Program is written by Aida Syafiqa
#Program is executing search - insertion - deletion - splaying operation functions

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
         
def newNode(key): 
    return Node(key) 
     
def rightRotate(x): 
    y = x.left 
    x.left = y.right 
    y.right = x
    return y
 
def leftRotate(x): 
    y = x.right 
    x.right = y.left 
    y.left = x
    return y
 
def splay(root, key): 
    # Base cases: root is None or key is present at root 
    if root == None or root.key == key: 
        return root 
    # If key lies in left subtree 
    if root.key > key: 
        # Key is not in tree, we are done 
        if root.left == None: 
            return root 
        # Zig-Zig (Left Left) 
        if root.left.key > key: 
            # First recursively bring the key as root of left-left 
            root.left.left = splay(root.left.left, key) 
            # Do first rotation for root, second rotation is done after else 
            root = rightRotate(root) 
        elif root.left.key < key: # Zig-Zag (Left Right) 
            # First recursively bring the key as root of left-right 
            root.left.right = splay(root.left.right, key) 
            # Do first rotation for root.left 
            if root.left.right != None: 
                root.left = leftRotate(root.left) 
        # Do second rotation for root 
        return root if root.left == None else rightRotate(root) 
                
    else: # If key lies in right subtree 
        # Key is not in tree, we are done 
        if root.right == None: 
            return root 
        # Zig-Zag (Right Left) 
        if root.right.key > key: 
            # Bring the key as root of right-left 
            root.right.left = splay(root.right.left, key) 
            # Do first rotation for root.right 
            if root.right.left != None: 
                root.right = rightRotate(root.right) 
        elif root.right.key < key: # Zag-Zag (Right Right) 
            # Bring the key as root of right-right and do first rotation 
            root.right.right = splay(root.right.right, key) 
            root = leftRotate(root) 
        # Do second rotation for root 
        return root if root.right == None else leftRotate(root) 
 
# Insert a new key in splay tree with given root 
def insert(root, key): 
    # Simple Case: If tree is empty 
    if (root == None): 
        return newNode(key) 
    root = splay(root, key) 
    # If key is already present, then return 
    if (root.key == key): 
        print("Item already exist in iventory")
        return root 
    # If key is not present, then insert this 
    # key into the tree 
    # If root's key is greater, make key as 
    # root of root's left subtree 
    if (root.key > key): 
        n = newNode(key) 
        n.right = root 
        n.left = root.left 
        root.left = None
        return n 
    else: 
        # If root's key is smaller, make key as 
        # root of root's right subtree 
        n = newNode(key) 
        n.left = root 
        n.right = root.right 
        root.right = None
        return n 
 
 
 def delete(self, p):
  self.splay(p)

#Store left and right trees with different variables
  left_subtree = SplayTree()
  left_subtree.root = self.root.left
  if left_subtree.root != None:
    left_subtree.root.parent = None
  right_subtree = SplayTree()
  right_subtree.root = self.root.right
  if right_subtree.root != None:
    right_subtree.root.parent = None

#Find maximum of left subtree and splay it to the root
  if left_subtree.root != None:
    m = left_subtree.maximum(left_subtree.root)
    left_subtree.splay(m)
    left_subtree.root.right = right_subtree.root
    self.root = left_subtree.root
            
#Make the right subtree the right child of the new root of left subtree
  else:
    self.root = right_subtree.root


 
 
# A utility function to print preorder 
# traversal of the tree. 
# The function also prints height of every 
# node 
def preOrder(root): 
    if (root != None): 
        print(root.key, end=' ') 
        preOrder(root.left) 
        preOrder(root.right) 
 
# Driver code
root = newNode(100)
root.left = newNode(50)
root.right = newNode(200)
root.left.left = newNode(40)
root.left.left.left = newNode(30)
root.left.left.left.left = newNode(20)
root = insert(root, 25)
print("Preorder traversal of the modified Splay tree is")
preOrder(root)
