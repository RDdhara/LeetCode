class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = -1
        max_idx = -1
        u = -1     # not in minK-maxK
        result = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                u = i
            if nums[i] == minK:
                min_idx = i
            if nums[i] == maxK:
                max_idx = i

            smaller = min(min_idx, max_idx)
            temp = smaller - u
            result += 0 if temp <= 0 else temp

        return result
