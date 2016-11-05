import math


def rotate_image(matrix):
    n = len(matrix)

    for i in range(int(len(matrix)/2)):
        for j in range(int(math.ceil(len(matrix)/2))):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp

    return matrix


print(rotate_image([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))
