# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)

        traverse(root)

        return inorder[k-1]
