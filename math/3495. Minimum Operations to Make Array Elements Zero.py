class Solution:
    def solve(self, left, right):
        L = 1
        S = 1
        steps = 0

        while L <= right:
            R = L * 4 - 1
            start = max(L, left)
            end = min(R, right)

            if start <= end:
                steps += (end - start + 1) * S

            S += 1
            L *= 4
        
        return steps


    def minOperations(self, queries: List[List[int]]) -> int:
        result = 0

        for left, right in queries:
            steps = self.solve(left, right)
            result += (steps + 1)// 2
        return result
