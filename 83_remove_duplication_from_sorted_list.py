class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = []
        
        for i in head:
            if i not in result:
                result.append(i)
        return result