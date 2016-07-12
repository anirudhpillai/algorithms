def answer(food, grid):
    return answerrec(food, grid, 0, 0)

dp = dict()

def answerrec(food, grid, x, y):
    key = str((food, x, y))
    if key in dp:
        return dp[key]

    if food < 0:
        return -1

    if x == len(grid[0])-1 and y == len(grid) - 1:
        food -= grid[y][x]
        return food if food > -1 else -1

    if x < len(grid[0]) and x >= 0 and y < len(grid) and y >= 0:
        food -= grid[y][x]
        if x+1 > len(grid[0]) - 1:
            dp[key] = answerrec(food, grid, x, y+1)
        elif y+1 > len(grid) - 1:
            dp[key] = answerrec(food, grid, x+1, y)
        else:
            dp[key] = find_min(answerrec(food, grid, x+1, y), answerrec(food, grid, x, y+1))
        return dp[key]


def find_min(a, b):
    if a == -1:
        return b
    elif b == -1:
        return a
    else:
        return min(a, b)

grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]

print(answer(7, grid))
