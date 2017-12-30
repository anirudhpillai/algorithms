class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def helper(node):
            if not node:
                result.append("#")
            else:
                result.append(str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(i):
            if data[i] == " ":
                i += 1

            if i >= len(data) or data[i] == "#":
                return (None, i)

            j = i
            while i < len(data) and data[i] != " ":
                i += 1

            node = TreeNode(int(data[j:i]))
            left, i = helper(i+1)
            right, i = helper(i+1)
            node.left = left
            node.right = right
            return node, i

        return helper(0)[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
