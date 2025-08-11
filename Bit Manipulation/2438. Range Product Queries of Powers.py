class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        Mod = 10**9 + 7
        result = []
        power = []

        for i in range(32):
            if n & (1 << i) != 0:
                power.append(1 << i)

        for start, end in queries:
            temp = 1
            for i in range(start, end+1):
                temp = (temp * power[i]) % Mod
        
            result.append(temp)

        return result    
