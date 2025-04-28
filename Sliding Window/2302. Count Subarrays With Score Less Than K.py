class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        i, j = 0, 0
        sum_ = 0
        while j < len(nums):
            sum_ += nums[j]
            while i <= j and sum_ * (j - i + 1) >= k:
                sum_ -= nums[i]
                i += 1
            result += (j - i + 1)
            j += 1
        return result
