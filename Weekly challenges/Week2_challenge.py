# SIMPLE
"""
Create a dictionary with 3 keys
Index the dictionary to find the last letter of the first skill
"""

yoojin = {
    'name': 'Yoojin Ko',
    'skills': ['python', 'QA testing', 'communication'],
}

first_skill_last_letter = yoojin['skills'][0][-1]
print(first_skill_last_letter)


"""
Create a function which checks whether a word is a palindrome or not 
"""
def is_it_palindrome(word):
    # make the word lowercase
    word = word.lower()
    # divide the word in half (when the length is odd, no need to check the middle character)
    for i in range(len(word)//2):
        # compare characters from forward and backward, and if it doesn't match fail it
        if word[i] != word[len(word)-1-i]:
            return False
    return True
    
print(is_it_palindrome('NotPalindrome'))
print(is_it_palindrome('ABBCA'))


#%%
"""
Create a function which prints the first 100 fibonnaci numbers. Can you turn this into a recursive function which calls itself?
"""
fib_nums = [0,1]
def n_th_fibonnaci(nth):
    try:
        fib_nums[nth-1]
    except:
        fib_num = n_th_fibonnaci(nth-1) + n_th_fibonnaci(nth-2)
        fib_nums.append(fib_num)
    finally:
        return fib_nums[nth-1]

for i in range(1,101):
    print(n_th_fibonnaci(i))


# CHALLENGING - object oriented programming, unpacking, error handling, comprehensions
#%%
"""
Create a class called Person
"""
from datetime import date
from os import error

class Person:
    # define it's initialiser, take in a name, and a date of birth in ISO format (YYYY-MM-DD)
    # optionally a list of "friends"
    def __init__(self, name, date_of_birth, friends=[]):
        try:
            self.name = name
            self.date_of_birth = date.fromisoformat(date_of_birth)
            self.friends = friends
        except:
            print("Please enter the valid input.")
    # define a magic method which prints a string representation of the person, detailing their name, DOB and number of friends
    def __repr__(self):
        return f"Person: {self.name} was born in {self.date_of_birth} and has {len(self.friends)} friend(s)."
    
    # define greater than sign to compare the age of two people
    def __gt__(self, another):
        return another.date_of_birth > self.date_of_birth

    # Create a method called `add_friend`
    # which takes in another instance of the person class and adds it to this instance's friends attribute.
    # Assume that every relationship goes both ways: this method should append each friend to the other's list.
    def __add__(self, another):

        # assert that the type of the object passed into `add_friend` is an instance of the Person class. What's an assertion error?
        try:
            assert type(another) == Person
        
        # safely handle the assertion error
        except AssertionError:
            print('Please hand over Person object')
            return

        # if the person is already friend, return the func.
        if another in self.friends:
            return
        
        # copy my friends data and add another person
        updated_my_friends = [f for f in self.friends]
        updated_my_friends.append(another)

        # copy another person's friends data and add me
        updated_another_friends = [f for f in another.friends]
        updated_another_friends.append(self)
        
        # update the attribute with data
        self.friends = updated_my_friends
        another.friends = updated_another_friends
            
            

# instantiate your class and test that it works before continuing - do this for every section going forward
p1 = Person('Yoojin', '1986-09-11')
p2 = Person('Danny', '1986-09-22')
p3 = 'Test'

print(p1 > p2)

p1 + p2
p1 + p3



"""
Define a class called Shape
"""
#%%

class Shape:
    # num_sides(required), tessellates(optional)
    def __init__(self, num_sides, tessellates = False):
        # raise an error if num_sides is zero
        # if num_sides == 0:
        #     raise Exception("Number of sides is zero")
        self.num_sides = num_sides
        self.tessellates = tessellates

    # define a method called print_info which prints 
    def print_info(self):
        return  f"the number of the shape: {self.num_sides}\ntassellate: {self.tessellates}"
    
    # define a magic method which defines how to add the number of sides of a shape together
    # returns a new shape with that many sides
    def __add__(self, another):
        return Shape(self.num_sides + another.num_sides)
        
        
shape = Shape(1)
print(shape.print_info())


class Circle(Shape):
    def __init__(self):
        super().__init__(0)

    def print_info(self):
        print()
        pass
    

class Triangle(Shape):
    def __init__(self):
        super().__init__(3)
    

class Square(Shape):
    def __init__(self):
        super().__init__(4)
    

class Pentagon(Shape):
    def __init__(self):
        super().__init__(5)
    

class Hexagon(Shape):
    def __init__(self):
        super().__init__(6)
    

class ManySidedPolyGon(Shape):
    def __init__(self, num):
        super().__init__(num)
    

# for each of them, overwrite the print_info function and make it print the ?
circle = Circle()
circle.print_info()




# HARDCORE - generators, decorators, typing, context managers
"""
Create a function which takes in 3 arguments
"""
def func(a,b,c):
    pass

"""
Create a decorator called with_user_name
"""
def with_user_name(func):
    def wrapper():
        func()
    return wrapper


#%%
"""
Create an generator that generates incrementing binary bytes (8 digit numbers containing only ones and zeros) up to 256
"""
import math

# create a decorator which saves the output of a function to a file, and uses a context manager whilst doing so
def export(func):
    def wrapper(num):
        with open('exported.txt', 'a') as f:
            f.write(func(num))
            f.write('\n')
        return func(num)
    return wrapper


@export
def encode_binary_byte(num):
    if num == 0:
        return '0'
    m = math.trunc(math.log(num,2))
    res = ['0']*(m+1)

    while m >= 0:
        
        if num >= 2**m:
            res[m] = '1'
            if num == 2**m:
                break
            
        elif num < 2**m:
            res[m] = '0'

        num -= 2**m
        m = math.trunc(math.log(num,2))

    return ''.join(reversed(res))

gen_256 = (encode_binary_byte(i) for i in range(0,2**3))

for itm in gen_256:
    print(itm)





#%%
"""
Create an infinite generator comprehension that infinitely generates ones or zeros randomly
"""

import random

def infinite_generator():
    while True:
        yield random.randint(0,1)

inf_gen = (zero_or_one for zero_or_one in infinite_generator())

for i in inf_gen:
    print(i)






