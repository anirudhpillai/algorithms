class Solution(object):
    def subsets(self, nums):
        """Iterative Solution
        result = [[]]

        for num in nums:
            result += [item + [num] for item in result]

        return result
        """
        result = []

        def helper(curr_subset, leftover_nums):
            if not leftover_nums:
                result.append(curr_subset)
            else:
                helper(curr_subset, leftover_nums[1:])
                helper(curr_subset + [leftover_nums[0]], leftover_nums[1:])

        helper([], nums)
        return result
