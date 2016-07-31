def answer(heights):
    stack = []
    ret = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            curr = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            ret = max(ret, heights[curr] * width)
        stack.append(i)

    i = len(heights)

    while stack:
        curr = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        ret = max(ret, heights[curr] * width)

    return ret

print(answer([2,1,5,6,2,3]))
