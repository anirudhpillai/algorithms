class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_map = {}

        for word in words:
            mask = 0
            for c in word:
                mask |= (1 << (ord(c) - ord('a')))
            # mask becomes a binary number recording all the letters in the word
            letter_map[mask] = max(letter_map.get(mask, 0), len(word))

        result = 0

        for x in letter_map.keys():
            for y in letter_map.keys():
                if not x & y:
                    result = max(result, letter_map[x] * letter_map[y])

        return result
