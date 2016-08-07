# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isBalanced(node):
    if not node:
        return True

    lh = height(node.left)
    rh = height(node.right)

    if abs(lh - rh) <= 1 and isBalanced(node.left) and isBalanced(node.right):
        return True

    return False

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
