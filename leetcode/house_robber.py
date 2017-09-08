class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        result = 0
        
        def helper(curr_ind):
            if curr_ind >= len(nums):
                return 0
            
            if curr_ind in dp:
                return dp[curr_ind]
            
            ans = max(nums[curr_ind] + helper(curr_ind+2), helper(curr_ind+1))
            dp[curr_ind] = ans
            return ans
        
        return max(helper(0), helper(1))
        
