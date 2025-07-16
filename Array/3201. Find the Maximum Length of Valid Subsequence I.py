class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = 0
        odd_count = 0
        odd_even_count = 1

        if nums[0] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        state_ = nums[0] % 2

        for i in range(1, len(nums)):
            curr_state = nums[i] % 2

            if curr_state != state_:
                odd_even_count += 1
                state_ = curr_state

            if curr_state == 0:
                even_count += 1
            else:
                odd_count += 1

        return max(even_count, odd_count, odd_even_count)
