class Solution:
    def even_digit(self, num):
        count = 0
        while num > 0:
            count += 1
            num //= 10

        return count % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        # even_digit = lambda x : len(str(x)) & 1 == 0

        for num in nums:
            if self.even_digit(num):
                count += 1

        return count
