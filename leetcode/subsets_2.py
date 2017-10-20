class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        def dfs(curr_subset, left):
            if not left:
                result.append(curr_subset)
            else:
                if curr_subset and curr_subset[-1] == left[0]:
                    # if same element then we must add it
                    # as all subsets without the element have already been computed
                    dfs(curr_subset + [left[0]], left[1:])
                    return
                else:
                    dfs(curr_subset + [left[0]], left[1:])
                    dfs(curr_subset, left[1:])

        dfs([], nums)
        return result
