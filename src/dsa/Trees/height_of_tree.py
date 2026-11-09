class Node:
    def __init__(self,data , left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.left = Node(12)
# root.left.right.left.left = Node(25)
# root.left.right.left.left.right  = Node(30)
# root.left.right.left.left.right.left  = Node(50)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left.left = Node(8)

def height(root):
    if root == None:
        return 0
    if root.left is None and root.right is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height,right_height)+1

print(height(root))

