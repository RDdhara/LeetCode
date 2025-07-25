class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count = [-1] * 101
        max_neg = float("-inf")
        sum_ = 0

        for num in nums:
            if num <= 0:
                max_neg = max(max_neg, num)
            elif count[num] == -1:
                sum_ += num
                count[num] = 1

        return sum_ if sum_ > 0 else max_neg
