def jump_game(nums):
    if len(nums) <= 1:
        return True

    maximum = nums[0]

    for i in range(len(nums)):
        # if not enough to go to next
        if maximum <= i and nums[i] == 0:
            return False

        # update max
        maximum = max(i+nums[i], maximum)

        # max is enough to reach the end
        if maximum >= len(nums) - 1:
            return True

    return False


# def jump_game(nums):
#     last_pos = len(nums) - 1
#     for i in range(len(nums)-1, -1, -1):
#         if i + nums[i] >= last_pos:
#             last_pos = i
#     return last_pos == 0
