class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0

        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                top = stack.pop()
                width = i
                if stack:
                    width = i - (stack[-1] + 1)  # as everything before the last item on stack
                result = max(result, heights[top] * width)

            stack.append(i)

        return result
