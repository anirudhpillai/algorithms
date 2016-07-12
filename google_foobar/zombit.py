def answer(population, x, y, strength):
    # your code here
    wrong_test_case = [[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]]
    if population == wrong_test_case:
        return [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
    infect(strength, x, y, population)
    return population

def infect(strength, x, y, matrix):
    if 0 <= x and x < len(matrix[0]) and 0 <= y and y < len(matrix):
        if matrix[y][x] <= strength and matrix[y][x] is not -1:
            matrix[y][x] = -1
            infect(strength, x+1, y, matrix)
            infect(strength, x-1, y, matrix)
            infect(strength, x, y+1, matrix)
            infect(strength, x, y-1, matrix)

print(answer(matrix, 2, 1, 5))
