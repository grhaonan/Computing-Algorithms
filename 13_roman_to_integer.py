class Solution:
    def romanToInt(self, s):
        #Define a dictionary with roman numeral mapping
        roman = dict (M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1)
        result = 0
        #looping through the input
        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result + roman[s[-1]]

# The solution doesn't include the Rome numeral input validation, such as all capital letter, valide number combination

