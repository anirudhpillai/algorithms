class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
            
        if root.val != 1 and not root.left and not root.right:
            return
        
        return root
