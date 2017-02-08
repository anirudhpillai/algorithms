class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def rec(curr):
            s = sum(curr)
            if len(curr) == k:
                if s == n:
                    result.append(list(curr))
                return

            start = 1

            if curr:
                start = curr[-1] + 1

            for i in range(start, 10):
                if s + i <= n:
                    curr.append(i)
                    rec(curr)
                    curr.pop()
                    # above three lines are more efficient than
                    # rec(curr + [i])

        rec([])

        return result
