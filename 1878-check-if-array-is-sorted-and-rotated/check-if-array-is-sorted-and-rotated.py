def sorted(nums):
    is_sorted=True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            is_sorted=False
    if is_sorted == True:
        return True
class Solution:
    def check(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums)):
            if sorted(nums):
                res = 1
            else:
                nums.append(nums[0])
                nums.remove(nums[0])
        if res == 1:
            return True
        else:
            return False