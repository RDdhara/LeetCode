class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        freq = 1

        for i in range(1, len(s)):
            if s[i] == result[-1]:
                freq += 1
                if freq < 3:
                    result += s[i]
            else:
                result += s[i]
                freq = 1

        return result
