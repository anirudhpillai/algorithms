"""
Similar to find missing positive on leetcode

changing the index of nums at n
to indicate presence of n
"""

def repeatedNumber(nums):
    A, B = 0, 0
    for i in range(len(nums)):
        while nums[i] != i+1:
            temp = nums[i]
            # when nums[temp-1] already has the right (repeated) value
            if nums[i] == nums[temp-1]:
                A = nums[i]
                B = i+1
                break
            nums[i] = nums[temp-1]
            nums[temp-1] = temp

    return [A, B]


print(repeatedNumber([3, 1, 2, 5, 3]))
