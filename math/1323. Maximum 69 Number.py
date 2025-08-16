class Solution:
    def maximum69Number (self, num: int) -> int:
        pos = -1
        i = 0
        temp = num

        while temp > 0:
            if temp % 10 == 6:
                pos = i
            temp //= 10
            i += 1

        if pos == -1:
            return num
        return num + (3 * (10**pos))
