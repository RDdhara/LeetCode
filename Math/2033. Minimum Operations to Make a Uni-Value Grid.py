class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for i in grid for num in i]

        nums.sort()

        l = len(nums)
        target = nums[l//2]

        result = 0
        for num in nums:
            diff = abs(target - num)
            if diff % x != 0:
                return -1
            result += (diff // x)

        return result
