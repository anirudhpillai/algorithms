class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_to_freq = {0: 1}
        result = current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            result += sum_to_freq.get(current_sum - k, 0)
            sum_to_freq[current_sum] = sum_to_freq.get(current_sum, 0) + 1

        return result
