class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered_nums = []
        for num in nums:
            if num != val:
                filtered_nums.append(num)
        for idx, num in enumerate(filtered_nums):
            nums[idx] = num
        return len(filtered_nums)