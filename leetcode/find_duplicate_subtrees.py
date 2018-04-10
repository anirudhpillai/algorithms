class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        traversals_to_roots = {}

        def get_traversal(node):
            if node:
                traversal = (
                    get_traversal(node.left),
                    node.val,
                    get_traversal(node.right)
                )
                traversals_to_roots[traversal] = (
                    traversals_to_roots.get(traversal, []) + [node]
                )
                return traversal

        get_traversal(root)

        return [v[0] for k, v in traversals_to_roots.items() if v[1:]]
