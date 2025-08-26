class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for length, width in dimensions:
            diagonal = length * length + width * width
            area = length * width

            if max_diagonal < diagonal:
                max_diagonal = diagonal
                max_area = area
            elif max_diagonal == diagonal:
                max_area = max(max_area, area)

        return max_area
