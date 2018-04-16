class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []

        temp = root
        while temp:
            stack.append(temp)
            temp = temp.left

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                temp = node.right
                while temp:
                    stack.append(temp)
                    temp = temp.left

        return result
