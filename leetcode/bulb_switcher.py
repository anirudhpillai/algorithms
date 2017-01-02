def bulbSwitch(self, n):
        return int(n ** 0.5)

# @StefanPochmann's amazing explanation
# https://discuss.leetcode.com/topic/31929/math-solution/2

"""
# Brute force
def bulbSwitch(n):
    result = 0

    for i in range(1, n+1):
        temp = 0
        for j in range(1, i+1):
            if i % j == 0:
                temp += 1
        if temp % 2 == 1:
            result += 1

    return result

    # bulbs = [0 for _ in range(n)]
    # for i in range(n):
    #     for j in range(i, n, i+1):
    #         if bulbs[j] == 0:
    #             bulbs[j] = 1
    #         else:
    #             bulbs[j] = 0
    #     print(bulbs)
    #
    # return len([i for i in bulbs if i == 1])
"""
