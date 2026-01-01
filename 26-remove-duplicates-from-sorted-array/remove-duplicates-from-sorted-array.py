class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums)
        index = 0
        for i in set_nums:
            nums[index] = i
            index += 1
        for i in range(len(nums) - len(set_nums)):
            nums.pop()
        nums.sort()