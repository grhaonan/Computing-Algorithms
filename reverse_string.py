class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        
        #The issue is that range doesnt support negative numbers
        for i in range (-1, -(len(s)+1),-1):
            result += s[i]
        
        return result

# 本道题的解法用到了堆栈的思想方法