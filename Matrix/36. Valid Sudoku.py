class Solution:
    def solve(self, start_row, end_row, start_col, end_col, board):
        st = set()
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col+1):
                if board[row][col] == ".": continue
                if board[row][col] in st: return False
                st.add(board[row][col])
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            st = set()
            for col in range(9):
                if board[row][col] == ".": continue
                if board[row][col] in st: return False
                st.add(board[row][col])
        
        for col in range(9):
            st = set()
            for row in range(9):
                if board[row][col] == ".": continue
                if board[row][col] in st: return False
                st.add(board[row][col])

        for start_row in range(0, 9, 3):
            end_row = start_row + 2
            for start_col in range(0, 9, 3):
                end_col = start_col + 2
                if not self.solve(start_row, end_row, start_col, end_col, board):
                    return False
        
        return True
