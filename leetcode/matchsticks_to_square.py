class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 4 or sum(nums) % 4:
            return False

        side = sum(nums)/4
        nums = list(reversed(sorted(nums)))

        def dfs(sums, ind):
            if ind == len(nums):
                return all(map(lambda x: x == side, sums))

            for i in range(len(sums)):
                if sums[i] + nums[ind] > side:
                    continue
                sums[i] += nums[ind]
                if dfs(sums, ind+1):
                    return True
                sums[i] -= nums[ind]

            return False

        return dfs([0, 0, 0, 0], 0)
