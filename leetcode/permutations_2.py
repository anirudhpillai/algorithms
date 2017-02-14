# from itertools import permutations
#
#
# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         Solution using the library
#         """
#         ans = set()
#         for i in permutations(nums):
#             ans.add(i)
#         return [list(i) for i in ans]


def permute_unique(nums):
        """
        My amazing solution beats 88.74%
        """
        result = []

        def dfs(start):
            if start >= len(nums):
                result.append(list(nums))

            replaced_with = dict()
            for i in range(start, len(nums)):
                if nums[i] in replaced_with:
                    continue
                replaced_with[nums[i]] = True
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return result

print(permute_unique([1, 1, 2]))
