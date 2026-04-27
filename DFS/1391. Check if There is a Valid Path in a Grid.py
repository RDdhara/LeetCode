class Solution:
    dir = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }

    def dfs(self, i, j, grid, visited):
        if i == self.m - 1 and j == self.n - 1:
            return True
        
        visited[i][j] = True

        for i_, j_ in self.dir[grid[i][j]]:
            new_i = i + i_
            new_j = j + j_

            if new_i < 0 or new_i >= self.m or new_j < 0 or new_j >= self.n or visited[new_i][new_j]:
                continue
            
            for x, y in self.dir[grid[new_i][new_j]]:
                if new_i + x == i and new_j + y == j:
                    if self.dfs(new_i, new_j, grid, visited):
                        return True

        return False


    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if grid[0][0] == 5: return False
        if grid[-1][-1] == 4: return False

        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]
        
        return self.dfs(0, 0, grid, visited)
