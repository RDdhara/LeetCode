class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        max_row = -1
        min_row = row
        max_col = -1
        min_col = col

        for i in range(row):
            for j in range(col):
                if(grid[i][j] == 1):
                    max_row = max(max_row, i)
                    min_row = min(min_row, i)
                    max_col = max(max_col, j)
                    min_col = min(min_col, j)

        return (max_row - min_row + 1) * (max_col - min_col+ 1)
