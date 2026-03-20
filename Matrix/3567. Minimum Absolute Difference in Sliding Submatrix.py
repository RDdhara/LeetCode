class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for r in range(m-k+1):
            for c in range(n-k+1):
                temp = []
                for i in range(r, r+k):
                    for j in range(c,c+k):
                        temp.append(grid[i][j])
                
                if k == 1:
                    ans[r][c] = 0
                    continue
                
                temp = sorted(set(temp))
                if len(temp) <= 1:
                    ans[r][c] = 0
                    continue
                
                mini = float('inf')

                for x in range(1, len(temp)):
                    mini = min(mini, abs(temp[x] - temp[x-1]))
                
                ans[r][c] = mini
            
        return ans
                
