def add_binary(A, B):
    carry = 0
    A = list(reversed(A))
    B = list(reversed(B))

    if len(B) > len(A):
        A, B = B, A

    ans = ""
    for i in range(len(A)):
        temp = 0
        if i < len(B):
            temp = (int(A[i]) + int(B[i]) + carry) % 2
            carry = (int(A[i]) + int(B[i]) + carry) // 2
        else:
            temp = (int(A[i]) + carry) % 2
            carry = (int(A[i]) + carry) / 2

        ans += str(temp)

    if carry == 1:
        ans += '1'

    return ans[::-1]


print(add_binary("111", "11"))
