class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0]  * 26
        for ch in word:
            freq[ord(ch) - ord("a")] += 1

        freq.sort()
        result = len(word)
        cum_delete = 0

        for i in range(26):
            del_ = cum_delete
            for j in range(25, -1, -1):
                if freq[j] - freq[i] <= k:
                    break
                del_ += (freq[j] - freq[i] - k)
            
            result = min(result, del_)
            cum_delete += freq[i]

        return result
