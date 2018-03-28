from queue import PriorityQueue


def teamFormation(score, team, m):
    left = PriorityQueue()
    right = PriorityQueue()

    answer = 0
    l, r = m, max(len(score) - m - 1, m)

    # print(l, r)

    for i in range(l):
        # print("l", i)
        left.put((-score[i], i))

    for i in range(len(score)-1, r, -1):
        # print("r", i)
        right.put((-score[i], i))

    increment = True

    for _ in range(team):
        if not left and not right:
            return answer

        if l > r:
            increment = False

        l_val = li = ri = r_val = 0

        if not left.empty():
            l_val, li = left.get()
        if not right.empty():
            r_val, ri = right.get()

        l_val, r_val = abs(l_val), abs(r_val)

        if l_val >= r_val:
            # print("l val", l_val)
            right.put((-r_val, ri))
            answer += l_val
            if increment:
                # print("putting to left", l)
                left.put((score[l], l))
                l += 1
        else:
            # print("r val", r_val)
            left.put((-l_val, li))
            answer += r_val
            if increment:
                # print("putting to right", r)
                right.put((score[r], l))
                r -= 1

    return answer

# print(teamFormation([6,
# 18,
# 8,
# 14,
# 10,
# 12,
# 18,
# 9], 8, 3))

# # print(teamFormation([17,
# 12,
# 10,
# 2,
# 7,
# 2,
# 11,
# 20,
# 8], 3, 4))
