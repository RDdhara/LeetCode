class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] >= 1 and row-1 >= 0:
                    matrix[row][col] += matrix[row-1][col]
                
            curr_row = sorted(matrix[row], reverse = True)

            for i in range(n):
                height = curr_row[i]
                base = i+1
                
                result = max(result, height * base)
        
        return result
