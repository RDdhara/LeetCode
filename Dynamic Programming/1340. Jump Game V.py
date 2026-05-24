class Solution:
    def solve(self, arr, i, d):
        if self.dp[i] != -1:
            return self.dp[i]

        result = 1
        # left side of i
        for j in range(i-1, max(0, i-d) - 1, -1):
            if arr[i] <= arr[j]:
                break
            result = max(result, 1 + self.solve(arr, j, d))

        # right side of i
        for j in range(i+1, min(self.n-1, i+d) + 1):
            if arr[i] <= arr[j]:
                break
            result = max(result, 1 + self.solve(arr, j, d))
        
        self.dp[i] = result
        return self.dp[i]

    def maxJumps(self, arr: List[int], d: int) -> int:
        self.n = len(arr)
        result = 1
        self.dp = [-1] * (self.n+1)

        for i in range(self.n):
            result = max(result, self.solve(arr, i, d))

        return result
