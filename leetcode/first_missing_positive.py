def first_missing_positive(nums):

    for i in range(len(nums)):
        while nums[i] != i+1:
            if nums[i] <= 0 or nums[i] >= len(nums):
                break

            if nums[i] == nums[nums[i]-1]:
                break

            temp = nums[i]
            nums[i] = nums[temp-1]
            nums[temp-1] = temp

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1

    return len(nums)+1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            while 0 < nums[i] < len(nums) and nums[i] != nums[nums[i]-1]:
                swap(i, nums[i]-1)

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums)+1

print(first_missing_positive([3, 4, -1, 13]))
