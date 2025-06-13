class Solution:
    def solve(self, x, nums, n, p):
        count = 0
        i = 0
        while i < n - 1:
            if abs(nums[i] - nums[i+1]) <= x:
                count += 1
                i += 2
            else:
                i += 1
            if count == p:
                return True
        return False

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)
        l = 0
        r = nums[n-1] - nums[0]
        result = r

        while l <= r:
            mid = l + (r-l) // 2
            if self.solve(mid, nums, n, p):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
