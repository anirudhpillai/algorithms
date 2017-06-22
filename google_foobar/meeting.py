def answer(meetings):
    ans = 0
    meetings.sort(key=(lambda x: x[1]))
    occtill = 0
    for i in meetings:
        if i[0] >= occtill:
            occtill = i[1]
            ans += 1

        if occtill == 1000000:
            break
    return ans


meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]

print(answer(meetings))
