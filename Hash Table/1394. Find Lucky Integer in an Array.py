class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1

        lucky_num = -1
        for key, val in count.items():
            if key == val:
                lucky_num = max(lucky_num, val)

        return lucky_num
