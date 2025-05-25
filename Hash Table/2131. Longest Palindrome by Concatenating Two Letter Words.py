class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)          # SC: O(n)
        for word in words:
            count[word] += 1

        result = 0
        mid_used = False

        for word in list(count.keys()):    # TC: O(n)  ->   in worst time hash map have all different key
            rev = word[::-1]

            if word != rev:      # 'ab', 'ba' such type of string
                if rev in count:
                    pair_count = min(count[word], count[rev])  # count how many pair possible whit this tr at once
                    result += (pair_count * 4)
                    count[word] -= pair_count
                    count[rev] -= pair_count
            else:                # 'aa', 'bb' such type of string
                pair_count = count[word] // 2
                result += (pair_count * 4)
                count[word] -= pair_count * 2
                if count[word] == 1 and not mid_used:
                    result += 2
                    mid_used = True

        return result
