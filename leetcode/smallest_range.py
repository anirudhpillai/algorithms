class Solution(object):
    def smallestRange(self, nums):
        """
        Similar to Minimum Window Substring
        """
        ans = -1e9, 1e9

        for right in sorted(set(x for row in nums for x in row))[::-1]:
            left = 1e9

            for row in nums:
                while row and row[-1] > right:
                    row.pop()

                if not row:
                    return ans

                left = min(left, row[-1])

            if right - left <= ans[1] - ans[0]:
                ans = left, right

        return ans
