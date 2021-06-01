import random

# Create generator infintely cycle through list
my_list = range(1,6)

def my_generator():
    counter = 0
    while True:
        for itm in my_list:
            yield itm
   
for item in my_generator():
    print(item)


# storing an infinite generator in a list crashes VSCode
# my_list = list(my_generator())
# print(my_list)


# This function generates a random number 10 times
def random_number_generator():
    for i in range(10):
        yield random.random()

for item in random_number_generator():
    print(item)


# create a generator that takes in two numbers 
# and generates all multiples of 3 between the two of them

def multiples_of_3_generator(x,y):
    for i in range (x,y):
        if i % 3 == 0:
            yield i

for item in multiples_of_3_generator(7,100):
    print(item)


# create a generator that generates the square of every number up to 100,
# if that number is even or is a multiple of 3

def even_or_multiple_of_3_generator():
    for i in range (1,101):
        if i % 3 == 0 or i % 2 ==0:
            yield i

for item in even_or_multiple_of_3_generator():
    print(item)



#turn the above generator into a generator comprehension

comp_even_or_multiple_of_3_generator = (i for i in range(1,101) if i % 3 == 0 or i % 2 == 0)

for item in comp_even_or_multiple_of_3_generator:
    print(item)


# create a generator that generates generators
# which each generate ranges up to a random number passed to them as an argument
#%%
import random
generate_generators = ((i for i in range(random.randint(1,11))) for j in range(3))

for gen in generate_generators:
    for random_range in gen:
        print(random_range)


# %%
