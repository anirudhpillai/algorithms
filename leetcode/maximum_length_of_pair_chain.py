class Solution(object):
    def findLongestChain(self, pairs):
        """ DP
        pairs.sort(key=lambda x: x[0])

        memo = [1 for _ in pairs]

        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)
        """

        current = -1e9
        result = 0

        for pair in sorted(pairs, key=lambda x: x[1]):
            if pair[0] > current:
                current = pair[1]
                result += 1

        return result
