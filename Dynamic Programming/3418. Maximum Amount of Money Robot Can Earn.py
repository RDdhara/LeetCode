class Solution:
    def solve(self, coins, i, j, n_):
        if i == self.m-1 and j == self.n-1:
            if coins[i][j] < 0 and n_ > 0:
                return 0
        
            return coins[i][j]
        
        if i >= self.m or j >= self.n:
            return float("-inf")
        
        if self.mem[i][j][n_] != float("-inf"):
            return self.mem[i][j][n_]
        
        take = coins[i][j] + max(self.solve(coins, i+1, j, n_), self.solve(coins, i, j+1, n_))
        
        skip = float("-inf")

        if coins[i][j] < 0 and n_ > 0:
            skip_down = self.solve(coins, i+1, j, n_-1)
            skip_right = self.solve(coins, i, j+1, n_-1)

            skip = max(skip_down, skip_right)
        
        self.mem[i][j][n_] = max(take, skip)

        return self.mem[i][j][n_]


    def maximumAmount(self, coins: List[List[int]]) -> int:
        self.m = len(coins)
        self.n = len(coins[0])

        self.mem = [[[float("-inf")] * 3 for _ in range(self.n)] for _ in range(self.m)]

        return self.solve(coins, 0, 0, 2)
