class Solution:
    directions = [(0,1), (0,-1), (1,0), (-1, 0)]
    
    def dfs(self, i, j, prev_i, prev_j, grid, visited):
        visited[i][j] = True
        
        for i_, j_ in self.directions:
            new_i = i + i_
            new_j = j + j_

            if new_i >= 0 and new_i < self.m and new_j >= 0 and new_j < self.n and grid[i][j] == grid[new_i][new_j]:
                if new_i == prev_i and new_j == prev_j:
                    continue
                
                if visited[new_i][new_j]:
                    return True
                
                if self.dfs(new_i, new_j, i, j, grid, visited):
                    return True
        
        return False


    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])
        
        visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j]:
                    if self.dfs(i, j, -1, -1, grid, visited):
                        return True
            
        return False
