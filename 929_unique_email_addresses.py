class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for i in range(len(emails)):
            #Python list unpacking feature
            local, host = emails[i].split('@')
            if '+' in local:
                #如何在一个string中截取指定的前后段
                local = local[:local.index('+')]
            #如何在string中替换某一个字符
            result.add(local.replace('.','') + '@' + host)
        #利用到了set的element非duplicated的特性 
        return len(result)
