class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i+1, j+1]
            elif sum_ < target:
                i += 1
            else:
                j -= 1
