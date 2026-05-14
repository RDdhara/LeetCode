class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        seen = set()
        n_duplicate = False

        for num in nums:
            if num > n:
                return False
        
            if num in seen:
                if num < n or n_duplicate:
                    return False

                n_duplicate = True
                continue
            
            seen.add(num)
        
        return True
        
            
