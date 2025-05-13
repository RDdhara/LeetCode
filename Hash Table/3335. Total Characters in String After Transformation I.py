class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        M = 10**9 + 7
        count = [0] * 26  # for 'a' to 'z'

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            temp = [0] * 26
            for i in range(26):
                if i < 25:  # 'a' to 'y'
                    temp[i + 1] = (temp[i + 1] + count[i]) % M
                else:  # 'z'
                    temp[0] = (temp[0] + count[i]) % M  # 'a'
                    temp[1] = (temp[1] + count[i]) % M  # 'b'
            count = temp

        return sum(count) % M

        
