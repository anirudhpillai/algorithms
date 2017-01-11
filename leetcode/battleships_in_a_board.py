class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        board = map(list, board)
        count = 0

        def dfs(x, y):
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if board[x][y] == 'X':
                    board[x][y] = 'O'
                    dfs(x+1, y)
                    dfs(x, y+1)
                    dfs(x-1, y)
                    dfs(x, y-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                dfs(i, j)

        return count


def countBattleships(board):
    """
    Better solution by counting only
    top left cell of each battleship
    """
    if len(board) == 0:
        return 0
    m, n = len(board), len(board[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') \
                and (j == 0 or board[i][j-1] == '.'):
                count += 1
    return count
