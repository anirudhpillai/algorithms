class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = 0

        # depth is no of nodes on branch not the no of edges
        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            self.maximum = max(self.maximum, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.maximum
