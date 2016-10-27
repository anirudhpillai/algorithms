class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def dfs(j, target, curr):
            if target == 0:
                result.append(curr)
                return

            prev = -1
            for i in range(j, len(nums)):
                if target < nums[i]:
                    return

                # start from diff elem each time
                # if there are multiple ones in nums
                # then we only make all the combs with one one only once
                if nums[i] != prev:
                    # i+1 to prevent reuse of the same element
                    dfs(i+1, target-nums[i], curr+[nums[i]])
                    prev = nums[i]

        dfs(0, target, [])

        return result
