class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i-1 >= 0: grid[i][j] += grid[i-1][j]
                if j-1 >= 0: grid[i][j] += grid[i][j-1]
                if j-1 >= 0 and i-1 >= 0:
                    grid[i][j] -= grid[i-1][j-1]
                
                if grid[i][j] <= k:
                    result += 1
                else:
                    break

        return result
