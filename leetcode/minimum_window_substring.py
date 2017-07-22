"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dp = {}
        for i in t:
            dp[i] = dp.get(i, 0) + 1

        result = ""
        missing = len(t)
        l, r = 0, 0

        while r <= len(s):
            if missing == 0:
                if not result or r-l < len(result):
                    result = s[l:r]

                if s[l] in dp:
                    dp[s[l]] += 1
                    if dp[s[l]] > 0:
                        missing += 1
                l += 1
            else:
                if r == len(s):
                    break

                if s[r] in dp:
                    dp[s[r]] -= 1
                    if dp[s[r]] >= 0:
                        missing -= 1
                r += 1

        return result
