

# create a function which returns true if the number is a multiple of 7 and false otherwise
def isMultiple7(num):
    if num % 7 == 0:
        return True
    return False


# write a for loop that prints the first 100 fibonnaci numbers
n1, n2 = 0, 1

for i in range(100):
    
    #print fibonnaci numbers
    # print(n1)

    #check the number is multiple of 7
    isMultiple7(n1)

    #check the number is multiple of 7
    if n1 >= 100:
        print(f"{n1} is larger than 100")
    elif n1 < 50:
        print(f"{n1} is less than 50")
    
    # save the value temporarily
    temp = n1
    # assign bigger number to smaller number
    n1 = n2
    # add original small number to bigger number
    n2 += temp


