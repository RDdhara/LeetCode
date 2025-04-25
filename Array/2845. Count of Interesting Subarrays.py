class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        result = 0
        s = 0

        for num in nums:
            if num % modulo == k:
                s += 1
            result += cnt[(s - k + modulo) % modulo]
            cnt[s % modulo] += 1
        return result
