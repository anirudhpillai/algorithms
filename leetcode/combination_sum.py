def combination_sum(nums, target):
    result = []
    nums.sort()

    def dfs(target, j, curr):
        if target == 0:
            result.append(list(curr))
            return

        for i in range(j, len(nums)):
            if target < nums[i]:
                return

            dfs(target - nums[i], i, curr + nums[i])

    dfs(target, 0, [])

    return result
