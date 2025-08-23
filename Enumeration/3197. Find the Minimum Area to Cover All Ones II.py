class Solution:
    def rotate(self, grid):
        m, n = len(grid), len(grid[0])
        rotated_grid = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_grid[j][m - i - 1] = grid[i][j]
        return rotated_grid

    def min_area(self, start_row, end_row, start_col, end_col, grid):
        m, n = len(grid), len(grid[0])
        min_row, max_row = m, -1
        min_col, max_col = n, -1

        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        if max_row == -1:
            return 0
        return (max_row - min_row + 1) * (max_col - min_col + 1)

    def calculate(self, grid):
        m, n = len(grid), len(grid[0])
        result = float('inf')

        # Case 1
        for row_split in range(1, m):
            for col_split in range(1, n):
                top = self.min_area(0, row_split, 0, n, grid)
                bottom_left = self.min_area(row_split, m, 0, col_split, grid)
                bottom_right = self.min_area(row_split, m, col_split, n, grid)
                result = min(result, top + bottom_left + bottom_right)

        # Case 2
        for row_split in range(1, m):
            for col_split in range(1, n):
                top_left = self.min_area(0, row_split, 0, col_split, grid)
                top_right = self.min_area(0, row_split, col_split, n, grid)
                bottom = self.min_area(row_split, m, 0, n, grid)
                result = min(result, top_left + top_right + bottom)

        # Case 3
        for split1 in range(1, m):
            for split2 in range(split1 + 1, m):
                top = self.min_area(0, split1, 0, n, grid)
                middle = self.min_area(split1, split2, 0, n, grid)
                bottom = self.min_area(split2, m, 0, n, grid)
                result = min(result, top + middle + bottom)

        return result

    def minimumSum(self, grid: List[List[int]]) -> int:
        result = self.calculate(grid)
        rotated_grid = self.rotate(grid)
        result = min(result, self.calculate(rotated_grid))
        return result
