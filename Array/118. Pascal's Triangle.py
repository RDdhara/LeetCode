class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            curr = [1] * (row + 1)

            for i in range(1, row):
                curr[i] = result[row - 1][i - 1] + result[row - 1][i]

            result.append(curr)
        
        return result
