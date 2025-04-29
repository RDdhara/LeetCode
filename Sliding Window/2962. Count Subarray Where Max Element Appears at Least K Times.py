class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        i, j = 0, 0
        result = 0
        count = 0

        while j < len(nums):
            if nums[j] == max_num:
                count += 1
            while count >= k:
                result += (len(nums) - j)

                if nums[i] == max_num:
                    count -= 1
                i += 1

            j += 1
        
        return result
