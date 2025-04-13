class Solution:
    def pow(self, x: int, n: int) -> int:   # binary exponentiation
        M = 10**9 + 7
        if n == 0:
            return 1
        half = self.pow(x, n//2)
        result = (half * half) % M
        if n % 2 == 1:
            result = (result * x) % M
        return result

    def countGoodNumbers(self, n: int) -> int:
        M = 10**9 + 7
        prime = n // 2
        odd = n - prime

        return self.pow(4, prime) * self.pow(5, odd) % M
