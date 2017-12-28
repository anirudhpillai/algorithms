class Solution:
    def postorderTraversal(self, root):
        """
        Using stack to handle exact reverse of postorder,
        which is up, right, left. Then we reverse it to get
        postorder.
        """
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return result[::-1]
