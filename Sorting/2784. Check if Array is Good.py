class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        nums.sort()

        n = 1
        for i in range(len(nums) - 2):
            if nums[i] != n:
                return False
            
            n += 1
        
        return nums[-1] == nums[-2] and nums[-1] == n
