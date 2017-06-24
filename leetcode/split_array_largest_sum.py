class Solution(object):
    def splitArray(self, nums, m):
        """Top Down DP
        if m == 1:
            return sum(nums)

        minimum = sum(nums)

        dp = {}

        for i in range(1, len(nums)):
            if (i, m-1) in dp:
                curr = dp[(i, m-1)]
            else:
                curr = max(sum(nums[:i]), self.splitArray(nums[i:], m-1))
                dp[(i, m-1)] = curr
            minimum = min(minimum, curr)

        return minimum
        """

        # Using Binary Search
        def valid(mid):
            current_sum = 0
            splits = 1

            for i in nums:
                current_sum += i

                if current_sum > mid:
                    splits += 1
                    if splits > m:
                        return False
                    current_sum = i

            return True

        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l + r) / 2

            if valid(mid):
                r = mid
            else:
                l = mid + 1

        return l
