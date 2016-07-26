# My Original Solution
def answer(arr):
    stack = []
    ret = []
    for i in arr:
        while True:
            if not stack:
                ret.append(-1)
                stack.append(i)
                break
            else:
                p = stack[-1]
                if p >= i:
                    stack.pop()
                else:
                    ret.append(p)
                    stack.append(i)
                    break
    return ret

# Improved solution which is shorter
def answer(arr):
    stack = []
    ret = []
    for i in arr:
        while stack and stack[-1] >= i:
            stack.pop()
        if not stack:
            ret.append(-1)
        else:
            ret.append(stack[-1])
        stack.append(i)
    return ret
