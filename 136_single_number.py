class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []

        for i in range(len(nums)):
            if nums[i] in result:
                result.remove(nums[i])
            else:
                result.append(nums[i])
        return result[0]
    
#This solution proves to be extremly time consuming. please refer to leetcode
#official solution 4 as a leaner approach.