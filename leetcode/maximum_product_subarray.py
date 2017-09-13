class Solution(object):
    def maxProduct(self, nums):
        """
        Keep track of the max product so far and the min product
        so far for the contiguous subarray
        """
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            result = max(result, max_product)

        return result
