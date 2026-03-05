class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        start_0 = 0

        for i in range(n):
            if i % 2 == 1 and s[i] == '0':
                start_0 += 1
            if i % 2 == 0 and s[i] == '1':
                start_0 += 1
        
        start_1 = n - start_0

        return min(start_0, start_1)
