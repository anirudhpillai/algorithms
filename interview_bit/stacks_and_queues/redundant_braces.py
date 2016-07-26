def answer(s):
    stack = []
    for i in s:
        if i == ')':
            seen = False
            while len(stack) > 0:
                p = stack.pop()
                if p == '(':
                    if not seen:
                        return 1
                    else:
                        break
                else:
                    seen = True
        elif i in "+-*/(":
            stack.append(i)
    return 0
