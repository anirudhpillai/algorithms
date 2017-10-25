# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def create_trees(start, end):
            if start > end:
                return [None]

            if start == end:
                return [TreeNode(start)]

            result = []

            for i in range(start, end+1):
                left = create_trees(start, i-1)
                right = create_trees(i+1, end)

                for lnode in left:
                    for rnode in right:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        result.append(root)

            return result

        return create_trees(1, n)
