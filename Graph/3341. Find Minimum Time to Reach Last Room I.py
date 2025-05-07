class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(moveTime)
        n = len(moveTime[0])

        result = [[float('inf')] * n for _ in range(m)]
        pq = []

        result[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))  # time, i, j

        while pq:
            currTime, i, j = heapq.heappop(pq)

            if i == m - 1 and j == n - 1:   # reached end
                return currTime

            for dir in directions:
                i_, j_ = i + dir[0], j + dir[1]
                
                if 0 <= i_ < m and 0 <= j_ < n:
                    wait = max(moveTime[i_][j_] - currTime, 0)
                    arrTime = currTime + wait + 1
                    
                    if result[i_][j_] > arrTime:
                        result[i_][j_] = arrTime
                        heapq.heappush(pq, (arrTime, i_, j_))
        
        return -1  # if the bottom-right cell is unreachable
