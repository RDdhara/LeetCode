class Solution:
    def solve(self, string, suff, limit):
        n = len(string)
        m = len(suff)
        
        if n < m:
            return 0

        count = 0
        remaining_length = n - m
        remaining_str = string[: remaining_length]

        for i in range(remaining_length):
            digit = int(string[i])
            if digit <= limit:
                count += (digit * (limit+1) ** (remaining_length - i - 1))
            else:
                count += ((limit+1) ** (remaining_length - i))
                return count

        if string[remaining_length :] >= suff:
            count += 1

        return count

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start_str = str(start - 1)
        finish_str = str(finish)
        return self.solve(finish_str, s, limit) - self.solve(start_str, s, limit)
