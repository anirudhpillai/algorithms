class Solution(object):
    def maxSubArray(self, nums):
        """
        As soon as current sum gets negative,
        you start summing again
        """
        if not nums:
            return 0

        max_so_far = max_ending_here = nums[0]

        for num in nums[1:]:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
