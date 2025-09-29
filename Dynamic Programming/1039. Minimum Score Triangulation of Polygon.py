class Solution:
    def solve(self, val, i, j, dp):
        if i + 1 == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        result = float("inf")
        for k in range(i+1, j):
            result = min(result, val[i]*val[j]*val[k] + self.solve(val, i, k, dp) + self.solve(val, k, j, dp))
        
        dp[i][j] = result
        return dp[i][j]


    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]

        return self.solve(values, 0, n-1, dp)
