def permute(nums):
    result = []

    def rec(start):
        print(start)
        if start >= len(nums):
            result.append(list(nums))
        for j in range(start, len(nums)):
            nums[start], nums[j] = nums[j], nums[start]
            rec(start+1)
            nums[start], nums[j] = nums[j], nums[start]

    rec(0)
    return result

print(permute([1,2,3]))
