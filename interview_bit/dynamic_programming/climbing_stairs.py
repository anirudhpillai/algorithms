class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        dp = [1 for i in range(A+1)]

        for i in range(2, A+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[A]
