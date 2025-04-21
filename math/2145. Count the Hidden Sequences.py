class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0
        max_val = 0
        min_val = 0

        for diff in differences:
            curr += diff
            max_val = max(max_val, curr)
            min_val = min(min_val, curr)

            if (upper - max_val) - (lower - min_val) + 1 <= 0:
                return 0

        return (upper - max_val) - (lower - min_val) + 1
