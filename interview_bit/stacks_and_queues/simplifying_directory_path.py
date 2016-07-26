def answer(path):
     arr = path.split('/')
        stack = []
        for i in arr:
            if i == "..":
                if len(stack) > 0:
                    stack.pop()
            elif i != "." and i != "":
                stack.append(i)
        return '/' + '/'.join(stack)
