class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        result = float("inf")

        for k in range(len(nums)):
            pos[nums[k]].append(k)

            if len(pos[nums[k]]) >= 3:
                i = pos[nums[k]][-3]
                temp_dis = k-i

                result = min(result, temp_dis)
        
        return -1 if result == float("inf") else 2 * result
