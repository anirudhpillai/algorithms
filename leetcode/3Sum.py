class Solution(object):
    def threeSum(self, nums):
        """
        Beats 83%
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            j = i+1
            k = len(nums)-1

            if nums[i] > 0:
                break

            while j < k:
                temp = nums[j] + nums[k]

                if temp < -nums[i]:
                    j += 1
                elif temp > -nums[i]:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return result
