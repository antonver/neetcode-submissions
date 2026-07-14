class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = [dict() for _ in range((len(board)*len(board[0])) // 9)]
        columns = [dict() for i in range(len(board[0]))]
        rows = [dict() for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if grid[(i//3) * 3 + (j // 3)].get(board[i][j]):
                    return False
                else:
                    grid[(i//3) * 3 + (j // 3)][board[i][j]] = 1
                if columns[j].get(board[i][j]):
                    return False
                else:
                    columns[j][board[i][j]] = 1
                if rows[i].get(board[i][j]):
                    return False
                else:
                    rows[i][board[i][j]] = 1
        return True
