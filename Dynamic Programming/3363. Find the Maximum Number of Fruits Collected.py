class Solution:
    def child1(self, fruits, n):
        count = 0
        for i in range(n):
            count += fruits[i][i]

        return count

    def child2(self, i, j, fruits, n, dp):
        if i >= n or j < 0 or j >= n:
            return 0
        if i== n-1 and j == n-1:
            return 0
        if i == j or i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        bottom_left = fruits[i][j] + self.child2(i+1, j-1, fruits, n, dp)
        bottom = fruits[i][j] + self.child2(i+1, j, fruits, n, dp)
        bottom_right = fruits[i][j] + self.child2(i+1, j+1, fruits, n, dp)

        dp[i][j] = max(bottom_left, bottom, bottom_right)
        return dp[i][j]
    
    def child3(self, i, j, fruits, n, dp):
        if i >= n or j < 0 or j >= n:
            return 0
        if i== n-1 and j == n-1:
            return 0
        if i == j or i < j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        up_right = fruits[i][j] + self.child3(i-1, j+1, fruits, n, dp)
        right = fruits[i][j] + self.child3(i, j+1, fruits, n, dp)
        bottom_right = fruits[i][j] + self.child3(i+1, j+1, fruits, n, dp)

        dp[i][j] = max(up_right, right, bottom_right)
        return dp[i][j]

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        c1 = self.child1(fruits, n)
        c2 = self.child2(0, n-1, fruits, n, dp)
        c3 = self.child3(n-1, 0, fruits, n, dp)

        return c1 + c2 + c3
