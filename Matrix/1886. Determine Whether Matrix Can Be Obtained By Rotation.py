class Solution:
    def rotate(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(n):
            mat[i].reverse()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)

        for x in range(4):
            equal = True

            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        equal = False
                        break
                if not equal:
                    break

            if equal:
                return True
            else:
                self.rotate(mat)

        return False        
