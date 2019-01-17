class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result =[]
        #conver int to str and eventually to list
        input_as_list = list(str(x))

        for i in str(x):
            if ord(i) in range(48,58):
                number = input_as_list.pop()
                result.append(number)
            else:
                result.append(i)
        return int(''.join(result))

#这个题还没有做完，没有考虑input超出[-2^31, 2^31]范围需要返回0的问题
#其次我也不是很理解为什么使用for i in str(x)的时候 input_as_list.pop()是可以输出所有数值的。如果使用for i in input_as_list, 就只能pop出两个数值就停止了