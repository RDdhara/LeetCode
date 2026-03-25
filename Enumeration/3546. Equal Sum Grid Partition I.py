class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        row_sum = [0] * m
        col_sum = [0] * n
        total_sum = 0

        for i in range(m):
            for j in range(n):
                num = grid[i][j]

                row_sum[i] += num
                col_sum[j] += num
                total_sum += num

        if total_sum % 2 != 0:
            return False
        
        sum_ = 0
        for i in range(m-1):
            sum_ += row_sum[i]
            if sum_ == total_sum - sum_:
                return True

        sum_ = 0
        for j in range(n-1):
            sum_ += col_sum[j]
            if sum_ == total_sum - sum_:
                return True 

        return False
