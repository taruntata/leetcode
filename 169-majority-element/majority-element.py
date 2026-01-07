class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for item in nums:
            if item in res:
                res[item] += 1
            else:
                res[item] = 1
        return max(res ,key = res.get)