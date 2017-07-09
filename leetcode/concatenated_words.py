class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        Use word_break.py
        """
        words.sort(key=len)
        result = []
        word_dict = {}

        def broken(word):
            if not word_dict:
                return False

            dp = [True] + [False for _ in word]

            for i in range(len(word)+1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_dict:
                        dp[i] = True
                        break

            return dp[len(word)]

        for i, word in enumerate(words):
            if broken(word):
                result.append(word)
            word_dict[word] = True

        return result
