class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        # loop through and count
        for num in nums:
            if num == 0:
                if curr_len > 0:
                    max_len = max(max_len, curr_len)
                    curr_len = 0
            else:
                curr_len += 1
        # check last segment!
        if curr_len > max_len:
            return curr_len

        # return max seen
        return max_len