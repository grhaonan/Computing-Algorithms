class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        all_letters = []
        result = []
         #retreive all letters from the input string and put them into to a new, seperated list
        all_letters = [x for x in S if x.isalpha()]
        
        for x in S:
            if x.isalpha():
                result.append(all_letters.pop())
            else:
                result.append(x)
        return ''.join(result)

#这里的reverse也用到了堆栈的思路和实现方法。除此之外还有一个tricks就是使用''.join()的方法快速将一个list转化为string