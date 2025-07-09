class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0])

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])

        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[:k+1])
        ans = window
        for i in range(k+1, n+1):
            window -= gaps[i-(k+1)]
            window += gaps[i]
            ans = max(ans, window)
        return ans
