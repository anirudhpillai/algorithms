def maxsum(nums):
    curr_sum = 0
    result = -1000000

    for i in nums:
        curr_sum += i
        result = max(result, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return result

print(maxsum([-2,1,-3,4,-1,2,1,-5,4]))
