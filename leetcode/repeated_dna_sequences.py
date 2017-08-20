class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """Using Bit Manipulation
        memo = {}
        result = set()

        for i in range(len(s)-9):
            mask = 0
            for c in s[i:i+10]:
                mask <<= 5
                mask |= ord(c) - ord('A')

            if mask in memo:
                result.add(s[i:i+10])
            else:
                memo[mask] = True

        return list(result)
        """
        memo = {}

        for i in range(len(s)-9):
            memo[s[i:i+10]] = memo.get(s[i:i+10], 0) + 1

        return [k for k, v in memo.items() if v > 1]
