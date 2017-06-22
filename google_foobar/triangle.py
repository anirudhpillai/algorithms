def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def on_boundary(a, b):
    if a[0] == b[0]:
        return abs(a[1] - b[1]) - 1

    if a[1] == b[1]:
        return abs(a[0] - b[0]) - 1

    return gcd(abs(a[0]-b[0]), abs(a[1]-b[1])) - 1


def answer(vertices):
    v1, v2, v3 = vertices
    boundary = on_boundary(v1, v2) + on_boundary(v2, v3) + on_boundary(v3,v1) + 3

    doubleArea = abs(v1[0]*(v2[1] - v3[1]) + v2[0]*(v3[1] - v1[1]) + v3[0]*(v1[1] - v2[1]))

    return int((doubleArea - boundary + 2) / 2)


vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
print(answer(vertices))

# using area

# def area(v1, v2, v3):
#     [x1, y1], [x2, y2], [x3, y3] = v1, v2, v3
#     return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2)
#
# def check(vertices, p):
#
#     if on_boundary(vertices, p):
#         return False
#
#     v1, v2, v3 = vertices
#     at = area(v1, v2, v3)
#     a1 = area(v1, v2, p)
#     a2 = area(v1, v3, p)
#     a3 = area(v2, v3, p)
#
#     return at == a1 + a2 + a3
#
# def on_line(v1, v2, p):
#     [x1, y1], [x2, y2], [px, py] = v1, v2, p
#     m = (y2 - y1) / (x2 - x1)
#     return (y2 - py) == m*(x2 - px)
#
# def on_boundary(vertices, p):
#     v1, v2, v3 = vertices
#     return on_line(v1, v2, p) or on_line(v2, v3, p) or on_line(v3, v1, p)
#
# def answer(vertices):
#     v1, v2, v3 = vertices
#     x_min = min([i[0] for i in vertices])
#     x_max = max([i[0] for i in vertices])
#     y_min = min([i[1] for i in vertices])
#     y_max = max([i[1] for i in vertices])
#
#     x = list(range(x_min, x_max+1))
#     y = list(range(y_min, y_max+1))
#
#     counter = 0
#     for i in x:
#         for j in y:
#             if check(vertices, [i, j]):
#                 counter += 1
#
#     return counter
#
#
# vertices = [[2, 3], [6, 9], [10, 160]]
#
# print(answer(vertices))
