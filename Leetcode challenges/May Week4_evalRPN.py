import operator
import math
from typing import List

#defined the operation dictinaries to call
ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

class Solution:
    #defined the function for calculation 
    def evalRPN(self, tokens: List[str]) -> int:
        
        # if the token length is 1, then there is no operand to left
        if len(tokens) == 1:
            return tokens[0]

        # otherwise, create a empty list to put calculated numbers
        result=[]

        for i in range(len(tokens)):
            # when there is an operation
            if tokens[i] in ops.keys():
                # calculate the result with two numbers ahead the operation and truncate the result
                res = math.trunc(ops[tokens[i]](int(tokens[i-2]), int(tokens[i-1])))
                
                # create a new list with calculated result
                result.extend(tokens[:i-2])
                result.append(res)
                result.extend(tokens[i+1:])
                break
            
        # call RPN function again
        return self.evalRPN(result)
        
        
        