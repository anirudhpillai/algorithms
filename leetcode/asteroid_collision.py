class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        right_movers = []

        for i in asteroids:
            if i < 0:
                if right_movers:
                    while right_movers and right_movers[-1] < abs(i):
                        right_movers.pop()
                    if not right_movers:
                        result.append(i)
                    elif right_movers[-1] == abs(i):
                        right_movers.pop()
                else:
                    result.append(i)
            else:
                right_movers.append(i)

        return result + right_movers
