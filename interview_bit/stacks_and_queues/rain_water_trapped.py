def answer(heights):
    ret = 0
    if not heights or len(heights) <= 2:
        return ret

    left, right = [0]*len(heights), [0]*len(heights)

    mx = heights[0]
    left[0] = heights[0]

    for i in range(len(heights)):
        if heights[i] < mx:
            left[i] = mx
        else:
            left[i] = heights[i]
            mx = heights[i]

    mx = heights[len(heights) -1]
    right[len(heights) -1] = heights[len(heights) -1]

    for i in range(len(heights) - 2, -1, -1):
        if heights[i] < mx:
            right[i] = mx
        else:
            right[i] = heights[i]
            mx = heights[i]

    for i in range(len(heights)):
        ret += min(left[i], right[i]) - heights[i]

    return ret

print(answer([0,1,0,2,1,0,1,3,2,1,2,1]))
