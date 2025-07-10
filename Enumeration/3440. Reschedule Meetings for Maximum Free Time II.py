class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0])

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])

        gaps.append(eventTime - endTime[-1])

        m = len(gaps)
        max_right_free = [0] * m
        max_left_free = [0] * m

        for i in range(m-2, -1, -1):
            max_right_free[i] = max(max_right_free[i+1], gaps[i+1])
        for i in range(1, m):
            max_left_free[i] = max(max_left_free[i-1], gaps[i-1])

        result = 0

        for i in range(1, m):
            curr_event = endTime[i-1] - startTime[i-1]

            if curr_event <= max(max_left_free[i-1], max_right_free[i]):
                #  move from current position
                result = max(result, gaps[i-1] + curr_event + gaps[i])
            
            # shift left or right
            result = max(result, gaps[i-1] + gaps[i])

        return result
