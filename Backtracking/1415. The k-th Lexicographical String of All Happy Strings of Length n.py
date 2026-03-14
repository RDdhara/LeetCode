class Solution:
    def solve(self, n, curr, k):
        if len(curr) == n:
            self.counter += 1
            if self.counter == k:
                self.result = "".join(curr)
            return 

        for ch in "abc":
            if curr and curr[-1] == ch:
                continue
            
            curr.append(ch)

            self.solve(n, curr, k)

            curr.pop()

    def getHappyString(self, n: int, k: int) -> str:
        self.result = ""
        self.counter = 0

        self.solve(n, [], k)

        return self.result
