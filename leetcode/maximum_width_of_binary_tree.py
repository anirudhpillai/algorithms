class Solution:
    def widthOfBinaryTree(self, root):
        """
        Basicall use level order traversal and use
        the 2*n and 2*n + 1 to index each node
        """
        level = [(root, 1)]
        width = 0

        while level:
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for node, val in level:
                if node.left:
                    next_level.append((node.left, val * 2))
                if node.right:
                    next_level.append((node.right, val * 2 + 1))
            level = next_level

        return width
