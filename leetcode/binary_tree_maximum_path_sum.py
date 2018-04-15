class Solution:
    def maxPathSum(self, root):
        """
        Nice trick to update global var separately
        and return something unrelated
        """
        if not root:
            return 0

        global result
        result = -1e9

        def max_sum_with_node(node):
            global result

            if not node:
                return 0

            left = max(max_sum_with_node(node.left), 0)
            right = max(max_sum_with_node(node.right), 0)

            result = max(
                result,
                node.val + left + right
            )

            return node.val + max(left, right)

        max_sum_with_node(root)
        return result
