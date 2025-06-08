class Solution:
    def solve(self, curr, n, result):
        if curr > n:
            return 
        result.append(curr)

        for i in range(10):
            new_num = (curr * 10) + i
            if new_num > n:
                continue
            self.solve(new_num, n, result)
            

    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, 10):
            self.solve(i, n, result)
        return result
        
