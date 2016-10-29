def flip(A):
    l, r, curr = 0, 0, 0
    max_so_far = 0
    hit = False
    for i, k in enumerate(A):
        if k == "0":
            hit = True
            curr += 1
        else:
            curr -= 1

        if curr < 0:
            curr = 0
            l = i

        if curr > max_so_far:
            max_so_far = curr
            r = i

    if not hit:
        return []

    return [l+1, r+1]


print(flip("01"))
