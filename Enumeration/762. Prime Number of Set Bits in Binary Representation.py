class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
        result = 0

        for num in range(left, right + 1):
            if num.bit_count() in prime_numbers:
                result += 1
        
        return result
