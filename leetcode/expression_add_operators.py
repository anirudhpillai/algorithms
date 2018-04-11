class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
            
        result = []
        
        def helper(accumulated, last, expression, leftover):
            if not leftover:
                if accumulated == target:
                    result.append(expression)
            
            for i in range(len(leftover)):
                val = leftover[:i+1]
                
                
                if not expression:
                    if i == 0 or val[0] != "0":
                        helper(int(val), int(val), val, leftover[i+1:])
                elif i == 0 or val[0] != "0":
                    helper(accumulated + int(val), int(val), expression + "+" + val, leftover[i+1:])
                    helper(accumulated - int(val), -int(val), expression + "-" + val, leftover[i+1:])
                    helper(accumulated - last + last * int(val), last * int(val), expression + "*" + val, leftover[i+1:])
        
        helper(0, 1, "", num)
        return result
