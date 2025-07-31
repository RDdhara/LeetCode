class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        result = set()

        for num in arr:
            curr = {num}
            for x in prev:
                curr.add(x | num)
            result.update(curr)
            prev = curr

        return len(result)
