def answer(vertices):
    v1, v2, v3 = vertices
    x_min = min([i[0] for i in vertices])
    x_max = max([i[0] for i in vertices])
    y_min = min([i[1] for i in vertices])
    y_max = max([i[1] for i in vertices])

    x = list(range(x_min, x_max+1))
    y = list(range(y_min, y_max+1))

    points = [[i, j] for i in x for j in y]

    counter = 0
    for i in points:
        if check_point(v1, v2, v3, i):
            counter += 1

    return counter

def make_vector(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return (x, y)

def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1]

def get_side(v1, v2, ref):
    side = make_vector(v1, v2)
    side_to_ref = make_vector(v1, ref)
    return True if dot_product(side, side_to_ref) >= 0 else False

def same_side(v1, v2, ref, p):
    return get_side(v1, v2, ref) == get_side(v1, v2, p)

def check_point(v1, v2, v3, p):
    return same_side(v1, v2, v3, p) and same_side(v2, v3, v1, p) and same_side(v3, v1, v2, p)


vertices = [[2, 3], [6, 9], [10, 160]]

print(same_side([6, 9], [10, 160], [2, 3],  [6, 10]))

print(answer(vertices))
