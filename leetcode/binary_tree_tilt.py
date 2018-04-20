class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        
        def sum_tree(node):
            if not node:
                return 0
            
            left = sum_tree(node.left)
            right = sum_tree(node.right)
            
            self.tilt += abs(left - right)
            
            return node.val + left + right
        
        sum_tree(root)
        return self.tilt
