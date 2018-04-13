class Solution:
    def jump(self, nums):
        """ TLE
        dp = [0] + [1e9 for _ in range(len(nums) - 1)]
        
        for i in range(len(nums)):
            for j in range(i+1, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
            
        return dp[-1]
        """
        old_reach = max_reach = jumps = 0
        
        for i in range(len(nums)):
            if i > max_reach:
                return 0
            
            # prev reach not enough so use another jump
            # to get the current max reach
            if old_reach < i:
                old_reach = max_reach
                jumps += 1
            
            max_reach = max(max_reach, nums[i] + i)
            
        return jumps
