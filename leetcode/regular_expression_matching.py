class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s == ""

        # p[1] is not "*"
        if len(p) <= 1 or p[1] != "*":
            return (
                (s != "")
                and (p[0] == s[0] or p[0] == ".")
                and self.isMatch(s[1:], p[1:])
            )

        i = 0

        # while s[i] matches p[0]
        while i < len(s) and (p[0] == s[i] or p[0] == "."):
            if self.isMatch(s[i+1:], p[2:]):
                return True
            i += 1

        # * goes to 0 occurence
        return self.isMatch(s, p[2:])

        """ DP Solution O(s*p)
        dp = [[False for __ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        # matches x* to ""
        for j in range(1, len(p)+1):
            if p[j-1] == "*" and dp[0][j-2]: # a* -> "", ignore pattern (as -2)
                dp[0][j] = True

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        # we already know prev char matches
                        dp[i][j] = (
                            dp[i][j-2]   # a* -> "", ignore pattern (as -2)
                            or dp[i][j-1]  # a* -> a, ignore * (as -1)
                            or dp[i-1][j]  # a* -> aa.., count s[i-1] as repetition
                        )
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[-1][-1]
        """
