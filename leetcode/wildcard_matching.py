class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        # while *** matches s = ""
        for j in range(1, len(p)+1):
            if p[j-1] != "*":
                break
            dp[0][j] = True

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # dp[i-1][j] -> start is occurence of some char
                    # dp[i][j-1] -> * goes to "" (everything before it matches)
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]
