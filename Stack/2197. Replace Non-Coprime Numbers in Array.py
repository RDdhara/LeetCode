from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            while result:
                prev = result[-1]
                curr = num

                GCD = gcd(prev, curr)
                if GCD == 1: break

                result.pop()
                LCM = prev // GCD * curr
                num = LCM

            result.append(num)

        return result
