class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        for num in answers:
            count[num] += 1

        result = 0
        for key, value in count.items():
            curr = math.ceil(value / (key+1))
            result += (curr * (key+1))

        return result
