class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_set = set()
        count = 2**k

        for i in range(k, len(s) + 1):
            sub_str = s[i-k : i]

            if sub_str not in binary_set:
                binary_set.add(sub_str)
                count -= 1
            
            if count == 0:
                return True
        
        return False
