# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = 0

        def depth(node, curr_depth):
            if not node:
                return 0

            left = depth(node.left, 1)
            right = depth(node.right, 1)

            self.maximum = max(self.maximum, left + right)
            return curr_depth + max(left, right)

        depth(root, 0)
        return self.maximum
