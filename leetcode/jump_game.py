class Solution:
    def canJump(self, nums):
        reach = 0

        for i, n in enumerate(nums):
            if i > reach:
                return False

            reach = max(reach, i+n)

        return True


# def jump_game(nums):
#     last_pos = len(nums) - 1
#     for i in range(len(nums)-1, -1, -1):
#         if i + nums[i] >= last_pos:
#             last_pos = i
#     return last_pos == 0
