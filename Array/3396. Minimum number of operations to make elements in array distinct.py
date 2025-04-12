class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        count = defaultdict(int)
        index = -1
        for i in range(len(nums) - 1, -1, -1):
            count[nums[i]] += 1
            if count[nums[i]] == 2:
                index = i
                break
        if index == -1:
            return 0
            
        return math.ceil((index + 1) / 3)
