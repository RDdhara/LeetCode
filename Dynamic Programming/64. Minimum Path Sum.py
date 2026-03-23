class Solution:
    def solve(self, grid, i, j, mem):
        if i == self.m - 1 and j == self.n - 1:
            return grid[i][j]
        
        if mem[i][j] != -1:
            return mem[i][j]
        
        if i == self.m-1:
            mem[i][j] = grid[i][j] + self.solve(grid, i, j+1, mem)
            return mem[i][j]
        elif j == self.n-1:
            mem[i][j] = grid[i][j] + self.solve(grid, i+1, j, mem)
            return mem[i][j]
        else:
            mem[i][j] = grid[i][j] + min(self.solve(grid, i, j+1, mem), self.solve(grid, i+1, j, mem))
            return mem[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        mem = [[-1] * (self.n+1) for _ in range(self.m+1)]

        return self.solve(grid, 0, 0, mem)
