class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        nums=[]
        n = len(pos) + len(neg)
        for i in range(n):
            if i%2 == 0:
                nums.append(pos[0])
                pos.remove(pos[0])
            else:
                nums.append(neg[0])
                neg.remove(neg[0])
        return nums