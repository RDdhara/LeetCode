class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            if num > 10 and num < 100 and (num % 11 == 0):
                count += 1

            if num > 1000 and num < 10000:
                first = (num // 1000) % 10
                second = (num // 100) % 10
                third = (num // 10) % 10
                forth = num % 10

                if first + second == third + forth:
                    count += 1

        return count
