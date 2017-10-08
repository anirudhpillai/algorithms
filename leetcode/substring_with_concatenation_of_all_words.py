"""
You are given a string, s, and a list of words, words,
that are all of the same length. Find all starting indices
of substring(s) in s that is a concatenation of each word
in words exactly once and without any intervening characters.
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # dict to gather frequecy of words
        map = {}
        for w in words:
            if w not in map:
                map[w] = 1
            else:
                map[w] += 1

        ret = []

        substring_len = len(words)*len(words[0])
        word_len = len(words[0])

        for i in range(0, len(s)-substring_len + 1):
            curr = {}
            for j in range(i, i+substring_len, word_len):
                w = s[j:j+word_len]

                if w not in map:
                    break

                if w not in curr:
                    curr[w] = 1
                else:
                    curr[w] += 1

                if curr[w] > map[w]:
                    break

            if curr == map:
                ret.append(i)

        return ret
