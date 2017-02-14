def permute(nums):
    result = []

    def rec(start):
        if start >= len(nums):
            result.append(list(nums))
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            rec(start+1)
            nums[start], nums[i] = nums[i], nums[start]

    rec(0)
    return result

print(permute([1, 2, 3]))
