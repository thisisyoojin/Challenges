import time

def decorator(func):
    def wrapper(num):
        print('start')
        func(num)
        print('end')
    return wrapper


def measureTime(func):
    def wrapper(num):
        startingTime = time.time()
        func(num)
        endingTime = time.time()
        print(endingTime - startingTime)
    return wrapper


def wordDecorator(func):
    def wrapper(startingWord, endingWord, num):
        print(startingWord)
        func(num)
        print(endingWord)
    return wrapper


# @decorator
# @measureTime
@wordDecorator
def printNumber(num):
    for i in range(1,num):
        print(i)


printNumber('start', 'end', 10)


