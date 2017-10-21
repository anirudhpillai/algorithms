import collections


class Solution(object):
    def minStickers(self, stickers, target):
        """
        Still getting TLE
        Can improve BFS as order of adding elements doesn't matter
        and we should give priority to keys with less remaining elements
        """
        target = collections.Counter(target)
        stickers = map(collections.Counter, stickers)

        visited = {}
        queue = collections.deque()
        queue.appendleft((0, target))

        while queue:
            used, head = queue.pop()
            if not head:
                return used

            key = tuple(sorted(head.elements()))
            if key in visited:
                continue

            visited[key] = True
            for s in stickers:
                queue.appendleft((used+1, head - s))

        return -1
