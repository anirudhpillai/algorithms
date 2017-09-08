class Solution(object):
    def nextGreaterElements(self, nums):
        """
        https://discuss.leetcode.com/topic/77881/typical-ways-to-solve-circular-array-problems-java-solution/2
        """
        stack = list(reversed(range(0, len(nums))))
        result = [-1 for _ in nums]

        for i in reversed(range(0, len(nums))):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                result[i] = nums[stack[-1]]

            stack.append(i)

        return result
