class Solution:
    def solve(self, n, num, x, dp):
        Mod = 10**9 + 7
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        num_power = num**x
        if num_power > n:
            return 0

        if dp[n][num] != -1:
            return dp[n][num]        

        take = self.solve(n - num_power, num + 1, x, dp)
        skip = self.solve(n, num + 1, x, dp)

        dp[n][num] =  (take + skip) % Mod
        return dp[n][num]

    def numberOfWays(self, n: int, x: int) -> int:
        dp = [[-1 for _ in range(301)] for _ in range(301)]
        return self.solve(n, 1, x, dp)
