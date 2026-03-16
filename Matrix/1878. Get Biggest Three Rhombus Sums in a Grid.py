class Solution:
    def big_update(self, num, st):
        st.add(num) 

        if len(st) > 3:
            smallest = min(st)
            st.remove(smallest)

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        big_3 = set()

        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                self.big_update(grid[r][c], big_3)

                side = 1
                while r-side >= 0 and r+side < m and c-side >= 0 and c+side < n:
                    sum_ = 0
                    for k in range(side):
                        sum_  += grid[r-side+k][c+k]  #top to right
                        sum_  += grid[r+k][c+side-k]  #right to bottom
                        sum_  += grid[r+side-k][c-k]  #bottom to left
                        sum_  += grid[r-k][c-side+k]  #left to top
                    
                    self.big_update(sum_, big_3)
                    
                    side += 1

        return sorted(big_3, reverse = True)
