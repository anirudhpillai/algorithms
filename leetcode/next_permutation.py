def next_permutation(nums):
    if not nums or len(nums) < 2:
        return

    p = 0
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            p=i
            break

    q = 0
    for i in range(len(nums)-1, p, -1):
        if nums[i] > nums[p]:
            q=i
            break

    if p == 0 and q == 0:
        reverse(nums, 0, len(nums) - 1)
        return

    temp = nums[p]
    nums[p] = nums[q]
    nums[q] = temp

    if p<len(nums)-1:
        reverse(nums, p+1, nums.length-1)


def reverse(nums, left, right):
    while left< right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
