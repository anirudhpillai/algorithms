class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = []
        max_right = []

        max_so_far = 0
        for i in height:
            max_left.append(max_so_far)
            max_so_far = max(max_so_far, i)

        max_so_far = 0
        for i in reversed(height):
            max_right.append(max_so_far)
            max_so_far = max(max_so_far, i)

        max_right = max_right[::-1]

        result = 0

        for i in range(len(height)):
            curr = min(max_left[i], max_right[i])
            if curr > height[i]:
                result += curr - height[i]

        return result
