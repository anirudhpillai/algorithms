def gray_code(n):
    if not n:
        return [0]

    result = gray_code(n-1)
    num = 1 << n-1

    for i in range(len(result)-1, -1, -1):
        result.append(num+result[i])

    print(result)
    return result

gray_code(3)
