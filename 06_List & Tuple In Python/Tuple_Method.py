b =(1,3,45,45,45,56,False, "Rohan")
print(b)
no = b.count(45)
print(no)


i=b.index(45)
print(i)
print( len(b))

# In Python, tuples are immutable sequences, typically used to store collections of heterogeneous data. They have several methods and operations you can use. Since tuples are immutable, their built-in methods are limited compared to mutable types like lists. Here are some methods and operations associated with tuples:

# Tuple Methods
# count()

# Returns the number of occurrences of a specific element in a tuple.
# my_tuple = (1, 2, 2, 3, 4, 2)
# print(my_tuple.count(2))  # Output: 3
# index()

# Returns the index of the first occurrence of a specific element in a tuple. Raises a ValueError if the element is not found.
# my_tuple = (1, 2, 3, 4, 2)
# print(my_tuple.index(2))  # Output: 1
# Other Operations with Tuples
# Accessing Elements

# Use indexing to access individual elements of a tuple.
# my_tuple = (10, 20, 30)
# print(my_tuple[1])  # Output: 20
# Slicing

# Extract a portion of the tuple using slicing.
# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[1:4])  # Output: (20, 30, 40)
# Concatenation

# Combine two or more tuples.
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)
# Repetition

# Repeat elements in a tuple using the * operator.
# my_tuple = (1, 2, 3)
# print(my_tuple * 2)  # Output: (1, 2, 3, 1, 2, 3)
# Membership Testing

# Check if an element exists in the tuple using the in keyword.
# my_tuple = (1, 2, 3, 4)
# print(2 in my_tuple)  # Output: True
# Unpacking

# Assign tuple elements to variables.
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a, b, c)  # Output: 1 2 3
# Length

# Get the number of elements in a tuple using len().
# my_tuple = (1, 2, 3, 4)
# print(len(my_tuple))  # Output: 4
# Iteration

# Loop through the elements in a tuple.
# my_tuple = (1, 2, 3)
# for item in my_tuple:
#     print(item)
# Conversion

# Convert a list or other iterable into a tuple using the tuple() constructor.
# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(my_tuple)  # Output: (1, 2, 3)