def atoi(A):

    A = list(A.strip())

    flag = "+"

    i = 0

    if A[0] == '-':
        flag = '-'
        i += 1
    elif A[0] == '+':
        i += 1

    result = 0

    while i < len(A) and A[i] >= '0' and A[i] <= '9':
        result = result * 10 + (ord(A[i]) - ord('0'))
        i += 1

    if flag == '-':
        result = -result

    if result > 2147483647:
        return 2147483647

    if result < -2147483648:
        return -2147483648

    return result
