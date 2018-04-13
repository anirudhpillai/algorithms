class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[0])
        stack = [points[0]]

        for point in points:
            top = stack[-1]

            if point[0] <= top[1]:
                stack[-1] = [max(point[0], top[0]), min(point[1], top[1])]
            else:
                stack.append(point)

        return len(stack)
