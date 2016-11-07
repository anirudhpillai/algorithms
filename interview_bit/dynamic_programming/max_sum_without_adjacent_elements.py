class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):

        m = len(A[0])
        if m == 0:
            return 0

        dp = [0]*m
        dp[0] = max(A[0][0], A[1][0])

        if m == 1:
            return dp[0]

        dp[1] = max(A[0][1], A[1][1], dp[0])

        for i in range(2, m):
            temp = max(A[0][i], A[1][i])
            dp[i] = max(temp+dp[i-2], dp[i-1])
            dp[i] = max(dp[i], temp)

        return dp[m-1]
