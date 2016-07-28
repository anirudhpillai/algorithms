def evalRPN(A):
    stack = []
    for i in A:
        if i in "+-*/":
            a = int(stack.pop())
            b = int(stack.pop())
            if i == "+":
                stack.append(a+b)
            elif i == "-":
                stack.append(b-a)
            elif i == "*":
                stack.append(a*b)
            else:
                stack.append(b/a)
        else:
            stack.append(i)
    return stack.pop()

print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
