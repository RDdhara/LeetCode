class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_dis = 0
        east = 0
        west = 0
        north = 0
        south = 0

        for i in range(len(s)):
            if s[i] == 'N': north += 1
            elif s[i] == 'S': south += 1
            elif s[i] == 'E': east += 1
            elif s[i] == 'W': west += 1

            dist = abs(north - south) + abs(east - west)
            steps = i + 1
            false_steps = min(steps - dist, 2*k)

            max_dis = max(max_dis, dist + false_steps)

        return max_dis
