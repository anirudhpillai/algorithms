class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dp = {}
        result = []
        for i in range(len(s)):
            curr = s[i:i+10]
            if curr in dp:
                if dp[curr]:
                    result.append(curr)
                    dp[curr] = False
            else:
                dp[curr] = True
        return result
