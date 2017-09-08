class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_to_index = {0: 1}
        result = curr_sum = 0

        for num in nums:
            curr_sum += num
            result += sum_to_index.get(curr_sum - k, 0)
            sum_to_index[curr_sum] = sum_to_index.get(curr_sum, 0) + 1

        return result
