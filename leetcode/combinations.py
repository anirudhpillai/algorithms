class Solution(object):
    def combine(self, n, k):
        memo = {(n, 0): [[]]}

        def helper(n, k):
            if k > n:
                return []
            if k == 1:
                return [[i] for i in range(1, n+1)]
            if (n, k) not in memo:
                next_subsets = helper(n - 1, k - 1)
                memo[(n, k)] = [[n] + sub for sub in next_subsets] + helper(n - 1, k)
            return memo[(n, k)]

        return helper(n, k)
