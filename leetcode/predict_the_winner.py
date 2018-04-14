class Solution:
    def PredictTheWinner(self, nums):
        """
        Top down DP
        """
        memo = {}

        def max_score(i, j, p1_turn):
            if (i, j, p1_turn) in memo:
                return memo[(i, j, p1_turn)]

            if i > j:
                return 0

            first = p1_turn * nums[i] + max_score(i+1, j, -1 * p1_turn)
            last = p1_turn * nums[j] + max_score(i, j-1, -1 * p1_turn)

            result = 0
            if p1_turn == 1:
                result = max(first, last)
            else:
                result = min(first, last)

            memo[(i, j, p1_turn)] = result
            return result

        return True if max_score(0, len(nums)-1, 1) >= 0 else False
