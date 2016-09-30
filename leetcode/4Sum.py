def fourSum(nums, target):
    result = []

    if not nums or len(nums) < 4:
        return result

    nums.sort()

    for i in range(len(nums) - 3):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums) - 2):
            if j != i+1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = len(nums) - 1
            while k < l:
                if nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                    l -= 1
                else:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k<l and nums[l] == nums[l+1]:
                        l -= 1

                    while k<l and nums[k] == nums[k-1]:
                        k += 1

    return result

    

# brute force solution
# def fourSum(nums, target):
#     all = it.combinations(nums, 4)
#     all = [sorted(i) for i in all if sum(i) == target]
#     return [list(x) for x in set(tuple(x) for x in all)]
