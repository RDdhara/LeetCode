class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for ch in moves:
            if ch == "R": x += 1
            elif ch == "L": x -= 1
            elif ch == "D": y += 1
            else: y -= 1

        return x == 0 and y == 0
