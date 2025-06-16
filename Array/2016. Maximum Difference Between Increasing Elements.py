class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_ = nums[0]
        diff = -1
        for i in range(1, len(nums)):
            if nums[i] > min_:
                diff = max(diff, nums[i] - min_)
            else:
                min_ = nums[i]
        return diff
