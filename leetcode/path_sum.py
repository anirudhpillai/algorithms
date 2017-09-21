# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        def helper(node, curr_sum):
            if not node:
                return False

            if not node.left and not node.right:
                return curr_sum + node.val == target

            return helper(node.left, curr_sum + node.val) or helper(node.right, curr_sum + node.val)

        return helper(root, 0)
