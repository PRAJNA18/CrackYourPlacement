class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                ones = 0
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                        if abs(board[ni][nj]) == 1:
                            ones += 1
                
                if board[i][j] == 1:
                    if ones < 2 or ones > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if ones == 3:
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0