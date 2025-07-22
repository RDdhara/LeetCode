class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        i = 0
        j = 0
        sum_ = 0
        result = 0

        while j < n:
            if nums[j] not in st:
                sum_ += nums[j]
                result = max(result, sum_)
                st.add(nums[j])
                j += 1
            else:
                while i < n and nums[j] in st:
                    sum_ -= nums[i]
                    st.remove(nums[i])
                    i += 1

        return result
