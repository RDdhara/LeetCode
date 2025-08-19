class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                j = i
                while j < n and nums[j] == 0:
                    result += (j - i + 1)
                    j += 1
                i = j
            else:
                i += 1

        return result
