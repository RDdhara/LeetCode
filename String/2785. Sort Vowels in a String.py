class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = "AEIOUaeiou"
        
        vowel_list = [ch for ch in s if ch in vowel]
        vowel_list.sort()

        result = []

        j = 0
        for ch in s:
            if ch in vowel:
                result.append(vowel_list[j])
                j += 1
            else:
                result.append(ch)
        
        return "".join(result)
            
