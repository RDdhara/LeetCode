class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0
        result = 0
        strick = 0

        for num in nums:
            if num > max_num:
                max_num = num
                result = 0
                strick = 0
            
            if num == max_num:
                strick += 1
            else:
                strick = 0
            
            result = max(result, strick)
        
        return result
