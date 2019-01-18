class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_in_string = ''

        for element in digits:
            digits_in_string += str(element)
    
        digits_in_integer = int(digits_in_string)
        digit_plus_one = digits_in_integer +1
        digit_plus_one_in_string = str(digit_plus_one)
        
        return list(int(i) for i in digit_plus_one_in_string)
      
        