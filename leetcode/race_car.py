from collections import deque


class Solution:
    def racecar(self, target):
        """
        queue = deque()
        queue.appendleft([0, 1, 0])  # [pos, speed, moves]

        visited = set()

        while queue:
            pos, speed, moves = queue.pop()
            if pos == target:
                return moves

            p1, s1 = pos + speed, speed * 2
            if (p1, s1) not in visited:
                visited.add((p1, s1))
                queue.appendleft([p1, s1, moves + 1])

            p2, s2 = pos, -1 if speed > 0 else 1
            if (p2, s2) not in visited:
                visited.add((p2, s2))
                queue.appendleft([p2, s2, moves + 1])

        return -1
        """

        level = [(0, 1)]  # [(pos, speed)]
        visited = set()
        moves = 0

        while level:
            next_level = []
            for pos, speed in level:
                p1, s1 = pos + speed, speed * 2

                if pos == target:
                    return moves

                """ Not doing this as memory limit exceeded
                if (p1, s1) not in visited:
                    visited.add((p1, s1))
                    next_level.append((p1, s1))
                """
                next_level.append((p1, s1))

                p2, s2 = pos, -1 if speed > 0 else 1
                if (p2, s2) not in visited:
                    visited.add((p2, s2))
                    next_level.append((p2, s2))

            moves += 1
            level = next_level

        return -1
