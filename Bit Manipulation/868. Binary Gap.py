class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        curr = 0
        result = 0

        while n > 0:
            if n % 2 == 1:
                result = result if prev == -1 else max(result, curr - prev)
                prev = curr
            n //= 2
            curr += 1
        
        return result
