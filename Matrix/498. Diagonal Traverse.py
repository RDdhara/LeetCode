class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mp = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mp[i+j].append(mat[i][j])
        
        result = []
        reverse = True
        for i in range(len(mat) + len(mat[0]) - 1):
            if reverse:
                result.extend(mp[i][::-1])
            else:
                result.extend(mp[i])
            reverse = not reverse
        
        return result
