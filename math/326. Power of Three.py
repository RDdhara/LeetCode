class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        max_num = 3**19
        return max_num % n == 0
