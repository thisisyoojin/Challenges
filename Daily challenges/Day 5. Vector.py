# create a class called Vector
class Vector:
    """
    The function creates a vector with input coordinates.
    input corrdinates should be a list.
    """

    # define its initialiser
    def __init__(self, coordinates: list[int]):
        self.data = coordinates
        self.dimension = len(coordinates)
        self.size = round(sum(coordinate**2 for coordinate in coordinates)**0.5, 5)
        

    # use the `__repr__` method to define what is printed 
    def __repr__(self):
        return f'{type(self)}: coordiate({self.data}), magnitude({self.size})'
        

    # define how you add two vectors together and return added vector
    def __add__(self, another: "Vector") -> "Vector":
        try:
            return Vector([self.data[idx] + another[idx] for idx in range(self.dimension)])
        except:
            print('You can\' add vectors with different dimensions.')



    # define how you index an item in the vector
    def __getitem__(self, idx: int) -> int:
        try:
            return self.data[idx]
        except:
            print('Index is not valid.')
            return None

    
    # define how you measure whether it is greater than another vector (use Pythagoras theorem) 
    def __gt__(self, another: "Vector") -> bool:
        return self.size >= another.size


vector1 = Vector([3,4,4])
vector2 = Vector([2,3,3])

# Calling __repr__
print(vector1)
print(vector2)

# Calling __getitem__
vector1[2]
vector2[4]

# Calling __add__
print(vector1+vector2)

# Calling __gt__ 
print(vector1 > vector2)
