# use a list comprehension to capitalise every element in the list `['Hello', 'world']`
capitalised_list = [w.upper() for w in ['Hello', 'World']]
print(capitalised_list)

# use a list comprehension to filter out every multiple of 5 from a range of numbers up to 100
multipleof5 = [number for number in range(1,101) if number % 5 == 0]
print(multipleof5)

# use a dictionary comprehension to create a map between every integer up to 15 and it's value squared
squares = {number: number**2 for number in range(1,16)}
print(squares)

# now, use a dictionary comprehension to create a dictionary that does the inverse! 
# (hint: iterate over squares.items())
inverse_comprehension = {v: k for k, v in squares.items()}
print(inverse_comprehension)

# create a list of dictionaries, each with a key called name
# then use a list comprehension to map that list to the names themselves by indexing the dicts 
listOfDicts = [
    {'name':'Alisha'},
    {'name':'Yoojin'}
]

names = [d['name'] for d in listOfDicts]
