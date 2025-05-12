class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        count = [0] * 10
        for i in digits:
            count[i] += 1

        result = []
        for i in range(1, 10):
            if count[i] == 0: continue
            count[i] -= 1

            for j in range(10):
                if count[j] == 0: continue
                count[j] -= 1

                for k in range(0, 9, 2):
                    if count[k] == 0: continue
                    num = (i * 100) + (j * 10) + k
                    result.append(num)

                count[j] += 1
            count[i] += 1

        return result
