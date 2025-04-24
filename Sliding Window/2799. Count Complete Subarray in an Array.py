class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(set(nums))
        count = defaultdict(int)
        i = 0
        j = 0
        result = 0
        while(j < n):
            count[nums[j]] += 1
            while len(count) == m:
                result += (n-j)
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i +=1
            j += 1

        return result
