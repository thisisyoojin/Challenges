# Create a list of dictionary with name and favourite colours
group_data = [
    {
        "name": "Yoojin",
        "favourite_color": "Black",
    },
    {
        "name": "Kaoutar",
        "favourite_color": "Purple",
    },
    {
        "name": "Alisha",
        "favourite_color": "Green",
    },
]


# Define the function return 
def if_the_name_is_long(name: str, favourite_color: str) -> bool:
    """
    The function printing the info depending on the length of name.
    """
    if len(name) > 6:
        print(f"{name} has a long name and likes {favourite_color}.")
        return True
    else:
        print(f"{name} has a short name and likes {favourite_color}.")
        return False

# iterate over the group_data
for d in group_data:
    # unpacking input from the dictionary data matching with 
    if_the_name_is_long(**d)



