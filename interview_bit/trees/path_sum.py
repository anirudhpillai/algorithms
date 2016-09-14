"""

Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given sum.

"""

def hasPathSum(node, s):
    if not node:
        return False
    if node.val == s and not node.left and not node.right:
        return True
    return hasPathSum(node.left, s - node.val) \
            or hasPathSum(node.right, s - node.val)
