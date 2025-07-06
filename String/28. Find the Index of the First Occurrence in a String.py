class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        res = -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i : i+n] == needle:
                return i
        return -1
