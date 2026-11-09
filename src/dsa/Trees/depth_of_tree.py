class Node:
    def __init__(self,data , left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = -1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(12)
root.left.right.left.left = Node(25)
root.left.right.left.left.right  = Node(30)
root.left.right.left.left.right.left  = Node(50)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

depth = 0

def measure_depth(root,depth):
    if root is None:
        return
    root.depth = depth
    measure_depth(root.left,depth+1)
    measure_depth(root.right ,depth+1)

measure_depth(root,depth=0)

