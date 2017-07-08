class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = {}

        def dfs(leftover):
            if leftover in dp:
                return dp[leftover]

            if not leftover:
                return []

            result = []

            for word in word_dict:
                if leftover.startswith(word):
                    sub = dfs(leftover[len(word):])

                    for ending in sub:
                        result.append(word + " " + ending)

                    if not leftover[len(word):]:
                        result.append(word)

            dp[leftover] = result
            return result

        return dfs(s)
