class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        k = k % n

        if k == 0:
            return True

        for i in range(m):
            for j in range(n):
                curr = j
                next = -1

                if i % 2 == 0:
                    next = (j + k) % n
                else:
                    next = (j - k + n) % n
                
                if mat[i][curr] != mat[i][next]:
                    return False
        
        return True
