class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def rec(left, right):
            if left and right:
                if left.val == right.val:
                    return rec(left.left, right.right) and rec(left.right, right.left)

            if not left and not right:
                return True

            return False

        return rec(root.left, root.right)
