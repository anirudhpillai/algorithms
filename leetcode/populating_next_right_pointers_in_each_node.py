class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        level = [root]

        while level:
            for i, node in enumerate(level):
                if i == len(level) - 1:
                    continue
                node.next = level[i+1]

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level
