def jump_game(nums):
    if not nums:
		return 0

	last_reach = 0
	reach = 0
	step = 0

    for i in range(0, len(nums)):
        if i > reach:
            return 0

        if i > last_reach:
            step += 1
            last_reach = reach

        reach = max(reach, nums[i]+i)

    if reach < len(nums) - 1:
        return 0

    return step
