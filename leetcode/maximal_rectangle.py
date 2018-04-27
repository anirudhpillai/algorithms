class Solution(object):
    def maximalRectangle(self, matrix):
        """
        based on largest_rectangle_in_histogram
        """
        if not matrix:
            return 0

        def find_largest_rectangle(heights):
            stack = []
            result = 0

            for i in range(len(heights)+1):
                while stack and (
                    i == len(heights)
                    or heights[i] < heights[stack[-1]]
                ):
                    top = stack.pop()
                    width = i
                    if stack:
                        width = i - 1 - stack[-1]
                    result = max(result, heights[top] * width)
                stack.append(i)

            return result

        result = 0
        heights = [0 for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j, col in enumerate(matrix[i]):
                if col == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            result = max(result, find_largest_rectangle(heights))

        return result
        """
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        left = [0 for _ in range(cols)]
        right = [cols for _ in range(cols)]
        height = [0 for _ in range(cols)]

        result = 0

        for row in range(rows):
            curr_left, curr_right = 0, cols
            for col in range(cols):
                if matrix[row][col] == '1':
                    height[col] += 1
                    left[col] = max(left[col], curr_left)
                else:
                    height[col] = 0
                    left[col], curr_left = 0, col+1

            for col in reversed(range(cols)):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], curr_right)
                else:
                    right[col], curr_right = cols, col
                result = max(result, (right[col] - left[col]) * height[col])

        return result
        """
