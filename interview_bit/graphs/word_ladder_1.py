from collections import deque

def ladderLength(start, end, dictV):
    dictV.append(end)

    def valid(one, two):
        one, two = list(one), list(two)
        tot = 0
        for i in range(len(one)):
            if one[i] != two[i]:
                tot += 1
                if tot > 1:
                    return False

        return True

    queue = deque()
    seen = []
    queue.append((start, 1))
    while queue:
        # print(queue)
        temp, curr = queue.pop()
        if temp == end:
            return curr

        if temp in seen:
            continue
        else:
            seen.append(temp)

        queue.extendleft((i, curr+1) for i in dictV if valid(i, temp))

    return 0

print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
