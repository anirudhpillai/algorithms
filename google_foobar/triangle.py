def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def on_boundary(a, b):
    if a[0] == b[0]:
        return abs(a[1] - b[1]) - 1

    if a[1] == b[1]:
        return abs(a[0] - b[0]) - 1;

    return gcd(abs(a[0]-b[0]), abs(a[1]-b[1])) - 1

def answer(vertices):
    v1, v2, v3 = vertices
    boundary = on_boundary(v1, v2) + on_boundary(v2, v3) + on_boundary(v3,v1) + 3

    doubleArea = abs(v1[0]*(v2[1] - v3[1]) + v2[0]*(v3[1] - v1[1]) + v3[0]*(v1[1] - v2[1]))

    return int((doubleArea - boundary + 2) / 2)


vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
print(answer(vertices))
