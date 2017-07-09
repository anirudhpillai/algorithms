from Queue import deque


class Solution(object):
    def removeInvalidParentheses(self, s):
        # BFS
        def is_balanced(s):
            count = 0

            for i in s:
                if i == "(":
                    count += 1
                elif i == ")":
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        queue = deque([s])
        result = []
        visited = {}
        reached = False

        while queue:
            top = queue.popleft()

            if is_balanced(top):
                result.append(top)
                reached = True  # stop adding as minimum removals reached
                continue

            if not reached:
                for i in range(len(top)):
                    if top[i] not in "()":  # as we can only remove brackets
                        continue

                    new_pattern = top[:i] + top[i+1:]

                    if new_pattern not in visited:
                        queue.append(new_pattern)
                        visited[new_pattern] = True

        return result
