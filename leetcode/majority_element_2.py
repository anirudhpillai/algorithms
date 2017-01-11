def majorityElement2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one, two = 0, 1
    c_one, c_two = 0, 0

    for i in nums:
        if i == one:
            c_one += 1
        elif i == two:
            c_two += 1
        elif c_one == 0:
            one, c_one = i, 1
        elif c_two == 0:
            two, c_two = i, 1
        else:
            c_one -= 1
            c_two -= 1

    c_one = len([i for i in nums if i == one])
    c_two = len([i for i in nums if i == two])

    res = []
    
    if c_one > len(nums) / 3:
        res.append(one)
    if c_two > len(nums) / 3:
        res.append(two)

    return res
