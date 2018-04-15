class Solution:
    def longestPalindromeSubseq(self, s):
        """
        dp[i][j] = longest palindrome subsequence of s[i to j].
        If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
        Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        memo = {}

        def helper(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                return helper(i+1, j-1) + 2
            else:
                return max(helper(i, j-1), helper(i+1, j))

        return helper(0, len(s)-1)
        """
        if s == s[::-1]:
            return len(s)

        dp = [[0 for _ in s] for _ in s]

        #  we only use half the matrix
        #  start filling from bottom
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if j == i:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][len(s) - 1]
