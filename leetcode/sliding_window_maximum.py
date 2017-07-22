from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        q = deque()

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if q[0] <= i-k:
                q.popleft()

            if i >= k-1:
                result.append(nums[q[0]])

        return result
