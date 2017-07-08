# Using Dynamic Programming
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        # dp[i] means that s[:i] is breakable

        for i in range(len(s)+1):  # +1 is important
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

# Simple Brute force
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         def helper(word):
#             if word in wordDict:
#                 return True
#             else:
#                 return any((helper(word[i:]) and helper(word[:i]))
#                            for i in range(1, len(word)))
#
#         return helper(s)
