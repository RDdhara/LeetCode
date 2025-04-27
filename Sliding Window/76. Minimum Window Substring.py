class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n: 
            return ""  

        mp = defaultdict(int)
        for ch in t:      # count all characters in t 
            mp[ch] += 1

        req_count = len(t)
        i, j = 0, 0
        window_size = float('inf')
        start_i = 0

        while(j < n):
            ch = s[j]

            if mp[ch] > 0:
                req_count -= 1
            mp[ch] -= 1

            while req_count == 0:
                curr_win_size = j - i + 1
                if window_size > curr_win_size:
                    window_size = curr_win_size
                    start_i = i

                mp[s[i]] += 1
                if mp[s[i]] > 0:
                    req_count += 1
                
                i += 1
            j += 1

        return "" if window_size == float('inf') else s[start_i : start_i + window_size]
