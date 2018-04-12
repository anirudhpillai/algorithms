class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        product_so_far = 1

        for num in nums:
            result.append(product_so_far)
            product_so_far *= num

        product_so_far = 1

        for i in reversed(range(len(nums))):
            result[i] *= product_so_far
            product_so_far *= nums[i]

        return result
