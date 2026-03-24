class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        MOD = 12345

        pref_sum_mat = [[0] * n for _ in range(m)]

        suffix_sum = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                pref_sum_mat[i][j] = suffix_sum
                suffix_sum = (suffix_sum * grid[i][j]) % MOD

        prefix_sum = 1
        for i in range(m):
            for j in range(n):
                pref_sum_mat[i][j] = (prefix_sum * pref_sum_mat[i][j]) % MOD
                prefix_sum = (prefix_sum * grid[i][j]) % MOD
        
        return pref_sum_mat
