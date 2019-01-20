class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = list()
        reverse = ''
        
        input_string = str(x)
        
        if x < 0: return False
        
        for num_string in input_string:
            number.append(num_string)
        
        for i in range(len(number)):
            reverse += number.pop()
        
        if x == int(reverse):
            return True
        else:
            return False

# 这个思路所需时间太长了，请参考leetcode的solution