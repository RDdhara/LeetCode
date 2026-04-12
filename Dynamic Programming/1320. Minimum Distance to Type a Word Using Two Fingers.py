class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def dp(si, f1, f2):
            if si == len(word):
                return 0
            
            result = inf

            s = word[si]
            pos = ord(s) - ord('A')
            i, j = pos // 6, pos % 6

            d1 = 0 if f1 == (-1, -1) else abs(i - f1[0]) + abs(j - f1[1])
            result = min(result, d1 + dp(si + 1, (i, j), f2))

            d2 = 0 if f2 == (-1, -1) else abs(i - f2[0]) + abs(j - f2[1])
            result = min(result, d2 + dp(si + 1, f1, (i, j)))

            return result
        
        return dp(0, (-1, -1), (-1, -1))
