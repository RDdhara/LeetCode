class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lower_last_occ = [-1] * 26
        upper_first_occ = [-1] * 26

        for i in range(n):
            ch = word[i]
            if ch.islower():
                lower_last_occ[ord(ch) - ord('a')] = i
            else:
                if upper_first_occ[ord(ch) - ord('A')] == -1:
                    upper_first_occ[ord(ch) - ord('A')] = i
        
        count = 0
        for i in range(26):
            if lower_last_occ[i] != -1 and upper_first_occ[i] != -1 and lower_last_occ[i] < upper_first_occ[i]:
                count += 1
        
        return count
