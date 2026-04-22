class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for q in queries:
            for d in dictionary:
                diff_count = 0
                n = min(len(q), len(d))
                for i in range(n):
                    if q[i] != d[i]:
                        diff_count += 1
                    
                    if diff_count > 2:
                        break
                
                if diff_count <= 2:
                    result.append(q)
                    break
        
        return result
