class Solution(object):
    def largestRectangleArea(self, heights):
        """
        We need to calculate area with each bar as the smallest bar
        in the rectangle. For this we need to know the closest bars which
        are shorter than the current bar, both on the right and the left.
        The stack provides a good way to keep track of the bar on the left
        and the loop automatically gets the bar on the right.
        """
        stack = []
        result = 0

        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                top = stack.pop()
                width = i
                if stack:
                    # as everything between the last item on stack
                    # and the curr i
                    width = (i - 1) - stack[-1]
                result = max(result, heights[top] * width)

            stack.append(i)

        return result
