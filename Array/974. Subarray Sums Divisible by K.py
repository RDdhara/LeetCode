class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_count = defaultdict(int)
        mod_count[0] = 1
        prefix_sum = 0
        result = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum % k
            if rem < 0:
                rem += k
            if rem in mod_count:
                result += mod_count[rem]
            mod_count[rem] += 1

        return result
