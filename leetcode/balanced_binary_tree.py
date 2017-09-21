# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def max_height(node):
            if not node:
                return 0

            left = max_height(node.left)
            right = max_height(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return max_height(root) != -1
