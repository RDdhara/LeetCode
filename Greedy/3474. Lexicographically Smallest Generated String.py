class Solution:
    def same(self, str1, str2, i, m):
        for j in range(m):
            if str1[i] != str2[j]:
                return False
            
            i += 1
        
        return True

    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        result_size = m + n - 1

        result = ['@'] * result_size
        can_change = [False] * result_size

        for i in range(n):
            if str1[i] == 'T':
                i_ = i
                
                for j in range(m):
                    if result[i_] != '@' and result[i_] != str2[j]:
                        return ""

                    result[i_] = str2[j]
                    i_ += 1 
            
        for i in range(result_size):
            if result[i] == '@':
                result[i] = 'a'
                can_change[i] = True
        
        for i in range(n):
            if str1[i] == 'F':
                if self.same(result, str2, i, m):
                    change = False

                    for k in range(i+m-1, i-1, -1):
                        if can_change[k] == True:
                            result[k] = 'b'
                            change = True
                            break
                    
                    if not change:
                        return ""

        return "".join(result)
