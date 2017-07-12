class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(max(num1, num2, key=len))):
            a, b = 0, 0
            if i < len(num1):
                a = int(num1[i])
            if i < len(num2):
                b = int(num2[i])
            
            curr = a + b + carry
            if curr > 9:
                curr -= 10
                carry = 1
            else:
                carry = 0
            
            result += str(curr)
            
        if carry:
            result += "1"
            
        return result[::-1]
