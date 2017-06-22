# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSameTree(self, a, b):
        if a and b and a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)

        if not a and not b:
            return True

        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
