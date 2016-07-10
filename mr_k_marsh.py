#solution learnt from https://github.com/monkeylyf/interviewjam/blob/master/arr/hackerrank_Mr_K_Marsh.java

def solve(m, n, land):
    r = [[0 for _ in range(m)] for _ in range(n)]
    res = 0

    #checking first row
    for up in range(m):
        r[0][up] = 0 if land[0][up] is '.' else 5000
    #seeing if a fence is possible from the top
    for up in range(1, n):
        for col in range(0, m):
            r[up][col] = min(r[up - 1][col], up) if land[up][col] is '.' else 5000
    #trying all possible rectangles with top side in the the row (up)
    for up in range(0, n):
        for low in range(up+1, n):
            lastCol = -1
            for col in range(m):
                if land[up][col] is '.' and land[low][col] is '.':
                    if r[low][col] <= up:
                        if lastCol != -1:
                            res = max(res, 2*(low-up-1) + 2*(col-lastCol+1))
                        else:
                            lastCol = col
                else:
                    lastCol = -1
    if res is 0:
        print("impossible")
    else:
        print(res)

def main():
    m, n = list(map(int, input().split()))
    land = []
    for _ in range(m):
        arr = list(input())
        land.append(arr)
    solve(n, m, land)

if __name__ == "__main__":
    main()
