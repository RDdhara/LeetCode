class Solution:
    def numTilings(self, n: int) -> int:
        M = 10 ** 9 + 7

        if n == 1 or n == 2:
            return n
        dp = [-1] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = ((2 * dp[i - 1] % M) + (dp[i - 3] %M)) % M
        return dp[n]
