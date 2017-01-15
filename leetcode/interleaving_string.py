class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """Solution beats 99.2%"""

        dp = {}

        def rec(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False

            if i < len(s1) and s1[i] == s3[k]:
                if rec(i+1, j, k+1):
                    return True
                else:
                    dp[(i+1, j, k+1)] = False

            if j < len(s2) and s2[j] == s3[k]:
                if rec(i, j+1, k+1):
                    return True
                else:
                    dp[(i, j+1, k+1)] = False

            return False

        return rec(0, 0, 0)


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """Bottom-up DP"""

        if (len(s1) + len(s2)) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        dp = [[None for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) \
                            or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[-1][-1]
