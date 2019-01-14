class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """ 
        result = ''
        for i in range (0, len(str)):
            if str[i].isupper():
                result += chr(ord(str[i])+32)
            else:
                result += str[i]
        return result

#解法利用到了ASICII 中大小写字母的数值相差32的特点