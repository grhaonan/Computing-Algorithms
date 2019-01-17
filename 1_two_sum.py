class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i

#enumerate的用法很奇妙