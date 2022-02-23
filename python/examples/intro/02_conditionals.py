"""Python Conditionals

Demonstration of python comparison
operators, logical operators, membership
operators, and conditionals.
"""


# Standard comparison operators are used
# in Python.
x = 10
print(x < 5)
print(x > 5)
print(x <= 5)
print(x >= 5)
print(x != 5)
print(x == 5)

# Python also has some nice shorthand 
# for comparison operators
print(2 > x < 5)
print(9 <= x >= 5)

# Standard logical operators are used
# in Python.
print(x > 5 and x <= 6)
print(x > 5 or x != 6)
print(not (x < 20)) 

# For things like collections (lists,
# dictionaries, tuples, sets, and strings, etc.)
# we can check if items are present in the 
# collection.
my_example_list = ["apple", "banana", "grape", "pineapple"]
print("grape" in my_example_list)
print("hotdog" in my_example_list)
print("grape" not in my_example_list)
print("hotdog" not in my_example_list)

# Conditional statements are similar to those in C/C++
# but with different syntax.
# Simple if
if 'grape' in my_example_list:
    print("Item in the list")

# Simple if else
if 'hotdog' in my_example_list:
    print("Item in the list")
else:
    print("Item not in the list")

# Multiple conditional if statement
if 'grape' in my_example_list:
    print("Purple Fruit")
elif 'banana' in my_example_list:
    print("Yellow Fruit")
elif 'pineapple' in my_example_list:
    print("Spiky Fruit")
else:
    print("Red Fruit")
    