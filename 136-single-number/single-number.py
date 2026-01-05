class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if nums.count(num) != 2:
                return num