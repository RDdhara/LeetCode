class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)

        cum_sum = 0
        for i in range(len(nums)):
            left_sum = cum_sum
            right_sum = sum_ - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            
            cum_sum += nums[i]
            
        return -1
