class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        
        level = [root]
        self.leftmost = root
        
        while level:
            self.leftmost = level[0]
            next_level = []
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
                    
        return self.leftmost.val
