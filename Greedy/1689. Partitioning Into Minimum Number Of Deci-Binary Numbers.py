class Solution:
    def minPartitions(self, n: str) -> int:
        # Since each step we can subtract a maximum of 1 from each digit, 
        # if we think greedily, the maximum valued digit of the number can be the answer.
        return int(max(n)) 
