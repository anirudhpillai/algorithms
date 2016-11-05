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

print(first_missing_positive([3, 4, -1, 13]))
