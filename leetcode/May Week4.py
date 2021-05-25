# import operator
# tokens = ["4", "13", "5", "/", "+"]
# tokens2 = ["4", "(13 / 5)", "+"]

#i-2,i-1,i
#~i-3
#i+1~

ops = ["+", "-", "*", "/"]

def isAnyOperator(tokens):
    for token in tokens:
        if token in ops:
            return True
    return False


def calculate(values):
    print('Calculating...')
    result=[]
    for i in range(len(values)):
        if values[i] in ops:
            print('values:',values)    
            if len(values) > 3:
                result.extend(values[i-3])
            result.append(f"({values[i-2]} {values[i]} {values[i-1]})")
            result.extend(values[i+1:])
            break

    if not isAnyOperator(result):
        return result
    else:
        calculate(result)

    

        
        
 
tokens = ["4", "13", "5", "/", "+"]
calculate(tokens)