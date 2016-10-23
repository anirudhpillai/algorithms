def step_num(A, B):
    
    def edges(n):
        ret = []
        if n == 0:
            return list(range(1,10))
        else:
            last = n % 10
            temp = n*10 + last
            if last == 0:
                return [temp+1]
            elif last == 9:
                return [temp-1]
            else:
                return [temp-1, temp+1]

    ret = []
    if A <= 0:
        ret.append(0)

    Q = deque()
    Q.appendleft(0)
    while Q:
        curr = Q.pop()
        for i in edges(curr):
            Q.appendleft(i)
            if i > B:
                Q = deque()
                break
            elif i >= A:
                ret.append(i)

    return ret
