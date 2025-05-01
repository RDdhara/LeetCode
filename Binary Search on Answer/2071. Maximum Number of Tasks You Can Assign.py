class Solution:
    def check(self, tasks: List[int], workers: List[int], pills: int, strength: int, mid: int) -> bool:
        pills_used = 0
        st = sorted(workers[:mid])  # best mid workers

        for i in range(mid - 1, -1, -1):
            reqrd = tasks[i]
            if st[-1] >= reqrd:
                st.pop()  # use the strongest available worker
            elif pills_used >= pills:
                return False
            else:
                # find the weakest worker which can do this strong task using pills
                idx = bisect_left(st, reqrd - strength)
                if idx == len(st):
                    return False
                del st[idx]
                pills_used += 1

        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m = len(tasks)
        n = len(workers)
        
        l = 0
        r = min(m, n)
        tasks.sort()
        workers.sort(reverse = True)

        result = 0

        while l <= r:
            mid = l + (r - l) // 2
            if self.check(tasks, workers, pills, strength, mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return result
