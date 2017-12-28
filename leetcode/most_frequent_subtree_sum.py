class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        sum_to_freq = {}

        def sum_tree(node):
            if not node:
                return 0

            left = sum_tree(node.left)
            right = sum_tree(node.right)
            total = node.val + left + right
            sum_to_freq[total] = sum_to_freq.get(total, 0) + 1
            return total

        sum_tree(root)
        max_freq = max(sum_to_freq.values())
        return [k for k, v in sum_to_freq.items() if v == max_freq]
