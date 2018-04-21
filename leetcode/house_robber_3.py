class Solution(object):
    def rob(self, root):
        """ Top down DP
        memo = {}
        
        def dfs(node, take):
            if not node:
                return 0
                
            if (node, take) in memo:
                return memo[(node, take)]
                
            left = dfs(node.left, not take)
            right = dfs(node.right, not take)
            
            if take:
                one = node.val + left + right
                left = dfs(node.left, take)
                right = dfs(node.right, take)
                two = left + right
                memo[(node, take)] = max(one, two)
            else:
                memo[(node, take)] = left + right
                
            return memo[(node, take)]
        
        return max(dfs(root, True), dfs(root, False))
        """
        
        def dfs(node):
            if not node:
                return 0, 0
            
            rob_left, leave_left = dfs(node.left)
            rob_right, leave_right = dfs(node.right)
            
            return (
                node.val + leave_left + leave_right,
                max(rob_left, leave_left) + max(rob_right, leave_right)
            )
        
        rob_root, leave_root = dfs(root)
        return max(rob_root, leave_root)
