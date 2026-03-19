class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cum_sum_x = [[0] * n for _ in range(m)]
        cum_sum_y = [[0] * n for _ in range(m)]
        
        count = 0

        for i in range(m):
            for j in range(n):
                # X prefix sum
                if i-1 >= 0:
                    cum_sum_x[i][j] += cum_sum_x[i-1][j]
                if j-1 >= 0:
                    cum_sum_x[i][j] += cum_sum_x[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    cum_sum_x[i][j] -= cum_sum_x[i-1][j-1]
                if grid[i][j] == 'X':
                    cum_sum_x[i][j] += 1

                 # Y prefix sum
                if i-1 >= 0:
                    cum_sum_y[i][j] += cum_sum_y[i-1][j]
                if j-1 >= 0:
                    cum_sum_y[i][j] += cum_sum_y[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    cum_sum_y[i][j] -= cum_sum_y[i-1][j-1]
                if grid[i][j] == 'Y':
                    cum_sum_y[i][j] += 1

                if cum_sum_x[i][j] > 0 and cum_sum_x[i][j] == cum_sum_y[i][j]:
                    count += 1
        
        return count

"""
m = len(grid)
        n = len(grid[0])

        cum_sum_x = [[0] * n for _ in range(m)]
        cum_sum_y = [[0] * n for _ in range(m)]
        
        count = 0

        for i in range(m):
            for j in range(n):
                cum_sum_x[i][j] = (grid[i][j] == 'X')
                cum_sum_y[i][j] = (grid[i][j] == 'Y')

                if i-1 >= 0:
                    cum_sum_x[i][j] += cum_sum_x[i-1][j]
                    cum_sum_y[i][j] += cum_sum_y[i-1][j]
                if j-1 >= 0:
                    cum_sum_x[i][j] += cum_sum_x[i][j-1]
                    cum_sum_y[i][j] += cum_sum_y[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    cum_sum_x[i][j] -= cum_sum_x[i-1][j-1]
                    cum_sum_y[i][j] -= cum_sum_y[i-1][j-1]


                if cum_sum_x[i][j] > 0 and cum_sum_x[i][j] == cum_sum_y[i][j]:
                    count += 1
        
        return count
"""
