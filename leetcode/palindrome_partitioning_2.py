class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [(i-1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                temp = s[j:i]
                if temp[:] == temp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]

        # cut = [0 for i in s]
        # pal = [[False for i in s] for i in s]

        # for i in range(len(s)):
        #     minimum = i
        #     for j in range(i):
        #         if s[j] == s[i] and (j+1 > i-1 or pal[j+1][i-1]):
        #             pal[j][i] = True
        #             print(cut)
        #             if j == 0:
        #                 mimimum = 0
        #             else:
        #                 minimum = min(minimum, cut[j-1]+1)

        #     cut[i] = minimum

        # return cut[-1]
