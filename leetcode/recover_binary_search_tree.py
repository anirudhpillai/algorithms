# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        global one, two, prev
        one, two, prev= None, None, None

        def inorder(node):
            global one, two, prev
            if node:
                inorder(node.left)

                if not prev:
                    prev = node
                else:
                    if node.val < prev.val:
                        if not one:
                            one = prev
                        two = node
                    prev = node

                inorder(node.right)

        inorder(root)

        temp = one.val
        one.val = two.val
        two.val = temp
        return
