class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1 = defaultdict(str)
        map_2 = defaultdict(str)

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if (ch1 in map_1 and map_1[ch1] != ch2) or (ch2 in map_2 and map_2[ch2] != ch1):
                return False
            map_1[ch1] = ch2
            map_2[ch2] = ch1
        return True
