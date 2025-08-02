class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = defaultdict(int)
        min_elm = float("inf")

        for n in basket1:
            count[n] += 1
            min_elm = min(min_elm, n)
        for n in basket2:
            count[n] -= 1
            min_elm = min(min_elm, n)

        final_count = []

        for key, value in count.items():
            price = key
            cnt = value

            if cnt == 0:
                continue
            if cnt % 2 != 0:
                return -1
            for i in range(abs(cnt) // 2):
                final_count.append(price)

        final_count.sort()

        result = 0
        for i in range(len(final_count) // 2):
            result += min(final_count[i], min_elm * 2)

        return result
