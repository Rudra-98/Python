class Node:
    def __init__(self,data , left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# inorder(root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# postorder(root)


preorder(root)

