class Solution:
    def solve(self, tops: List[int], bottoms: List[int], n: int) -> int:
        top_swap = 0
        bottom_swap = 0

        # check rotation of all n domino in both side
        for i in range(len(tops)):
            if tops[i] != n and bottoms[i] != n:
                return -1
            elif bottoms[i] != n:
                top_swap += 1
            elif tops[i] != n:
                bottom_swap += 1

        return min(top_swap, bottom_swap)


    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = len(tops) + 1

        # brute forcely check all possible values
        for i in range(1, 7):
            rotate = self.solve(tops, bottoms, i)
            if rotate != -1:
                result = min(result, rotate)
            
        return result if result != (len(tops) + 1) else -1
        
