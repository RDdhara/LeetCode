class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        result = float("inf")

        j = 0
        i = 0

        count_1 = 0
        count_2 = 0

        while j < n*2:
            expected_1 = '0' if (j % 2 == 0) else '1'
            expected_2 = '1' if (j % 2 == 0) else '0'

            if s[j % n] == expected_1:
                count_2 += 1
            else:
                count_1 += 1
            
            if j - i + 1 > n:
                expected_1 = '0' if (i % 2 == 0) else '1'

                if s[i % n] == expected_1:
                    count_2 -= 1
                else:
                    count_1 -= 1
                
                i += 1
                        
            if j - i + 1 == n:
                result = min(result, count_1, count_2)
            
            j += 1
    
        return result
