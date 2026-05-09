class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2 # total number of layer

        # rotate layer by layer
        for layer in range(layers):
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            temp_list = []

            # take : top-left to top-right 
            for i in range(left, right + 1):
                temp_list.append(grid[top][i])
            
            # take : top-right to bottom-right
            for i in range(top + 1, bottom + 1):
                temp_list.append(grid[i][right])

            # take : bottom-right to bottom-left 
            for i in range(right - 1, left - 1, -1):
                temp_list.append(grid[bottom][i])
            
            # take : bottom-left to top-left
            for i in range(bottom - 1, top, -1):
                temp_list.append(grid[i][left])
            
            redused_k = k % len(temp_list)
            temp_list[:] = temp_list[redused_k : ] + temp_list[ : redused_k]

            j = 0   # initial index of temp_list

            # give : top-left to top-right 
            for i in range(left, right + 1):
                grid[top][i] = temp_list[j]
                j += 1
            
            # give : top-right to bottom-right
            for i in range(top + 1, bottom + 1):
                grid[i][right] = temp_list[j]
                j += 1

            # give : bottom-right to bottom-left 
            for i in range(right - 1, left - 1, -1):
                grid[bottom][i] = temp_list[j]
                j += 1
            
            # give : bottom-left to top-left
            for i in range(bottom - 1, top, -1):
                grid[i][left] = temp_list[j]
                j += 1
        
        return grid
